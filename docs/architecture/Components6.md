# 1 Components

## 1.1 Components

### 1.1.1 TMS Odoo Addon

#### 1.1.1.1 Id

tms-odoo-addon-001

#### 1.1.1.2 Name

TMS Odoo Addon

#### 1.1.1.3 Description

The core modular monolith application component, built as an installable Odoo 18 addon. It encapsulates all primary business logic, data models, and standard user interfaces for the Transport Management System.

#### 1.1.1.4 Type

🔹 ModularMonolith

#### 1.1.1.5 Dependencies

- integration-gateway-003
- background-job-processor-004
- analytics-engine-005
- security-framework-006
- driver-portal-view-007

#### 1.1.1.6 Properties

| Property | Value |
|----------|-------|
| Odoo Version | 18 |
| Python Version | 3.11 |

#### 1.1.1.7 Interfaces

- Odoo Web UI
- Odoo ORM API

#### 1.1.1.8 Technology

Odoo 18, Python 3.11

#### 1.1.1.9 Resources

| Property | Value |
|----------|-------|
| Cpu | 4 vCPU |
| Memory | 16GB |
| Storage | Dependent on database and filestore size |

#### 1.1.1.10 Configuration

| Property | Value |
|----------|-------|
| Workers | Recommended based on user count |
| Db Host | From AWS Secrets Manager |
| Filestore S3 Bucket | From AWS Secrets Manager |

#### 1.1.1.11 Health Check

| Property | Value |
|----------|-------|
| Path | /web/database/selector |
| Interval | 30 |
| Timeout | 10 |

#### 1.1.1.12 Responsible Features

- REQ-1-002
- REQ-1-003
- REQ-1-004
- REQ-1-005
- REQ-1-012
- REQ-1-102
- REQ-1-103
- REQ-1-108
- REQ-1-111
- REQ-1-200
- REQ-1-203
- REQ-1-205
- REQ-1-900
- REQ-1-901
- REQ-1-902
- REQ-1-904

#### 1.1.1.13 Security

##### 1.1.1.13.1 Requires Authentication

✅ Yes

##### 1.1.1.13.2 Requires Authorization

✅ Yes

##### 1.1.1.13.3 Allowed Roles

- Admin
- Dispatch Manager
- Finance Officer
- Driver

### 1.1.2.0.0 GPS Ingestion Service

#### 1.1.2.1.0 Id

gps-ingestion-service-002

#### 1.1.2.2.0 Name

GPS Ingestion Service

#### 1.1.2.3.0 Description

A decoupled, lightweight microservice responsible for polling real-time location data from the third-party GPS provider's API, validating it, and publishing it to the message bus for asynchronous processing.

#### 1.1.2.4.0 Type

🔹 Microservice

#### 1.1.2.5.0 Dependencies

- messaging-bus-008

#### 1.1.2.6.0 Properties

| Property | Value |
|----------|-------|
| Framework | FastAPI |
| Python Version | 3.11 |

#### 1.1.2.7.0 Interfaces

- REST API Client (outbound)
- AMQP Publisher (outbound)

#### 1.1.2.8.0 Technology

FastAPI, Python 3.11, Docker

#### 1.1.2.9.0 Resources

| Property | Value |
|----------|-------|
| Cpu | 1 vCPU |
| Memory | 2GB |
| Network | 100Mbps |

#### 1.1.2.10.0 Configuration

| Property | Value |
|----------|-------|
| Gps Api Key | From AWS Secrets Manager |
| Polling Interval Seconds | 30 |
| Rabbitmq Url | From AWS Secrets Manager |
| Dlq Name | gps_dlq |

#### 1.1.2.11.0 Health Check

| Property | Value |
|----------|-------|
| Path | /health |
| Interval | 30 |
| Timeout | 5 |

#### 1.1.2.12.0 Responsible Features

- REQ-1-013
- REQ-1-301
- REQ-1-401
- REQ-1-400

#### 1.1.2.13.0 Security

##### 1.1.2.13.1 Requires Authentication

❌ No

##### 1.1.2.13.2 Requires Authorization

❌ No

##### 1.1.2.13.3 Allowed Roles

*No items available*

### 1.1.3.0.0 Integration Gateway

#### 1.1.3.1.0 Id

integration-gateway-003

#### 1.1.3.2.0 Name

Integration Gateway

#### 1.1.3.3.0 Description

A logical component representing the collection of clients and connectors within the Odoo addon that communicate with external services. It handles the specific protocols and error handling for each integration point.

#### 1.1.3.4.0 Type

🔹 Gateway

#### 1.1.3.5.0 Dependencies

- messaging-bus-008

