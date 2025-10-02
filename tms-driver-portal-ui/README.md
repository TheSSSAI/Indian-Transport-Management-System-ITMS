# TMS Driver Portal UI (tms_driver_portal)

This repository contains the complete frontend application for the Transport Management System (TMS) Driver Portal. It is built as a self-contained Odoo addon using the OWL 2.0 framework, JavaScript, and Sass.

## Overview

The primary responsibility of this module is to provide a responsive, mobile-first user experience for drivers. It is a pure client-side application that interacts with the main TMS backend (`tms_core_business_logic`) exclusively through a well-defined Odoo JSON-RPC API.

This separation allows a dedicated frontend team to iterate on the UI/UX independently of the backend business logic, focusing on usability and performance for on-the-go users.

### Key Features

- **Mobile-First Design**: Optimized for use on mobile devices with screen widths from 360px upwards (REQ-1-001).
- **Simplified Workflows**: Large touch targets and streamlined processes for on-the-go operations (REQ-1-112).
- **Trip Management**: View current and past assigned trips (US-047).
- **Status Updates**: Start trips and update their status (US-049).
- **Proof of Delivery**: Upload PODs via photo or e-signature (REQ-1-114).
- **Expense Submission**: Submit trip-related expenses with receipt uploads (REQ-1-107).
- **Self-Service**: Access help and training materials (US-092).

## Technology Stack

- **Framework**: Odoo 18 with OWL 2.0
- **Language**: JavaScript (ES6+)
- **Styling**: Sass (SCSS)
- **API Communication**: Odoo JSON-RPC
- **Development Tooling**: Node.js, ESLint, Prettier

## Development Setup

### Prerequisites

1.  **Odoo Environment**: A running Odoo 18 instance with the `tms_core_business_logic` addon installed.
2.  **Node.js**: Use of a specific Node.js version is required. It is highly recommended to use a version manager like `nvm`.

### Installation

1.  **Clone the repository** into your Odoo addons path:
    ```bash
    git clone <repository_url> path/to/odoo/addons/tms_driver_portal
    ```

2.  **Install Node.js version**: Navigate to the addon directory and use `nvm` to install and use the correct Node.js version.
    ```bash
    cd path/to/odoo/addons/tms_driver_portal
    nvm install
    nvm use
    ```

3.  **Install development dependencies**: Use `npm` to install the project's development tools (linters, formatters).
    ```bash
    npm install
    ```

4.  **Install the Odoo Addon**:
    - Start your Odoo server.
    - Navigate to `Apps` in the Odoo UI.
    - Update the Apps List.
    - Search for "TMS Driver Portal" and click `Install`.

## Available Scripts

This project uses `npm` to run scripts for maintaining code quality. These should be run before committing code.

- **Linting**: Check for code quality and potential errors.
  ```bash
  npm run lint
  ```

- **Formatting**: Automatically format all `.js` and `.scss` files according to the project's style guide.
  ```bash
  npm run format
  ```

- **Check Formatting**: Check if all files are correctly formatted (useful for CI pipelines).
  ```bash
  npm run format:check
  ```

## Architectural Notes

This addon follows a modern Single-Page Application (SPA) architecture within the Odoo ecosystem.

- **`static/src/`**: Contains all frontend source code.
  - **`components/`**: Reusable OWL components (views, screens, shared elements).
  - **`services/`**: Client-side services for API communication, session management, and routing.
  - **`scss/`**: All Sass files for styling.
  - **`main.js`**: The entry point for the OWL application.
- **`controllers/`**: Python controllers that serve the main HTML template for the SPA.
- **`views/`**: XML files that define Odoo menus, actions, and asset bundles.