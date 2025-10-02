/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, useState, useRef, onMounted, onWillUnmount } from "@odoo/owl";
import { useService } from "@web/core/browser/hooks";

import { TripListItem } from "../../components/trip_list_item/trip_list_item";
import { HeaderNav } from "../../components/header_nav/header_nav";

export class TripListScreen extends Component {
    static template = "tms_driver_portal.TripListScreen";
    static components = { TripListItem, HeaderNav };

    setup() {
        this.router = useService("router");
        this.tripService = useService("trip");
        this.notification = useService("notification");
        this.scrollContainerRef = useRef("scrollContainer");

        this.state = useState({
            isLoading: true,
            hasError: false,
            errorMessage: "",
            activeFilter: "current",
            trips: [],
            pagination: {
                offset: 0,
                limit: 20,
                hasMore: true,
            },
        });

        onWillStart(async () => {
            await this._loadTrips();
        });

        onMounted(() => {
            this.scrollContainerRef.el.addEventListener("scroll", this._onScroll.bind(this));
        });

        onWillUnmount(() => {
            this.scrollContainerRef.el.removeEventListener("scroll", this._onScroll.bind(this));
        });
    }

    async _loadTrips(append = false) {
        if (!this.state.pagination.hasMore && append) {
            return;
        }

        this.state.isLoading = true;
        this.state.hasError = false;

        try {
            const result = await this.tripService.fetchMyTrips({
                filter: this.state.activeFilter,
                offset: this.state.pagination.offset,
                limit: this.state.pagination.limit,
            });

            if (append) {
                this.state.trips.push(...result.trips);
            } else {
                this.state.trips = result.trips;
            }

            this.state.pagination.offset = this.state.trips.length;
            this.state.pagination.hasMore = result.trips.length === this.state.pagination.limit;
        } catch (e) {
            this.state.hasError = true;
            this.state.errorMessage = e.message || "An unknown error occurred while fetching trips.";
            this.notification.add(this.state.errorMessage, { type: "danger" });
        } finally {
            this.state.isLoading = false;
        }
    }

    async _onSwitchFilter(filter) {
        if (this.state.activeFilter === filter) {
            return;
        }
        this.state.activeFilter = filter;
        this.state.trips = [];
        this.state.pagination.offset = 0;
        this.state.pagination.hasMore = true;
        await this._loadTrips();
    }

    _onTripClick(tripId) {
        this.router.navigate({
            name: "trip_detail",
            params: { tripId: tripId },
        });
    }

    _onScroll(ev) {
        const { scrollTop, scrollHeight, clientHeight } = ev.target;
        // Trigger load more when user is 200px from the bottom
        if (scrollHeight - scrollTop - clientHeight < 200) {
            if (!this.state.isLoading && this.state.pagination.hasMore) {
                this._loadTrips(true);
            }
        }
    }
}

registry.category("screens").add("trip_list", TripListScreen);