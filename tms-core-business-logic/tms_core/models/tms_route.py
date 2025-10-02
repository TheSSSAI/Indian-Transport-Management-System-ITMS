# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TmsRoute(models.Model):
    """
    Master data for pre-defined transportation routes.
    Fulfills REQ-1-206 and user story US-019.
    """
    _name = "tms.route"
    _description = "Route Master"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "name"

    name = fields.Char(string="Route Name", required=True, index=True)
    source_location = fields.Char(string="Source Location", required=True)
    destination_location = fields.Char(
        string="Destination Location", required=True)
    standard_distance = fields.Float(
        string="Standard Distance (km)", required=True)
    estimated_transit_time = fields.Float(
        string="Estimated Transit Time (hours)")
    active = fields.Boolean(
        string="Active", default=True,
        help="Uncheck the active field to hide the route without removing it.")

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
         'A route with this name already exists.')
    ]

    @api.constrains('standard_distance', 'estimated_transit_time')
    def _check_positive_values(self):
        for route in self:
            if route.standard_distance <= 0:
                raise ValidationError(
                    _("Standard Distance must be greater than zero."))
            if route.estimated_transit_time < 0:
                raise ValidationError(
                    _("Estimated Transit Time cannot be negative."))