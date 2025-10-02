# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError, AccessError

class TmsTrip(models.Model):
    """
    The central transactional model for managing a transport job from planning to payment.
    This model orchestrates the trip lifecycle, enforces business rules, and aggregates
    financial data like revenue and profitability.
    """
    _name = 'tms.trip'
    _description = 'Transport Management Trip'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'create_date desc'

    # Core Fields
    name = fields.Char(
        string='Trip ID', required=True, readonly=True, copy=False,
        default=lambda self: _('New'), index=True,
    )
    state = fields.Selection(
        [
            ('planned', 'Planned'),
            ('assigned', 'Assigned'),
            ('in_transit', 'In-Transit'),
            ('on_hold', 'On Hold'),
            ('delivered', 'Delivered'),
            ('completed', 'Completed'),
            ('invoiced', 'Invoiced'),
            ('paid', 'Paid'),
            ('canceled', 'Canceled'),
        ],
        string='Status', default='planned', tracking=True, index=True,
        help="The current stage of the trip in its lifecycle."
    )

    # Relational Fields (Master Data)
    customer_id = fields.Many2one(
        'res.partner', string='Customer', required=True,
        domain="[('is_tms_customer', '=', True), ('active', '=', True)]",
        tracking=True
    )
    vehicle_id = fields.Many2one(
        'tms.vehicle', string='Vehicle',
        domain="[('active', '=', True)]",
        tracking=True, copy=False
    )
    driver_id = fields.Many2one(
        'hr.employee', string='Driver',
        domain="[('is_tms_driver', '=', True), ('active', '=', True)]",
        tracking=True, copy=False
    )
    route_id = fields.Many2one(
        'tms.route', string='Pre-defined Route',
        help="Select a pre-defined route to auto-populate source, destination, and distance."
    )
    material_id = fields.Many2one(
        'tms.material', string='Material', required=True
    )

    # Trip Details
    source_location = fields.Char(string='Source', required=True)
    destination_location = fields.Char(string='Destination', required=True)
    expected_delivery_date = fields.Datetime(string='Expected Delivery Date', required=True)
    actual_delivery_date = fields.Datetime(string='Actual Delivery Date', readonly=True)

    # Financials
    currency_id = fields.Many2one('res.currency', related='company_id.currency_id', store=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

    rate_type = fields.Selection(
        [
            ('fixed', 'Fixed'),
            ('per_km', 'Per KM'),
            ('per_ton', 'Per Ton'),
        ],
        string='Rate Type', required=True, default='fixed'
    )
    rate = fields.Float(string='Rate', digits='Product Price')
    weight = fields.Float(string='Weight (Tons)', help="Weight of the material in tons.")
    distance_km = fields.Float(string='Distance (KM)')
    
    total_revenue = fields.Monetary(
        string='Total Revenue', compute='_compute_total_revenue',
        store=True, help="Calculated revenue based on rate, type, weight, and distance."
    )
    total_approved_expenses = fields.Monetary(
        string='Total Approved Expenses', compute='_compute_profitability',
        store=True, help="Sum of all approved expenses for this trip."
    )
    profitability = fields.Monetary(
        string='Profitability', compute='_compute_profitability',
        store=True, help="Net profit or loss for the trip (Revenue - Approved Expenses)."
    )

    # Child Records (Links to Level 2 models)
    expense_ids = fields.One2many('tms.expense', 'trip_id', string='Expenses')
    pod_ids = fields.One2many('tms.pod', 'trip_id', string='Proof of Deliveries')
    event_ids = fields.One2many('tms.trip.event', 'trip_id', string='Trip Events')

    # Audit & Cancellation
    cancellation_reason = fields.Text(string="Cancellation Reason", readonly=True)


    # --------------------------------------------------
    # Constraints and Validations
    # --------------------------------------------------
    
    _sql_constraints = [
        ('name_uniq', 'unique(name)', 'Trip ID must be unique!')
    ]

    @api.constrains('vehicle_id', 'weight')
    def _check_vehicle_capacity(self):
        """ Enforces REQ-1-902 and BR-007 """
        for trip in self:
            if trip.vehicle_id and trip.weight > trip.vehicle_id.capacity:
                raise ValidationError(_(
                    "Material weight (%(weight)s Tons) exceeds the selected vehicle's capacity (%(capacity)s Tons)."
                ) % {'weight': trip.weight, 'capacity': trip.vehicle_id.capacity})

    @api.constrains('driver_id')
    def _check_driver_license(self):
        """ Enforces REQ-1-901 and BR-003 """
        for trip in self:
            if trip.driver_id and trip.driver_id.license_expiry_date and \
               trip.driver_id.license_expiry_date < fields.Date.today():
                raise ValidationError(_(
                    "Cannot assign driver %(driver)s. Their license expired on %(date)s."
                ) % {'driver': trip.driver_id.name, 'date': trip.driver_id.license_expiry_date})
    
    @api.constrains('expected_delivery_date')
    def _check_expected_delivery_date(self):
        """ Enforces BR-008 """
        for trip in self:
            if trip.expected_delivery_date and trip.expected_delivery_date < fields.Datetime.now():
                raise ValidationError(_("Expected Delivery Date cannot be in the past."))

    # --------------------------------------------------
    # ORM Overrides
    # --------------------------------------------------

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('tms.trip') or _('New')
        return super(TmsTrip, self).create(vals_list)

    def write(self, vals):
        """
        Handle automatic state transition from 'Planned' to 'Assigned'
        when both vehicle and driver are set.
        """
        res = super(TmsTrip, self).write(vals)
        for trip in self:
            if trip.state == 'planned' and trip.vehicle_id and trip.driver_id:
                trip.state = 'assigned'
        return res

    # --------------------------------------------------
    # Computed Fields Logic
    # --------------------------------------------------

    @api.depends('rate_type', 'rate', 'weight', 'distance_km')
    def _compute_total_revenue(self):
        """ Calculates trip revenue based on the selected rate type. """
        for trip in self:
            if trip.rate_type == 'fixed':
                trip.total_revenue = trip.rate
            elif trip.rate_type == 'per_km':
                trip.total_revenue = trip.rate * trip.distance_km
            elif trip.rate_type == 'per_ton':
                trip.total_revenue = trip.rate * trip.weight
            else:
                trip.total_revenue = 0.0

    @api.depends('total_revenue', 'expense_ids.state', 'expense_ids.amount')
    def _compute_profitability(self):
        """ 
        Calculates total approved expenses and net profitability.
        Fulfills REQ-1-111 and REQ-1-109.
        """
        for trip in self:
            approved_expenses = sum(
                trip.expense_ids.filtered(lambda e: e.state == 'approved').mapped('amount')
            )
            trip.total_approved_expenses = approved_expenses
            trip.profitability = trip.total_revenue - approved_expenses
    
    # --------------------------------------------------
    # Onchange Handlers
    # --------------------------------------------------
    
    @api.onchange('route_id')
    def _onchange_route_id(self):
        """ Auto-populates fields when a pre-defined route is selected. Fulfills US-028. """
        if self.route_id:
            self.source_location = self.route_id.source_location
            self.destination_location = self.route_id.destination_location
            self.distance_km = self.route_id.standard_distance
        else:
            self.source_location = False
            self.destination_location = False
            self.distance_km = 0.0

    # --------------------------------------------------
    # Action Methods (State Machine Transitions)
    # --------------------------------------------------
    
    def action_start_trip(self):
        self.ensure_one()
        if self.state != 'assigned':
            raise UserError(_("Trip must be in 'Assigned' state to be started."))
        # Security check: In a controller context, ensure `self.env.user` matches driver's user.
        # Here we assume it's triggered from a trusted context or checked before calling.
        self.write({'state': 'in_transit'})
        # Log the 'Trip Start' event
        self.env['tms.trip.event'].create({
            'trip_id': self.id,
            'driver_id': self.driver_id.id,
            'event_type': 'trip_start'
        })
        return True

    def action_put_on_hold(self, reason=''):
        """ Can be called automatically or manually """
        self.ensure_one()
        if self.state != 'in_transit':
             raise UserError(_("Only an 'In-Transit' trip can be put on hold."))
        self.write({'state': 'on_hold'})
        if reason:
            self.message_post(body=_("Trip put on hold. Reason: %s") % reason)
        return True

    def action_resume_from_hold(self):
        """ Launches wizard to get reason for resuming. Fulfills REQ-1-103. """
        self.ensure_one()
        if not self.env.user.has_group('tms_core.group_tms_dispatch_manager'):
             raise AccessError(_("Only a Dispatch Manager can resume a trip."))

        return {
            'type': 'ir.actions.act_window',
            'name': _('Resume Trip'),
            'res_model': 'tms.reason.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_model': self._name,
                'default_res_id': self.id,
                'default_target_method': '_execute_resume_trip',
                'title': 'Resume Trip'
            }
        }

    def _execute_resume_trip(self, reason):
        self.ensure_one()
        if self.state != 'on_hold':
            raise UserError(_("Trip must be 'On Hold' to be resumed."))
        self.write({'state': 'in_transit'})
        self.message_post(body=_("Trip resumed. Resolution: %s") % reason)

    def action_deliver(self, pod_id, recipient_name):
        self.ensure_one()
        if self.state != 'in_transit':
             raise UserError(_("Only an 'In-Transit' trip can be marked as delivered."))
        self.write({
            'state': 'delivered',
            'actual_delivery_date': fields.Datetime.now()
        })
        # The POD record creation is handled by the controller that calls this.
        self.message_post(body=_("Trip delivered to %s.") % recipient_name)
        return True

    def action_complete(self):
        self.ensure_one()
        if self.state != 'delivered':
             raise UserError(_("Only a 'Delivered' trip can be marked as complete."))
        self.write({'state': 'completed'})
        return True
    
    def action_generate_invoice(self):
        # This will be implemented more fully with integration to account.move
        self.ensure_one()
        if self.state != 'completed':
            raise UserError(_("Only a 'Completed' trip can be invoiced."))
        # Logic to create account.move would go here
        # For now, just change state
        self.write({'state': 'invoiced'})
        return True

    def action_cancel(self):
        """ Launches wizard to get mandatory cancellation reason. Fulfills REQ-1-104 """
        self.ensure_one()
        if self.state in ('delivered', 'completed', 'invoiced', 'paid', 'canceled'):
            raise UserError(_("Cannot cancel a trip that has already been delivered or processed."))
        
        return {
            'type': 'ir.actions.act_window',
            'name': _('Cancel Trip'),
            'res_model': 'tms.reason.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_model': self._name,
                'default_res_id': self.id,
                'default_target_method': '_execute_cancel',
                'title': 'Cancel Trip'
            }
        }

    def _execute_cancel(self, reason):
        self.ensure_one()
        self.write({
            'state': 'canceled',
            'cancellation_reason': reason
        })
        self.message_post(body=_("Trip Canceled. Reason: %s") % reason)
        # TODO: Trigger notification to driver (US-082)
        # self._send_cancellation_notification()