#### 1.1.3.6.0 Properties

*No data available*

#### 1.1.3.7.0 Interfaces

- GSP REST API
- AMQP Consumer

#### 1.1.3.8.0 Technology

Python (requests library), Odoo Background Jobs, AMQP libraries

#### 1.1.3.9.0 Resources

*No data available*

#### 1.1.3.10.0 Configuration

| Property | Value |
|----------|-------|
| Gsp Api Key | From AWS Secrets Manager |
| Gsp Endpoint Url | Configurable in Odoo |
| Retry Policy | Exponential backoff |

#### 1.1.3.11.0 Health Check

*No data available*

#### 1.1.3.12.0 Responsible Features

- REQ-1-006
- REQ-1-007
- REQ-1-301
- REQ-1-302

#### 1.1.3.13.0 Security

##### 1.1.3.13.1 Requires Authentication

❌ No

##### 1.1.3.13.2 Requires Authorization

❌ No

##### 1.1.3.13.3 Allowed Roles

*No items available*

### 1.1.4.0.0 Background Job Processor

#### 1.1.4.1.0 Id

background-job-processor-004

#### 1.1.4.2.0 Name

Background Job Processor

#### 1.1.4.3.0 Description

Represents the Odoo scheduled action (`ir.cron`) system. This component is responsible for executing all recurring and asynchronous tasks within the main application.

#### 1.1.4.4.0 Type

🔹 Worker

#### 1.1.4.5.0 Dependencies

- tms-odoo-addon-001
- integration-gateway-003

#### 1.1.4.6.0 Properties

| Property | Value |
|----------|-------|
| Execution Engine | Odoo Cron |

#### 1.1.4.7.0 Interfaces

*No items available*

#### 1.1.4.8.0 Technology

Odoo 18

#### 1.1.4.9.0 Resources

##### 1.1.4.9.1 Cpu

Shared with Odoo workers

##### 1.1.4.9.2 Memory

Shared with Odoo workers

#### 1.1.4.10.0 Configuration

##### 1.1.4.10.1 Cron Worker Count

1

#### 1.1.4.11.0 Health Check

*No data available*

#### 1.1.4.12.0 Responsible Features

- REQ-1-301 (Consumption side)
- REQ-1-302 (Retry mechanism)
- REQ-1-660
- REQ-1-663
- REQ-1-010

#### 1.1.4.13.0 Security

##### 1.1.4.13.1 Requires Authentication

❌ No

##### 1.1.4.13.2 Requires Authorization

❌ No

##### 1.1.4.13.3 Allowed Roles

*No items available*

### 1.1.5.0.0 Analytics Engine

#### 1.1.5.1.0 Id

analytics-engine-005

#### 1.1.5.2.0 Name

Analytics Engine

#### 1.1.5.3.0 Description

A logical component within the Odoo addon responsible for aggregating data and calculating KPIs for dashboards, and generating all operational and financial reports.

#### 1.1.5.4.0 Type

🔹 Service

#### 1.1.5.5.0 Dependencies

- tms-odoo-addon-001

#### 1.1.5.6.0 Properties

| Property | Value |
|----------|-------|
| Reporting Framework | Odoo QWeb |

#### 1.1.5.7.0 Interfaces

- Odoo Report Actions

#### 1.1.5.8.0 Technology

Odoo 18 ORM, QWeb, Python

#### 1.1.5.9.0 Resources

*No data available*

#### 1.1.5.10.0 Configuration

*No data available*

#### 1.1.5.11.0 Health Check

*No data available*

#### 1.1.5.12.0 Responsible Features

- REQ-1-009
- REQ-1-600
- REQ-1-601
- REQ-1-111

#### 1.1.5.13.0 Security

##### 1.1.5.13.1 Requires Authentication

✅ Yes

##### 1.1.5.13.2 Requires Authorization

✅ Yes

##### 1.1.5.13.3 Allowed Roles

- Admin
- Dispatch Manager
- Finance Officer

### 1.1.6.0.0 Security Framework

#### 1.1.6.1.0 Id

security-framework-006

#### 1.1.6.2.0 Name

Security Framework

#### 1.1.6.3.0 Description

Represents the implementation of Role-Based Access Control (RBAC) using Odoo's native security features. This component is defined through XML data files containing security groups, access control lists (ACLs), and record rules.

#### 1.1.6.4.0 Type

🔹 Framework

#### 1.1.6.5.0 Dependencies

*No items available*

#### 1.1.6.6.0 Properties

*No data available*

#### 1.1.6.7.0 Interfaces

*No items available*

#### 1.1.6.8.0 Technology

Odoo 18 (res.groups, ir.rule, ir.model.access)

