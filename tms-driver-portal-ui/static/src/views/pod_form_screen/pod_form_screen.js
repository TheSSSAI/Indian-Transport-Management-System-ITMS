/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, useRef } from "@odoo/owl";
import { useService } from "@web/core/browser/hooks";
import { HeaderNav } from "../../components/header_nav/header_nav";
import { FileUploader } from "../../components/file_uploader/file_uploader";
import { SignaturePad } from "../../components/signature_pad/signature_pad";

export class PodFormScreen extends Component {
    static template = "tms_driver_portal.PodFormScreen";
    static components = { HeaderNav, FileUploader, SignaturePad };
    static props = ["tripId"];

    setup() {
        this.router = useService("router");
        this.tripService = useService("trip");
        this.notification = useService("notification");
        this.signaturePadRef = useRef("signaturePad");

        this.state = useState({
            isSubmitting: false,
            validationErrors: {},
            form: {
                trip_id: parseInt(this.props.tripId, 10),
                pod_method: "photo", // 'photo' or 'signature'
                recipient_name: "",
                pod_file: null,
                pod_signature: null,
            },
        });
    }

    _onFileSelected(ev) {
        this.state.form.pod_file = ev.detail.file;
        this.state.form.pod_signature = null;
    }

    _validateForm() {
        const errors = {};
        const { form } = this.state;
        if (!form.recipient_name.trim()) {
            errors.recipient_name = "Recipient name is required.";
        }

        if (form.pod_method === "photo" && !form.pod_file) {
            errors.pod_file = "A POD photo is required.";
        }

        if (form.pod_method === "signature") {
            if (this.signaturePadRef.comp.isEmpty()) {
                errors.pod_signature = "A signature is required.";
            }
        }
        this.state.validationErrors = errors;
        return Object.keys(errors).length === 0;
    }

    async _onSubmit() {
        if (this.state.isSubmitting) return;

        if (this.state.form.pod_method === "signature") {
            this.state.form.pod_signature = this.signaturePadRef.comp.getDataURL();
            this.state.form.pod_file = null;
        }

        if (!this._validateForm()) {
            return;
        }
        
        this.state.isSubmitting = true;
        try {
            const payload = {
                recipient_name: this.state.form.recipient_name,
                pod_type: this.state.form.pod_method,
                attachment: this.state.form.pod_method === 'photo' ? this.state.form.pod_file : this.state.form.pod_signature,
            };
            
            await this.tripService.submitPod(this.state.form.trip_id, payload);

            this.notification.add("Proof of Delivery submitted successfully!", { type: "success" });
            this.router.navigate({ name: "trip_list" });
        } catch (e) {
            this.notification.add(e.message || "Failed to submit POD.", { type: "danger" });
        } finally {
            this.state.isSubmitting = false;
        }
    }
}

registry.category("screens").add("pod_form", PodFormScreen);