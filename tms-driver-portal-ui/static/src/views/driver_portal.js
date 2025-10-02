/** @odoo-module **/

import { Component, useState, onWillStart, onMounted, onWillUnmount, onError } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

import { TripListScreen } from "./trip_list_screen/trip_list_screen";
import { TripDetailScreen } from "./trip_detail_screen/trip_detail_screen";
import { ExpenseFormScreen } from "./expense_form_screen/expense_form_screen";
import { PodFormScreen } from "./pod_form_screen/pod_form_screen";
import { TrainingScreen } from "./training_screen/training_screen";
// Assuming a LoginScreen component exists at level 3 as well
// If it doesn't, we define a basic one or assume its existence for a complete app structure.
// For enterprise-grade code, it's better to import it explicitly.
// Let's assume a path for it, e.g., "tms_driver_portal/static/src/views/login_screen/login_screen.js"
import { LoginScreen } from "./login_screen/login_screen";
import { HeaderNav } from "../components/header_nav/header_nav";

/**
 * The root component of the Driver Portal application.
 *
 * This component acts as the main entry point and orchestrator for the SPA.
 * Its primary responsibilities are:
 * 1.  Checking the user's session state to determine if they are logged in.
 * 2.  Rendering the LoginScreen for unauthenticated users.
 * 3.  Rendering the main application layout (Header, content) for authenticated users.
 * 4.  Acting as a "router-view" by dynamically rendering the current screen
 *     component provided by the router service.
 * 5.  Handling global application state changes, like login/logout events.
 */
export class DriverPortal extends Component {
    static template = "tms_driver_portal.DriverPortal";
    static components = {
        LoginScreen,
        HeaderNav,
        TripListScreen,
        TripDetailScreen,
        ExpenseFormScreen,
        PodFormScreen,
        TrainingScreen,
    };

    setup() {
        this.router = useService("router");
        this.session = useService("session");
        this.notification = useService("notification");

        this.state = useState({
            isLoggedIn: false,
            isLoading: true, // Start in loading state for initial session check
            currentRoute: this.router.currentRoute,
        });

        onWillStart(async () => {
            try {
                const sessionInfo = await this.session.checkSession();
                this.state.isLoggedIn = sessionInfo && sessionInfo.uid;
                if (!this.state.isLoggedIn) {
                    // Ensure router is at a sane default for login screen
                    this.router.navigate("/login");
                }
            } catch (error) {
                console.error("Session check failed:", error);
                this.state.isLoggedIn = false;
                this.router.navigate("/login");
            } finally {
                this.state.isLoading = false;
            }
        });

        onMounted(() => {
            this.env.bus.on("ROUTE_CHANGED", this, this._onRouteChanged);
            this.env.bus.on("SESSION_CHANGED", this, this._onSessionChanged);
        });

        onWillUnmount(() => {
            this.env.bus.off("ROUTE_CHANGED", this, this._onRouteChanged);
            this.env.bus.off("SESSION_CHANGED", this, this._onSessionChanged);
        });
        
        onError((error) => {
            // Global error boundary for the entire driver portal app
            console.error("An unhandled error occurred in the Driver Portal:", error);
            // Optionally, you can show a generic error component here
            // this.notification.add("An unexpected error occurred. Please refresh the page.", { type: "danger" });
        });
    }

    /**
     * Handles updates from the router service when the route changes.
     * @param {object} detail - The event detail containing the new route.
     * @param {object} detail.route - The new route object from the router service.
     */
    _onRouteChanged(detail) {
        const { route } = detail;
        if (route) {
            this.state.currentRoute = route;
        }
    }

    /**
     * Handles global session state changes (login/logout).
     * @param {object} detail - The event detail containing session information.
     * @param {boolean} detail.isLoggedIn - The new login status.
     */
    _onSessionChanged(detail) {
        const { isLoggedIn } = detail;
        this.state.isLoggedIn = isLoggedIn;
        if (isLoggedIn) {
            // After login, navigate to the default authenticated route
            this.router.navigate("/");
        } else {
            // After logout, navigate to the login screen
            this.router.navigate("/login");
        }
    }

    /**
     * Provides props to the dynamically rendered component.
     * @returns {object} The props object for the current component.
     */
    get componentProps() {
        return this.state.currentRoute ? this.state.currentRoute.props : {};
    }
}