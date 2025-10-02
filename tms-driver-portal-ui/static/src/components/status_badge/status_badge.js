/** @odoo-module **/

import { Component } from "@odoo/owl";

/**
 * Status Badge Component
 *
 * A reusable component to display a styled badge for different statuses.
 * It maps a status string to a specific CSS class for color-coding.
 * This component is purely presentational ("dumb" component).
 *
 * Props:
 * - status (String): The status key (e.g., 'Assigned', 'In-Transit', 'Delivered').
 * - text (String): The text to display inside the badge.
 */
export class StatusBadge extends Component {
    static template = "tms_driver_portal.StatusBadge";
    static props = {
        status: { type: String, optional: false },
        text: { type: String, optional: false },
    };

    /**
     * Computes the CSS classes for the badge based on the status prop.
     * This ensures a consistent color-coding scheme across the application.
     * @returns {string} The computed CSS class string.
     */
    get badgeClass() {
        const statusClassMap = {
            // Trip Statuses (from Business Rule BR-004 and Requirement REQ-1-103)
            "Planned": "badge-light",
            "Assigned": "badge-info",
            "In-Transit": "badge-primary",
            "On Hold": "badge-warning",
            "Delivered": "badge-success",
            "Completed": "badge-success-dark",
            "Invoiced": "badge-secondary",
            "Paid": "badge-dark",
            "Canceled": "badge-error-light",

            // Expense Statuses
            "Submitted": "badge-info",
            "Approved": "badge-success",
            "Rejected": "badge-error",
            "Paid": "badge-dark", // Re-using 'Paid' status
        };

        const baseClass = "tms-status-badge";
        const statusSpecificClass = statusClassMap[this.props.status] || "badge-default";

        return `${baseClass} ${statusSpecificClass}`;
    }
}