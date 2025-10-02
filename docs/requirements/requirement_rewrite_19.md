### **Software Requirements Specification: Transport Management System (TMS)**

---

#### **1. Introduction**

##### **1.1 Purpose**
This document specifies the software requirements for the Transport Management System (TMS). It provides a detailed description of the system's features, capabilities, constraints, and interfaces. This SRS is intended for developers, project managers, quality assurance teams, and other stakeholders to ensure a common understanding of the system to be built.

##### **1.2 Project Scope (REQ-SCP-001)**
*   The system shall be a web-based, mobile-friendly Transport Management System.
*   The system shall be built as an Odoo 18 addon.
*   The system shall manage core master data for Vehicles, Drivers, Customers, Routes, and Materials.
*   The system shall manage the end-to-end trip lifecycle, including planning, assignment, tracking, delivery, and financial settlement.
*   The system shall include financial modules for expense tracking, invoicing, customer ledgers, and profitability analysis.
*   The invoicing module shall support Indian GST e-invoicing regulations.
*   The system shall provide real-time vehicle tracking via third-party GPS integration.
*   The system shall implement role-based access control for Admin, Dispatch Manager, Finance Officer, and Driver user types.
*   The system shall provide a comprehensive dashboard and reporting module for operational and financial insights.
*   The system shall provide system alerts and notifications for critical events.
*   The system shall not include the development of a native mobile application for iOS or Android.
*   The system shall not include direct integration with FASTag or diesel card providers for automated balance checking. Balances for these cards shall be managed manually within the system.
*   The initial release shall not include the future-ready features listed in Section 9.

---

#### **2. Overall Description**

##### **2.1 Product Perspective (REQ-OVR-001)**
*   The TMS shall be developed as a custom module (addon) for the Odoo 18 platform.
*   The TMS shall function as a core component within the Odoo ecosystem.
*   The TMS shall leverage Odoo's existing models, including `res.partner` for customers and `hr.employee` for drivers.
*   The TMS shall leverage Odoo's security framework.
*   The system shall be designed as a modular monolith.
*   The system shall include a decoupled microservice for high-volume GPS data ingestion.
*   The system shall interface with a GPS Provider API for receiving real-time vehicle location data.
*   The system shall interface with a GST Suvidha Provider (GSP) API for generating e-invoices.

##### **2.2 User Classes and Characteristics (REQ-USR-001)**
*   The system shall provide an 'Admin' user role with full system access, including permissions to manage users, system settings, all master data, and access to all reports and dashboards.
*   The system shall provide a 'Dispatch Manager' user role to manage core logistics operations, with permissions to create and manage trips, assign drivers and vehicles, approve expenses, and view operational reports.
*   The system shall provide a 'Finance Officer' user role to manage financial aspects, with permissions to handle invoicing, payments, customer ledgers, and financial reporting.
*   The system shall provide a 'Driver' user role for on-field users, who will access the system via a simple and intuitive mobile-friendly web interface to view trips, update status, and submit expenses.

##### **2.3 Operating Environment (REQ-DEP-001)**
*   The application shall be containerized using Docker.
*   The application shall be deployed on the Amazon Web Services (AWS) cloud platform.
*   The production environment shall be a high-availability Amazon Elastic Kubernetes Service (EKS) cluster.
*   The production environment shall use Amazon RDS for PostgreSQL 16 as its database service.
*   The production environment shall use Amazon S3 for file attachments.
*   The system shall use Odoo 18.
*   The system shall use Python 3.11.

##### **2.4 Design and Implementation Constraints (REQ-CON-001)**
*   The system must be developed as an Odoo 18 addon.
*   The frontend must use the Odoo Web Library (OWL).
*   The frontend must be mobile-responsive.
*   A separate native mobile app shall not be developed.
*   The database must be PostgreSQL.
*   Development shall reuse pre-existing Odoo components and conventions where possible.
*   The system must comply with Indian GST regulations for e-invoicing.

