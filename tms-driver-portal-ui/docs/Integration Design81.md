# 1 Integration Specifications

## 1.1 Extraction Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-DRV-UI |
| Extraction Timestamp | 2024-07-28T14:30:00Z |
| Mapping Validation Score | 100% |
| Context Completeness Score | 100% |
| Implementation Readiness Level | High |

## 1.2 Relevant Requirements

### 1.2.1 Requirement Id

#### 1.2.1.1 Requirement Id

REQ-1-112

#### 1.2.1.2 Requirement Text

The system shall provide a distinct user interface for the 'Driver' role, optimized for usability on mobile web browsers. This 'Driver Portal' shall feature a simplified layout, large touch targets (buttons, links), and streamlined workflows for on-the-go operations.

#### 1.2.1.3 Validation Criteria

- Log in as a Driver on a mobile device.
- Verify the interface is simple and easy to navigate.
- Confirm that core driver tasks (viewing trips, updating status, submitting expenses) can be completed with minimal clicks and no complex data entry.

#### 1.2.1.4 Implementation Implications

- The entire repository must be developed as a Single Page Application (SPA) using the OWL 2.0 framework to create a fluid, app-like experience.
- All CSS must follow a mobile-first strategy, targeting viewports from 360px upwards.
- All interactive elements must have a minimum touch target size of 44x44 CSS pixels.

#### 1.2.1.5 Extraction Reasoning

This is the foundational requirement that defines the entire purpose and scope of the REPO-DRV-UI repository, mandating a dedicated, mobile-optimized UI for the Driver role.

### 1.2.2.0 Requirement Id

#### 1.2.2.1 Requirement Id

REQ-1-114

#### 1.2.2.2 Requirement Text

The Driver Portal shall allow a driver to mark a trip as 'Delivered' by submitting a Proof of Delivery (POD). This process must support uploading a photo or capturing an e-signature as the POD. The submission form must also require the driver to enter the recipient's name.

#### 1.2.2.3 Validation Criteria

- As a Driver, for an 'In-Transit' trip, initiate the delivery process.
- Verify options exist to either upload a photo from the device's camera/gallery or to capture a signature on the screen.
- Complete the process by entering a recipient name and submitting.

#### 1.2.2.4 Implementation Implications

- An OWL component must be created for the POD submission form.
- The component must include a tabbed interface or similar control to switch between photo upload and e-signature.
- A backend RPC call to 'tms.trip.submit_pod' must be made to submit the data and file.

#### 1.2.2.5 Extraction Reasoning

This is a critical functional requirement for the Driver Portal UI, defining a core on-road task that requires a specific integration with the backend.

### 1.2.3.0 Requirement Id

#### 1.2.3.1 Requirement Id

REQ-1-107

#### 1.2.3.2 Requirement Text

The system's driver portal shall include a feature for submitting trip-related expenses. The submission form must allow the driver to select an expense type, enter the amount, and upload a photo of the receipt. If the expense type is 'Diesel', the form must also require fuel quantity and odometer reading.

#### 1.2.3.3 Validation Criteria

- Log in as a Driver and navigate to the expense submission form for an active trip.
- Successfully submit a 'Toll' expense with an amount and a receipt image.
- Submit a 'Diesel' expense and verify the form requires and accepts quantity and odometer reading.

#### 1.2.3.4 Implementation Implications

- An OWL component for the expense submission form must be created.
- The component must implement conditional logic to show/hide the 'Fuel Quantity' and 'Odometer Reading' fields.
- The file upload will follow a two-step process: get a pre-signed URL from the backend, then upload directly to S3.

#### 1.2.3.5 Extraction Reasoning

This requirement specifies a key feature of the Driver Portal UI, the implementation of which requires a multi-step API integration for file uploads.

### 1.2.4.0 Requirement Id

#### 1.2.4.1 Requirement Id

US-092

#### 1.2.4.2 Requirement Text

As a Driver, I want to access a dedicated 'Help & Training' section within my mobile portal that contains short video tutorials and a downloadable quick-reference guide, so that I can learn how to use the system's features correctly at my own pace.

#### 1.2.4.3 Validation Criteria

- Verify a 'Help & Training' option exists in the main navigation.
- Confirm the page lists available video tutorials with titles and plays them within the page.

#### 1.2.4.4 Implementation Implications

- A new OWL component must be created to fetch and display a list of training materials from a backend controller.
- The component must be able to render embedded video players and links to documents.

#### 1.2.4.5 Extraction Reasoning

This user story defines a UI feature for the Driver Portal that requires a new, dedicated backend API endpoint, highlighting an integration gap not covered by the original specification.

