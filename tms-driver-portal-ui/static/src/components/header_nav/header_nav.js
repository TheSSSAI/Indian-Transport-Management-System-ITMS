/** @odoo-module **/

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * Header Navigation Component for the Driver Portal.
 *
 * Provides a consistent header across all screens, displaying the current
 * screen's title, a back button for navigation, and a menu toggle button.
 * The visibility of the back and menu buttons is controlled by props.
 *
 * @extends Component
 */
export class HeaderNav extends Component {
    static template = "tms_driver_portal.HeaderNav";
    static props = {
        title: { type: String, optional: true },
        showBackButton: { type: Boolean, optional: true },
        showMenuButton: { type: Boolean, optional: true },
    };

    /**
     * Setup for the HeaderNav component.
     * Initializes services and state.
     */
    setup() {
        this.router = useService("router");

        this.state = useState({
            // The title can be updated dynamically if needed in the future
            title: this.props.title || "Driver Portal",
        });
    }

    /**
     * Handles the click event on the back button.
     * Navigates to the previous screen using the router service.
     * @private
     */
    _onBackClick() {
        this.router.back();
    }

    /**
     * Handles the click event on the menu button.
     * Emits a custom 'open-menu' event to be handled by the parent component.
     * @private
     */
    _onMenuClick() {
        this.env.bus.trigger("tms-open-menu");
    }
}