# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class TmsReasonWizard(models.TransientModel):
    """
    A generic wizard to capture a mandatory reason for various actions
    like cancellation, rejection, or resuming a trip.
    """
    _name = "tms.reason.wizard"
    _description = "Generic Reason Wizard for TMS"

    reason = fields.Text(string="Reason", required=True)

    def action_confirm(self):
        """
        Generic confirmation action. Reads the target model, record, and method
        from the context and executes it, passing the reason.
        This makes the wizard highly reusable.
        """
        self.ensure_one()
        context = self.env.context
        active_model = context.get('active_model')
        active_id = context.get('active_id')
        target_method_name = context.get('target_method')

        if not all([active_model, active_id, target_method_name]):
            raise UserError(
                _("Context is missing required keys (active_model, active_id, target_method)."))

        record = self.env[active_model].browse(active_id)

        if not hasattr(record, target_method_name):
            raise UserError(_("The target record of model '%s' does not have the method '%s'.",
                              active_model, target_method_name))

        # Get the method from the record
        target_method = getattr(record, target_method_name)

        # Call the target method with the reason
        # The target method is responsible for its own logic and state changes.
        return target_method(reason=self.reason)