## 1.3.0.0 Relevant Components

- {'component_name': 'Driver Portal (OWL Application)', 'component_specification': 'The root component that encapsulates the entire Driver Portal single-page application. It manages routing between screens (Login, Trip List, Trip Detail, etc.), handles user session state, and orchestrates data fetching from the backend.', 'implementation_requirements': ['Must be implemented as a self-contained Odoo addon using the OWL 2.0 framework.', 'Must handle all communication with the REPO-TMS-CORE backend via the Odoo RPC service.', 'Must be fully responsive and adhere to the mobile-first design specifications.'], 'architectural_context': "Resides in the Odoo Presentation Layer. It is the sole component within the tms-driver-portal-ui repository and serves as the user-facing entry point for the 'Driver' role.", 'extraction_reasoning': 'This is the primary and overarching component that constitutes the entire scope of the REPO-DRV-UI repository. All integration requirements are implemented to serve this component and its children.'}

## 1.4.0.0 Architectural Layers

- {'layer_name': 'Odoo Presentation Layer', 'layer_responsibilities': ['Rendering master data forms (Vehicle, Driver, Customer).', 'Displaying trip management interfaces.', 'Providing a responsive UI for mobile web browsers.', 'Implementing a simplified, custom Driver Portal with large touch targets.', 'Visualizing real-time vehicle locations on a map view.', 'Presenting dashboards and filterable reports.'], 'layer_constraints': ["Must use Odoo's native view system (XML) for backend interfaces and the OWL 2.0 Framework for custom frontend applications like the Driver Portal.", 'Business logic and data validation must be delegated to the Business Logic Layer.'], 'implementation_patterns': ['Component-Based UI (using OWL)', 'Single Page Application (SPA) for the Driver Portal'], 'extraction_reasoning': "The REPO-DRV-UI is the concrete implementation of the 'Driver Portal' responsibility within this architectural layer. Its scope and integration contracts are strictly confined to the responsibilities and constraints of this layer."}

## 1.5.0.0 Dependency Interfaces

### 1.5.1.0 Interface Name

#### 1.5.1.1 Interface Name

IOdooBackendApi

#### 1.5.1.2 Source Repository

REPO-TMS-CORE

#### 1.5.1.3 Method Contracts

##### 1.5.1.3.1 Method Name

###### 1.5.1.3.1.1 Method Name

authenticate

###### 1.5.1.3.1.2 Method Signature

rpc.call('/web/session/authenticate', {db, login, password})

###### 1.5.1.3.1.3 Method Purpose

Authenticates the driver and establishes a user session.

###### 1.5.1.3.1.4 Integration Context

Called from the Driver Login Screen (US-046) to initiate a session.

##### 1.5.1.3.2.0 Method Name

###### 1.5.1.3.2.1 Method Name

fetch_my_trips

###### 1.5.1.3.2.2 Method Signature

rpc.call('/tms/my_trips', {filter: string, offset: int, limit: int})

###### 1.5.1.3.2.3 Method Purpose

Retrieves a paginated list of trips assigned to the current driver, filterable by status ('current' or 'past').

###### 1.5.1.3.2.4 Integration Context

Called from the 'My Trips' dashboard screen (US-047) to populate the trip list.

##### 1.5.1.3.3.0 Method Name

###### 1.5.1.3.3.1 Method Name

fetch_trip_details

###### 1.5.1.3.3.2 Method Signature

rpc.call('/tms/trip_details', {trip_id: int})

###### 1.5.1.3.3.3 Method Purpose

Retrieves detailed information for a single trip.

###### 1.5.1.3.3.4 Integration Context

Called when a driver navigates to the Trip Detail Screen to view specific trip information.

##### 1.5.1.3.4.0 Method Name

###### 1.5.1.3.4.1 Method Name

start_trip

###### 1.5.1.3.4.2 Method Signature

orm.call('tms.trip', 'action_start', [trip_id])

###### 1.5.1.3.4.3 Method Purpose

Changes the status of a trip from 'Assigned' to 'In-Transit'.

###### 1.5.1.3.4.4 Integration Context

Called from the Trip Detail screen (US-049) when the driver begins their journey.

##### 1.5.1.3.5.0 Method Name

###### 1.5.1.3.5.1 Method Name

submit_pod

###### 1.5.1.3.5.2 Method Signature

orm.call('tms.trip', 'submit_pod', [trip_id], {pod_data, recipient_name, pod_type})

###### 1.5.1.3.5.3 Method Purpose

Submits the Proof of Delivery (photo or signature) and recipient name to update the trip status to 'Delivered'.

