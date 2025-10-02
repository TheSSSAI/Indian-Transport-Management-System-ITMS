# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class TmsAlert(models.Model):
    """
    Model to store and manage system-level alerts for critical events.
    These alerts are typically displayed on a dashboard for managers.
    Fulfills parts of REQ-1-010.
    """
    _name = "tms.alert"
    _description = "System Alert"
    _order = "create_date desc"

    name = fields.Char(string="Title", required=True, index=True)
    message = fields.Text(string="Message", required=True)
    alert_type = fields.Selection([
        ('document_expiry', 'Document Expiry'),
        ('low_balance', 'Low Card Balance'),
        ('critical_event', 'Critical Trip Event'),
        ('system', 'System'),
    ], string="Alert Type", required=True, index=True)

    is_active = fields.Boolean(string="Active", default=True, index=True)

    res_model = fields.Char(string="Related Model", readonly=True)
    res_id = fields.Integer(string="Related Record ID", readonly=True)

    acknowledged_by_id = fields.Many2one(
        'res.users', string="Acknowledged By", readonly=True)
    acknowledged_at = fields.Datetime(string="Acknowledged At", readonly=True)

    def action_acknowledge(self):
        """Marks the alert as acknowledged by the current user."""
        self.ensure_one()
        if not self.is_active:
            raise UserError(_("This alert has already been resolved."))
        if self.acknowledged_by_id:
            raise UserError(
                _("This alert has already been acknowledged by %s.", self.acknowledged_by_id.name))

        self.write({
            'acknowledged_by_id': self.env.user.id,
            'acknowledged_at': fields.Datetime.now()
        })
        return True

    def action_resolve(self):
        """Marks the alert as inactive/resolved."""
        self.write({'is_active': False})
        return True

    def action_view_related_record(self):
        """
        Returns an action to view the source record of the alert, if one exists.
        """
        self.ensure_one()
        if not self.res_model or not self.res_id:
            raise UserError(_("This alert has no related record to view."))

        return {
            'type': 'ir.actions.act_window',
            'res_model': self.res_model,
            'res_id': self.res_id,
            'view_mode': 'form',
            'views': [(False, 'form')],
            'target': 'current',
        }