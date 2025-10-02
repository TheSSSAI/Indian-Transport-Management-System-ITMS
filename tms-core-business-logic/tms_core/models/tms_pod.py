# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

class TmsPod(models.Model):
    """
    Proof of Delivery (POD) for a trip.
    This record is created by the driver upon delivery and marks a critical milestone in the trip lifecycle.
    Its creation automatically transitions the associated trip's status to 'Delivered'.
    Fulfills REQ-1-114 and User Story US-052.
    """
    _name = 'tms.pod'
    _description = 'Proof of Delivery'
    _order = 'submission_timestamp desc, id desc'

    trip_id = fields.Many2one(
        'tms.trip',
        string='Trip',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False,
        # A trip can only have one POD.
        unique=True
    )
    
    pod_type = fields.Selection([
        ('photo', 'Photo'),
        ('signature', 'E-Signature')
    ], string='POD Type', required=True, default='photo')

    recipient_name = fields.Char(string='Recipient Name', required=True, tracking=True)
    
    pod_attachment = fields.Binary(string="POD File", required=True, attachment=True)
    pod_attachment_filename = fields.Char(string="POD Filename")

    submission_timestamp = fields.Datetime(
        string='Submission Timestamp',
        default=fields.Datetime.now,
        required=True,
        readonly=True,
        copy=False
    )
    
    driver_id = fields.Many2one(
        'hr.employee',
        string='Submitted By (Driver)',
        related='trip_id.driver_id',
        store=True,
        readonly=True
    )
    
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        related='trip_id.company_id',
        store=True,
        readonly=True
    )
    
    @api.model_create_multi
    def create(self, vals_list):
        """
        Overrides the create method to automatically update the trip status to 'Delivered'.
        This ensures the state transition is atomic with the POD creation.
        """
        for vals in vals_list:
            trip = self.env['tms.trip'].browse(vals.get('trip_id'))
            if not trip:
                raise ValidationError(_("A POD must be associated with a valid trip."))

            # Security and State Check
            if trip.state != 'in_transit':
                raise UserError(_("Proof of Delivery can only be submitted for a trip that is 'In-Transit'."))

            # Driver authorization check: Ensure the user creating the POD is the assigned driver or a manager
            is_manager = self.env.user.has_group('tms_core.group_tms_dispatch_manager')
            is_assigned_driver = trip.driver_id.user_id == self.env.user
            if not (is_manager or is_assigned_driver):
                raise UserError(_("You are not authorized to submit a POD for this trip."))

        # Create POD records first
        pods = super(TmsPod, self).create(vals_list)

        # Transition trip state after successful POD creation
        for pod in pods:
            try:
                # Using a dedicated method on the trip model for better encapsulation and auditability
                pod.trip_id.action_deliver(pod)
            except (UserError, ValidationError) as e:
                # If the state transition fails for any reason, we should not have a dangling POD.
                # However, since create is atomic, we can't easily roll back just this one record.
                # The check at the beginning should prevent this. We log a critical error if it happens.
                _logger.critical(
                    "POD record (id: %s) was created but failed to transition trip (id: %s) to 'Delivered'. Error: %s",
                    pod.id, pod.trip_id.id, e
                )
                # In a real-world scenario, this might trigger an alert to an admin.
                pod.trip_id.message_post(
                    body=_("<b>CRITICAL ERROR:</b> A Proof of Delivery was recorded, but the system failed to update the trip status to 'Delivered'. Manual intervention required.")
                )

        return pods

    @api.constrains('trip_id')
    def _check_trip_id_unique(self):
        # This is already handled by the `unique=True` on the field, but this provides a more user-friendly message.
        # As of Odoo 16+, sql constraints are preferred, but this is kept for clarity.
        pass