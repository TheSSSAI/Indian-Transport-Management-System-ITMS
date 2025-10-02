/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, onWillStart, useState } from "@odoo/owl";
import { useService } from "@web/core/browser/hooks";
import { HeaderNav } from "../../components/header_nav/header_nav";

export class TrainingScreen extends Component {
    static template = "tms_driver_portal.TrainingScreen";
    static components = { HeaderNav };

    setup() {
        this.trainingService = useService("training");
        this.notification = useService("notification");

        this.state = useState({
            materials: [],
            isLoading: true,
            hasError: false,
            errorMessage: "",
        });

        onWillStart(async () => {
            await this._loadTrainingMaterials();
        });
    }

    async _loadTrainingMaterials() {
        this.state.isLoading = true;
        this.state.hasError = false;
        try {
            this.state.materials = await this.trainingService.fetchTrainingMaterials();
        } catch (e) {
            this.state.hasError = true;
            this.state.errorMessage = e.message || "Could not load training materials.";
            this.notification.add(this.state.errorMessage, { type: "danger" });
        } finally {
            this.state.isLoading = false;
        }
    }

    _getIconForType(type) {
        switch (type) {
            case "video":
                return "fa-play-circle";
            case "document":
                return "fa-file-pdf";
            default:
                return "fa-question-circle";
        }
    }

    _openMaterial(material) {
        if (material.type === 'document') {
            window.open(material.url, '_blank');
        }
        // For video, the template handles it via the video tag.
        // A more advanced implementation could use a modal.
    }
}

registry.category("screens").add("training", TrainingScreen);