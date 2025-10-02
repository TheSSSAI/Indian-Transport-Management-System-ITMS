# -*- coding: utf-8 -*-
{
    'name': 'Transport Management System - Core',
    'version': '18.0.1.0.0',
    'category': 'Operations/Transport',
    'summary': """
        Core module for the Transport Management System.
        Manages master data (Vehicles, Drivers, Customers),
        the complete trip lifecycle, expense tracking, and provides
        foundational business logic for the TMS application.
    """,
    'description': """
        This repository is the core of the Transport Management System.
        It contains the fundamental Odoo 18 module that defines the data models
        (e.g., Trip, Vehicle, Driver), core business logic, workflow state
        machines, and access control rules (RBAC).

        Key Features:
        - Master Data Management for Vehicles, Drivers, Customers, Routes, Materials.
        - Comprehensive Trip Management with a strict lifecycle state machine.
        - Expense tracking and approval workflow.
        - Role-Based Access Control for Admin, Dispatch Manager, Finance Officer, and Driver roles.
        - Core backend views (Form, List, Kanban) for all models.
        - Foundation for integrations like GPS, GSP, and the Driver Portal.
    """,
    'author': 'Principal Software Architect',
    'website': 'https://www.example.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'mail',
        'hr',
        'account',
        'web',
    ],
    'data': [
        # 1. Security
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',

        # 2. Data
        'data/ir_sequence_data.xml',

        # 3. Wizards
        'wizards/tms_reason_wizard_views.xml',

        # 4. Views
        'views/tms_vehicle_views.xml',
        'views/hr_employee_views.xml',
        'views/res_partner_views.xml',
        'views/tms_route_views.xml',
        'views/tms_material_views.xml',
        'views/tms_trip_views.xml',
        'views/tms_expense_views.xml',
        'views/tms_card_views.xml',
        'views/tms_alert_views.xml',

        # 5. Menus (loaded last)
        'views/tms_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},
}