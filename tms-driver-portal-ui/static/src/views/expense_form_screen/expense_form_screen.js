/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/browser/hooks";
import { HeaderNav } from "../../components/header_nav/header_nav";
import { FileUploader } from "../../components/file_uploader/file_uploader";

export class ExpenseFormScreen extends Component {
    static template = "tms_driver_portal.ExpenseFormScreen";
    static components = { HeaderNav, FileUploader };
    static props = ["tripId"];

    setup() {
        this.router = useService("router");
        this.expenseService = useService("expense");
        this.notification = useService("notification");

        this.state = useState({
            isSubmitting: false,
            validationErrors: {},
            expenseTypes: [],
            form: {
                trip_id: parseInt(this.props.tripId, 10),
                expense_type: null,
                amount: null,
                date: new Date().toISOString().slice(0, 10),
                description: "",
                receipt_file: null,
                odometer: null,
                quantity: null,
            },
        });

        onWillStart(async () => {
            await this._loadExpenseTypes();
        });
    }

    async _loadExpenseTypes() {
        try {
            this.state.expenseTypes = await this.expenseService.getExpenseTypes();
        } catch (e) {
            this.notification.add(e.message || "Failed to load expense types.", { type: "danger" });
        }
    }

    _onFileSelected(ev) {
        this.state.form.receipt_file = ev.detail.file;
    }

    _validateForm() {
        const errors = {};
        const { form } = this.state;

        if (!form.expense_type) {
            errors.expense_type = "Expense type is required.";
        }
        if (!form.amount || form.amount <= 0) {
            errors.amount = "Amount must be a positive number.";
        }
        if (!form.receipt_file) {
            errors.receipt_file = "A receipt is required.";
        }

        if (form.expense_type === "diesel") {
            if (!form.odometer || form.odometer <= 0) {
                errors.odometer = "Odometer reading is required for diesel expenses.";
            }
            if (!form.quantity || form.quantity <= 0) {
                errors.quantity = "Fuel quantity is required for diesel expenses.";
            }
        }
        this.state.validationErrors = errors;
        return Object.keys(errors).length === 0;
    }

    async _onSubmit() {
        if (!this._validateForm() || this.state.isSubmitting) {
            return;
        }

        this.state.isSubmitting = true;
        try {
            const expenseData = { ...this.state.form };
            await this.expenseService.submitExpense(expenseData);
            this.notification.add("Expense submitted successfully!", { type: "success" });
            this.router.back();
        } catch (e) {
            this.notification.add(e.message || "Failed to submit expense.", { type: "danger" });
        } finally {
            this.state.isSubmitting = false;
        }
    }
}

registry.category("screens").add("expense_form", ExpenseFormScreen);