##### **2.5 Assumptions and Dependencies (REQ-DEP-002)**
*   The system shall depend on a procured and maintained subscription with a third-party GPS provider that offers an accessible API.
*   The system shall depend on a procured and maintained subscription with a GST Suvidha Provider (GSP) for e-invoicing integration.
*   The system shall assume users have access to a modern web browser and a stable internet connection.

---

#### **3. System Features (Functional Requirements)**

##### **3.1 Role-Based Access Control (REQ-FNC-001)**
*   The system shall implement distinct user roles with pre-defined permissions.
*   A user assigned the 'Driver' role shall only be able to view trips assigned to them and shall not be able to view company financial data, such as trip revenue, customer rates, or overall profitability. However, they are permitted to view financial data directly related to their personal compensation, such as incentives earned and expense reimbursements.
*   A user assigned the 'Finance Officer' role shall be able to generate invoices but not create or assign new trips.
*   A user assigned the 'Dispatch Manager' role shall be able to create trips, approve expenses, and manage the status of 'On Hold' trips, but not manage user accounts.
*   A user assigned the 'Admin' role shall have unrestricted access to all system features.
*   The system shall enforce Business Rule BR-001. The system shall, however, allow the use of Odoo's standard group-based permissions to grant additional, specific access rights if required.

##### **3.2 Trip Management (REQ-FNC-002)**
*   The system shall provide functionality to create, manage, and track trips from planning to payment.
*   The system shall allow a Dispatch Manager to create a new trip with details for Source, Destination, Customer, Material, Weight, Rate (per km/ton/fixed), and Expected Delivery Date. The system shall enforce Business Rules BR-006, BR-007, and BR-008.
*   The system shall allow the assignment of an available vehicle and an available driver to a trip. The system shall prevent the assignment of 'Inactive' vehicles or drivers and enforce Business Rule BR-003.
*   A trip shall progress through a defined set of statuses as defined in Business Rule BR-004.
*   The 'On Hold' status can be entered from 'In-Transit' when a critical event is logged.
*   A user with the 'Dispatch Manager' role shall have the permission to change the status of an 'On Hold' trip back to 'In-Transit'. This action shall require a mandatory text comment explaining the resolution, which will be logged in the trip's event history.
*   The system shall provide a 'Canceled' status that can be set at any stage before 'Delivered'. Canceling a trip shall require a mandatory reason and will trigger a notification to the assigned driver, if any.

##### **3.3 GPS Tracking and Geofencing (REQ-FNC-003)**
*   The system shall provide real-time tracking of vehicles on a map, with a maximum data latency of 60 seconds from the GPS device to the user interface.
*   The system shall display the current location of vehicles associated with 'In-Transit' trips on an integrated map view.
*   The system shall allow a user to define geofences for key locations (e.g., customer sites, warehouses).
*   The system shall generate an alert when a vehicle enters or exits a defined geofence.

##### **3.4 Expense Management and Approval (REQ-FNC-004)**
*   The system shall provide a module for recording and approving all trip-related and vehicle-related expenses.
*   The system shall allow a Driver, via the web interface, to submit an expense for an assigned trip, specifying the type (Diesel, Toll, Food), amount, an uploaded photo of the receipt, and, if the type is 'Diesel', the quantity in liters and the vehicle's current odometer reading. The system shall enforce Business Rule BR-009.
*   Uploaded receipt files shall be restricted to common image and document formats (JPG, PNG, PDF) with a maximum file size of 5MB.
*   Submitted expenses shall enter an approval queue for a Dispatch Manager or Finance Officer.
*   The system shall allow an approver to 'Approve' or 'Reject' a submitted expense. Rejected expenses must include a reason for rejection.
*   Only 'Approved' expenses shall be included in the trip's profitability calculation.
*   The system shall allow a Finance Officer to add non-trip-related expenses (e.g., Maintenance, Insurance, Fines) directly to a vehicle's record.

