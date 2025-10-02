# -*- coding: utf-8 -*-

import logging
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError

_logger = logging.getLogger(__name__)

class TmsExpense(models.Model):
    """
    Represents a single expense entry, which can be related to a trip or a vehicle directly.
    This model manages the lifecycle of an expense from submission to approval and reimbursement.
    It includes specific fields for fuel expenses to enable efficiency tracking.
    """
    _name = 'tms.expense'
    _description = 'Transport Management Expense'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'expense_date desc, id desc'

    name = fields.Char(string="Title", required=True, tracking=True)
    trip_id = fields.Many2one(
        'tms.trip',
        string='Trip',
        ondelete='cascade',
        index=True,
        help="The trip this expense is associated with."
    )
    driver_id = fields.Many2one(
        'hr.employee',
        string='Driver',
        required=True,
        index=True,
        domain="[('is_tms_driver', '=', True)]",
        help="The driver who incurred the expense."
    )
    vehicle_id = fields.Many2one(
        'tms.vehicle',
        string='Vehicle',
        required=True,
        index=True,
        help="The vehicle for which the expense was incurred."
    )
    expense_type = fields.Selection([
        ('diesel', 'Diesel'),
        ('toll', 'Toll'),
        ('food', 'Food'),
        ('repair', 'Repair'),
        ('maintenance', 'Maintenance'),
        ('fine', 'Fine'),
        ('other', 'Other'),
    ], string='Expense Type', required=True, tracking=True)
    
    amount = fields.Monetary(
        string='Amount',
        required=True,
        tracking=True,
        currency_field='company_currency_id'
    )
    expense_date = fields.Date(
        string='Expense Date',
        required=True,
        default=fields.Date.context_today,
        tracking=True
    )
    
    state = fields.Selection([
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='submitted', required=True, tracking=True, copy=False)

    receipt = fields.Binary(string="Receipt", attachment=True, help="Attach a photo or scan of the receipt.")
    receipt_filename = fields.Char(string="Receipt Filename")

    # Fuel-specific fields
    odometer = fields.Float(string='Odometer (km)', help="Vehicle's odometer reading at the time of fuel purchase.")
    fuel_quantity = fields.Float(string='Fuel Quantity (Liters)', help="Quantity of fuel purchased in liters.")

    rejection_reason = fields.Text(string="Rejection Reason", readonly=True, copy=False)
    
    company_currency_id = fields.Many2one(
        'res.currency',
        string='Company Currency',
        related='trip_id.company_id.currency_id',
        store=True,
        readonly=True
    )

    company_id = fields.Many2one('res.company', string='Company', related='trip_id.company_id', store=True, readonly=True)

    @api.constrains('odometer', 'vehicle_id', 'expense_type', 'expense_date')
    def _check_odometer(self):
        """
        Validates the odometer reading for diesel expenses.
        Ensures the entered value is greater than the most recently recorded reading for the vehicle.
        This implements business rule BR-009 / REQ-1-903.
        """
        for expense in self.filtered(lambda e: e.expense_type == 'diesel' and e.vehicle_id and e.odometer > 0):
            last_expense_with_odometer = self.search([
                ('vehicle_id', '=', expense.vehicle_id.id),
                ('expense_type', '=', 'diesel'),
                ('odometer', '>', 0),
                '|',
                ('expense_date', '<', expense.expense_date),
                '&',
                ('expense_date', '=', expense.expense_date),
                ('id', '<', expense.id) # For same-day entries
            ], order='expense_date desc, id desc', limit=1)

            if last_expense_with_odometer and expense.odometer <= last_expense_with_odometer.odometer:
                raise ValidationError(_(
                    "Odometer reading for '%(vehicle)s' must be greater than the last recorded value of %(last_odometer)s km.",
                    vehicle=expense.vehicle_id.truck_number,
                    last_odometer=last_expense_with_odometer.odometer
                ))

    @api.onchange('trip_id')
    def _onchange_trip_id(self):
        """Auto-populate driver and vehicle from the selected trip."""
        if self.trip_id:
            self.driver_id = self.trip_id.driver_id
            self.vehicle_id = self.trip_id.vehicle_id
    
    def action_approve(self):
        """
        Approves a submitted expense.
        This action is restricted to users with appropriate permissions (Dispatch Manager or Finance Officer).
        Implements User Story US-033.
        """
        if not self.user_has_groups('tms_core.group_tms_dispatch_manager,tms_core.group_tms_finance_officer'):
            raise UserError(_("You do not have the necessary permissions to approve expenses."))
        
        approved_expenses = self.filtered(lambda e: e.state == 'submitted')
        if not approved_expenses:
            raise UserError(_("Only submitted expenses can be approved."))
            
        approved_expenses.write({
            'state': 'approved'
        })
        for expense in approved_expenses:
            expense.message_post(body=_("Expense approved by %s.") % self.env.user.name)
        return True

    def action_reject(self):
        """
        Launches a wizard to capture the mandatory rejection reason.
        Implements User Story US-034.
        """
        if not self.user_has_groups('tms_core.group_tms_dispatch_manager,tms_core.group_tms_finance_officer'):
            raise UserError(_("You do not have the necessary permissions to reject expenses."))
        
        return {
            'name': _('Rejection Reason'),
            'type': 'ir.actions.act_window',
            'res_model': 'tms.reason.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_model': self._name,
                'default_record_ids': self.ids,
                'default_target_method': '_action_reject_with_reason',
            }
        }
    
    def _action_reject_with_reason(self, reason):
        """
        Internal method called by the reason wizard to perform the rejection.
        """
        rejected_expenses = self.filtered(lambda e: e.state == 'submitted')
        if not rejected_expenses:
            _logger.warning("Attempted to reject expenses not in 'submitted' state: %s", self.ids)
            return

        rejected_expenses.write({
            'state': 'rejected',
            'rejection_reason': reason
        })
        for expense in rejected_expenses:
            expense.message_post(body=_("Expense rejected by %(user)s. Reason: %(reason)s") % {
                'user': self.env.user.name,
                'reason': reason
            })