#### 1.1.6.9.0 Resources

*No data available*

#### 1.1.6.10.0 Configuration

*No data available*

#### 1.1.6.11.0 Health Check

*No data available*

#### 1.1.6.12.0 Responsible Features

- REQ-1-008
- REQ-1-101
- REQ-1-643

#### 1.1.6.13.0 Security

##### 1.1.6.13.1 Requires Authentication

✅ Yes

##### 1.1.6.13.2 Requires Authorization

✅ Yes

##### 1.1.6.13.3 Allowed Roles

*No items available*

### 1.1.7.0.0 Driver Portal View

#### 1.1.7.1.0 Id

driver-portal-view-007

#### 1.1.7.2.0 Name

Driver Portal View

#### 1.1.7.3.0 Description

A specialized, responsive user interface component built with Odoo's OWL framework. It provides a simplified, mobile-first experience for drivers to perform on-the-go tasks.

#### 1.1.7.4.0 Type

🔹 UIComponent

#### 1.1.7.5.0 Dependencies

- tms-odoo-addon-001

#### 1.1.7.6.0 Properties

| Property | Value |
|----------|-------|
| Responsive | ✅ |
| Mobile Optimized | ✅ |

#### 1.1.7.7.0 Interfaces

- Web UI

#### 1.1.7.8.0 Technology

Odoo OWL 2.0, JavaScript, XML, CSS

#### 1.1.7.9.0 Resources

*No data available*

#### 1.1.7.10.0 Configuration

*No data available*

#### 1.1.7.11.0 Health Check

*No data available*

#### 1.1.7.12.0 Responsible Features

- REQ-1-001
- REQ-1-112
- REQ-1-113
- REQ-1-114
- REQ-1-115
- REQ-1-107
- REQ-1-300

#### 1.1.7.13.0 Security

##### 1.1.7.13.1 Requires Authentication

✅ Yes

##### 1.1.7.13.2 Requires Authorization

✅ Yes

##### 1.1.7.13.3 Allowed Roles

- Driver

### 1.1.8.0.0 Messaging Bus

#### 1.1.8.1.0 Id

messaging-bus-008

#### 1.1.8.2.0 Name

Messaging Bus

#### 1.1.8.3.0 Description

The central messaging infrastructure component that decouples the GPS Ingestion Service from the TMS Odoo Addon. It provides reliable, asynchronous message delivery.

#### 1.1.8.4.0 Type

🔹 MessageBroker

#### 1.1.8.5.0 Dependencies

*No items available*

#### 1.1.8.6.0 Properties

| Property | Value |
|----------|-------|
| High Availability | ✅ |

#### 1.1.8.7.0 Interfaces

- AMQP Protocol

#### 1.1.8.8.0 Technology

RabbitMQ (Amazon MQ)

#### 1.1.8.9.0 Resources

##### 1.1.8.9.1 Cpu

Managed by AWS

##### 1.1.8.9.2 Memory

Managed by AWS

#### 1.1.8.10.0 Configuration

##### 1.1.8.10.1 Vhost

/

##### 1.1.8.10.2 Queues

- gps_location_updates

##### 1.1.8.10.3 Exchanges

- tms_direct_exchange

##### 1.1.8.10.4 Dead Letter Exchange

tms_dlx

#### 1.1.8.11.0 Health Check

*No data available*

#### 1.1.8.12.0 Responsible Features

- REQ-1-301

#### 1.1.8.13.0 Security

##### 1.1.8.13.1 Requires Authentication

✅ Yes

##### 1.1.8.13.2 Requires Authorization

✅ Yes

##### 1.1.8.13.3 Allowed Roles

*No items available*

## 1.2.0.0.0 Configuration

| Property | Value |
|----------|-------|
| Environment | production |
| Logging Level | INFO |
| Secrets Management | AWS Secrets Manager |
| Infrastructure As Code | Terraform |
| Ci Cd Pipeline | GitHub Actions |
| Container Orchestration | Amazon EKS |

# 2.0.0.0.0 Component Relations

## 2.1.0.0.0 Architecture

### 2.1.1.0.0 Components

#### 2.1.1.1.0 TMS Core Module (Odoo Addon)

##### 2.1.1.1.1 Id

tms-core-module-001

##### 2.1.1.1.2 Name

TMS Core Module (Odoo Addon)

##### 2.1.1.1.3 Description

The primary modular monolith component encapsulating all core Transport Management System business logic, data models, and workflows. It is developed as an installable addon for the Odoo 18 framework. REQ-1-002.

##### 2.1.1.1.4 Type

🔹 Module

##### 2.1.1.1.5 Dependencies

