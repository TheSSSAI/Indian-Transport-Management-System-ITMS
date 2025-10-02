# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _


class TmsMaterial(models.Model):
    """
    Master data for material types that can be transported.
    Fulfills REQ-1-003 and user story US-020.
    """
    _name = "tms.material"
    _description = "Material Master"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "name"

    name = fields.Char(string="Material Name", required=True, index=True)
    handling_instructions = fields.Text(string="Special Handling Instructions")
    active = fields.Boolean(
        string="Active", default=True,
        help="Uncheck the active field to hide the material type without removing it.")

    _sql_constraints = [
        ('name_uniq', 'unique (name)',
         'A material type with this name already exists.')
    ]