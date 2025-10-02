/** @odoo-module **/

import { Component, useRef, useState } from "@odoo/owl";

/**
 * Reusable File Uploader Component
 *
 * A mobile-first component for selecting a file, showing a preview, and
 * performing client-side validation for file type and size.
 * It emits an event with the valid file for the parent component to handle.
 *
 * Implements requirements from US-083, REQ-FNC-004-Validation and UI Mockup 668.
 *
 * Props:
 * - id (String): A unique ID for the file input element.
 * - acceptedFileTypes (String): A comma-separated string of MIME types (e.g., "image/png,image/jpeg").
 * - maxFileSizeMB (Number): The maximum allowed file size in megabytes.
 */
export class FileUploader extends Component {
    static template = "tms_driver_portal.FileUploader";
    static props = {
        id: { type: String },
        acceptedFileTypes: { type: String },
        maxFileSizeMB: { type: Number },
    };

    setup() {
        this.inputRef = useRef("fileInput");
        this.state = useState({
            fileName: null,
            previewUrl: null,
            errorMsg: null,
        });
    }

    /**
     * Triggers the hidden file input element.
     */
    onClick() {
        this.inputRef.el.click();
    }

    /**
     * Handles the file selection event from the input element.
     * Performs validation and updates the component's state.
     * @param {Event} ev The change event from the file input.
     */
    async onFileChanged(ev) {
        const file = ev.target.files[0];
        if (!file) {
            return;
        }

        // Reset state
        this.state.errorMsg = null;

        // 1. Validate File Type
        const allowedTypes = this.props.acceptedFileTypes.split(",").map(t => t.trim());
        if (!allowedTypes.includes(file.type)) {
            this.state.errorMsg = `Invalid file type. Please upload one of: ${this.getFriendlyFileTypes()}`;
            this.clearFile();
            return;
        }

        // 2. Validate File Size
        const maxSizeBytes = this.props.maxFileSizeMB * 1024 * 1024;
        if (file.size > maxSizeBytes) {
            this.state.errorMsg = `File is too large. Maximum size is ${this.props.maxFileSizeMB}MB.`;
            this.clearFile();
            return;
        }

        // 3. Update state with valid file
        this.state.fileName = file.name;
        if (file.type.startsWith("image/")) {
            this.state.previewUrl = await this.readFileAsDataURL(file);
        } else {
            this.state.previewUrl = this.getIconForMimeType(file.type);
        }
        
        // 4. Notify parent component
        this.trigger("file-select", { file: file });
    }

    /**
     * Resets the component state and clears the file input.
     */
    clearFile() {
        this.state.fileName = null;
        this.state.previewUrl = null;
        this.inputRef.el.value = ""; // Clear the input so the same file can be re-selected
        this.trigger("file-clear");
    }

    /**
     * Reads a file and returns its content as a Data URL for preview.
     * @param {File} file The file to read.
     * @returns {Promise<string>} A promise that resolves with the data URL.
     */
    readFileAsDataURL(file) {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.onload = () => resolve(reader.result);
            reader.onerror = () => reject(reader.error);
            reader.readAsDataURL(file);
        });
    }
    
    /**
     * Returns a FontAwesome icon class based on the file's MIME type.
     * @param {string} mimeType The MIME type of the file.
     * @returns {string} A FontAwesome class string.
     */
    getIconForMimeType(mimeType) {
        if (mimeType === "application/pdf") {
            return "fa-file-pdf";
        }
        return "fa-file";
    }

    /**
     * Generates a user-friendly list of allowed file extensions.
     * @returns {string} A string like "JPG, PNG, PDF".
     */
    getFriendlyFileTypes() {
        return this.props.acceptedFileTypes
            .split(",")
            .map(t => t.split("/")[1].toUpperCase())
            .join(", ");
    }
}