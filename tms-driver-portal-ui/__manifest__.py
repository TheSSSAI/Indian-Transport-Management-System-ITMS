# -*- coding: utf-8 -*-
{
    'name': 'Transport Management - Driver Portal',
    'version': '18.0.1.0.0',
    'category': 'Fleet Management',
    'summary': 'Provides a dedicated mobile-first web portal for drivers.',
    'description': """
This module implements the complete frontend application for the Driver Portal. 
It is built as a self-contained Odoo addon using the OWL 2.0 framework, JavaScript, and CSS. 

Its sole responsibility is to provide a responsive, mobile-first user experience for drivers, allowing them to:
- Securely log in to the system.
- View their list of current and past trips.
- Access detailed information for their assigned trips.
- Update trip statuses (e.g., start a trip).
- Log trip events (e.g., fueling, accident).
- Submit trip-related expenses with receipt uploads.
- Upload Proof of Delivery (POD) via photo or e-signature.
- Access self-service training materials.

This addon is architecturally decoupled from the backend business logic, interacting with the system exclusively through the Odoo ORM/controller APIs provided by the 'tms_core' module. This separation allows for independent development and iteration on the driver-facing UI/UX, focusing on usability and performance for on-the-go users.
    """,
    'author': 'FleetOps Inc.',
    'website': 'https://www.fleetops.com',
    'license': 'OEEL-1',
    'depends': [
        'web',
        'tms_core',
    ],
    'data': [
        # Data files are loaded first to be available for asset bundles
        'views/driver_portal_menus.xml',
        'views/driver_portal_templates.xml',
        # Asset definitions must be loaded before they are used
        'views/assets.xml',
    ],
    'assets': {
        'tms_driver_portal.driver_portal_assets': [
            # SCSS entrypoint
            'tms_driver_portal/static/src/scss/main.scss',
            # JavaScript entrypoint (which will mount the OWL application)
            'tms_driver_portal/static/src/main.js',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}