##### **3.5 Card Balance Management (REQ-FNC-005)**
*   The system shall provide a feature to manually track and receive alerts for low balances on FASTag and diesel cards.
*   The system shall allow a user to create records for FASTag and diesel cards, manually update the current balance, and set a low-balance threshold for each card.
*   The system shall generate an alert when the manually updated balance falls below the set threshold.

##### **3.6 Invoicing and Payments (REQ-FNC-006)**
*   The system shall provide functionality for the generation of GST-compliant invoices and tracking of payments.
*   The system shall allow generating a GST-compliant invoice for any trip in the 'Completed' state, with details auto-populated from the trip record, enforcing Business Rule BR-010.
*   The system shall integrate with a GSP to generate a valid IRN for e-invoicing.
*   In case of repeated GSP API failures, the system shall flag the invoice for manual intervention and generate a high-priority alert for the Finance Officer.
*   The system shall allow a user to record partial or full payments against an invoice.
*   The system shall maintain a customer ledger showing all invoices, payments, and the outstanding balance for each customer.

##### **3.7 Profitability Calculation (REQ-FNC-007)**
*   The system shall automatically calculate the profitability for each trip.
*   For each trip, the system shall display the total revenue, the sum of all 'Approved' trip-related expenses, and the calculated profitability (Revenue - Approved Expenses).

##### **3.8 Driver Portal (REQ-FNC-008)**
*   The system shall provide a mobile-friendly web interface specifically designed for drivers.
*   A logged-in driver shall be able to:
    *   View a list of their currently assigned and past trips.
    *   Perform only pre-defined status transitions, such as changing the status from 'Assigned' to 'In-Transit' (at trip start) and from 'In-Transit' to 'Delivered' (upon POD upload). All other status changes, particularly resolving an 'On Hold' state, must be performed by a manager.
    *   Upload a Proof of Delivery (POD) in photo or e-signature format to mark a trip as 'Delivered'. The POD submission shall require capturing the recipient's name and a timestamp.
    *   Access the 'Expense Submission' feature.
    *   View and download the documents for their currently assigned vehicle.
    *   Submit advance requests and leave applications.
    *   Report a trip halt by providing a mandatory text-based reason.
    *   Log specific events associated with a trip from a predefined list: 'Accident', 'Repair', 'Government Stoppage', 'Fueling', 'Trip Start'.
    *   Attach a photo to a logged event.
*   The system shall enforce Business Rule BR-005.
*   The system shall generate a high-priority alert on the Admin/Manager dashboard when a critical event is logged.

---

#### **4. Data Requirements**

##### **4.1 Vehicle Master (REQ-DAT-001)**
*   The system shall provide a centralized repository to manage all company-owned and outsourced vehicles.
*   The system shall allow a user to create a new vehicle record with fields for Truck Number, Model, Capacity (in Tons), Owner Details (including a flag for 'Company-Owned' vs. 'Outsourced'), Fuel Type, Last Service Date, and Next Service Due Date.
*   The system shall enforce Business Rule BR-002 and shall validate the truck number format against standard Indian vehicle registration number patterns.
*   The system shall allow a user to attach multiple documents to a vehicle record, each with a 'Document Type' (e.g., RC, Insurance, Fitness Certificate) and an 'Expiry Date'.
*   The system shall automatically generate an alert 30, 15, and 7 days before a document's expiry date.
*   The system shall allow a user to log service history entries for a vehicle.
*   Each vehicle record shall have an 'Active'/'Inactive' status field. Inactive vehicles shall be excluded from selection lists for new trips but retained in the database for historical reporting.

##### **4.2 Driver Master (REQ-DAT-002)**
*   The system shall provide a module to manage all driver information by extending the standard Odoo `hr.employee` model.
*   A driver record shall include fields for License Number and License Expiry Date.
*   The system shall allow for the upload and storage of a scanned copy of the driver's license.
*   The system shall generate an alert 30, 15, and 7 days before a driver's license expiry date.
*   The system shall display a log of all trips and incentives earned by the driver.
*   The system shall enforce Business Rule BR-003.
*   Each driver record shall have an 'Active'/'Inactive' status field. Inactive drivers shall be excluded from selection lists for new trips but retained in the database for historical reporting.

