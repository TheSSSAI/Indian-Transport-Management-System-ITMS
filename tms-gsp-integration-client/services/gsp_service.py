# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import logging
from requests.exceptions import Timeout, ConnectionError, HTTPError

from odoo import _
from odoo.exceptions import UserError

from ..services.gsp_api_client import GspApiClient
from ..services.gsp_api_client import (
    GspApiTimeoutError,
    GspApiConnectionError,
    GspApiDataError,
    GspApiServerError,
)
from ..services.gsp_request_mapper import GspRequestMapper

_logger = logging.getLogger(__name__)


class GspService:
    """
    Orchestration service for the e-invoice generation process.
    This service coordinates data mapping, synchronous API calls, and the
    asynchronous fallback logic as required by REQ-1-302.
    It acts as the central point of control for the GSP integration use case.
    """

    def __init__(self, env):
        """
        Initializes the service with the Odoo environment.
        :param env: Odoo Environment
        """
        self.env = env

    def _process_success_response(self, invoice, response_data):
        """
        Processes a successful response from the GSP API.
        Updates the invoice record with the IRN, QR code, and sets the status to 'generated'.

        :param invoice: The odoo 'account.move' recordset.
        :param response_data: The dictionary parsed from the GSP API JSON response.
        """
        _logger.info("Processing successful GSP response for invoice %s", invoice.name)

        irn = response_data.get("Irn")
        qr_code_data = response_data.get("SignedQRCode")
        ack_no = response_data.get("AckNo")
        ack_dt = response_data.get("AckDt")

        if not irn or not qr_code_data:
            _logger.error(
                "GSP success response for invoice %s is missing required fields "
                "(IRN or QRCode). Response: %s",
                invoice.name,
                response_data,
            )
            invoice.write(
                {
                    "gsp_status": "failed",
                    "gsp_error_message": _(
                        "GSP API response was successful but is missing required "
                        "data (IRN/QR Code). Please check the logs and contact support."
                    ),
                }
            )
            return

        vals_to_write = {
            "gsp_irn": irn,
            "gsp_qr_code": qr_code_data,
            "gsp_status": "generated",
            "gsp_ack_no": str(ack_no),
            "gsp_ack_date": ack_dt,
            "gsp_error_message": False,
        }
        invoice.write(vals_to_write)
        invoice.message_post(
            body=_(
                "E-Invoice generated successfully. IRN: %s. Acknowledged on: %s",
                irn,
                ack_dt,
            )
        )

    def generate_einvoice(self, invoice):
        """
        Orchestrates the e-invoice generation for a single invoice record.

        - Maps the Odoo invoice to the GSP API payload.
        - Attempts a synchronous API call.
        - On transient failure, enqueues a background job for retries.
        - On permanent failure, marks the invoice as failed with an error.
        - On success, updates the invoice with the IRN and QR code.

        This method implements the core logic of REQ-1-302 and Sequence Diagram 227.

        :param invoice: A single odoo 'account.move' recordset.
        """
        invoice.ensure_one()
        _logger.info("Starting e-invoice generation process for invoice: %s", invoice.name)

        try:
            # 1. Instantiate mapper and API client
            mapper = GspRequestMapper(self.env)
            api_client = GspApiClient(self.env)

            # 2. Map Odoo record to GSP payload
            payload = mapper.map_invoice_to_gsp_payload(invoice)
            _logger.debug("GSP payload generated for invoice %s", invoice.name)

            # 3. Attempt synchronous API call
            _logger.info("Attempting synchronous GSP API call for invoice %s", invoice.name)
            response_data = api_client.send_invoice_data(payload)

            # 4. Process successful response
            self._process_success_response(invoice, response_data)

        except (GspApiTimeoutError, GspApiConnectionError, GspApiServerError) as e:
            # 5. Handle transient errors: enqueue background job for retries
            error_message = _(
                "E-invoicing for %s failed due to a temporary connection "
                "issue (%s). The system will retry automatically in the background.",
                invoice.name,
                str(e),
            )
            _logger.warning(error_message)
            invoice.write(
                {
                    "gsp_status": "pending",
                    "gsp_error_message": _(
                        "API connection issue. Will retry automatically."
                    ),
                }
            )
            # Use with_delay to enqueue the job on the invoice's model method
            invoice.with_delay(
                description=f"Retry e-invoice generation for {invoice.name}"
            )._job_generate_einvoice()
            self.env.cr.commit()  # Commit the state change and job enqueue
            raise UserError(error_message)

        except GspApiDataError as e:
            # 6. Handle permanent data errors (4xx): mark as failed
            error_message = _(
                "E-invoicing for %s failed due to invalid data. "
                "GSP API returned: %s",
                invoice.name,
                str(e),
            )
            _logger.error(error_message)
            invoice.write({"gsp_status": "failed", "gsp_error_message": str(e)})
            invoice.message_post(body=error_message)
            raise UserError(error_message)

        except ValueError as e:
            # 7. Handle data mapping errors
            error_message = _(
                "Failed to generate e-invoice payload for %s. "
                "Reason: %s. Please check the invoice and customer data.",
                invoice.name,
                str(e),
            )
            _logger.error(error_message)
            invoice.write(
                {"gsp_status": "failed", "gsp_error_message": error_message}
            )
            invoice.message_post(body=error_message)
            raise UserError(error_message)

        except Exception as e:
            # 8. Catch-all for any other unexpected errors
            error_message = _(
                "An unexpected error occurred during e-invoicing for %s: %s",
                invoice.name,
                str(e),
            )
            _logger.exception(
                "Unexpected error during e-invoice generation for invoice %s",
                invoice.name,
            )
            invoice.write(
                {
                    "gsp_status": "failed",
                    "gsp_error_message": _(
                        "An unexpected system error occurred. "
                        "Please check logs for details."
                    ),
                }
            )
            invoice.message_post(body=error_message)
            raise UserError(error_message)