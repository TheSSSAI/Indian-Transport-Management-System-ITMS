# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import unittest
from unittest.mock import patch, MagicMock

from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError, ValidationError

# Assuming custom exceptions are defined in the gsp_api_client
from odoo.addons.tms_gsp_integration.services.gsp_api_client import (
    GspApiDataError,
    GspApiTimeoutError,
    GspApiConnectionError
)

class TestGspService(TransactionCase):
    """
    Unit tests for the GspService orchestration logic.
    These tests mock the dependencies (ApiClient, Mapper, Job Queue) to isolate the
    service's behavior under various conditions.
    """

    def setUp(self):
        super(TestGspService, self).setUp()
        self.GspService = self.env['tms_gsp_integration.gsp_service']

        # Create a test customer and invoice
        self.partner = self.env['res.partner'].create({
            'name': 'Test Customer',
            'vat': '27AAFCE1234A1Z5',  # Valid GSTIN for testing
        })
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
            'l10n_in_hsn_code': '9983',
        })
        self.invoice = self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.partner.id,
            'invoice_date': '2024-01-01',
            'invoice_line_ids': [(0, 0, {
                'product_id': self.product.id,
                'quantity': 1,
                'price_unit': 1000,
            })],
        })
        self.invoice.action_post()

    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspRequestMapper')
    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspApiClient')
    def test_generate_einvoice_sync_success(self, MockGspApiClient, MockGspRequestMapper):
        """
        Test the successful synchronous e-invoice generation path.
        Verifies that the API client is called and the invoice is updated with the IRN.
        """
        # Arrange
        mock_api_client_instance = MockGspApiClient.return_value
        mock_mapper_instance = MockGspRequestMapper.return_value

        mock_payload = {'test_payload': 'data'}
        mock_mapper_instance.map_invoice_to_gsp_payload.return_value = mock_payload

        mock_api_response = {
            'Success': True,
            'Irn': 'TEST_IRN_12345',
            'SignedQRCode': 'TEST_QR_CODE_DATA',
        }
        mock_api_client_instance.send_invoice_data.return_value = mock_api_response

        # Act
        self.GspService.generate_einvoice(self.invoice)

        # Assert
        mock_mapper_instance.map_invoice_to_gsp_payload.assert_called_once_with(self.invoice)
        mock_api_client_instance.send_invoice_data.assert_called_once_with(mock_payload)

        self.assertEqual(self.invoice.gsp_status, 'generated')
        self.assertEqual(self.invoice.gsp_irn, 'TEST_IRN_12345')
        self.assertEqual(self.invoice.gsp_qr_code, 'TEST_QR_CODE_DATA')
        self.assertFalse(self.invoice.gsp_error_message)

    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspRequestMapper')
    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspApiClient')
    @patch('odoo.addons.tms_gsp_integration.models.account_move.AccountMove.with_delay')
    def test_generate_einvoice_async_fallback_on_timeout(self, mock_with_delay, MockGspApiClient, MockGspRequestMapper):
        """
        Test the asynchronous fallback mechanism on a timeout error from the GSP API.
        Verifies the invoice status is set to 'pending' and a background job is enqueued.
        """
        # Arrange
        mock_api_client_instance = MockGspApiClient.return_value
        mock_mapper_instance = MockGspRequestMapper.return_value

        mock_payload = {'test_payload': 'data'}
        mock_mapper_instance.map_invoice_to_gsp_payload.return_value = mock_payload

        # Simulate a timeout from the API client
        mock_api_client_instance.send_invoice_data.side_effect = GspApiTimeoutError("Request timed out")

        # Act
        self.GspService.generate_einvoice(self.invoice)

        # Assert
        mock_mapper_instance.map_invoice_to_gsp_payload.assert_called_once_with(self.invoice)
        mock_api_client_instance.send_invoice_data.assert_called_once_with(mock_payload)
        
        self.assertEqual(self.invoice.gsp_status, 'pending')
        self.assertTrue('Request timed out' in self.invoice.gsp_error_message)
        self.assertFalse(self.invoice.gsp_irn)

        # Check if the job was enqueued
        mock_with_delay.assert_called_once()
        mock_with_delay.return_value._job_generate_einvoice.assert_called_once()

    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspRequestMapper')
    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspApiClient')
    @patch('odoo.addons.tms_gsp_integration.models.account_move.AccountMove.with_delay')
    def test_generate_einvoice_async_fallback_on_connection_error(self, mock_with_delay, MockGspApiClient, MockGspRequestMapper):
        """
        Test the asynchronous fallback mechanism on a connection error from the GSP API.
        Verifies the invoice status is set to 'pending' and a background job is enqueued.
        """
        # Arrange
        mock_api_client_instance = MockGspApiClient.return_value
        mock_api_client_instance.send_invoice_data.side_effect = GspApiConnectionError("GSP unreachable")
        mock_mapper_instance = MockGspRequestMapper.return_value
        mock_mapper_instance.map_invoice_to_gsp_payload.return_value = {}

        # Act
        self.GspService.generate_einvoice(self.invoice)

        # Assert
        self.assertEqual(self.invoice.gsp_status, 'pending')
        self.assertTrue('GSP unreachable' in self.invoice.gsp_error_message)
        mock_with_delay.assert_called_once()
        mock_with_delay.return_value._job_generate_einvoice.assert_called_once()

    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspRequestMapper')
    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspApiClient')
    @patch('odoo.addons.tms_gsp_integration.models.account_move.AccountMove.with_delay')
    def test_generate_einvoice_immediate_failure_on_data_error(self, mock_with_delay, MockGspApiClient, MockGspRequestMapper):
        """
        Test the immediate failure path for a 4xx data-related error from the GSP API.
        Verifies the invoice status is set to 'failed' and no background job is created.
        """
        # Arrange
        mock_api_client_instance = MockGspApiClient.return_value
        mock_mapper_instance = MockGspRequestMapper.return_value
        mock_mapper_instance.map_invoice_to_gsp_payload.return_value = {}

        # Simulate a 400 Bad Request from the API client
        mock_api_client_instance.send_invoice_data.side_effect = GspApiDataError("Invalid GSTIN for recipient")

        # Act
        self.GspService.generate_einvoice(self.invoice)

        # Assert
        mock_api_client_instance.send_invoice_data.assert_called_once()
        
        self.assertEqual(self.invoice.gsp_status, 'failed')
        self.assertEqual(self.invoice.gsp_error_message, 'Invalid GSTIN for recipient')
        self.assertFalse(self.invoice.gsp_irn)

        # Check that the job was NOT enqueued
        mock_with_delay.assert_not_called()

    @patch('odoo.addons.tms_gsp_integration.services.gsp_service.GspRequestMapper')
    def test_generate_einvoice_raises_error_on_mapping_failure(self, MockGspRequestMapper):
        """Test that if the data mapper raises an error (e.g., missing data), the service fails gracefully."""
        # Arrange
        mock_mapper_instance = MockGspRequestMapper.return_value
        mock_mapper_instance.map_invoice_to_gsp_payload.side_effect = ValueError("HSN code is missing for a line item.")

        # Act & Assert
        with self.assertRaises(ValidationError) as e:
            self.GspService.generate_einvoice(self.invoice)
        
        self.assertIn("HSN code is missing", str(e.exception))
        self.assertEqual(self.invoice.gsp_status, 'failed')
        self.assertIn("HSN code is missing", self.invoice.gsp_error_message)

if __name__ == '__main__':
    unittest.main()