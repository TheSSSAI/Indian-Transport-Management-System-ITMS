/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/browser/hooks";
import { HeaderNav } from "../../components/header_nav/header_nav";
import { StatusBadge } from "../../components/status_badge/status_badge";

export class TripDetailScreen extends Component {
    static template = "tms_driver_portal.TripDetailScreen";
    static components = { HeaderNav, StatusBadge };
    static props = ["tripId"];

    setup() {
        this.router = useService("router");
        this.tripService = useService("trip");
        this.notification = useService("notification");

        this.state = useState({
            trip: null,
            isLoading: true,
            isSubmitting: false,
            hasError: false,
            errorMessage: "",
        });

        onWillStart(async () => {
            await this._loadTripDetails();
        });
    }

    get canStartTrip() {
        return this.state.trip && this.state.trip.status === "assigned";
    }

    get canDeliverTrip() {
        return this.state.trip && this.state.trip.status === "in_transit";
    }

    get canAddExpense() {
        const activeStatuses = ["assigned", "in_transit", "on_hold"];
        return this.state.trip && activeStatuses.includes(this.state.trip.status);
    }

    async _loadTripDetails() {
        this.state.isLoading = true;
        this.state.hasError = false;
        try {
            const tripData = await this.tripService.getTripDetails(this.props.tripId);
            this.state.trip = tripData;
        } catch (e) {
            this.state.hasError = true;
            this.state.errorMessage = e.message || "Could not load trip details.";
            this.notification.add(this.state.errorMessage, { type: "danger" });
        } finally {
            this.state.isLoading = false;
        }
    }

    async _onStartTrip() {
        if (!this.canStartTrip || this.state.isSubmitting) return;

        this.state.isSubmitting = true;
        try {
            await this.tripService.startTrip(this.state.trip.id);
            this.notification.add("Trip started successfully!", { type: "success" });
            await this._loadTripDetails(); // Refresh data
        } catch (e) {
            this.notification.add(e.message || "Failed to start trip.", { type: "danger" });
        } finally {
            this.state.isSubmitting = false;
        }
    }

    _onAddExpense() {
        if (!this.canAddExpense) return;
        this.router.navigate({
            name: "expense_form",
            params: { tripId: this.state.trip.id },
        });
    }

    _onDeliverTrip() {
        if (!this.canDeliverTrip) return;
        this.router.navigate({
            name: "pod_form",
            params: { tripId: this.state.trip.id },
        });
    }
}

registry.category("screens").add("trip_detail", TripDetailScreen);