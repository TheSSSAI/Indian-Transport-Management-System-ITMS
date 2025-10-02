/** @odoo-module **/

import { App, whenReady } from "@odoo/owl";
import { browser } from "@web/core/browser/browser";
import { registry } from "@web/core/registry";

// Root Component
import { DriverPortalApp } from "./views/driver_portal.js";

// Application Services
import { RouterService } from "./services/router_service.js";
import { SessionService } from "./services/session_service.js";
import { NotificationService } from "./services/notification_service.js";
import { BackendApiService } from "./services/backend_api_service.js";
import { TripService } from "./services/trip_service.js";
import { ExpenseService } from "./services/expense_service.js";
import { TrainingService } from "./services/training_service.js";

const { mount } = App;

/**
 * This file serves as the main entry point for the TMS Driver Portal OWL application.
 * It is responsible for:
 * 1. Defining the services that will be available throughout the application.
 * 2. Registering the client action that Odoo uses to launch the application.
 * 3. Creating and mounting the root OWL component (`DriverPortalApp`) into the DOM.
 */

// Define the client action tag that will be used in the XML to launch the portal.
const TmsDriverPortalClientAction = "tms_driver_portal.action_driver_portal_main";

// Get the client action registry from the Odoo web core.
const clientActionRegistry = registry.category("actions");

clientActionRegistry.add(TmsDriverPortalClientAction, {
    Component: DriverPortalApp,
    /**
     * The `target` property specifies where the Odoo web client should render this action.
     * 'new' indicates it should replace the current view in a new container,
     * effectively creating a single-page application experience.
     */
    target: "new",

    /**
     * Odoo 18 provides a simpler way to mount the root component.
     * We just need to define the services here. Odoo will handle the mounting.
     *
     * @returns {object} An object containing the service definitions.
     */
    get services() {
        /**
         * This object defines the dependency injection container for the OWL application.
         * Each key is a service name that can be requested by any component using `useService(serviceName)`.
         * Each value is the service class definition. OWL will instantiate these as singletons
         * for the application's lifecycle.
         */
        const services = {
            router: RouterService,
            session: SessionService,
            notification: NotificationService,
            backendAPI: BackendApiService,
            trip: TripService,
            expense: ExpenseService,
            training: TrainingService,
        };

        return services;
    },
});

// An alternative, more explicit way of mounting for older patterns or custom targets.
// The new `get services()` approach is preferred for Odoo 18.
// This is kept here for reference but the main logic uses the Odoo 18 style above.
/*
clientActionRegistry.add(TmsDriverPortalClientAction, async ({ env, props }) => {
    await whenReady();

    const services = {
        router: RouterService,
        session: SessionService,
        notification: NotificationService,
        backendAPI: BackendApiService,
        trip: TripService,
        expense: ExpenseService,
        training: TrainingService,
    };

    const app = new App(DriverPortalApp, {
        target: props.target,
        env: env,
        props: props,
        templates: env.getTemplates(),
        dev: env.debug,
        translateFn: env._t,
        services,
    });

    return mount(app, { target: props.target });
});
*/