##### **4.3 Customer Master (REQ-DAT-003)**
*   The system shall provide a centralized database of all clients by extending Odoo's `res.partner` model.
*   The system shall allow a user to create a new customer with fields for Customer Name, Billing Address, GSTIN, and Contact Person.
*   The system shall validate the format of the GSTIN field upon entry.
*   The system shall allow a customer to have multiple shipping locations associated with their record.
*   The system shall allow storing customer-specific rate agreements.
*   Each customer record shall have an 'Active'/'Inactive' status field. Inactive customers shall be excluded from selection lists for new trips but retained in the database for historical reporting.

##### **4.4 Route Master (REQ-DAT-004)**
*   The system shall provide a module to pre-define standard transportation routes.
*   The system shall allow a user to create a new route with fields for Route Name, Source, Destination, Standard Distance (km), and Estimated Transit Time.
*   The system shall auto-populate the source, destination, and distance fields when a pre-defined route is selected during trip creation.

##### **4.5 Material Master (REQ-DAT-005)**
*   The system shall provide a repository for the types of materials transported.
*   The system shall allow an Admin to create and manage a list of material types and associate special handling instructions with each.

##### **4.6 Data Privacy (REQ-DAT-007)**
*   The system shall classify data to identify Personally Identifiable Information (PII), such as driver and customer contact details.
*   Access to PII shall be restricted based on the user's role and the principle of least privilege.
*   All PII shall be handled in accordance with the Indian Digital Personal Data Protection Act (DPDPA), 2023.

##### **4.7 Audit Trails (REQ-DAT-008)**
*   The system shall maintain an immutable audit trail for all create, update, and delete (CRUD) operations on critical data models, including Trips, Invoices, Payments, and user permissions.
*   Each audit log entry shall record the user who performed the action, the timestamp, the type of action, the record affected, and the specific data that was changed (old and new values).
*   Audit logs shall be accessible only to users with the 'Admin' role.

---

#### **5. External Interface Requirements**

##### **5.1 User Interfaces (REQ-INT-001)**
*   The user interface shall follow Odoo's standard design language for consistency, utilizing standard views like Kanban, List, Form, and Map where appropriate.
*   The driver-facing interface shall be simplified with large buttons and a clear layout for ease of use on mobile devices.
*   All screens shall be fully responsive and functional on screen sizes from 360px width upwards.
*   The system shall strive to meet WCAG 2.1 Level AA accessibility standards.
*   The system shall provide key screens including: Admin/Manager Dashboard, Trip List View, Trip Form View, and Driver Portal View.

##### **5.2 Hardware Interfaces (REQ-INT-002)**
*   The system shall require access to the device's camera via the web browser for uploading photos for POD and expense receipts.

##### **5.3 Software Interfaces (REQ-INT-003)**
*   **GPS Provider Integration:**
    *   The system shall integrate with a third-party GPS provider's API to fetch real-time location data.
    *   The integration pattern shall be asynchronous via a RabbitMQ message queue to ensure message durability and delivery guarantees.
    *   A dedicated microservice shall poll the GPS API, validate the data, and publish it to a RabbitMQ topic.
    *   The microservice shall expect location data in a JSON format with a fixed data contract: `{ "vehicle_identifier": "string", "latitude": float, "longitude": float, "timestamp": "ISO 8601 string" }`.
    *   An Odoo scheduled job shall consume data from the message queue to update vehicle locations.
    *   The microservice shall implement a robust error handling strategy, including an exponential backoff retry mechanism for polling the GPS API, a dead-letter queue (DLQ) for messages that repeatedly fail processing, and comprehensive logging of API and message queue failures.
*   **GSP Integration:**
    *   The system shall integrate with a GSP's API to generate compliant e-invoices.
    *   The integration pattern shall be a synchronous API call with an asynchronous fallback. If a synchronous call fails or times out, the task shall be added to a dedicated queue for automatic retries with exponential backoff.
    *   The system shall use secure API keys for authentication with the GSP, which shall be stored and managed securely using AWS Secrets Manager.
