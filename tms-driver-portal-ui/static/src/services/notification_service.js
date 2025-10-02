/** @odoo-module **/

/**
 * @typedef {'success' | 'warning' | 'danger' | 'info'} NotificationType
 */

/**
 * Service to handle UI notifications for the Driver Portal.
 *
 * This service acts as a wrapper around Odoo's core notification service.
 * It provides a simplified and consistent API for displaying toast-style
 * notifications (success, warning, error, info) to the user. This abstraction
 * helps centralize notification logic and makes it easier to replace the
 * underlying notification system in the future if needed.
 */
export const notificationService = {
    dependencies: ["notification"],

    /**
     * @param {import("@web/env").OdooEnv} env
     * @param {{ notification: import("@web/core/notifications/notification_service").NotificationService }} services
     */
    start(env, { notification }) {
        this.notification = notification;

        /**
         * Displays a generic notification.
         *
         * @param {object} params
         * @param {string} params.message The main text content of the notification.
         * @param {string} [params.title] The title of the notification.
         * @param {NotificationType} [params.type='info'] The type of notification.
         * @param {boolean} [params.sticky=false] Whether the notification should stay until closed.
         */
        const add = (params) => {
            return this.notification.add(params.message, {
                title: params.title,
                type: params.type || "info",
                sticky: params.sticky || false,
            });
        };

        /**
         * Displays a success notification.
         *
         * @param {object} params
         * @param {string} params.message The message to display.
         * @param {string} [params.title='Success'] The title of the notification.
         */
        const success = (params) => {
            return add({
                title: params.title || "Success",
                message: params.message,
                type: "success",
            });
        };

        /**
         * Displays a warning notification.
         *
         * @param {object} params
         * @param {string} params.message The message to display.
         * @param {string} [params.title='Warning'] The title of the notification.
         */
        const warning = (params) => {
            return add({
                title: params.title || "Warning",
                message: params.message,
                type: "warning",
            });
        };

        /**
         * Displays an error (danger) notification.
         *
         * @param {object} params
         * @param {string} params.message The message to display.
         * @param {string} [params.title='Error'] The title of the notification.
         */
        const error = (params) => {
            return add({
                title: params.title || "Error",
                message: params.message,
                type: "danger",
                sticky: true, // Errors should be sticky by default
            });
        };

        /**
         * Displays an info notification.
         *
         * @param {object} params
         * @param {string} params.message The message to display.
         * @param {string} [params.title='Information'] The title of the notification.
         */
        const info = (params) => {
            return add({
                title: params.title || "Information",
                message: params.message,
                type: "info",
            });
        };

        return {
            add,
            success,
            warning,
            error,
            info,
        };
    },
};