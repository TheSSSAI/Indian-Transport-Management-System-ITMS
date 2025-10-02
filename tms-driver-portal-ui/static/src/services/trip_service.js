/** @odoo-module **/

/**
 * Service to handle all backend communications related to Trips.
 * This service abstracts the Odoo RPC calls for trip management,
 * providing a clean, async-based API for UI components. It centralizes
 * model names, method names, and error handling for all trip-related operations.
 */
export const tripService = {
    dependencies: ["rpc", "notification"],

    /**
     * @param {import("@web/env").OdooEnv} env
     * @param {{ rpc: import("@web/core/network/rpc_service").RPCService, notification: import("@web/core/notifications/notification_service").NotificationService }} services
     */
    start(env, { rpc, notification }) {
        this.rpc = rpc;
        this.notification = notification;

        /**
         * Fetches a paginated list of trips for the currently logged-in driver.
         * Corresponds to US-047.
         * @param {{ filter: 'current' | 'past', offset?: number, limit?: number }} params
         * @returns {Promise<Array<object>|null>} A promise that resolves to an array of trip objects or null on failure.
         */
        const fetchMyTrips = async ({ filter, offset = 0, limit = 20 }) => {
            try {
                return await this.rpc("/tms/my_trips", {
                    filter: filter,
                    offset: offset,
                    limit: limit,
                });
            } catch (e) {
                console.error("Failed to fetch trips:", e);
                this.notification.add("Could not load trips. Please check your connection and try again.", {
                    title: "Network Error",
                    type: "danger",
                });
                return null;
            }
        };

        /**
         * Fetches detailed information for a single trip.
         * @param {number} tripId The ID of the trip to fetch.
         * @returns {Promise<object|null>} A promise that resolves to the trip detail object or null on failure.
         */
        const fetchTripDetails = async (tripId) => {
            try {
                return await this.rpc("/tms/trip_details", {
                    trip_id: tripId,
                });
            } catch (e) {
                console.error(`Failed to fetch details for trip ${tripId}:`, e);
                this.notification.add("Could not load trip details. Please try again.", {
                    title: "Error",
                    type: "danger",
                });
                return null;
            }
        };

        /**
         * Starts a trip, changing its status from 'Assigned' to 'In-Transit'.
         * Corresponds to US-049.
         * @param {number} tripId The ID of the trip to start.
         * @returns {Promise<boolean>} A promise that resolves to true on success, false on failure.
         */
        const startTrip = async (tripId) => {
            try {
                const result = await this.rpc("/web/dataset/call_kw/tms.trip/action_start", {
                    model: "tms.trip",
                    method: "action_start",
                    args: [[tripId]],
                    kwargs: {},
                });
                if (result) {
                    return true;
                }
                // Handle cases where the backend returns a falsy value for a "soft" failure
                this.notification.add("Could not start the trip. It may already be in progress or canceled.", {
                    title: "Action Failed",
                    type: "warning",
                });
                return false;
            } catch (e) {
                console.error(`Failed to start trip ${tripId}:`, e);
                this.notification.add(e.message?.data?.message || "An unknown error occurred while starting the trip.", {
                    title: "Error Starting Trip",
                    type: "danger",
                });
                return false;
            }
        };

        /**
         * Submits a Proof of Delivery (POD) for a trip.
         * Corresponds to REQ-1-114 and US-052.
         * @param {number} tripId The ID of the trip.
         * @param {{ podData: string, recipientName: string, podType: 'photo' | 'signature' }} data
         * @returns {Promise<boolean>} A promise that resolves to true on success, false on failure.
         */
        const submitPod = async (tripId, { podData, recipientName, podType }) => {
            try {
                await this.rpc("/web/dataset/call_kw/tms.trip/submit_pod", {
                    model: "tms.trip",
                    method: "submit_pod",
                    args: [
                        [tripId],
                        {
                            pod_data: podData,
                            recipient_name: recipientName,
                            pod_type: podType,
                        },
                    ],
                    kwargs: {},
                });
                return true;
            } catch (e) {
                console.error(`Failed to submit POD for trip ${tripId}:`, e);
                this.notification.add(e.message?.data?.message || "An unknown error occurred while submitting the POD.", {
                    title: "POD Submission Failed",
                    type: "danger",
                });
                return false;
            }
        };

        return {
            fetchMyTrips,
            fetchTripDetails,
            startTrip,
            submitPod,
        };
    },
};