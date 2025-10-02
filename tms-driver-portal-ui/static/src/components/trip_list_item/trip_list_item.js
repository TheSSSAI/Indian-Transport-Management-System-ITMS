/** @odoo-module **/

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { StatusBadge } from "@tms_driver_portal/components/status_badge/status_badge";

/**
 * Trip List Item Component
 *
 * A reusable component that displays a summary of a single trip in a list.
 * It is designed to be used within the TripListScreen. It handles navigation
 * to the trip detail screen when clicked.
 *
 * @extends Component
 */
export class TripListItem extends Component {
    static template = "tms_driver_portal.TripListItem";
    static components = { StatusBadge };
    static props = {
        trip: {
            type: Object,
            shape: {
                id: Number,
                name: String,
                customer_name: String,
                source_location: String,
                destination_location: String,
                status: String,
                status_label: String,
            },
        },
    };

    /**
     * Setup for the TripListItem component.
     * Initializes the router service.
     */
    setup() {
        this.router = useService("router");
    }

    /**
     * Handles the click event on the trip item.
     * Navigates to the detailed view of the clicked trip.
     * @private
     * @param {Event} ev - The click event.
     */
    _onTripClick(ev) {
        ev.preventDefault();
        this.router.navigate({
            to: "TRIP_DETAIL",
            params: { id: this.props.trip.id },
        });
    }
}