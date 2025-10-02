# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# This file is necessary to make the 'tests' directory a Python package,
# allowing the Odoo test runner to discover and execute tests within this module.

# As tests are added for the Python components of this addon (e.g., controllers),
# they should be imported here. For example:
#
# from . import test_controllers
#
# Since tms_driver_portal is primarily a frontend (OWL) application,
# the majority of tests will be JavaScript-based (e.g., QUnit, Tours)
# and will not be imported here. Python tests would typically cover
# the controllers that serve the application and handle specific RPCs
# if any were defined outside the standard ORM methods.