- gps-data-consumer-001
- gsp-integration-client-001
- alerting-engine-001
- gps-ingestion-service-001

##### 2.1.1.1.6 Properties

| Property | Value |
|----------|-------|
| Version | 1.0.0 |
| Addon Name | tms_management |

##### 2.1.1.1.7 Interfaces

*No items available*

##### 2.1.1.1.8 Technology

Odoo 18, Python 3.11

##### 2.1.1.1.9 Resources

| Property | Value |
|----------|-------|
| Cpu | 4 cores |
| Memory | 16GB |
| Storage | 50GB |

##### 2.1.1.1.10 Configuration

###### 2.1.1.1.10.1 Odoo Workers

5

##### 2.1.1.1.11.0 Health Check

| Property | Value |
|----------|-------|
| Path | / |
| Interval | 60 |
| Timeout | 15 |

##### 2.1.1.1.12.0 Responsible Features

- Transport Management System (TMS)

##### 2.1.1.1.13.0 Security

###### 2.1.1.1.13.1 Requires Authentication

✅ Yes

###### 2.1.1.1.13.2 Requires Authorization

✅ Yes

###### 2.1.1.1.13.3 Allowed Roles

- Admin
- Dispatch Manager
- Finance Officer
- Driver

#### 2.1.1.2.0.0 Master Data Service

##### 2.1.1.2.1.0 Id

master-data-service-001

##### 2.1.1.2.2.0 Name

Master Data Service

##### 2.1.1.2.3.0 Description

Manages the Create, Read, Update, and Deactivation (CRUD) operations for core business entities: Vehicles, Drivers, Customers, Routes, and Materials. Implemented by extending Odoo's native models (`res.partner`, `hr.employee`) and creating new ones. REQ-1-003, REQ-1-012.

##### 2.1.1.2.4.0 Type

🔹 Service

##### 2.1.1.2.5.0 Dependencies

*No items available*

##### 2.1.1.2.6.0 Properties

*No data available*

##### 2.1.1.2.7.0 Interfaces

*No items available*

##### 2.1.1.2.8.0 Technology

Odoo 18 ORM

##### 2.1.1.2.9.0 Resources

*No data available*

##### 2.1.1.2.10.0 Configuration

*No data available*

##### 2.1.1.2.11.0 Health Check

*Not specified*

##### 2.1.1.2.12.0 Responsible Features

- Vehicle Master Data (REQ-1-200)
- Driver Master Data (REQ-1-203)
- Customer Master Data (REQ-1-205)
- Route Master Data (REQ-1-206)
- Material Master Data (REQ-1-003)

##### 2.1.1.2.13.0 Security

###### 2.1.1.2.13.1 Requires Authentication

✅ Yes

###### 2.1.1.2.13.2 Requires Authorization

✅ Yes

###### 2.1.1.2.13.3 Allowed Roles

- Admin
- Dispatch Manager

#### 2.1.1.3.0.0 Trip Management Service

##### 2.1.1.3.1.0 Id

trip-management-service-001

##### 2.1.1.3.2.0 Name

Trip Management Service

##### 2.1.1.3.3.0 Description

Orchestrates the entire lifecycle of a transport job. This includes trip creation, assignment, state transitions according to a strict state machine, cancellation logic, and logging of critical events. Implemented as the `tms.trip` Odoo model. REQ-1-004, REQ-1-103.

##### 2.1.1.3.4.0 Type

🔹 Service

##### 2.1.1.3.5.0 Dependencies

- master-data-service-001
- expense-management-service-001
- alerting-engine-001

##### 2.1.1.3.6.0 Properties

*No data available*

##### 2.1.1.3.7.0 Interfaces

*No items available*

##### 2.1.1.3.8.0 Technology

Odoo 18 ORM

##### 2.1.1.3.9.0 Resources

*No data available*

##### 2.1.1.3.10.0 Configuration

*No data available*

##### 2.1.1.3.11.0 Health Check

*Not specified*

##### 2.1.1.3.12.0 Responsible Features

- Trip Lifecycle Management (REQ-1-103)
- Trip Creation (REQ-1-102)
- Trip Cancellation (REQ-1-104)
- Trip Event Logging (REQ-1-115)

##### 2.1.1.3.13.0 Security

###### 2.1.1.3.13.1 Requires Authentication

✅ Yes

###### 2.1.1.3.13.2 Requires Authorization

✅ Yes

###### 2.1.1.3.13.3 Allowed Roles

- Admin
- Dispatch Manager
- Driver

#### 2.1.1.4.0.0 Expense Management Service

##### 2.1.1.4.1.0 Id

expense-management-service-001

##### 2.1.1.4.2.0 Name

