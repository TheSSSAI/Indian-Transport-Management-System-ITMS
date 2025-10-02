# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

"""
This package is reserved for defining asynchronous background jobs using Odoo's
queue_job module.

In the current implementation, the job definition (_job_generate_einvoice) is
located directly on the account.move model for convenience and direct access
to the recordset. This file ensures the 'jobs' directory is recognized as a
Python package for potential future use if job definitions are refactored
into separate files for better organization.
"""