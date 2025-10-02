/** @odoo-module **/

/**
 * Service to handle backend communication for fetching Help & Training materials.
 * This service provides a clean API for the UI components to get the list of
 * training videos and documents available to the driver.
 */
export const trainingService = {
    dependencies: ["rpc", "notification"],

    /**
     * @param {import("@web/env").OdooEnv} env
     * @param {{ rpc: import("@web/core/network/rpc_service").RPCService, notification: import("@web/core/notifications/notification_service").NotificationService }} services
     */
    start(env, { rpc, notification }) {
        this.rpc = rpc;
        this.notification = notification;

        /**
         * Fetches the list of available training materials for the current user.
         * Corresponds to US-092 and Sequence Diagram 236.
         * @returns {Promise<Array<object>|null>} A promise that resolves to an array of training material objects or null on failure.
         */
        const fetchTrainingMaterials = async () => {
            try {
                const materials = await this.rpc("/tms/training_materials", {});
                return materials;
            } catch (e) {
                console.error("Failed to fetch training materials:", e);
                this.notification.add(
                    "Could not load training materials. Please check your connection and try again.", {
                        title: "Network Error",
                        type: "danger",
                    }
                );
                return null;
            }
        };

        return {
            fetchTrainingMaterials,
        };
    },
};