Expense Management Service

##### 2.1.1.4.3.0 Description

Manages the workflow for trip-related expenses, from submission by drivers via the portal to the review and approval/rejection process by managers. Enforces validation rules, such as for odometer readings. REQ-1-107, REQ-1-108, REQ-1-903.

##### 2.1.1.4.4.0 Type

🔹 Service

##### 2.1.1.4.5.0 Dependencies

- trip-management-service-001
- driver-portal-ui-001

##### 2.1.1.4.6.0 Properties

*No data available*

##### 2.1.1.4.7.0 Interfaces

*No items available*

##### 2.1.1.4.8.0 Technology

Odoo 18 ORM

##### 2.1.1.4.9.0 Resources

*No data available*

##### 2.1.1.4.10.0 Configuration

*No data available*

##### 2.1.1.4.11.0 Health Check

*Not specified*

##### 2.1.1.4.12.0 Responsible Features

- Expense Submission
- Expense Approval Workflow
- Odometer Validation

##### 2.1.1.4.13.0 Security

###### 2.1.1.4.13.1 Requires Authentication

✅ Yes

###### 2.1.1.4.13.2 Requires Authorization

✅ Yes

###### 2.1.1.4.13.3 Allowed Roles

- Dispatch Manager
- Finance Officer
- Driver

#### 2.1.1.5.0.0 Financial Service

##### 2.1.1.5.1.0 Id

financial-service-001

##### 2.1.1.5.2.0 Name

Financial Service

##### 2.1.1.5.3.0 Description

Handles all financial aspects of the TMS, including the generation of GST-compliant invoices, tracking of customer payments and receivables, and the automatic calculation of trip profitability. REQ-1-005, REQ-1-111.

##### 2.1.1.5.4.0 Type

🔹 Service

##### 2.1.1.5.5.0 Dependencies

- trip-management-service-001
- gsp-integration-client-001
- expense-management-service-001

##### 2.1.1.5.6.0 Properties

*No data available*

##### 2.1.1.5.7.0 Interfaces

*No items available*

##### 2.1.1.5.8.0 Technology

Odoo 18 ORM (extending account.move)

##### 2.1.1.5.9.0 Resources

*No data available*

##### 2.1.1.5.10.0 Configuration

*No data available*

##### 2.1.1.5.11.0 Health Check

*Not specified*

##### 2.1.1.5.12.0 Responsible Features

- GST-Compliant Invoicing
- Customer Receivables Ledger
- Trip Profitability Calculation

##### 2.1.1.5.13.0 Security

###### 2.1.1.5.13.1 Requires Authentication

✅ Yes

###### 2.1.1.5.13.2 Requires Authorization

✅ Yes

###### 2.1.1.5.13.3 Allowed Roles

- Admin
- Finance Officer

#### 2.1.1.6.0.0 RBAC Service

##### 2.1.1.6.1.0 Id

rbac-service-001

##### 2.1.1.6.2.0 Name

RBAC Service

##### 2.1.1.6.3.0 Description

Implements the Role-Based Access Control mechanism. Defines security groups, access control lists (ACLs), and record rules (`ir.rule`) to enforce data visibility, feature access, and separation of duties for different user roles. REQ-1-008, REQ-1-643.

##### 2.1.1.6.4.0 Type

🔹 Security

##### 2.1.1.6.5.0 Dependencies

*No items available*

##### 2.1.1.6.6.0 Properties

*No data available*

##### 2.1.1.6.7.0 Interfaces

*No items available*

##### 2.1.1.6.8.0 Technology

Odoo 18 Security Framework (XML)

##### 2.1.1.6.9.0 Resources

*No data available*

##### 2.1.1.6.10.0 Configuration

*No data available*

##### 2.1.1.6.11.0 Health Check

*Not specified*

##### 2.1.1.6.12.0 Responsible Features

- Role Permissions Definition
- Driver Data Segregation
- Separation of Duties Enforcement

##### 2.1.1.6.13.0 Security

###### 2.1.1.6.13.1 Requires Authentication

✅ Yes

###### 2.1.1.6.13.2 Requires Authorization

✅ Yes

###### 2.1.1.6.13.3 Allowed Roles

- Admin

#### 2.1.1.7.0.0 TMS Web UI (Admin/Manager Portal)

##### 2.1.1.7.1.0 Id

tms-web-ui-001

##### 2.1.1.7.2.0 Name

TMS Web UI (Admin/Manager Portal)

##### 2.1.1.7.3.0 Description

The standard user interface for back-office roles (Admin, Manager, Finance), rendered using Odoo's native view system (List, Form, Kanban, Map) to ensure a consistent and familiar user experience. REQ-1-300.

