/** @odoo-module **/

import { Component, onMounted, onWillUnmount, useRef } from "@odoo/owl";

/**
 * Signature Pad Component
 *
 * A reusable component that wraps the 'signature_pad' third-party library
 * to provide an e-signature capture canvas. It is designed to be embedded
 * in parent forms (like the POD Submission screen).
 *
 * This component is a "controlled" component; the parent is responsible for
 * calling a public method to retrieve the signature data.
 *
 * Relies on the global `SignaturePad` object being available.
 * This library must be loaded via Odoo's asset management.
 */
export class SignaturePad extends Component {
    static template = "tms_driver_portal.SignaturePad";

    setup() {
        this.canvasRef = useRef("signatureCanvas");
        this.signaturePad = null;

        onMounted(() => {
            if (!window.SignaturePad) {
                console.error("SignaturePad library is not loaded. Please check asset bundles.");
                return;
            }
            const canvas = this.canvasRef.el;
            this.resizeCanvas(canvas);
            this.signaturePad = new SignaturePad(canvas, {
                backgroundColor: 'rgb(255, 255, 255)',
            });
            window.addEventListener("resize", this.onResize.bind(this));
        });

        onWillUnmount(() => {
            window.removeEventListener("resize", this.onResize.bind(this));
            if (this.signaturePad) {
                this.signaturePad.off();
            }
        });
    }

    /**
     * Handles window resize events to adjust the canvas dimensions,
     * preserving the signature.
     */
    onResize() {
        if (this.signaturePad) {
            const canvas = this.canvasRef.el;
            const data = this.signaturePad.toDataURL(); // Save current signature
            this.resizeCanvas(canvas);
            this.signaturePad.fromDataURL(data); // Restore signature
        }
    }

    /**
     * Sets the canvas dimensions to match its container's size.
     * @param {HTMLCanvasElement} canvas The canvas element to resize.
     */
    resizeCanvas(canvas) {
        const ratio = Math.max(window.devicePixelRatio || 1, 1);
        canvas.width = canvas.offsetWidth * ratio;
        canvas.height = canvas.offsetHeight * ratio;
        canvas.getContext("2d").scale(ratio, ratio);
    }

    /**
     * Clears the signature canvas.
     * This method is called from the template via a button click.
     */
    clear() {
        if (this.signaturePad) {
            this.signaturePad.clear();
        }
    }

    /**
     * Public method for parent components to retrieve signature data.
     * Checks if the signature pad is empty before returning data.
     * @returns {string | null} The signature as a base64 encoded PNG data URL, or null if empty.
     */
    @odoo.component.publicMethod
    getSignatureData() {
        if (this.signaturePad && !this.signaturePad.isEmpty()) {
            // Return as PNG with a white background
            return this.signaturePad.toDataURL("image/png");
        }
        return null;
    }
}