*   **API Versioning:**
    *   All external API integrations shall specify and use a fixed version of the provider's API to prevent breaking changes from unexpected updates.

##### **5.4 Communication Interfaces (REQ-INT-004)**
*   All communication between the client browser and the server shall be over HTTPS.
*   HTTPS communication shall be enforced with TLS 1.2 or newer.

---

#### **6. System Architecture & Technology**

##### **6.1 High-Level Architecture (REQ-ARC-001)**
*   The system shall use a Hybrid architectural pattern: Modular Monolith with a Decoupled Microservice.
*   The core TMS application shall be a modular monolith built as an Odoo 18 addon, fronted by an Nginx reverse proxy.
*   A separate, lightweight microservice, exposed via AWS API Gateway, shall be used for high-volume GPS data ingestion.
*   The GPS ingestion microservice shall be developed using the FastAPI Python framework and packaged as a distinct Docker image.
*   The GPS ingestion microservice shall communicate with the Odoo monolith asynchronously via an Amazon MQ for RabbitMQ message queue.

##### **6.2 Technology Stack (REQ-TEC-001)**
*   **Platform:** Odoo 18
*   **Backend:** Python 3.11, FastAPI (for GPS microservice)
*   **Database:** Amazon RDS for PostgreSQL 16
*   **Frontend Framework:** Odoo Web Library (OWL) 2.0
*   **Infrastructure Components:**
    *   **Caching:** Amazon ElastiCache for Redis
    *   **Message Queue:** Amazon MQ for RabbitMQ
    *   **Reverse Proxy:** Nginx
    *   **API Gateway:** AWS API Gateway
*   **Storage:** Amazon S3
*   **Deployment & Orchestration:**
    *   **Containerization:** Docker
    *   **Orchestration:** Amazon EKS
    *   **Infrastructure as Code:** Terraform
*   **CI/CD & Development:**
    *   **CI/CD Pipeline:** GitHub Actions
    *   **Code Quality:** Flake8 (linting), Black (formatting), isort (import sorting)
    *   **Testing Framework:** Pytest
*   **Security:**
    *   **Secrets Management:** AWS Secrets Manager

---

#### **7. Non-Functional Requirements (NFRs)**

##### **7.1 Performance (REQ-NFR-001)**
*   95% of all standard GET requests shall be completed in under 200ms.
*   Key pages (Dashboard, Trip List) shall achieve a Largest Contentful Paint (LCP) of under 3 seconds on a standard broadband connection.
*   The system shall submit an e-invoice generation request and provide initial feedback to the user within 2 seconds. The final status of the invoice (e.g., 'Generated', 'Failed') will be updated asynchronously as soon as the response is received from the GSP.
*   The end-to-end latency for processing a GPS data point (from ingestion by the microservice to update in the Odoo database) shall be under 10 seconds.
*   The system shall support a minimum of 100 concurrent users performing standard operations without performance degradation.

##### **7.2 Reliability & Availability (REQ-NFR-002)**
*   The system shall maintain an uptime of 99.9% during business hours, excluding scheduled maintenance windows.
*   The PostgreSQL database shall be configured for Point-In-Time-Recovery (PITR).
*   The backup strategy shall include daily automated snapshots of the database and transaction logs. Database snapshots shall be retained for at least 30 days.
*   The entire infrastructure shall be defined using Infrastructure as Code (Terraform).
*   A read replica of the PostgreSQL database shall be maintained for failover.
*   The application shall be deployed with multiple replicas in Kubernetes for high availability.
*   The system shall have a Recovery Point Objective (RPO) of 15 minutes and a Recovery Time Objective (RTO) of 4 hours for disaster recovery scenarios.

