# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class TmsCard(models.Model):
    """
    Model for managing company-issued FASTag and diesel cards.
    Fulfills REQ-1-110 and user stories US-042, US-043, US-081.
    """
    _name = "tms.card"
    _description = "FASTag/Diesel Card Management"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Card Name", compute="_compute_name", store=True)
    card_number = fields.Char(string="Card Number", required=True, copy=False)
    card_number_masked = fields.Char(
        string="Card Number", compute="_compute_card_number_masked", store=True)
    card_type = fields.Selection([
        ('fastag', 'FASTag'),
        ('diesel', 'Diesel'),
        ('other', 'Other'),
    ], string="Card Type", required=True, default='other', index=True)

    provider = fields.Char(string="Provider")
    assigned_vehicle_id = fields.Many2one(
        'tms.vehicle', string="Assigned Vehicle", tracking=True)
    active = fields.Boolean(string="Active", default=True, tracking=True)

    currency_id = fields.Many2one(
        'res.currency', string='Currency',
        default=lambda self: self.env.company.currency_id)
    current_balance = fields.Monetary(string="Current Balance", tracking=True)
    low_balance_threshold = fields.Monetary(
        string="Low Balance Threshold", tracking=True)

    _sql_constraints = [
        ('card_number_uniq', 'unique (card_number)',
         'A card with this number already exists.')
    ]

    @api.depends('card_number', 'card_type')
    def _compute_name(self):
        for card in self:
            card_type_display = dict(
                card._fields['card_type'].selection).get(card.card_type)
            if card.card_number:
                card.name = f"{card_type_display} - ...{card.card_number[-4:]}"
            else:
                card.name = card_type_display or _("New Card")

    @api.depends('card_number')
    def _compute_card_number_masked(self):
        for card in self:
            if card.card_number and len(card.card_number) > 4:
                card.card_number_masked = f"************{card.card_number[-4:]}"
            else:
                card.card_number_masked = card.card_number

    @api.constrains('low_balance_threshold', 'current_balance')
    def _check_non_negative_values(self):
        for card in self:
            if card.low_balance_threshold < 0:
                raise ValidationError(
                    _("Low-Balance Threshold cannot be negative."))
            if card.current_balance < 0:
                raise ValidationError(
                    _("Current Balance cannot be negative."))

    def write(self, vals):
        """
        Overrides write to check for low balance threshold breach
        and trigger an alert.
        """
        Alert = self.env['tms.alert']
        tracked_vals = {}
        if 'current_balance' in vals:
            for card in self:
                old_balance = card.current_balance
                new_balance = vals.get('current_balance')
                threshold = card.low_balance_threshold
                if threshold > 0 and new_balance < threshold and old_balance >= threshold:
                    tracked_vals[card.id] = True

        res = super(TmsCard, self).write(vals)

        if tracked_vals:
            for card in self.filtered(lambda c: c.id in tracked_vals):
                # Resolve any existing low balance alert for this card
                existing_alerts = Alert.search([
                    ('res_model', '=', self._name),
                    ('res_id', '=', card.id),
                    ('alert_type', '=', 'low_balance'),
                    ('is_active', '=', True)
                ])
                if not existing_alerts:
                    Alert.create({
                        'name': _("Low Balance: %s", card.name),
                        'message': _(
                            "The balance for card %s (%s) has dropped to %s, which is below the threshold of %s.",
                            card.name, card.provider or '', card.current_balance, card.low_balance_threshold
                        ),
                        'alert_type': 'low_balance',
                        'res_model': self._name,
                        'res_id': card.id,
                    })

        # Clear active alerts if balance is replenished
        if 'current_balance' in vals:
            for card in self:
                if card.current_balance >= card.low_balance_threshold:
                    alerts_to_resolve = Alert.search([
                        ('res_model', '=', self._name),
                        ('res_id', '=', card.id),
                        ('alert_type', '=', 'low_balance'),
                        ('is_active', '=', True)
                    ])
                    if alerts_to_resolve:
                        alerts_to_resolve.action_resolve()

        return res