##### 2.1.1.7.4.0 Type

🔹 UI

##### 2.1.1.7.5.0 Dependencies

- master-data-service-001
- trip-management-service-001
- financial-service-001
- reporting-engine-001
- dashboard-service-001

##### 2.1.1.7.6.0 Properties

*No data available*

##### 2.1.1.7.7.0 Interfaces

*No items available*

##### 2.1.1.7.8.0 Technology

Odoo 18 Views (XML)

##### 2.1.1.7.9.0 Resources

*No data available*

##### 2.1.1.7.10.0 Configuration

*No data available*

##### 2.1.1.7.11.0 Health Check

*Not specified*

##### 2.1.1.7.12.0 Responsible Features

- Master Data Views
- Trip Management Views
- Dashboard Visualization
- Report Visualization

##### 2.1.1.7.13.0 Security

###### 2.1.1.7.13.1 Requires Authentication

✅ Yes

###### 2.1.1.7.13.2 Requires Authorization

✅ Yes

###### 2.1.1.7.13.3 Allowed Roles

- Admin
- Dispatch Manager
- Finance Officer

#### 2.1.1.8.0.0 Driver Portal UI

##### 2.1.1.8.1.0 Id

driver-portal-ui-001

##### 2.1.1.8.2.0 Name

Driver Portal UI

##### 2.1.1.8.3.0 Description

A custom, responsive UI component optimized for mobile web browsers. It provides drivers with a simplified interface featuring large touch targets for on-the-go operations like trip status updates and expense submissions. REQ-1-112.

##### 2.1.1.8.4.0 Type

🔹 UI

##### 2.1.1.8.5.0 Dependencies

- trip-management-service-001
- expense-management-service-001

##### 2.1.1.8.6.0 Properties

| Property | Value |
|----------|-------|
| Framework | OWL 2.0 |

##### 2.1.1.8.7.0 Interfaces

*No items available*

##### 2.1.1.8.8.0 Technology

Odoo OWL 2.0 Framework, JavaScript, CSS/Sass

##### 2.1.1.8.9.0 Resources

*No data available*

##### 2.1.1.8.10.0 Configuration

*No data available*

##### 2.1.1.8.11.0 Health Check

*Not specified*

##### 2.1.1.8.12.0 Responsible Features

- Mobile-Optimized Driver View
- Driver Trip Status Updates (REQ-1-113)
- Proof of Delivery Upload (REQ-1-114)
- Driver Expense Submission (REQ-1-107)

##### 2.1.1.8.13.0 Security

###### 2.1.1.8.13.1 Requires Authentication

✅ Yes

###### 2.1.1.8.13.2 Requires Authorization

✅ Yes

###### 2.1.1.8.13.3 Allowed Roles

- Driver

#### 2.1.1.9.0.0 GSP Integration Client

##### 2.1.1.9.1.0 Id

gsp-integration-client-001

##### 2.1.1.9.2.0 Name

GSP Integration Client

##### 2.1.1.9.3.0 Description

Manages all communication with the external GST Suvidha Provider (GSP) API. It handles the synchronous REST calls for generating e-invoice IRNs and implements a fallback mechanism to an asynchronous background job queue upon failure. REQ-1-302.

##### 2.1.1.9.4.0 Type

🔹 Integration

##### 2.1.1.9.5.0 Dependencies

- financial-service-001

##### 2.1.1.9.6.0 Properties

| Property | Value |
|----------|-------|
| Retry Policy | Exponential Backoff |

##### 2.1.1.9.7.0 Interfaces

*No items available*

##### 2.1.1.9.8.0 Technology

Python (requests), Odoo Job Queue

##### 2.1.1.9.9.0 Resources

*No data available*

##### 2.1.1.9.10.0 Configuration

###### 2.1.1.9.10.1 Gsp Api Endpoint

Stored in AWS Secrets Manager

###### 2.1.1.9.10.2 Gsp Api Key

Stored in AWS Secrets Manager

##### 2.1.1.9.11.0 Health Check

*Not specified*

##### 2.1.1.9.12.0 Responsible Features

- E-Invoice IRN Generation (REQ-1-006)

##### 2.1.1.9.13.0 Security

###### 2.1.1.9.13.1 Requires Authentication

✅ Yes

###### 2.1.1.9.13.2 Requires Authorization

✅ Yes

###### 2.1.1.9.13.3 Allowed Roles

- Finance Officer

#### 2.1.1.10.0.0 GPS Data Consumer

##### 2.1.1.10.1.0 Id

gps-data-consumer-001

##### 2.1.1.10.2.0 Name

GPS Data Consumer