###### 1.5.1.3.5.4 Integration Context

Called from the POD Submission Form (REQ-1-114, US-052) upon completion of a delivery.

##### 1.5.1.3.6.0 Method Name

###### 1.5.1.3.6.1 Method Name

get_presigned_url_for_expense

###### 1.5.1.3.6.2 Method Signature

rpc.call('/tms/expense/get_upload_url', {filename, content_type})

###### 1.5.1.3.6.3 Method Purpose

Requests a temporary, pre-signed URL from the backend to allow for a direct file upload to Amazon S3.

###### 1.5.1.3.6.4 Integration Context

Called from the Expense Submission Form (REQ-1-107) as the first step of uploading a receipt image.

##### 1.5.1.3.7.0 Method Name

###### 1.5.1.3.7.1 Method Name

create_expense

###### 1.5.1.3.7.2 Method Signature

orm.call('tms.expense', 'create', [expense_data])

###### 1.5.1.3.7.3 Method Purpose

Submits a new expense record with receipt details for approval. The 'expense_data' payload includes the S3 key of the uploaded receipt.

###### 1.5.1.3.7.4 Integration Context

Called from the Expense Submission Form (REQ-1-107, US-053) after the receipt file has been successfully uploaded to S3.

##### 1.5.1.3.8.0 Method Name

###### 1.5.1.3.8.1 Method Name

fetch_training_materials

###### 1.5.1.3.8.2 Method Signature

rpc.call('/tms/training_materials', {})

###### 1.5.1.3.8.3 Method Purpose

Retrieves the list of available training videos and documents for the driver.

###### 1.5.1.3.8.4 Integration Context

Called from the Help & Training screen (US-092) to populate the list of available materials.

#### 1.5.1.4.0.0 Integration Pattern

Client-Server Request-Response via Odoo RPC

#### 1.5.1.5.0.0 Communication Protocol

HTTP/JSON-RPC

#### 1.5.1.6.0.0 Extraction Reasoning

As a pure frontend application, REPO-DRV-UI is entirely dependent on its backend (REPO-TMS-CORE) for all data and business logic. This interface contract defines all necessary interactions, including those identified as gaps in the initial analysis.

### 1.5.2.0.0.0 Interface Name

#### 1.5.2.1.0.0 Interface Name

IS3FileStorageApi

#### 1.5.2.2.0.0 Source Repository

REPO-TMS-INFRA

#### 1.5.2.3.0.0 Method Contracts

- {'method_name': 'uploadFile', 'method_signature': 'HTTP PUT/POST to a pre-signed URL', 'method_purpose': 'To upload a file (e.g., expense receipt, POD photo) directly to an Amazon S3 bucket.', 'integration_context': "This call is made directly from the client's browser after obtaining a pre-signed URL from the `IOdooBackendApi`."}

#### 1.5.2.4.0.0 Integration Pattern

Direct Client-to-Cloud Storage via Pre-signed URL

#### 1.5.2.5.0.0 Communication Protocol

HTTPS

#### 1.5.2.6.0.0 Extraction Reasoning

This repository integrates directly with the S3 service (provisioned by REPO-TMS-INFRA) for file uploads to offload traffic from the core application server, which is a key performance and scalability pattern defined in the architecture.

## 1.6.0.0.0.0 Exposed Interfaces

*No items available*

## 1.7.0.0.0.0 Technology Context

### 1.7.1.0.0.0 Framework Requirements

Odoo 18 with the OWL 2.0 framework for all component development. All frontend logic must be implemented in JavaScript (ES6+).

### 1.7.2.0.0.0 Integration Technologies

- Odoo RPC (JSON-RPC over HTTP) for all backend communication.
- HTTPS for direct file uploads to Amazon S3.

### 1.7.3.0.0.0 Performance Constraints

Must provide fast load times (LCP < 3s) and a responsive user experience on mobile networks. Minimize RPC calls and optimize asset loading.

### 1.7.4.0.0.0 Security Requirements

All backend calls are authenticated via the user's Odoo session cookie. The UI must not store sensitive credentials. All business rule enforcement and data authorization is handled by the backend. File uploads use secure, time-limited pre-signed URLs.

## 1.8.0.0.0.0 Extraction Validation

| Property | Value |
|----------|-------|
| Mapping Completeness Check | All repository mappings specified in its definitio... |
| Cross Reference Validation | Requirements (e.g., REQ-1-114) have been successfu... |
| Implementation Readiness Assessment | The repository is highly implementation-ready. The... |
| Quality Assurance Confirmation | The extracted context has been systematically revi... |

