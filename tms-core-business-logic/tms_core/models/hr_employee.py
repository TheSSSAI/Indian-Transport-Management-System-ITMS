# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class HrEmployee(models.Model):
    """
    Extends the HR Employee model to add driver-specific details for TMS.
    Fulfills REQ-1-012, REQ-1-203, US-011, US-012.
    """
    _inherit = "hr.employee"

    is_tms_driver = fields.Boolean(
        string="Is a TMS Driver",
        help="Check this box if this employee is a driver for the Transport Management System.")

    license_number = fields.Char(string="License Number", tracking=True)
    license_expiry_date = fields.Date(string="License Expiry Date", tracking=True)

    def write(self, vals):
        """
        Override to prevent deactivation if assigned to an active trip.
        """
        if 'active' in vals and not vals['active']:
            for employee in self.filtered(lambda e: e.is_tms_driver):
                active_trips = self.env['tms.trip'].search([
                    ('driver_id', '=', employee.id),
                    ('state', 'in', ['planned', 'assigned', 'in_transit', 'on_hold'])
                ])
                if active_trips:
                    raise ValidationError(_(
                        "Driver %s cannot be deactivated as they are assigned to active trip(s): %s.",
                        employee.name,
                        ', '.join(active_trips.mapped('name'))
                    ))
        return super(HrEmployee, self).write(vals)

    @api.constrains('is_tms_driver', 'license_number', 'license_expiry_date')
    def _check_driver_details(self):
        for employee in self:
            if employee.is_tms_driver:
                if not employee.license_number:
                    raise ValidationError(
                        _("License Number is required for a TMS driver."))
                if not employee.license_expiry_date:
                    raise ValidationError(
                        _("License Expiry Date is required for a TMS driver."))