##### 2.1.1.10.3.0 Description

An Odoo scheduled job that acts as a RabbitMQ consumer. It polls the designated queue, retrieves validated vehicle location messages, and updates the corresponding vehicle records in the Odoo database. REQ-1-301.

##### 2.1.1.10.4.0 Type

🔹 Background Worker

##### 2.1.1.10.5.0 Dependencies

- master-data-service-001
- RabbitMQ Message Broker

##### 2.1.1.10.6.0 Properties

| Property | Value |
|----------|-------|
| Queue Name | gps_location_updates |

##### 2.1.1.10.7.0 Interfaces

*No items available*

##### 2.1.1.10.8.0 Technology

Odoo Scheduled Actions, Python (pika)

##### 2.1.1.10.9.0 Resources

*No data available*

##### 2.1.1.10.10.0 Configuration

###### 2.1.1.10.10.1 Batch Size

50 messages

###### 2.1.1.10.10.2 Poll Interval

5s

##### 2.1.1.10.11.0 Health Check

*Not specified*

##### 2.1.1.10.12.0 Responsible Features

- Real-time Vehicle Location Update in Odoo

##### 2.1.1.10.13.0 Security

###### 2.1.1.10.13.1 Requires Authentication

✅ Yes

###### 2.1.1.10.13.2 Notes

Authenticates to RabbitMQ via injected secrets.

#### 2.1.1.11.0.0 Alerting Engine

##### 2.1.1.11.1.0 Id

alerting-engine-001

##### 2.1.1.11.2.0 Name

Alerting Engine

##### 2.1.1.11.3.0 Description

A background processing component, implemented as Odoo scheduled jobs, that periodically scans the database to identify and generate alerts for predefined critical events like upcoming document/license expiries and low card balances. REQ-1-010.

##### 2.1.1.11.4.0 Type

🔹 Background Worker

##### 2.1.1.11.5.0 Dependencies

- master-data-service-001

##### 2.1.1.11.6.0 Properties

| Property | Value |
|----------|-------|
| Check Frequency | Daily |

##### 2.1.1.11.7.0 Interfaces

*No items available*

##### 2.1.1.11.8.0 Technology

Odoo Scheduled Actions

##### 2.1.1.11.9.0 Resources

*No data available*

##### 2.1.1.11.10.0 Configuration

###### 2.1.1.11.10.1 Expiry Thresholds

[30, 15, 7] days

##### 2.1.1.11.11.0 Health Check

*Not specified*

##### 2.1.1.11.12.0 Responsible Features

- Document Expiry Alerts (REQ-1-660)
- License Expiry Alerts (REQ-1-663)
- Low Balance Alerts (REQ-1-110)

##### 2.1.1.11.13.0 Security

###### 2.1.1.11.13.1 Requires Authentication

❌ No

###### 2.1.1.11.13.2 Notes

Runs as a system user.

#### 2.1.1.12.0.0 Reporting Engine

##### 2.1.1.12.1.0 Id

reporting-engine-001

##### 2.1.1.12.2.0 Name

Reporting Engine

##### 2.1.1.12.3.0 Description

A service responsible for generating a suite of standard operational and financial reports. It handles data aggregation and provides functionality to export the generated reports to PDF and Excel formats. REQ-1-600.

##### 2.1.1.12.4.0 Type

🔹 Service

##### 2.1.1.12.5.0 Dependencies

- trip-management-service-001
- financial-service-001

##### 2.1.1.12.6.0 Properties

*No data available*

##### 2.1.1.12.7.0 Interfaces

*No items available*

##### 2.1.1.12.8.0 Technology

Odoo Reporting Framework, wkhtmltopdf

##### 2.1.1.12.9.0 Resources

*No data available*

##### 2.1.1.12.10.0 Configuration

*No data available*

##### 2.1.1.12.11.0 Health Check

*Not specified*

##### 2.1.1.12.12.0 Responsible Features

- Standard Report Generation
- PDF/Excel Export

##### 2.1.1.12.13.0 Security

###### 2.1.1.12.13.1 Requires Authentication

✅ Yes

###### 2.1.1.12.13.2 Requires Authorization

✅ Yes

###### 2.1.1.12.13.3 Allowed Roles

- Admin
- Dispatch Manager
- Finance Officer

#### 2.1.1.13.0.0 Dashboard Service

##### 2.1.1.13.1.0 Id

dashboard-service-001

##### 2.1.1.13.2.0 Name

Dashboard Service

##### 2.1.1.13.3.0 Description

Provides aggregated data and Key Performance Indicators (KPIs) for display in real-time on the main dashboards for Admin and Manager roles. REQ-1-601.

##### 2.1.1.13.4.0 Type