##### **7.3 Security (REQ-NFR-003)**
*   User authentication shall be handled by Odoo's built-in user management system (`res.users`), including its password policies and multi-factor authentication capabilities.
*   Authorization shall be strictly enforced using Odoo's Role-Based Access Control (RBAC), including model-level permissions (`ir.model.access.csv`) and row-level security (`ir.rule`).
*   All web traffic shall be encrypted in transit using TLS 1.2 or newer, terminated at the reverse proxy or load balancer.
*   Data at rest in the managed PostgreSQL database and in the object storage bucket shall be encrypted by default by the cloud provider.
*   All sensitive credentials (API keys, database passwords, third-party tokens) shall be managed using AWS Secrets Manager and injected into the application environment at runtime, never stored in the codebase or configuration files.
*   The system shall implement user session timeout after a configurable period of inactivity.
*   The system shall be developed with best practices to mitigate common web application vulnerabilities as defined by the OWASP Top 10.
*   The system shall undergo periodic automated vulnerability scanning, and a third-party penetration test shall be conducted before the initial production launch and annually thereafter.

##### **7.4 Software Quality Attributes (REQ-NFR-004)**
*   **Maintainability:**
    *   The TMS shall be developed as a self-contained Odoo addon with clear dependencies.
    *   The code shall be automatically formatted using Black and isort, and validated against Flake8 standards in the CI/CD pipeline.
    *   All custom models and complex methods shall be documented with docstrings following Google Style.
*   **Scalability:**
    *   The Odoo application and the GPS ingestion service shall be designed to scale horizontally by adjusting replica counts in Kubernetes.
    *   The managed database shall be able to be scaled vertically (instance size) and support read replicas for improved read performance.
    *   The system architecture shall support data growth of at least 100GB per year.
*   **Testability:**
    *   A minimum of 80% unit test coverage, implemented using the Pytest framework, shall be required for all new business logic and enforced by the CI/CD pipeline.
    *   The CI/CD pipeline shall execute a suite of automated integration tests.
    *   A dedicated, production-like staging environment shall be maintained for user acceptance testing (UAT) and pre-release validation.
    *   Processes for generating and anonymizing test data shall be established.
*   **Localization:**
    *   The system shall be developed using internationalization (i18n) best practices, such as externalizing all user-facing strings into resource files, to facilitate future translation into multiple languages.
*   **Documentation:**
    *   The project shall produce and maintain comprehensive documentation, including a User Manual for end-users, an Administrator Guide for system configuration and management, and technical documentation (architecture diagrams, API specifications) for developers.

##### **7.5 Data Retention (REQ-NFR-005)**
*   A data retention and archiving policy shall be established to manage database growth and maintain system performance.
*   Detailed, high-volume data such as GPS location history shall be aggregated and archived to cold storage after 12 months.
*   Core transactional records, including trip summaries, invoices, and payment records, shall be retained for a minimum of 7 years to meet financial compliance requirements.
*   Audit logs shall be retained for a minimum of 18 months online and archived for 7 years.

---

#### **8. Reporting, Alerts, and Monitoring**

##### **8.1 Reporting (REQ-REP-001)**
*   The system shall provide standard reports exportable to Excel and PDF.
*   The system shall provide the following reports:
    *   **Trip Report:** Filterable by date range, customer, vehicle, and driver.
    *   **Vehicle Utilization Report:** Showing on-trip vs. idle time.
    *   **Driver Performance Report:** With metrics like on-time delivery percentage and total incentives.
    *   **Fuel Efficiency Report:** Calculating km per liter for each vehicle.
    *   **Trip Profitability Report:** Listing revenue, expenses, and net profit per trip.
    *   **Vehicle Profitability Report:** Aggregating revenue and expenses per vehicle.
    *   **Customer Revenue Report:** Showing total revenue per customer.
    *   **Outstanding Invoices Report (Aging Report):** Categorized by overdue duration (0-30, 31-60, 61-90, 90+ days).
    *   **Detailed Expense Report:** Filterable by type, vehicle, and driver.
    *   **Trip Interruption Report:** Filterable by date range, driver, vehicle, and event/halt type to analyze operational disruptions.

