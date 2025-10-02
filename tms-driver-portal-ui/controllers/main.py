# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import odoo
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.home import Home
import logging

_logger = logging.getLogger(__name__)


class DriverPortalController(http.Controller):
    """
    Main controller for the TMS Driver Portal.

    This controller is responsible for serving the main entry point of the
    Driver Portal Single Page Application (SPA) built with OWL. It ensures
    that only authenticated users with the 'Driver' role can access the portal.
    """

    @http.route([
        '/my',
        '/my/<path:path>',
    ], type='http', auth='user', website=True)
    def driver_portal_home(self, **kwargs):
        """
        Serves the root of the Driver Portal SPA.

        This method catches all routes under '/my/' and serves the main
        template. This allows the client-side OWL router to handle all
        subsequent navigation.

        It performs a crucial authorization check to ensure the logged-in user
        is a designated driver. If not, they are redirected to the standard
        Odoo backend interface. This enforces the requirement for a distinct
        UI for the driver role (REQ-1-112).

        Args:
            **kwargs: Arbitrary keyword arguments, including path variables.

        Returns:
            An HTTP response that either renders the SPA template or redirects
            the user.
        """
        # Security: Enforce that only users in the 'Driver' group can access the portal.
        # This aligns with REQ-FNC-001 and the principle of least privilege.
        # We assume the core module defines 'tms_management.group_tms_driver'.
        is_driver = request.env.user.has_group('tms_management.group_tms_driver')

        if not is_driver:
            # If the user is not a driver (e.g., an admin or manager),
            # redirect them to the standard backend to avoid confusion or access errors.
            _logger.warning(
                "Non-driver user (ID: %s) attempted to access the Driver Portal. Redirecting to /web.",
                request.env.user.id
            )
            return request.redirect('/web')

        try:
            # Render the main template that will bootstrap the OWL application.
            # This template is defined in `views/driver_portal_templates.xml`.
            return request.render('tms_driver_portal.driver_portal_root', {})
        except ValueError as e:
            # This error typically occurs if the template is not found.
            # It's a configuration/development error, so we log it critically.
            _logger.critical(
                "Driver Portal root template 'tms_driver_portal.driver_portal_root' not found. Error: %s", e
            )
            # We can use the Home controller to render a standard Odoo error page.
            return Home().web_client(request.session, **kwargs)