# -*- coding: utf-8 -*-
import base64
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)

try:
    from odoo.addons.queue_job.job import job, RetryableJobError
except ImportError:
    _logger.warning("The 'queue_job' addon is not available.")
    job = lambda *args, **kwargs: lambda func: func
    RetryableJobError = Exception


class AccountMove(models.Model):
    """
    Inherits from account.move to add fields and methods for GST e-invoicing
    integration. This model acts as the primary entry point from the Odoo UI,
    orchestrating the communication with the GSP service layer and handling
    the state management for the e-invoicing process.
    """
    _inherit = 'account.move'

    gsp_irn = fields.Char(
        string="IRN",
        readonly=True,
        index=True,
        copy=False,
        help="Invoice Reference Number received from the GSP."
    )
    gsp_qr_code = fields.Text(
        string="QR Code Data",
        readonly=True,
        copy=False,
        help="Base64 encoded QR code string received from the GSP."
    )
    gsp_qr_code_image = fields.Binary(
        string="QR Code Image",
        compute='_compute_gsp_qr_code_image',
        store=False,  # This is a computed field, not stored in DB
        help="The QR code as a displayable image."
    )
    gsp_status = fields.Selection(
        selection=[
            ('not_generated', 'Not Generated'),
            ('pending', 'Pending Retry'),
            ('generated', 'Generated'),
            ('failed', 'Failed'),
        ],
        string="E-Invoice Status",
        default='not_generated',
        required=True,
        copy=False,
        index=True,
        help="Tracks the status of the e-invoice generation process."
    )
    gsp_error_message = fields.Text(
        string="Last GSP Error",
        readonly=True,
        copy=False,
        help="Stores the last error message received from the GSP API for diagnostics."
    )

    @api.depends('gsp_qr_code')
    def _compute_gsp_qr_code_image(self):
        """
        Decodes the Base64 QR code data into a binary image for display in Odoo views.
        """
        for move in self:
            if move.gsp_qr_code:
                try:
                    move.gsp_qr_code_image = base64.b64decode(move.gsp_qr_code)
                except (TypeError, base64.binascii.Error) as e:
                    _logger.warning(
                        "Could not decode GSP QR code for invoice %s. Error: %s",
                        move.name, e
                    )
                    move.gsp_qr_code_image = False
            else:
                move.gsp_qr_code_image = False

    def action_generate_einvoice(self):
        """
        UI action to initiate the e-invoice generation process. It performs
        pre-flight validations and then calls the GSP service to handle the
        API communication and fallback logic.
        """
        self.ensure_one()
        _logger.info("Attempting to generate e-invoice for invoice: %s", self.name)

        # Pre-flight validation checks
        if self.state != 'posted':
            raise UserError(_("E-invoicing can only be performed on posted invoices."))
        if self.move_type not in ('out_invoice', 'out_refund'):
            raise UserError(_("E-invoicing is only applicable for customer invoices and credit notes."))
        if not self.partner_id.vat:
            raise UserError(_("Cannot generate e-invoice: The customer '%s' is missing a valid GSTIN.") % self.partner_id.name)
        if self.gsp_status == 'generated':
            raise UserError(_("This invoice already has a generated IRN."))

        try:
            # Delegate to the GSP service layer
            gsp_service = self.env['gsp.service']
            gsp_service.generate_einvoice(self)

            # Provide feedback based on the outcome
            if self.gsp_status == 'generated':
                self.message_post(body=_("E-Invoice generated successfully with IRN: %s") % self.gsp_irn)
            elif self.gsp_status == 'pending':
                self.message_post(body=_("E-Invoice generation failed due to a temporary issue. The system will retry automatically in the background."))
            
        except UserError as e:
            # Re-raise user errors to be displayed directly in the UI
            raise e
        except Exception as e:
            _logger.error(
                "An unexpected error occurred during e-invoice generation for invoice %s: %s",
                self.name, str(e), exc_info=True
            )
            self.write({
                'gsp_status': 'failed',
                'gsp_error_message': _("An unexpected system error occurred. Please check the logs or contact an administrator."),
            })
            self.message_post(body=_("E-Invoice generation failed due to an unexpected system error."))
            # We don't raise UserError here to avoid showing a raw traceback to the user
            # for unexpected errors. The status change and message_post are sufficient.

        return True

    def action_retry_einvoice(self):
        """
        UI action to manually retry a failed e-invoice generation.
        This simply re-triggers the main generation action.
        """
        self.ensure_one()
        if self.gsp_status != 'failed':
            raise UserError(_("You can only retry e-invoices that have a 'Failed' status."))
        
        _logger.info("Manually retrying e-invoice generation for invoice: %s", self.name)
        return self.action_generate_einvoice()

    @job(retry_pattern={
        1: 60,      # 1st retry in 1 minute
        2: 300,     # 2nd retry in 5 minutes
        3: 1800,    # 3rd retry in 30 minutes
        4: 7200,    # 4th retry in 2 hours
        5: 21600    # 5th retry in 6 hours (Final)
    })
    def _job_generate_einvoice(self):
        """
        Asynchronous background job to retry e-invoice generation.
        This method is enqueued by the GspService on synchronous call failures.
        It calls the GspService to perform the actual API communication.
        """
        self.ensure_one()
        _logger.info("Running background job for e-invoice generation for invoice: %s", self.name)

        # Prevent re-running if the status has changed (e.g., manual intervention)
        if self.gsp_status != 'pending':
            _logger.warning(
                "Skipping e-invoice job for invoice %s as its status is now '%s', not 'pending'.",
                self.name, self.gsp_status
            )
            return

        try:
            gsp_service = self.env['gsp.service']
            # Re-call the main service. It will handle the API call again.
            gsp_service.generate_einvoice_sync_only(self)
            if self.gsp_status == 'generated':
                body = _("E-Invoice successfully generated in the background. IRN: %s") % self.gsp_irn
                self.message_post(body=body)
                # Optionally, notify the user who triggered the original action
                # self.activity_schedule(...)
        except RetryableJobError:
            # This specific exception is caught by queue_job to trigger a retry.
            # We re-raise it to let the queue manager handle the retry logic.
            _logger.info("E-invoice job for %s failed with a retryable error. Re-enqueuing.", self.name)
            raise
        except Exception as e:
            # Any other exception is considered a final failure for this job attempt.
            # If it was a retryable error, the GspService would have raised RetryableJobError.
            # This block will execute if it's a permanent error (e.g. 4xx) or if
            # an unexpected error occurs.
            job_uuid = self.env.context.get('job_uuid')
            current_job = self.env['queue.job'].search([('uuid', '=', job_uuid)], limit=1)
            
            error_message = str(e)
            
            if current_job and current_job.retry >= current_job.max_retries:
                _logger.error(
                    "Final attempt to generate e-invoice for %s failed. Setting status to 'Failed'. Error: %s",
                    self.name, error_message, exc_info=True
                )
                self.write({
                    'gsp_status': 'failed',
                    'gsp_error_message': error_message
                })
                body = _("All automated attempts to generate the e-invoice have failed. "
                         "Please review the error and take manual action. Last error: %s") % error_message
                self.message_post(body=body)
                # Optionally notify a specific user group (e.g., Finance)
            else:
                _logger.warning(
                    "E-invoice job for %s failed but may be retried. Error: %s",
                    self.name, error_message, exc_info=True
                )
                # Let the job queue handle the retry based on the pattern
                raise RetryableJobError(e)