# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from unittest.mock import patch

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError, ValidationError

class TestAccountMoveGspIntegration(TransactionCase):
    """
    Integration tests for the methods added to the account.move model.
    These tests verify the behavior of the action methods, their preconditions,
    and their interaction with the GspService.
    """

    def setUp(self):
        super(TestAccountMoveGspIntegration, self).setUp()
        
        # User setup
        self.finance_officer_group = self.env.ref('account.group_account_invoice')
        self.finance_user = self.env['res.users'].create({
            'name': 'Finance Officer',
            'login': 'finance_officer',
            'groups_id': [(6, 0, [self.finance_officer_group.id])]
        })

        # Test data setup
        self.partner = self.env['res.partner'].create({
            'name': 'Test B2B Customer',
            'vat': '29AAFCE1234A1Z5',  # Valid GSTIN
        })
        self.product = self.env['product.product'].create({
            'name': 'Test Service',
            'l10n_in_hsn_code': '9983',
        })
        self.invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner.id,
            'invoice_date': '2024-01-15',
            'invoice_line_ids': [(0, 0, {
                'product_id': self.product.id,
                'quantity': 1,
                'price_unit': 100.0,
            })],
        })

    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspService.generate_einvoice')
    def test_action_generate_einvoice_success(self, mock_generate_einvoice):
        """Test that the action method calls the GspService for a posted invoice."""
        # Arrange
        self.invoice.action_post()
        self.assertEqual(self.invoice.state, 'posted')
        self.assertEqual(self.invoice.gsp_status, 'not_generated')

        # Act
        self.invoice.with_user(self.finance_user).action_generate_einvoice()

        # Assert
        mock_generate_einvoice.assert_called_once_with(self.invoice)

    def test_action_generate_einvoice_raises_error_if_not_posted(self):
        """Test that an error is raised if trying to generate for a draft invoice."""
        # Arrange
        self.assertEqual(self.invoice.state, 'draft')

        # Act & Assert
        with self.assertRaises(UserError) as e:
            self.invoice.with_user(self.finance_user).action_generate_einvoice()
        
        self.assertIn("Only posted invoices can be submitted for e-invoicing.", str(e.exception))
        self.assertEqual(self.invoice.gsp_status, 'not_generated')

    def test_action_generate_einvoice_raises_error_if_no_gstin(self):
        """Test that an error is raised if the customer has no GSTIN."""
        # Arrange
        self.partner.vat = False
        self.invoice.action_post()
        
        # Act & Assert
        with self.assertRaises(ValidationError) as e:
            self.invoice.with_user(self.finance_user).action_generate_einvoice()

        self.assertIn("Customer GSTIN is required for e-invoicing.", str(e.exception))
        self.assertEqual(self.invoice.gsp_status, 'not_generated')

    @patch('odoo.addons.tms_gsp_integration.models.account_move.AccountMove.action_generate_einvoice')
    def test_action_retry_einvoice_success(self, mock_action_generate):
        """Test that the retry action calls the main generation action for a failed invoice."""
        # Arrange
        self.invoice.gsp_status = 'failed'

        # Act
        self.invoice.with_user(self.finance_user).action_retry_einvoice()

        # Assert
        mock_action_generate.assert_called_once()

    def test_action_retry_einvoice_raises_error_if_not_failed(self):
        """Test that retry is not allowed if the invoice is not in a 'failed' state."""
        # Arrange
        self.invoice.gsp_status = 'generated'

        # Act & Assert
        with self.assertRaises(UserError) as e:
            self.invoice.with_user(self.finance_user).action_retry_einvoice()
        
        self.assertIn("Retry is only possible for invoices that have a 'Failed' e-invoice status.", str(e.exception))
        
    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspService.generate_einvoice')
    def test_job_generate_einvoice_flow(self, mock_generate_einvoice):
        """Test the background job method calls the GspService."""
        # This is a simplified test for the job method itself.
        # The queueing mechanism is tested in test_gsp_service.py.
        # Arrange
        self.invoice.gsp_status = 'pending'
        
        # Act
        # In a real job scenario, 'self' would be the recordset for the job.
        self.invoice._job_generate_einvoice()
        
        # Assert
        mock_generate_einvoice.assert_called_once_with(self.invoice)
        
    def test_job_generate_einvoice_skips_if_not_pending(self):
        """Test that the job aborts if the invoice is no longer pending (e.g., manually handled)."""
        with patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspService.generate_einvoice') as mock_generate:
            # Arrange
            self.invoice.gsp_status = 'generated' # Status changed by another process
            
            # Act
            self.invoice._job_generate_einvoice()
            
            # Assert
            mock_generate.assert_not_called()