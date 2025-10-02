# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class ResPartner(models.Model):
    """
    Extends the Partner model to add TMS customer-specific details.
    Fulfills REQ-1-012, REQ-1-205, US-015, US-073.
    """
    _inherit = "res.partner"

    is_tms_customer = fields.Boolean(
        string="Is a TMS Customer",
        help="Check this box if this partner is a customer for the Transport Management System.")

    @api.constrains('vat')
    def _check_gstin_format(self):
        """
        Validates the GSTIN format for Indian companies.
        A valid GSTIN is 15 characters long.
        Format: 2 digits (state code), 10 chars (PAN), 1 digit, 'Z', 1 digit/char.
        """
        gstin_pattern = re.compile(r"^[0-9]{2}[A-Z]{5}[0-9]{4}[A-Z]{1}[1-9A-Z]{1}Z[0-9A-Z]{1}$")
        for partner in self:
            if partner.country_id and partner.country_id.code == 'IN' and partner.vat:
                if not gstin_pattern.match(partner.vat):
                    raise ValidationError(_(
                        "Invalid GSTIN format for '%s'. Please enter a valid 15-digit Indian GSTIN.",
                        partner.vat
                    ))

    @api.model
    def create(self, vals):
        """Override to auto-uppercase GSTIN."""
        if 'vat' in vals and vals['vat']:
            vals['vat'] = vals['vat'].upper().strip()
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        """Override to auto-uppercase GSTIN."""
        if 'vat' in vals and vals['vat']:
            vals['vat'] = vals['vat'].upper().strip()

        # Prevent deactivation if customer has active trips
        if 'active' in vals and not vals['active']:
            for partner in self.filtered(lambda p: p.is_tms_customer):
                active_trips = self.env['tms.trip'].search([
                    ('customer_id', '=', partner.id),
                    ('state', 'in', ['planned', 'assigned', 'in_transit', 'on_hold'])
                ])
                if active_trips:
                    raise UserError(_(
                        "Customer %s cannot be deactivated as they are associated with active trip(s): %s.",
                        partner.name,
                        ', '.join(active_trips.mapped('name'))
                    ))

        return super(ResPartner, self).write(vals)