# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

"""
This __init__.py file serves as the entry point for the Python components of the
tms_core Odoo module.

It is responsible for importing the sub-packages that contain the core business
logic and data models of the Transport Management System. By importing these
packages, it makes all the defined Odoo models, wizards, and their associated
business logic discoverable by the Odoo framework's ORM and module loading
mechanisms.

This file ensures that when the 'tms_core' module is loaded by an Odoo instance,
all the necessary Python classes are registered and integrated into the system.
"""

from . import models
from . import wizards