🔹 Service

##### 2.1.1.13.5.0 Dependencies

- trip-management-service-001
- financial-service-001

##### 2.1.1.13.6.0 Properties

*No data available*

##### 2.1.1.13.7.0 Interfaces

*No items available*

##### 2.1.1.13.8.0 Technology

Odoo 18 ORM (read_group)

##### 2.1.1.13.9.0 Resources

*No data available*

##### 2.1.1.13.10.0 Configuration

*No data available*

##### 2.1.1.13.11.0 Health Check

*Not specified*

##### 2.1.1.13.12.0 Responsible Features

- Dashboard KPI Calculation

##### 2.1.1.13.13.0 Security

###### 2.1.1.13.13.1 Requires Authentication

✅ Yes

###### 2.1.1.13.13.2 Requires Authorization

✅ Yes

###### 2.1.1.13.13.3 Allowed Roles

- Admin
- Dispatch Manager

#### 2.1.1.14.0.0 Audit Trail Service

##### 2.1.1.14.1.0 Id

audit-trail-service-001

##### 2.1.1.14.2.0 Name

Audit Trail Service

##### 2.1.1.14.3.0 Description

Implements an immutable audit trail for critical models (Trip, Invoice, Payment) by inheriting and enabling Odoo's built-in `mail.thread` (chatter) functionality, which automatically logs field changes. REQ-1-207.

##### 2.1.1.14.4.0 Type

🔹 Utility

##### 2.1.1.14.5.0 Dependencies

*No items available*

##### 2.1.1.14.6.0 Properties

*No data available*

##### 2.1.1.14.7.0 Interfaces

*No items available*

##### 2.1.1.14.8.0 Technology

Odoo Framework (`mail.thread` mixin)

##### 2.1.1.14.9.0 Resources

*No data available*

##### 2.1.1.14.10.0 Configuration

*No data available*

##### 2.1.1.14.11.0 Health Check

*Not specified*

##### 2.1.1.14.12.0 Responsible Features

- Audit Logging for Trips, Invoices, Payments

##### 2.1.1.14.13.0 Security

###### 2.1.1.14.13.1 Requires Authentication

✅ Yes

###### 2.1.1.14.13.2 Requires Authorization

✅ Yes

###### 2.1.1.14.13.3 Allowed Roles

- Admin

#### 2.1.1.15.0.0 GPS Ingestion Microservice

##### 2.1.1.15.1.0 Id

gps-ingestion-service-001

##### 2.1.1.15.2.0 Name

GPS Ingestion Microservice

##### 2.1.1.15.3.0 Description

A standalone, containerized microservice that polls a third-party GPS provider's API, validates the incoming location data against a strict contract, and publishes it to a RabbitMQ message queue for asynchronous consumption by the Odoo application. REQ-1-013, REQ-1-301.

##### 2.1.1.15.4.0 Type

🔹 Microservice

##### 2.1.1.15.5.0 Dependencies

- RabbitMQ Message Broker
- Third-Party GPS API

##### 2.1.1.15.6.0 Properties

| Property | Value |
|----------|-------|
| Resilience | Exponential backoff, Dead-Letter Queue |

##### 2.1.1.15.7.0 Interfaces

- Exposes a health check endpoint via AWS API Gateway

##### 2.1.1.15.8.0 Technology

Python 3.11, FastAPI, Docker

##### 2.1.1.15.9.0 Resources

| Property | Value |
|----------|-------|
| Cpu | 0.5 vCPU |
| Memory | 512MB |
| Storage | 1GB |

##### 2.1.1.15.10.0 Configuration

###### 2.1.1.15.10.1 Gps Api Token

Stored in AWS Secrets Manager

###### 2.1.1.15.10.2 Rabbitmq Url

Stored in AWS Secrets Manager

##### 2.1.1.15.11.0 Health Check

| Property | Value |
|----------|-------|
| Path | /health |
| Interval | 30 |
| Timeout | 5 |

##### 2.1.1.15.12.0 Responsible Features

- GPS Data Ingestion
- Real-time Vehicle Tracking (Polling)

##### 2.1.1.15.13.0 Security

###### 2.1.1.15.13.1 Requires Authentication

❌ No

###### 2.1.1.15.13.2 Notes

Network access controlled by AWS Security Groups. Authenticates to external services via injected secrets.

### 2.1.2.0.0.0 Configuration

| Property | Value |
|----------|-------|
| Environment | production |
| Logging Level | INFO |
| Database Url | Amazon RDS for PostgreSQL 16 |
| Secrets Manager | AWS Secrets Manager |
| Message Broker | Amazon MQ for RabbitMQ |