##### **8.2 Dashboard (REQ-REP-002)**
*   The system shall provide a real-time, filterable dashboard for Admin/Manager roles.
*   The dashboard shall include a 'Vehicle Status' widget as a pie chart (Available vs. On-Trip vs. In-Maintenance).
*   The dashboard shall include KPIs for 'Pending Deliveries' and 'Delayed Trips'.
*   The dashboard shall include financial summary KPIs for 'Pending Payment Collections', 'Total Revenue (MTD/YTD)', and 'Total Expenses (MTD/YTD)'.
*   The dashboard shall include an 'Alerts Panel' for upcoming document expiries, critical trip events logged by drivers (e.g., Accident, Repair), low card balances, and other critical system alerts.

##### **8.3 Monitoring & Logging (REQ-REP-003)**
*   The system shall use Prometheus for scraping key application and infrastructure metrics from Kubernetes and application endpoints.
*   The system shall use Fluentbit to collect logs from all application containers, which shall be forwarded to a centralized OpenSearch cluster for storage, indexing, and analysis.
*   Application logs shall be written in a structured JSON format to facilitate efficient parsing, searching, and analysis in the centralized logging system.
*   The system shall use Grafana for creating unified monitoring dashboards for both metrics (from Prometheus) and logs (from OpenSearch).
*   Monitored metrics shall include technical indicators (CPU/memory usage, API latency, error rates) and key business indicators (e.g., trips created per hour, invoice generation failures, POD uploads).
*   The system shall use Alertmanager, integrated with Prometheus, to send notifications for critical events, including high API latency, high error rates, and a full message queue.
*   Centralized logs shall be retained for 90 days for active querying and archived for 12 months.

##### **8.4 System Alerts and Notifications (REQ-REP-004)**
*   The system shall deliver alerts and notifications through multiple channels.
*   At a minimum, delivery channels shall include Odoo's internal notification system (bell icon) and email.
*   The system shall provide a user-configurable notification settings screen.
*   On this screen, users shall be able to choose which types of alerts they receive (e.g., document expiry, critical trip events, low card balance) and via which channel(s) to prevent alert fatigue.
*   The system shall provide an administrative interface for managing the rules, thresholds, and recipients of system-level alerts (e.g., API failures, high error rates).
*   Planned maintenance windows shall be scheduled during off-peak hours, and users shall be notified at least 24 hours in advance.

---

#### **9. Future Considerations**

##### **9.1 Future-Ready Features (REQ-FTR-001)**
*   The system design shall consider future implementation of live load tracking for customers via a public link or a dedicated customer login portal.
*   The system design shall consider future integration with logistics marketplaces.
*   The system design shall consider future implementation of predictive maintenance alerts using AI.
*   The system design shall consider future implementation of a multilingual UI.

---

#### **10. Transition Requirements**

##### **10.1 Implementation Strategy (REQ-TRN-001)**
*   The system shall be deployed using a phased rollout approach to minimize business disruption.
*   **Phase 1 (Core Operations):** Deployment of Master Data modules (Vehicle, Driver, Customer), Trip Management, and Expense Management. This phase will run in parallel with the legacy system for one billing cycle.
*   **Phase 2 (Finance & Tracking):** Deployment of Invoicing & Payments, GPS Tracking integration, Dashboards, and Reporting. This phase will commence after successful validation of Phase 1.

##### **10.2 Data Migration (REQ-TRN-002)**
*   A one-time data migration from the legacy system shall be performed before go-live.
*   **Scope:** The migration shall include active Customers, all Vehicles, active Drivers, and open financial transactions (unpaid invoices).
*   **Tools:** Migration will be performed using Odoo's Data Import module, supplemented with custom Python scripts for data transformation and cleansing.
*   **Validation:** A mandatory dry-run of the migration shall be performed in the staging environment. Post-migration validation shall include record counts, financial reconciliation of open balances, and spot-checking of at least 10% of migrated master records.
*   **Rollback:** In case of migration failure during the production cutover, the process will be halted, and the cutover will be rescheduled.

