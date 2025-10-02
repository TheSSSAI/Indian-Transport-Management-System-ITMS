# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

# List of event types considered critical, which trigger an 'On Hold' status.
CRITICAL_EVENTS = ['accident', 'repair', 'gov_stoppage']

class TmsTripEvent(models.Model):
    """
    Logs an event that occurred during a trip.
    This can be a standard operational event (e.g., Fueling) or a critical disruption (e.g., Accident).
    The creation of a critical event automatically triggers a state change on the parent trip.
    Fulfills REQ-1-115, REQ-1-905, and User Story US-050.
    """
    _name = 'tms.trip.event'
    _description = 'Trip Event Log'
    _order = 'event_timestamp desc, id desc'

    trip_id = fields.Many2one(
        'tms.trip',
        string='Trip',
        required=True,
        ondelete='cascade',
        index=True
    )
    
    event_type = fields.Selection([
        ('trip_start', 'Trip Start'),
        ('fueling', 'Fueling'),
        ('repair', 'Repair'),
        ('accident', 'Accident'),
        ('gov_stoppage', 'Government Stoppage'),
        ('other', 'Other'),
    ], string='Event Type', required=True, index=True)

    description = fields.Text(string="Description / Notes")
    
    photo = fields.Binary(string="Attached Photo", attachment=True)
    photo_filename = fields.Char(string="Photo Filename")
    
    event_timestamp = fields.Datetime(
        string='Event Timestamp',
        default=fields.Datetime.now,
        required=True,
        readonly=True
    )
    
    driver_id = fields.Many2one(
        'hr.employee',
        string='Logged By (Driver)',
        related='trip_id.driver_id',
        store=True,
        readonly=True
    )

    company_id = fields.Many2one('res.company', string='Company', related='trip_id.company_id', store=True, readonly=True)

    @api.model_create_multi
    def create(self, vals_list):
        """
        Overrides the create method to check for critical events.
        If a critical event is logged, it automatically changes the associated trip's status to 'On Hold'.
        This implements the reactive logic required by REQ-1-905 and US-077.
        """
        # First, perform authorization and validation checks
        for vals in vals_list:
            trip = self.env['tms.trip'].browse(vals.get('trip_id'))
            if not trip:
                raise UserError(_("An event must be logged against a valid trip."))
            
            # Authorize: Only the assigned driver or a manager can log an event.
            is_manager = self.env.user.has_group('tms_core.group_tms_dispatch_manager')
            is_assigned_driver = trip.driver_id and trip.driver_id.user_id == self.env.user

            if not (is_manager or is_assigned_driver):
                raise UserError(_("You are not authorized to log an event for this trip."))
            
            # State validation: Events can typically only be logged on active trips
            if trip.state not in ['assigned', 'in_transit', 'on_hold']:
                 _logger.warning(
                     "User %s attempted to log an event for trip %s in a non-active state ('%s').",
                     self.env.user.name, trip.name, trip.state
                 )
                 # We allow it but log it, as it might be a post-facto log.
                 # Stricter validation would be to raise a UserError here.

        # Create the event records
        events = super(TmsTripEvent, self).create(vals_list)

        # Post-creation logic: Handle state transitions for critical events
        for event in events:
            if event.event_type in CRITICAL_EVENTS:
                # We check the trip's state again to ensure it's still active.
                if event.trip_id.state in ['in_transit', 'assigned']:
                    try:
                        # Call the dedicated method on the trip model
                        event.trip_id.action_put_on_hold(
                            _("Trip automatically put on hold due to critical event: %s.") % event.display_name
                        )
                        _logger.info(
                            "Trip %s automatically put on hold due to critical event %s.",
                            event.trip_id.name, event.id
                        )
                    except UserError as e:
                        # Log if the state transition fails, but don't block the event creation.
                        _logger.error(
                            "Failed to put trip %s on hold after critical event %s. Reason: %s",
                            event.trip_id.name, event.id, e
                        )
                        event.trip_id.message_post(body=_(
                            "<b>System Warning:</b> A critical event was logged, but the system failed to automatically place the trip on hold. Manual review required."
                        ))

        return events