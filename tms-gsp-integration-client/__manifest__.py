# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'TMS :: GSP E-Invoicing Integration',
    'version': '18.0.1.0.0',
    'summary': 'Provides integration with GST Suvidha Providers (GSP) for Indian E-Invoicing compliance.',
    'description': """
This module handles all aspects of communicating with a GSP for generating
Invoice Reference Numbers (IRN) and QR codes as per Indian GST regulations.

Key Features:
- Extends the Customer Invoice form with E-Invoicing capabilities.
- Implements a resilient synchronous API call with an asynchronous fallback mechanism.
- Leverages Odoo's Job Queue for automated retries on API failures.
- Securely handles API credentials via an external secrets management service.
- Provides a user interface for manual intervention on failed submissions.
    """,
    'author': 'Your Company Name',
    'website': 'https://www.yourcompany.com',
    'category': 'Accounting/Localizations/EDI',
    'depends': [
        'account',
        'queue_job',
        'tms', # Assuming a base 'tms' module exists
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_config_parameter_data.xml',
        'views/account_move_view.xml',
    ],
    'external_dependencies': {
        'python': [
            'requests',
            'boto3',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'OEEL-1',
}