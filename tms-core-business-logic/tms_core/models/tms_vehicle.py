# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class TmsVehicle(models.Model):
    """
    Master data for all vehicles in the fleet.
    Fulfills REQ-1-200, REQ-1-900, BR-002, US-006, US-007, US-008.
    """
    _name = "tms.vehicle"
    _description = "Vehicle Master"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "truck_number"

    name = fields.Char(string="Name", compute="_compute_name", store=True)
    truck_number = fields.Char(
        string="Truck Number", required=True, index=True, copy=False, tracking=True)
    model = fields.Char(string="Model", tracking=True)
    capacity = fields.Float(string="Capacity (Tons)", required=True, tracking=True)
    owner_details = fields.Char(string="Owner Details", tracking=True)
    ownership_type = fields.Selection([
        ('company_owned', 'Company-Owned'),
        ('outsourced', 'Outsourced'),
    ], string="Ownership Type", required=True, default='company_owned', tracking=True)
    fuel_type = fields.Selection([
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('cng', 'CNG'),
        ('electric', 'Electric'),
        ('other', 'Other'),
    ], string="Fuel Type", tracking=True)
    last_service_date = fields.Date(string="Last Service Date", tracking=True)
    next_service_due_date = fields.Date(
        string="Next Service Due Date", tracking=True)
    active = fields.Boolean(
        string="Active", default=True, tracking=True,
        help="Uncheck the active field to hide the vehicle from selection lists.")
    last_odometer = fields.Float(
        string="Last Recorded Odometer", readonly=True, copy=False,
        help="The last known odometer reading from a diesel expense entry.")

    _sql_constraints = [
        ('truck_number_uniq', 'unique (truck_number)',
         'A vehicle with this truck number already exists.')
    ]

    @api.depends('truck_number', 'model')
    def _compute_name(self):
        for vehicle in self:
            name = vehicle.truck_number or _("New Vehicle")
            if vehicle.model:
                name = f"{name} ({vehicle.model})"
            vehicle.name = name

    @api.constrains('truck_number')
    def _check_truck_number_format(self):
        # Regex for standard Indian vehicle registration numbers
        # Covers formats like MH12AB1234, DL01C1234, etc.
        # This is a basic regex and can be improved for more complex formats.
        pattern = re.compile(
            r"^[A-Z]{2}[0-9]{1,2}(?:[A-Z])?(?:[A-Z]*)?[0-9]{1,4}$")
        for vehicle in self:
            if vehicle.truck_number:
                normalized_number = vehicle.truck_number.upper().replace(" ", "").replace("-", "")
                if not pattern.match(normalized_number):
                    raise ValidationError(_(
                        "Invalid Truck Number format for '%s'. Please use a valid Indian vehicle "
                        "registration number format (e.g., MH12AB1234).",
                        vehicle.truck_number
                    ))

    @api.constrains('capacity')
    def _check_capacity(self):
        for vehicle in self:
            if vehicle.capacity <= 0:
                raise ValidationError(_("Capacity must be a positive number."))

    def write(self, vals):
        """
        Override to prevent deactivation if assigned to an active trip.
        Also normalizes truck number.
        """
        if vals.get('truck_number'):
            vals['truck_number'] = vals['truck_number'].upper().replace(" ", "").replace("-", "")

        if 'active' in vals and not vals['active']:
            for vehicle in self:
                active_trips = self.env['tms.trip'].search([
                    ('vehicle_id', '=', vehicle.id),
                    ('state', 'in', ['planned', 'assigned', 'in_transit', 'on_hold'])
                ])
                if active_trips:
                    raise UserError(_(
                        "Vehicle %s cannot be deactivated as it is assigned to active trip(s): %s.",
                        vehicle.name,
                        ', '.join(active_trips.mapped('name'))
                    ))
        return super(TmsVehicle, self).write(vals)

    @api.model
    def create(self, vals):
        """Override to normalize truck number on creation."""
        if vals.get('truck_number'):
            vals['truck_number'] = vals['truck_number'].upper().replace(" ", "").replace("-", "")
        return super(TmsVehicle, self).create(vals)