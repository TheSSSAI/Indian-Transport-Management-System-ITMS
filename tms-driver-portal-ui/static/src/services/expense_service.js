/** @odoo-module **/

/**
 * Service to handle all backend communications related to Expenses.
 * This service implements the two-step secure file upload pattern for expense receipts,
 * first obtaining a pre-signed URL and then uploading directly to S3.
 * It abstracts this complexity from the UI components.
 */
export const expenseService = {
    dependencies: ["rpc", "notification"],

    /**
     * @param {import("@web/env").OdooEnv} env
     * @param {{ rpc: import("@web/core/network/rpc_service").RPCService, notification: import("@web/core/notifications/notification_service").NotificationService }} services
     */
    start(env, { rpc, notification }) {
        this.rpc = rpc;
        this.notification = notification;

        /**
         * Step 1 of the upload process: Get a pre-signed URL from the backend.
         * Corresponds to Sequence Diagram 225.
         * @param {{ fileName: string, contentType: string }} fileInfo
         * @returns {Promise<object|null>} A promise that resolves with the pre-signed URL data or null on failure.
         */
        const getPresignedUrl = async ({ fileName, contentType }) => {
            try {
                return await this.rpc("/tms/expense/get_upload_url", {
                    file_name: fileName,
                    content_type: contentType,
                });
            } catch (e) {
                console.error("Failed to get pre-signed URL:", e);
                this.notification.add("Could not prepare file upload. Please try again.", {
                    title: "Upload Error",
                    type: "danger",
                });
                return null;
            }
        };

        /**
         * Step 2 of the upload process: Upload the file directly to S3 using the pre-signed URL.
         * @param {{ url: string, fields: object }} presignedPostData
         * @param {File} file
         * @returns {Promise<string|null>} A promise that resolves with the S3 file key on success, or null on failure.
         */
        const uploadFileToS3 = async (presignedPostData, file) => {
            const formData = new FormData();
            Object.entries(presignedPostData.fields).forEach(([key, value]) => {
                formData.append(key, value);
            });
            formData.append("file", file);

            try {
                const response = await fetch(presignedPostData.url, {
                    method: "POST",
                    body: formData,
                });

                if (!response.ok) {
                    const errorText = await response.text();
                    console.error("S3 Upload Failed:", response.status, errorText);
                    throw new Error("File could not be uploaded to the server.");
                }
                // The key is needed for the final submission to Odoo
                return presignedPostData.fields.key;
            } catch (e) {
                console.error("Network error during S3 upload:", e);
                this.notification.add(e.message || "Upload failed. Please check your network connection.", {
                    title: "Upload Error",
                    type: "danger",
                });
                return null;
            }
        };

        /**
         * Step 3 of the process: Create the expense record in Odoo with the key of the uploaded file.
         * Corresponds to REQ-1-107 and US-053.
         * @param {object} expenseData - The expense form data, including the `s3_key`.
         * @returns {Promise<number|null>} A promise that resolves with the new expense ID on success, or null on failure.
         */
        const createExpense = async (expenseData) => {
            try {
                return await this.rpc("/web/dataset/call_kw/tms.expense/create_from_portal", {
                    model: "tms.expense",
                    method: "create_from_portal",
                    args: [expenseData],
                    kwargs: {},
                });
            } catch (e) {
                console.error("Failed to create expense record:", e);
                this.notification.add(e.message?.data?.message || "An unknown error occurred while saving the expense.", {
                    title: "Submission Failed",
                    type: "danger",
                });
                return null;
            }
        };

        return {
            getPresignedUrl,
            uploadFileToS3,
            createExpense,
        };
    },
};