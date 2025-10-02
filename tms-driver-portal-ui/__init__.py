# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# This init file is used to import the Python packages of the addon.
# When the Odoo server loads this module, it executes this file,
# making the imported submodules available to the framework.

# In the case of the 'tms_driver_portal' addon, the primary Python component
# is the controller, which is responsible for serving the main OWL application
# template and handling specific HTTP routes.
from . import controllers