##### **10.3 Training Plan (REQ-TRN-003)**
*   Role-based training shall be provided to all user classes before go-live.
*   **Admin, Dispatch Manager, Finance Officer:** Shall receive instructor-led classroom training sessions covering all relevant modules.
*   **Driver:** Shall be provided with short video tutorials accessible via the web portal and a laminated quick-reference guide (QRG).
*   **Materials:** A comprehensive User Manual and role-specific QRGs shall be created and distributed.

##### **10.4 Cutover Plan (REQ-TRN-004)**
*   The production go-live (cutover) shall be scheduled over a weekend to minimize impact on operations.
*   **Sequence:**
    1.  Freeze all transactions in the legacy system.
    2.  Perform final data migration.
    3.  Execute a post-migration validation checklist.
    4.  Switch user access from the legacy system to the new TMS.
    5.  Set the legacy system to a read-only state.
*   **Success Criteria:** The cutover will be deemed successful if a designated super-user can complete a full, predefined end-to-end business process (from trip creation to payment recording) without critical errors.
*   **Rollback Plan:** If the success criteria are not met within 8 hours of the planned go-live, the cutover will be rolled back by reverting user access to the legacy system.
*   **Post-Launch Support:** A dedicated support team (hypercare) will be available for the first two weeks post-go-live to address user issues promptly.

##### **10.5 Legacy System Decommissioning (REQ-TRN-005)**
*   The legacy system shall be maintained in a read-only state for 6 months post-go-live for historical data lookup and audit purposes.
*   After 6 months, a final data archive will be taken, and the legacy system will be fully decommissioned.

---

#### **11. Business Rules and Constraints**

##### **11.1 Business Rules (REQ-BRC-001)**
*   **BR-001:** A user shall be assigned only one primary role (Admin, Dispatch Manager, Finance Officer, Driver).
*   **BR-002:** The 'Truck Number' for each vehicle must be unique across all vehicle records.
*   **BR-003:** A driver with an expired license cannot be assigned to a new trip.
*   **BR-004:** The trip status lifecycle must follow the defined path: `Planned` -> `Assigned` -> `In-Transit` <-> `On Hold` -> `Delivered` -> `Completed` -> `Invoiced` -> `Paid`.
*   **BR-005:** Logging of critical events ('Accident', 'Repair', 'Government Stoppage') by a driver shall automatically change the trip status to 'On Hold'.
*   **BR-006:** A new trip record cannot be saved without a valid Customer, Source location, and Destination location.
*   **BR-007:** The specified material weight for a trip shall not exceed the assigned vehicle's registered capacity.
*   **BR-008:** The 'Expected Delivery Date' for a new trip must be on or after the current date.
*   **BR-009:** The odometer reading submitted with a 'Diesel' expense entry must be greater than the previously recorded odometer reading for that vehicle.
*   **BR-010:** An invoice can only be generated for a trip that is in the 'Completed' state.
*   **BR-011:** All system-generated invoice numbers must follow the sequential format: `INV/YYYY/NNNNN`.

##### **11.2 Regulatory Compliance (REQ-BRC-002)**
*   The system's e-invoicing functionality must comply with the Goods and Services Tax Act, 2017, and all subsequent e-invoicing mandates issued by the GST Council of India.
*   Vehicle and driver data management, particularly document validity checks, must adhere to the requirements of the Indian Motor Vehicles Act, 1988.
*   The collection, storage, and processing of all personal data (customer and driver) must comply with the Indian Digital Personal Data Protection Act (DPDPA), 2023.

##### **11.3 Organizational Policies (REQ-BRC-003)**
*   The system shall provide a configurable setting for maximum allowable expense amounts per category (e.g., Food) that can be approved without requiring Admin-level review.
*   The system shall enforce a policy that all trip-related expenses must be submitted by the driver within 7 calendar days of the trip's 'Delivered' date. Submissions after this period will be flagged for manager review.