# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date, timedelta
import logging

_logger = logging.getLogger(__name__)

class TmsVehicleDocument(models.Model):
    """
    Represents a compliance document associated with a vehicle.
    This model stores the document itself, its type, and its expiry date.
    It includes logic to automatically generate alerts for upcoming expiries.
    """
    _name = 'tms.vehicle.document'
    _description = 'Vehicle Document'
    _order = 'expiry_date asc'

    vehicle_id = fields.Many2one(
        'tms.vehicle',
        string='Vehicle',
        required=True,
        ondelete='cascade',
        help="The vehicle to which this document belongs."
    )
    document_type = fields.Selection(
        [
            ('rc', 'Registration Certificate (RC)'),
            ('insurance', 'Insurance'),
            ('fitness', 'Fitness Certificate'),
            ('puc', 'Pollution Under Control (PUC)'),
            ('national_permit', 'National Permit'),
            ('other', 'Other'),
        ],
        string='Document Type',
        required=True,
        help="The type of the document."
    )
    expiry_date = fields.Date(
        string='Expiry Date',
        required=True,
        help="The date on which this document expires."
    )
    attachment = fields.Binary(
        string="Attachment",
        required=True,
        help="The scanned copy of the document."
    )
    attachment_filename = fields.Char(
        string="Attachment Filename"
    )

    @api.constrains('expiry_date')
    def _check_expiry_date(self):
        """
        Although past dates are allowed for historical records,
        this provides a warning if a user enters a past date for a new document.
        For simplicity in this model, we'll allow past dates but business processes
        should highlight them. The alert cron job will handle expired docs.
        """
        # A non-blocking warning could be implemented in the UI layer if needed.
        # For this model, we allow past dates to store historical data.
        pass

    @api.model
    def _cron_check_document_expiries(self):
        """
        Scheduled action to generate alerts for vehicle documents nearing expiry.
        This job is intended to run once daily.
        It checks for documents expiring in 30, 15, and 7 days.
        It also creates/maintains alerts for already expired documents.

        Fulfills requirements: REQ-1-201, REQ-1-010, US-009, US-078.
        """
        _logger.info("Starting cron job: Check Vehicle Document Expiries.")
        today = date.today()
        alert_model = self.env['tms.alert']
        alert_days = [30, 15, 7]

        # 1. Find documents expiring on specific future dates
        for days in alert_days:
            expiry_target_date = today + timedelta(days=days)
            expiring_docs = self.search([
                ('expiry_date', '=', expiry_target_date),
                ('vehicle_id.active', '=', True) # REQ-BRC-002 from US-078
            ])
            for doc in expiring_docs:
                message = _(
                    "Vehicle document '%(doc_type)s' for vehicle '%(vehicle)s' is expiring in %(days)d days on %(date)s."
                ) % {
                    'doc_type': dict(self._fields['document_type'].selection).get(doc.document_type),
                    'vehicle': doc.vehicle_id.display_name,
                    'days': days,
                    'date': doc.expiry_date.strftime('%d-%m-%Y'),
                }
                
                # Check if an alert for this specific document and milestone already exists
                existing_alert = alert_model.search([
                    ('res_model', '=', self._name),
                    ('res_id', '=', doc.id),
                    ('alert_type', '=', 'document_expiry'),
                    ('message', '=', message) # Ensures idempotency for this exact message
                ], limit=1)
                
                if not existing_alert:
                    alert_model.create({
                        'alert_type': 'document_expiry',
                        'message': message,
                        'res_model': self._name,
                        'res_id': doc.id,
                        'priority': '2' if days > 7 else '1', # Medium priority, High for 7 days
                    })
                    _logger.info(f"Created {days}-day expiry alert for document ID {doc.id}.")

        # 2. Find documents that have already expired and ensure an alert exists
        expired_docs = self.search([
            ('expiry_date', '<', today),
            ('vehicle_id.active', '=', True)
        ])
        for doc in expired_docs:
            message = _(
                "DOCUMENT EXPIRED: '%(doc_type)s' for vehicle '%(vehicle)s' expired on %(date)s."
            ) % {
                'doc_type': dict(self._fields['document_type'].selection).get(doc.document_type),
                'vehicle': doc.vehicle_id.display_name,
                'date': doc.expiry_date.strftime('%d-%m-%Y'),
            }
            
            # Check if an "EXPIRED" alert already exists for this document to avoid spam
            existing_alert = alert_model.search([
                ('res_model', '=', self._name),
                ('res_id', '=', doc.id),
                ('alert_type', '=', 'document_expired'),
            ], limit=1)
            
            if not existing_alert:
                 # Clear any old upcoming expiry alerts for this document
                old_alerts = alert_model.search([
                    ('res_model', '=', self._name),
                    ('res_id', '=', doc.id),
                    ('alert_type', '=', 'document_expiry'),
                ])
                if old_alerts:
                    old_alerts.write({'active': False}) # Or unlink()

                alert_model.create({
                    'alert_type': 'document_expired',
                    'message': message,
                    'res_model': self._name,
                    'res_id': doc.id,
                    'priority': '0', # Highest priority
                })
                _logger.info(f"Created EXPIRED alert for document ID {doc.id}.")
        _logger.info("Finished cron job: Check Vehicle Document Expiries.")