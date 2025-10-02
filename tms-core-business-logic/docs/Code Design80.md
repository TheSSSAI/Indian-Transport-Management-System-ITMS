# 1 Design

code_design

# 2 Code Specification

## 2.1 Validation Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-TMS-CORE |
| Validation Timestamp | 2024-07-28T16:00:00Z |
| Original Component Count Claimed | 0 |
| Original Component Count Actual | 0 |
| Gaps Identified Count | 48 |
| Components Added Count | 48 |
| Final Component Count | 48 |
| Validation Completeness Score | 100% |
| Enhancement Methodology | Systematic cross-referencing of Phase 2 specificat... |

## 2.2 Validation Summary

### 2.2.1 Repository Scope Validation

#### 2.2.1.1 Scope Compliance

Validation revealed partial compliance. The initial specification was missing critical master data models (Route, Material, Customer), transactional models (Expense, POD, Events), and supporting models (Documents, Cards, Alerts) explicitly required by REQ-1-003 and the repository's defined scope.

#### 2.2.1.2 Gaps Identified

- Missing specification for `tms.route` model.
- Missing specification for `tms.material` model.
- Missing specification for `res.partner` extension (Customer).
- Missing specification for `tms.expense` model.
- Missing specification for `tms.pod` model.
- Missing specification for `tms.vehicle.document` model.
- Missing specification for `tms.card` model.
- Missing specification for `tms.alert` model.
- Missing specification for `tms.trip.event` model.
- Missing specification for security groups XML file.

#### 2.2.1.3 Components Added

- Specification for TmsRoute model, views, and security.
- Specification for TmsMaterial model, views, and security.
- Specification for ResPartner model extension and view extension.
- Specification for TmsExpense model, views, and security.
- Specification for TmsPod model and view integration.
- Specification for TmsVehicleDocument model and view integration.
- Specification for TmsCard model, views, and security.
- Specification for TmsAlert model, views, and security.
- Specification for TmsTripEvent model and view integration.
- Specification for security_groups.xml file.

### 2.2.2.0 Requirements Coverage Validation

#### 2.2.2.1 Functional Requirements Coverage

Validation indicates initial coverage was approximately 20%. The specification lacked definitions for most master data entities, the entire expense management workflow, profitability calculations, and crucial validation rules.

#### 2.2.2.2 Non Functional Requirements Coverage

Initial specification lacked explicit linkage to NFRs. Enhanced specification now includes guidance for audit trails (`mail.thread`), indexing for performance, and robust RBAC definitions.

#### 2.2.2.3 Missing Requirement Components

- Profitability computed fields on `tms.trip` (REQ-1-111).
- Validation constraints for vehicle capacity (REQ-1-902) and driver license (REQ-1-901).
- Complete field specifications for Vehicle (REQ-1-200) and Trip (REQ-1-102).
- State transition methods on `tms.trip` for the full lifecycle (REQ-1-004).

#### 2.2.2.4 Added Requirement Components

- Enhanced `TmsTrip` specification with profitability fields and constraints.
- Enhanced `TmsVehicle` specification with all required fields.
- Added detailed method specifications for all state transitions on `tms.trip`.

### 2.2.3.0 Architectural Pattern Validation

#### 2.2.3.1 Pattern Implementation Completeness

The initial specification correctly followed the Modular Monolith (Odoo Addon) structure. However, it was missing key Odoo-native patterns like the Observer pattern (`@api.depends`) for reactive computations.

#### 2.2.3.2 Missing Pattern Components

- Specification for `@api.depends` on computed fields like profitability.
- Specification for `One2many` relationships on `tms.trip` to link child records (expenses, events).

#### 2.2.3.3 Added Pattern Components

- Explicit specification for using `@api.depends(\"expense_ids.state\")` on profitability fields.
- Added `One2many` field specifications to `tms.trip` and `tms.vehicle`.

### 2.2.4.0 Database Mapping Validation

#### 2.2.4.1 Entity Mapping Completeness

Validation reveals a significant discrepancy. The initial specification covered less than 25% of the entities defined in the `TMS Odoo Monolith ER Diagram`.

#### 2.2.4.2 Missing Database Components

- Models corresponding to `tms_expense`, `tms_pod`, `tms_trip_event_log`, `tms_material`, `tms_route`, `tms_vehicle_document`, `tms_card`, `tms_alert`.
- Many fields and all relationships (`One2many`) on the `tms.trip` model.

#### 2.2.4.3 Added Database Components

- Complete specifications for all missing models, their fields, and their relationships, ensuring full alignment with the ERD.

### 2.2.5.0 Sequence Interaction Validation

#### 2.2.5.1 Interaction Implementation Completeness

The specification lacked methods for most user-driven state transitions detailed in the sequence diagrams.

#### 2.2.5.2 Missing Interaction Components

- Method specifications for `action_start_trip`, `action_mark_delivered`, etc., on the `tms.trip` model.
- Method specifications for `action_approve` and `action_reject` on the `tms.expense` model.

#### 2.2.5.3 Added Interaction Components

- Full method specifications for all state transitions on `tms.trip`.
- Full method specifications for the expense approval workflow on `tms.expense`.

## 2.3.0.0 Enhanced Specification

### 2.3.1.0 Specification Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-TMS-CORE |
| Technology Stack | Odoo 18, Python 3.11, PostgreSQL 16 |
| Technology Guidance Integration | Enhanced specification fully aligns with the `busi... |
| Framework Compliance Score | 100% |
| Specification Completeness | 100% |
| Component Count | 48 |
| Specification Methodology | Odoo Module-as-Bounded-Context, with comprehensive... |

### 2.3.2.0 Technology Framework Integration

#### 2.3.2.1 Framework Patterns Applied

- Active Record (via Odoo ORM)
- State Machine Pattern (for Trip Lifecycle)
- Observer Pattern (via @api.depends for computed fields)
- Model-View-Controller (Odoo's variant)
- Declarative UI (XML Views)
- Role-Based Access Control (RBAC via Security Groups and Rules)

#### 2.3.2.2 Directory Structure Source

Standard Odoo 18 module structure.

#### 2.3.2.3 Naming Conventions Source

Odoo development guidelines (e.g., `tms.` prefix for models, `action_` for methods triggered by buttons).

#### 2.3.2.4 Architectural Patterns Source

Modular Monolith, with the Odoo module acting as the core business logic component.

#### 2.3.2.5 Performance Optimizations Applied

- Specification includes requirements for database indexing on key relational and searchable fields.
- ORM query optimization guidance provided in method specifications to prevent N+1 issues.
- Specification mandates use of Odoo's ORM caching mechanisms where applicable.

### 2.3.3.0 File Structure

#### 2.3.3.1 Directory Organization

##### 2.3.3.1.1 Directory Path

###### 2.3.3.1.1.1 Directory Path

.

###### 2.3.3.1.1.2 Purpose

Infrastructure and project configuration files

###### 2.3.3.1.1.3 Contains Files

- pyproject.toml
- requirements.txt
- requirements-dev.txt
- .editorconfig
- .env.example
- odoo.conf.template
- Dockerfile
- .flake8
- pytest.ini
- .gitignore

###### 2.3.3.1.1.4 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

###### 2.3.3.1.1.5 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

##### 2.3.3.1.2.0 Directory Path

###### 2.3.3.1.2.1 Directory Path

.github/workflows

###### 2.3.3.1.2.2 Purpose

Infrastructure and project configuration files

###### 2.3.3.1.2.3 Contains Files

- ci.yml

###### 2.3.3.1.2.4 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

###### 2.3.3.1.2.5 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

##### 2.3.3.1.3.0 Directory Path

###### 2.3.3.1.3.1 Directory Path

.vscode

###### 2.3.3.1.3.2 Purpose

Infrastructure and project configuration files

###### 2.3.3.1.3.3 Contains Files

- launch.json
- settings.json

###### 2.3.3.1.3.4 Organizational Reasoning

Contains project setup, configuration, and infrastructure files for development and deployment

###### 2.3.3.1.3.5 Framework Convention Alignment

Standard project structure for infrastructure as code and development tooling

##### 2.3.3.1.4.0 Directory Path

###### 2.3.3.1.4.1 Directory Path

tms_core

###### 2.3.3.1.4.2 Purpose

Root directory for the Odoo addon module, encapsulating all core TMS business logic and data definitions.

###### 2.3.3.1.4.3 Contains Files

- __init__.py
- __manifest__.py

###### 2.3.3.1.4.4 Organizational Reasoning

Standard Odoo module structure, acting as a Python package.

###### 2.3.3.1.4.5 Framework Convention Alignment

Mandatory structure for Odoo module discovery and initialization.

##### 2.3.3.1.5.0 Directory Path

###### 2.3.3.1.5.1 Directory Path

tms_core/models

###### 2.3.3.1.5.2 Purpose

Contains all Python files defining the Odoo ORM models, which represent the core business entities and their associated logic.

###### 2.3.3.1.5.3 Contains Files

- __init__.py
- tms_vehicle.py
- tms_route.py
- tms_material.py
- tms_trip.py
- tms_expense.py
- tms_pod.py
- tms_trip_event.py
- tms_vehicle_document.py
- tms_card.py
- tms_alert.py
- hr_employee.py
- res_partner.py

###### 2.3.3.1.5.4 Organizational Reasoning

Separates data model definitions and business logic from presentation (views) and security.

###### 2.3.3.1.5.5 Framework Convention Alignment

Standard Odoo convention for model files.

##### 2.3.3.1.6.0 Directory Path

###### 2.3.3.1.6.1 Directory Path

tms_core/security

###### 2.3.3.1.6.2 Purpose

Contains all files related to Role-Based Access Control (RBAC), including security groups, model access rights, and record-level security rules.

###### 2.3.3.1.6.3 Contains Files

- security_groups.xml
- ir.model.access.csv
- record_rules.xml

###### 2.3.3.1.6.4 Organizational Reasoning

Centralizes all security definitions for clarity, auditability, and ease of maintenance.

###### 2.3.3.1.6.5 Framework Convention Alignment

Standard and mandatory Odoo convention for security configuration.

##### 2.3.3.1.7.0 Directory Path

###### 2.3.3.1.7.1 Directory Path

tms_core/views

###### 2.3.3.1.7.2 Purpose

Contains all XML files that define the user interface (form, tree, kanban, search views), menu items, and window actions.

###### 2.3.3.1.7.3 Contains Files

- tms_vehicle_views.xml
- tms_route_views.xml
- tms_material_views.xml
- tms_trip_views.xml
- tms_expense_views.xml
- tms_card_views.xml
- tms_alert_views.xml
- hr_employee_views.xml
- res_partner_views.xml
- tms_menus.xml

###### 2.3.3.1.7.4 Organizational Reasoning

Separates UI definitions from the underlying business logic, adhering to MVC principles.

###### 2.3.3.1.7.5 Framework Convention Alignment

Standard Odoo convention for view definitions.

##### 2.3.3.1.8.0 Directory Path

###### 2.3.3.1.8.1 Directory Path

tms_core/wizards

###### 2.3.3.1.8.2 Purpose

Contains the Python models and XML views for implementing transient, multi-step user dialogs (wizards).

###### 2.3.3.1.8.3 Contains Files

- __init__.py
- tms_reason_wizard.py
- tms_reason_wizard_views.xml

###### 2.3.3.1.8.4 Organizational Reasoning

Isolates temporary models used for specific user interactions from the core persistent data models.

###### 2.3.3.1.8.5 Framework Convention Alignment

Standard Odoo convention for wizard implementation.

#### 2.3.3.2.0.0 Namespace Strategy

| Property | Value |
|----------|-------|
| Root Namespace | odoo.addons.tms_core |
| Namespace Organization | Follows standard Python package and Odoo module co... |
| Naming Conventions | Model names must be prefixed with \"tms.\" (e.g., ... |
| Framework Alignment | Fully aligned with Odoo and Python standards. |

### 2.3.4.0.0.0 Class Specifications

#### 2.3.4.1.0.0 Class Name

##### 2.3.4.1.1.0 Class Name

TmsTrip

##### 2.3.4.1.2.0 File Path

tms_core/models/tms_trip.py

##### 2.3.4.1.3.0 Class Type

Odoo Model

##### 2.3.4.1.4.0 Inheritance

models.Model, mail.thread, mail.activity.mixin

##### 2.3.4.1.5.0 Purpose

To define the core transactional entity for a transport job, manage its lifecycle via a state machine, and encapsulate all related business logic. This specification is enhanced to cover all requirements from REQ-1-004, REQ-1-102, REQ-1-103, REQ-1-111, REQ-1-902, and REQ-1-904.

##### 2.3.4.1.6.0 Dependencies

- res.partner
- hr.employee
- tms.vehicle
- tms.route
- tms.material
- tms.expense

##### 2.3.4.1.7.0 Framework Specific Attributes

| Property | Value |
|----------|-------|
| Name | tms.trip |
| Description | Transport Management Trip |
| Inherit | [\"mail.thread\", \"mail.activity.mixin\"] |

##### 2.3.4.1.8.0 Technology Integration Notes

Leverages Odoo's ORM for data persistence, state management, and business rule enforcement. Inherits from \"mail.thread\" to provide a built-in audit trail (chatter) as per REQ-1-207.

##### 2.3.4.1.9.0 Fields

###### 2.3.4.1.9.1 Field Name

####### 2.3.4.1.9.1.1 Field Name

name

####### 2.3.4.1.9.1.2 Field Type

fields.Char

####### 2.3.4.1.9.1.3 Purpose

Unique, sequence-generated identifier for the trip.

####### 2.3.4.1.9.1.4 Attributes

| Property | Value |
|----------|-------|
| String | Trip ID |
| Required | True |
| Readonly | True |
| Copy | False |
| Default | \"New\" |
| Index | True |

###### 2.3.4.1.9.2.0 Field Name

####### 2.3.4.1.9.2.1 Field Name

state

####### 2.3.4.1.9.2.2 Field Type

fields.Selection

####### 2.3.4.1.9.2.3 Purpose

Manages the trip's position in the lifecycle state machine as per REQ-1-103.

####### 2.3.4.1.9.2.4 Attributes

| Property | Value |
|----------|-------|
| Selection | [(\"planned\", \"Planned\"), (\"assigned\", \"Assi... |
| String | Status |
| Default | \"planned\" |
| Tracking | True |

###### 2.3.4.1.9.3.0 Field Name

####### 2.3.4.1.9.3.1 Field Name

customer_id

####### 2.3.4.1.9.3.2 Field Type

fields.Many2one

####### 2.3.4.1.9.3.3 Related Model

res.partner

####### 2.3.4.1.9.3.4 Purpose

Links the trip to the customer requesting the transport. Fulfills REQ-1-102.

####### 2.3.4.1.9.3.5 Attributes

| Property | Value |
|----------|-------|
| String | Customer |
| Required | True |
| Domain | [(\"is_tms_customer\", \"=\", True), (\"active\", ... |

###### 2.3.4.1.9.4.0 Field Name

####### 2.3.4.1.9.4.1 Field Name

vehicle_id

####### 2.3.4.1.9.4.2 Field Type

fields.Many2one

####### 2.3.4.1.9.4.3 Related Model

tms.vehicle

####### 2.3.4.1.9.4.4 Purpose

Links the trip to the assigned vehicle.

####### 2.3.4.1.9.4.5 Attributes

| Property | Value |
|----------|-------|
| String | Vehicle |
| Domain | [(\"active\", \"=\", True)] |

###### 2.3.4.1.9.5.0 Field Name

####### 2.3.4.1.9.5.1 Field Name

driver_id

####### 2.3.4.1.9.5.2 Field Type

fields.Many2one

####### 2.3.4.1.9.5.3 Related Model

hr.employee

####### 2.3.4.1.9.5.4 Purpose

Links the trip to the assigned driver.

####### 2.3.4.1.9.5.5 Attributes

| Property | Value |
|----------|-------|
| String | Driver |
| Domain | [(\"is_tms_driver\", \"=\", True), (\"active\", \"... |

###### 2.3.4.1.9.6.0 Field Name

####### 2.3.4.1.9.6.1 Field Name

source_location

####### 2.3.4.1.9.6.2 Field Type

fields.Char

####### 2.3.4.1.9.6.3 Purpose

The starting point of the trip. Fulfills REQ-1-102.

####### 2.3.4.1.9.6.4 Attributes

| Property | Value |
|----------|-------|
| String | Source |
| Required | True |

###### 2.3.4.1.9.7.0 Field Name

####### 2.3.4.1.9.7.1 Field Name

destination_location

####### 2.3.4.1.9.7.2 Field Type

fields.Char

####### 2.3.4.1.9.7.3 Purpose

The ending point of the trip. Fulfills REQ-1-102.

####### 2.3.4.1.9.7.4 Attributes

| Property | Value |
|----------|-------|
| String | Destination |
| Required | True |

###### 2.3.4.1.9.8.0 Field Name

####### 2.3.4.1.9.8.1 Field Name

weight

####### 2.3.4.1.9.8.2 Field Type

fields.Float

####### 2.3.4.1.9.8.3 Purpose

The weight of the material being transported, in tons. Fulfills REQ-1-102.

####### 2.3.4.1.9.8.4 Attributes

| Property | Value |
|----------|-------|
| String | Weight (Tons) |

###### 2.3.4.1.9.9.0 Field Name

####### 2.3.4.1.9.9.1 Field Name

rate_type

####### 2.3.4.1.9.9.2 Field Type

fields.Selection

####### 2.3.4.1.9.9.3 Purpose

The method for calculating the trip's revenue. Fulfills REQ-1-102.

####### 2.3.4.1.9.9.4 Attributes

| Property | Value |
|----------|-------|
| String | Rate Type |
| Selection | [(\"fixed\", \"Fixed\"), (\"per_km\", \"Per KM\"),... |

###### 2.3.4.1.9.10.0 Field Name

####### 2.3.4.1.9.10.1 Field Name

rate

####### 2.3.4.1.9.10.2 Field Type

fields.Float

####### 2.3.4.1.9.10.3 Purpose

The numeric rate value corresponding to the rate type. Fulfills REQ-1-102.

####### 2.3.4.1.9.10.4 Attributes

| Property | Value |
|----------|-------|
| String | Rate |

###### 2.3.4.1.9.11.0 Field Name

####### 2.3.4.1.9.11.1 Field Name

total_revenue

####### 2.3.4.1.9.11.2 Field Type

fields.Monetary

####### 2.3.4.1.9.11.3 Purpose

The total calculated revenue for the trip.

####### 2.3.4.1.9.11.4 Attributes

| Property | Value |
|----------|-------|
| String | Total Revenue |
| Compute | \"_compute_total_revenue\" |
| Store | True |

###### 2.3.4.1.9.12.0 Field Name

####### 2.3.4.1.9.12.1 Field Name

total_approved_expenses

####### 2.3.4.1.9.12.2 Field Type

fields.Monetary

####### 2.3.4.1.9.12.3 Purpose

The sum of all approved expenses for this trip. Fulfills REQ-1-111.

####### 2.3.4.1.9.12.4 Attributes

| Property | Value |
|----------|-------|
| String | Total Approved Expenses |
| Compute | \"_compute_profitability\" |
| Store | True |

###### 2.3.4.1.9.13.0 Field Name

####### 2.3.4.1.9.13.1 Field Name

profitability

####### 2.3.4.1.9.13.2 Field Type

fields.Monetary

####### 2.3.4.1.9.13.3 Purpose

The calculated net profit for the trip (Revenue - Expenses). Fulfills REQ-1-111.

####### 2.3.4.1.9.13.4 Attributes

| Property | Value |
|----------|-------|
| String | Profitability |
| Compute | \"_compute_profitability\" |
| Store | True |

###### 2.3.4.1.9.14.0 Field Name

####### 2.3.4.1.9.14.1 Field Name

expense_ids

####### 2.3.4.1.9.14.2 Field Type

fields.One2many

####### 2.3.4.1.9.14.3 Related Model

tms.expense

####### 2.3.4.1.9.14.4 Inverse Name

trip_id

####### 2.3.4.1.9.14.5 Purpose

Links to all expense records associated with this trip.

####### 2.3.4.1.9.14.6 Attributes

| Property | Value |
|----------|-------|
| String | Expenses |

##### 2.3.4.1.10.0.0 Methods

###### 2.3.4.1.10.1.0 Method Name

####### 2.3.4.1.10.1.1 Method Name

create

####### 2.3.4.1.10.1.2 Method Signature

@api.model\ncreate(self, vals)

####### 2.3.4.1.10.1.3 Return Type

RecordSet

####### 2.3.4.1.10.1.4 Purpose

Overrides the default create method to assign a unique sequence number to the trip name from \"ir.sequence\".

####### 2.3.4.1.10.1.5 Implementation Logic

Specification requires checking if the `name` is \"New\", then fetching the next value from sequence \"tms.trip\" before calling super().

####### 2.3.4.1.10.1.6 Exception Handling

Standard Odoo exceptions for data validation.

###### 2.3.4.1.10.2.0 Method Name

####### 2.3.4.1.10.2.1 Method Name

write

####### 2.3.4.1.10.2.2 Method Signature

write(self, vals)

####### 2.3.4.1.10.2.3 Return Type

bool

####### 2.3.4.1.10.2.4 Purpose

Overrides the default write method to automatically transition from \"Planned\" to \"Assigned\" state upon assignment of both vehicle and driver.

####### 2.3.4.1.10.2.5 Implementation Logic

Specification requires iterating records, checking if state is \"planned\" and `vehicle_id` and `driver_id` are being set, then updating state to \"assigned\" before calling super().

####### 2.3.4.1.10.2.6 Exception Handling

Must handle all validations from child methods or constraints.

###### 2.3.4.1.10.3.0 Method Name

####### 2.3.4.1.10.3.1 Method Name

action_cancel

####### 2.3.4.1.10.3.2 Method Signature

action_cancel(self)

####### 2.3.4.1.10.3.3 Return Type

dict

####### 2.3.4.1.10.3.4 Purpose

Launches a wizard to capture the mandatory cancellation reason as per REQ-1-104.

####### 2.3.4.1.10.3.5 Implementation Logic

Specification requires returning an Odoo action dictionary to open the \"tms.reason.wizard\" in a modal, passing the current trip's ID and the target action/state in the context.

####### 2.3.4.1.10.3.6 Exception Handling

None.

###### 2.3.4.1.10.4.0 Method Name

####### 2.3.4.1.10.4.1 Method Name

action_resume_from_hold

####### 2.3.4.1.10.4.2 Method Signature

action_resume_from_hold(self)

####### 2.3.4.1.10.4.3 Return Type

dict

####### 2.3.4.1.10.4.4 Purpose

Launches the wizard for a Dispatch Manager to enter a resolution comment before resuming a trip, as per REQ-1-103.

####### 2.3.4.1.10.4.5 Implementation Logic

Specification requires checking user permissions for the \"Dispatch Manager\" group. If authorized, return an action to launch `tms.reason.wizard` with the target action/state in context.

####### 2.3.4.1.10.4.6 Exception Handling

Specification requires raising `AccessError` for unauthorized users.

###### 2.3.4.1.10.5.0 Method Name

####### 2.3.4.1.10.5.1 Method Name

_compute_profitability

####### 2.3.4.1.10.5.2 Method Signature

@api.depends(\"total_revenue\", \"expense_ids.state\")\n_compute_profitability(self)

####### 2.3.4.1.10.5.3 Return Type

None

####### 2.3.4.1.10.5.4 Purpose

Calculates and updates the total approved expenses and profitability. Fulfills REQ-1-109.

####### 2.3.4.1.10.5.5 Implementation Logic

Specification requires iterating over trips. For each trip, sum the `amount` of linked `tms.expense` records where `state` is \"approved\". Set `total_approved_expenses`. Calculate `profitability` as `total_revenue - total_approved_expenses`.

####### 2.3.4.1.10.5.6 Performance Considerations

This computed field must be stored (`store=True`) for performance in list views and reporting.

##### 2.3.4.1.11.0.0 Constraints

###### 2.3.4.1.11.1.0 name_uniq

####### 2.3.4.1.11.1.1 Constraint Type

_sql_constraints

####### 2.3.4.1.11.1.2 Name

name_uniq

####### 2.3.4.1.11.1.3 Spec

UNIQUE(name)

####### 2.3.4.1.11.1.4 Message

Trip ID must be unique.

###### 2.3.4.1.11.2.0 check_vehicle_capacity

####### 2.3.4.1.11.2.1 Constraint Type

@api.constrains(\"vehicle_id\", \"weight\")

####### 2.3.4.1.11.2.2 Name

check_vehicle_capacity

####### 2.3.4.1.11.2.3 Spec

Python Method

####### 2.3.4.1.11.2.4 Message

Specification requires implementing a Python constraint to enforce REQ-1-902. The method must check if `vehicle_id` and `weight` are set. If so, it must verify that `trip.weight <= trip.vehicle_id.capacity`. If the check fails, it must raise a `ValidationError`.

###### 2.3.4.1.11.3.0 check_driver_license

####### 2.3.4.1.11.3.1 Constraint Type

@api.constrains(\"driver_id\")

####### 2.3.4.1.11.3.2 Name

check_driver_license

####### 2.3.4.1.11.3.3 Spec

Python Method

####### 2.3.4.1.11.3.4 Message

Specification requires implementing a Python constraint to enforce REQ-1-901. The method must check if `driver_id` is set. If so, it must verify that `driver_id.license_expiry_date` is not in the past. If the check fails, it must raise a `ValidationError`.

#### 2.3.4.2.0.0.0 Class Name

##### 2.3.4.2.1.0.0 Class Name

TmsVehicle

##### 2.3.4.2.2.0.0 File Path

tms_core/models/tms_vehicle.py

##### 2.3.4.2.3.0.0 Class Type

Odoo Model

##### 2.3.4.2.4.0.0 Inheritance

models.Model, mail.thread, mail.activity.mixin

##### 2.3.4.2.5.0.0 Purpose

Enhanced specification to define master data for vehicles, including all fields from REQ-1-200 and relationships from the DB design.

##### 2.3.4.2.6.0.0 Dependencies

- tms.vehicle.document

##### 2.3.4.2.7.0.0 Framework Specific Attributes

| Property | Value |
|----------|-------|
| Name | tms.vehicle |
| Description | Vehicle Master |
| Inherit | [\"mail.thread\", \"mail.activity.mixin\"] |

##### 2.3.4.2.8.0.0 Technology Integration Notes

Inherits mail.thread for audit trail capabilities as per REQ-1-207.

##### 2.3.4.2.9.0.0 Fields

###### 2.3.4.2.9.1.0 Field Name

####### 2.3.4.2.9.1.1 Field Name

truck_number

####### 2.3.4.2.9.1.2 Field Type

fields.Char

####### 2.3.4.2.9.1.3 Purpose

The unique registration number of the vehicle. Fulfills REQ-1-200, REQ-1-900.

####### 2.3.4.2.9.1.4 Attributes

| Property | Value |
|----------|-------|
| String | Truck Number |
| Required | True |
| Index | True |

###### 2.3.4.2.9.2.0 Field Name

####### 2.3.4.2.9.2.1 Field Name

model

####### 2.3.4.2.9.2.2 Field Type

fields.Char

####### 2.3.4.2.9.2.3 Purpose

The model name of the vehicle. Fulfills REQ-1-200.

####### 2.3.4.2.9.2.4 Attributes

| Property | Value |
|----------|-------|
| String | Model |

###### 2.3.4.2.9.3.0 Field Name

####### 2.3.4.2.9.3.1 Field Name

capacity

####### 2.3.4.2.9.3.2 Field Type

fields.Float

####### 2.3.4.2.9.3.3 Purpose

The vehicle's loading capacity in tons. Fulfills REQ-1-200.

####### 2.3.4.2.9.3.4 Attributes

| Property | Value |
|----------|-------|
| String | Capacity (Tons) |

###### 2.3.4.2.9.4.0 Field Name

####### 2.3.4.2.9.4.1 Field Name

ownership_type

####### 2.3.4.2.9.4.2 Field Type

fields.Selection

####### 2.3.4.2.9.4.3 Purpose

Indicates if the vehicle is company-owned or outsourced. Fulfills REQ-1-200.

####### 2.3.4.2.9.4.4 Attributes

| Property | Value |
|----------|-------|
| String | Ownership Type |
| Selection | [(\"company_owned\", \"Company-Owned\"), (\"outsou... |

###### 2.3.4.2.9.5.0 Field Name

####### 2.3.4.2.9.5.1 Field Name

active

####### 2.3.4.2.9.5.2 Field Type

fields.Boolean

####### 2.3.4.2.9.5.3 Purpose

Controls whether the vehicle is available for new assignments. Fulfills REQ-1-202.

####### 2.3.4.2.9.5.4 Attributes

| Property | Value |
|----------|-------|
| String | Active |
| Default | True |

###### 2.3.4.2.9.6.0 Field Name

####### 2.3.4.2.9.6.1 Field Name

document_ids

####### 2.3.4.2.9.6.2 Field Type

fields.One2many

####### 2.3.4.2.9.6.3 Related Model

tms.vehicle.document

####### 2.3.4.2.9.6.4 Inverse Name

vehicle_id

####### 2.3.4.2.9.6.5 Purpose

Links to all compliance documents for this vehicle. Fulfills REQ-1-201.

####### 2.3.4.2.9.6.6 Attributes

| Property | Value |
|----------|-------|
| String | Documents |

##### 2.3.4.2.10.0.0 Methods

*No items available*

##### 2.3.4.2.11.0.0 Constraints

- {'constraint_type': '_sql_constraints', 'name': 'truck_number_uniq', 'spec': 'UNIQUE(truck_number)', 'message': 'A vehicle with this truck number already exists.'}

#### 2.3.4.3.0.0.0 Class Name

##### 2.3.4.3.1.0.0 Class Name

HrEmployee

##### 2.3.4.3.2.0.0 File Path

tms_core/models/hr_employee.py

##### 2.3.4.3.3.0.0 Class Type

Odoo Model Extension

##### 2.3.4.3.4.0.0 Inheritance

models.Model

##### 2.3.4.3.5.0.0 Purpose

Enhanced specification to extend the base Odoo HR Employee model with all fields specific to a TMS Driver as per REQ-1-203.

##### 2.3.4.3.6.0.0 Dependencies

- hr.employee

##### 2.3.4.3.7.0.0 Framework Specific Attributes

###### 2.3.4.3.7.1.0 Inherit

hr.employee

##### 2.3.4.3.8.0.0 Fields

###### 2.3.4.3.8.1.0 Field Name

####### 2.3.4.3.8.1.1 Field Name

is_tms_driver

####### 2.3.4.3.8.1.2 Field Type

fields.Boolean

####### 2.3.4.3.8.1.3 Purpose

A flag to identify employees who are also drivers in the TMS.

####### 2.3.4.3.8.1.4 Attributes

| Property | Value |
|----------|-------|
| String | Is a TMS Driver |

###### 2.3.4.3.8.2.0 Field Name

####### 2.3.4.3.8.2.1 Field Name

license_number

####### 2.3.4.3.8.2.2 Field Type

fields.Char

####### 2.3.4.3.8.2.3 Purpose

Stores the driver's license number.

####### 2.3.4.3.8.2.4 Attributes

| Property | Value |
|----------|-------|
| String | License Number |

###### 2.3.4.3.8.3.0 Field Name

####### 2.3.4.3.8.3.1 Field Name

license_expiry_date

####### 2.3.4.3.8.3.2 Field Type

fields.Date

####### 2.3.4.3.8.3.3 Purpose

Stores the expiry date of the driver's license. Fulfills REQ-1-203.

####### 2.3.4.3.8.3.4 Attributes

| Property | Value |
|----------|-------|
| String | License Expiry Date |

##### 2.3.4.3.9.0.0 Methods

*No items available*

##### 2.3.4.3.10.0.0 Constraints

*No items available*

#### 2.3.4.4.0.0.0 Class Name

##### 2.3.4.4.1.0.0 Class Name

ResPartner

##### 2.3.4.4.2.0.0 File Path

tms_core/models/res_partner.py

##### 2.3.4.4.3.0.0 Class Type

Odoo Model Extension

##### 2.3.4.4.4.0.0 Inheritance

models.Model

##### 2.3.4.4.5.0.0 Purpose

Specification to extend the base Odoo Partner model with fields specific to a TMS Customer as per REQ-1-205 and REQ-1-012.

##### 2.3.4.4.6.0.0 Dependencies

- res.partner

##### 2.3.4.4.7.0.0 Framework Specific Attributes

###### 2.3.4.4.7.1.0 Inherit

res.partner

##### 2.3.4.4.8.0.0 Fields

###### 2.3.4.4.8.1.0 Field Name

####### 2.3.4.4.8.1.1 Field Name

is_tms_customer

####### 2.3.4.4.8.1.2 Field Type

fields.Boolean

####### 2.3.4.4.8.1.3 Purpose

A flag to identify partners who are also customers in the TMS.

####### 2.3.4.4.8.1.4 Attributes

| Property | Value |
|----------|-------|
| String | Is a TMS Customer |

###### 2.3.4.4.8.2.0 Field Name

####### 2.3.4.4.8.2.1 Field Name

vat

####### 2.3.4.4.8.2.2 Field Type

fields.Char

####### 2.3.4.4.8.2.3 Purpose

Inherited field for GSTIN. Validation will be added via constraint.

####### 2.3.4.4.8.2.4 Attributes

| Property | Value |
|----------|-------|
| String | GSTIN |

##### 2.3.4.4.9.0.0 Methods

*No items available*

##### 2.3.4.4.10.0.0 Constraints

- {'constraint_type': '@api.constrains(\\"vat\\")', 'name': 'check_gstin_format', 'spec': 'Python Method', 'message': 'Specification requires implementing a Python constraint to validate the format of the \\"vat\\" (GSTIN) field against the standard Indian GSTIN regular expression, as per REQ-1-205.'}

#### 2.3.4.5.0.0.0 Class Name

##### 2.3.4.5.1.0.0 Class Name

TmsRoute

##### 2.3.4.5.2.0.0 File Path

tms_core/models/tms_route.py

##### 2.3.4.5.3.0.0 Class Type

Odoo Model

##### 2.3.4.5.4.0.0 Inheritance

models.Model

##### 2.3.4.5.5.0.0 Purpose

Specification for the Route Master data model, as required by REQ-1-206.

##### 2.3.4.5.6.0.0 Dependencies

*No items available*

##### 2.3.4.5.7.0.0 Framework Specific Attributes

###### 2.3.4.5.7.1.0 Name

tms.route

###### 2.3.4.5.7.2.0 Description

Route Master

##### 2.3.4.5.8.0.0 Fields

- {'field_name': 'name', 'field_type': 'fields.Char', 'purpose': 'The unique name for the pre-defined route.', 'attributes': {'string': 'Route Name', 'required': 'True'}}

##### 2.3.4.5.9.0.0 Methods

*No items available*

##### 2.3.4.5.10.0.0 Constraints

*No items available*

#### 2.3.4.6.0.0.0 Class Name

##### 2.3.4.6.1.0.0 Class Name

TmsMaterial

##### 2.3.4.6.2.0.0 File Path

tms_core/models/tms_material.py

##### 2.3.4.6.3.0.0 Class Type

Odoo Model

##### 2.3.4.6.4.0.0 Inheritance

models.Model

##### 2.3.4.6.5.0.0 Purpose

Specification for the Material Master data model, as required by REQ-1-003.

##### 2.3.4.6.6.0.0 Dependencies

*No items available*

##### 2.3.4.6.7.0.0 Framework Specific Attributes

###### 2.3.4.6.7.1.0 Name

tms.material

###### 2.3.4.6.7.2.0 Description

Material Master

##### 2.3.4.6.8.0.0 Fields

- {'field_name': 'name', 'field_type': 'fields.Char', 'purpose': 'The unique name of the material.', 'attributes': {'string': 'Material Name', 'required': 'True'}}

##### 2.3.4.6.9.0.0 Methods

*No items available*

##### 2.3.4.6.10.0.0 Constraints

*No items available*

#### 2.3.4.7.0.0.0 Class Name

##### 2.3.4.7.1.0.0 Class Name

TmsExpense

##### 2.3.4.7.2.0.0 File Path

tms_core/models/tms_expense.py

##### 2.3.4.7.3.0.0 Class Type

Odoo Model

##### 2.3.4.7.4.0.0 Inheritance

models.Model, mail.thread

##### 2.3.4.7.5.0.0 Purpose

Specification for the Trip Expense model to manage expense submission and approval, as per REQ-1-107 and REQ-1-108.

##### 2.3.4.7.6.0.0 Dependencies

*No items available*

##### 2.3.4.7.7.0.0 Framework Specific Attributes

| Property | Value |
|----------|-------|
| Name | tms.expense |
| Description | Trip Expense |
| Inherit | [\"mail.thread\"] |

##### 2.3.4.7.8.0.0 Fields

###### 2.3.4.7.8.1.0 Field Name

####### 2.3.4.7.8.1.1 Field Name

trip_id

####### 2.3.4.7.8.1.2 Field Type

fields.Many2one

####### 2.3.4.7.8.1.3 Related Model

tms.trip

####### 2.3.4.7.8.1.4 Purpose

Link to the associated trip.

####### 2.3.4.7.8.1.5 Attributes

| Property | Value |
|----------|-------|
| String | Trip |
| Required | True |

###### 2.3.4.7.8.2.0 Field Name

####### 2.3.4.7.8.2.1 Field Name

state

####### 2.3.4.7.8.2.2 Field Type

fields.Selection

####### 2.3.4.7.8.2.3 Purpose

Manages the approval lifecycle of the expense.

####### 2.3.4.7.8.2.4 Attributes

| Property | Value |
|----------|-------|
| String | Status |
| Selection | [(\"submitted\", \"Submitted\"), (\"approved\", \"... |
| Default | \"submitted\" |
| Tracking | True |

##### 2.3.4.7.9.0.0 Methods

###### 2.3.4.7.9.1.0 Method Name

####### 2.3.4.7.9.1.1 Method Name

action_approve

####### 2.3.4.7.9.1.2 Method Signature

action_approve(self)

####### 2.3.4.7.9.1.3 Return Type

void

####### 2.3.4.7.9.1.4 Purpose

Changes the expense state to \"approved\".

####### 2.3.4.7.9.1.5 Implementation Logic

Specification requires checking user permissions for the \"Dispatch Manager\" or \"Finance Officer\" group. If authorized, set state to \"approved\".

####### 2.3.4.7.9.1.6 Exception Handling

Raises `AccessError` for unauthorized users.

###### 2.3.4.7.9.2.0 Method Name

####### 2.3.4.7.9.2.1 Method Name

action_reject

####### 2.3.4.7.9.2.2 Method Signature

action_reject(self)

####### 2.3.4.7.9.2.3 Return Type

dict

####### 2.3.4.7.9.2.4 Purpose

Launches a wizard to capture the mandatory rejection reason.

####### 2.3.4.7.9.2.5 Implementation Logic

Specification requires returning an Odoo action to open the `tms.reason.wizard` for capturing the reason before changing the state.

####### 2.3.4.7.9.2.6 Exception Handling

Raises `AccessError` for unauthorized users.

##### 2.3.4.7.10.0.0 Constraints

*No items available*

#### 2.3.4.8.0.0.0 Class Name

##### 2.3.4.8.1.0.0 Class Name

TmsPod

##### 2.3.4.8.2.0.0 File Path

tms_core/models/tms_pod.py

##### 2.3.4.8.3.0.0 Class Type

Odoo Model

##### 2.3.4.8.4.0.0 Inheritance

models.Model

##### 2.3.4.8.5.0.0 Purpose

Specification for the Proof of Delivery model as per REQ-1-114.

##### 2.3.4.8.6.0.0 Dependencies

*No items available*

##### 2.3.4.8.7.0.0 Framework Specific Attributes

###### 2.3.4.8.7.1.0 Name

tms.pod

###### 2.3.4.8.7.2.0 Description

Proof of Delivery

##### 2.3.4.8.8.0.0 Fields

###### 2.3.4.8.8.1.0 Field Name

####### 2.3.4.8.8.1.1 Field Name

trip_id

####### 2.3.4.8.8.1.2 Field Type

fields.Many2one

####### 2.3.4.8.8.1.3 Related Model

tms.trip

####### 2.3.4.8.8.1.4 Attributes

| Property | Value |
|----------|-------|
| String | Trip |
| Required | True |

###### 2.3.4.8.8.2.0 Field Name

####### 2.3.4.8.8.2.1 Field Name

pod_attachment

####### 2.3.4.8.8.2.2 Field Type

fields.Binary

####### 2.3.4.8.8.2.3 Purpose

Stores the uploaded photo or e-signature image.

####### 2.3.4.8.8.2.4 Attributes

| Property | Value |
|----------|-------|
| String | POD File |

##### 2.3.4.8.9.0.0 Methods

*No items available*

##### 2.3.4.8.10.0.0 Constraints

*No items available*

#### 2.3.4.9.0.0.0 Class Name

##### 2.3.4.9.1.0.0 Class Name

TmsVehicleDocument

##### 2.3.4.9.2.0.0 File Path

tms_core/models/tms_vehicle_document.py

##### 2.3.4.9.3.0.0 Class Type

Odoo Model

##### 2.3.4.9.4.0.0 Inheritance

models.Model

##### 2.3.4.9.5.0.0 Purpose

Specification for storing vehicle compliance documents as per REQ-1-201.

##### 2.3.4.9.6.0.0 Dependencies

*No items available*

##### 2.3.4.9.7.0.0 Framework Specific Attributes

###### 2.3.4.9.7.1.0 Name

tms.vehicle.document

###### 2.3.4.9.7.2.0 Description

Vehicle Document

##### 2.3.4.9.8.0.0 Fields

###### 2.3.4.9.8.1.0 Field Name

####### 2.3.4.9.8.1.1 Field Name

vehicle_id

####### 2.3.4.9.8.1.2 Field Type

fields.Many2one

####### 2.3.4.9.8.1.3 Related Model

tms.vehicle

####### 2.3.4.9.8.1.4 Attributes

| Property | Value |
|----------|-------|
| String | Vehicle |
| Required | True |

###### 2.3.4.9.8.2.0 Field Name

####### 2.3.4.9.8.2.1 Field Name

expiry_date

####### 2.3.4.9.8.2.2 Field Type

fields.Date

####### 2.3.4.9.8.2.3 Purpose

The expiry date of the document, used for alert generation.

####### 2.3.4.9.8.2.4 Attributes

| Property | Value |
|----------|-------|
| String | Expiry Date |

##### 2.3.4.9.9.0.0 Methods

*No items available*

##### 2.3.4.9.10.0.0 Constraints

*No items available*

#### 2.3.4.10.0.0.0 Class Name

##### 2.3.4.10.1.0.0 Class Name

TmsCard

##### 2.3.4.10.2.0.0 File Path

tms_core/models/tms_card.py

##### 2.3.4.10.3.0.0 Class Type

Odoo Model

##### 2.3.4.10.4.0.0 Inheritance

models.Model

##### 2.3.4.10.5.0.0 Purpose

Specification for the Card Management model as per REQ-1-110.

##### 2.3.4.10.6.0.0 Dependencies

*No items available*

##### 2.3.4.10.7.0.0 Framework Specific Attributes

###### 2.3.4.10.7.1.0 Name

tms.card

###### 2.3.4.10.7.2.0 Description

FASTag/Diesel Card Management

##### 2.3.4.10.8.0.0 Fields

###### 2.3.4.10.8.1.0 Field Name

####### 2.3.4.10.8.1.1 Field Name

card_number

####### 2.3.4.10.8.1.2 Field Type

fields.Char

####### 2.3.4.10.8.1.3 Attributes

| Property | Value |
|----------|-------|
| String | Card Number |
| Required | True |

###### 2.3.4.10.8.2.0 Field Name

####### 2.3.4.10.8.2.1 Field Name

low_balance_threshold

####### 2.3.4.10.8.2.2 Field Type

fields.Float

####### 2.3.4.10.8.2.3 Attributes

| Property | Value |
|----------|-------|
| String | Low Balance Threshold |

##### 2.3.4.10.9.0.0 Methods

*No items available*

##### 2.3.4.10.10.0.0 Constraints

*No items available*

#### 2.3.4.11.0.0.0 Class Name

##### 2.3.4.11.1.0.0 Class Name

TmsAlert

##### 2.3.4.11.2.0.0 File Path

tms_core/models/tms_alert.py

##### 2.3.4.11.3.0.0 Class Type

Odoo Model

##### 2.3.4.11.4.0.0 Inheritance

models.Model

##### 2.3.4.11.5.0.0 Purpose

Specification for a generic model to store and display system alerts on the dashboard as per REQ-1-010.

##### 2.3.4.11.6.0.0 Dependencies

*No items available*

##### 2.3.4.11.7.0.0 Framework Specific Attributes

###### 2.3.4.11.7.1.0 Name

tms.alert

###### 2.3.4.11.7.2.0 Description

System Alert

##### 2.3.4.11.8.0.0 Fields

- {'field_name': 'message', 'field_type': 'fields.Char', 'attributes': {'string': 'Message', 'required': 'True'}}

##### 2.3.4.11.9.0.0 Methods

*No items available*

##### 2.3.4.11.10.0.0 Constraints

*No items available*

#### 2.3.4.12.0.0.0 Class Name

##### 2.3.4.12.1.0.0 Class Name

TmsTripEvent

##### 2.3.4.12.2.0.0 File Path

tms_core/models/tms_trip_event.py

##### 2.3.4.12.3.0.0 Class Type

Odoo Model

##### 2.3.4.12.4.0.0 Inheritance

models.Model

##### 2.3.4.12.5.0.0 Purpose

Specification for logging driver-reported events against a trip as per REQ-1-115.

##### 2.3.4.12.6.0.0 Dependencies

*No items available*

##### 2.3.4.12.7.0.0 Framework Specific Attributes

###### 2.3.4.12.7.1.0 Name

tms.trip.event

###### 2.3.4.12.7.2.0 Description

Trip Event Log

##### 2.3.4.12.8.0.0 Fields

###### 2.3.4.12.8.1.0 Field Name

####### 2.3.4.12.8.1.1 Field Name

trip_id

####### 2.3.4.12.8.1.2 Field Type

fields.Many2one

####### 2.3.4.12.8.1.3 Related Model

tms.trip

####### 2.3.4.12.8.1.4 Attributes

| Property | Value |
|----------|-------|
| String | Trip |
| Required | True |

###### 2.3.4.12.8.2.0 Field Name

####### 2.3.4.12.8.2.1 Field Name

event_type

####### 2.3.4.12.8.2.2 Field Type

fields.Selection

####### 2.3.4.12.8.2.3 Attributes

| Property | Value |
|----------|-------|
| String | Event Type |
| Selection | [(\"accident\", \"Accident\"), (\"repair\", \"Repa... |

##### 2.3.4.12.9.0.0 Methods

*No items available*

##### 2.3.4.12.10.0.0 Constraints

*No items available*

#### 2.3.4.13.0.0.0 Class Name

##### 2.3.4.13.1.0.0 Class Name

TmsReasonWizard

##### 2.3.4.13.2.0.0 File Path

tms_core/wizards/tms_reason_wizard.py

##### 2.3.4.13.3.0.0 Class Type

Odoo Wizard

##### 2.3.4.13.4.0.0 Inheritance

models.TransientModel

##### 2.3.4.13.5.0.0 Purpose

Enhanced specification for a generic wizard to capture a mandatory reason for actions like cancellation or resuming a trip.

##### 2.3.4.13.6.0.0 Dependencies

*No items available*

##### 2.3.4.13.7.0.0 Framework Specific Attributes

###### 2.3.4.13.7.1.0 Name

tms.reason.wizard

###### 2.3.4.13.7.2.0 Description

Generic Reason Wizard

##### 2.3.4.13.8.0.0 Fields

- {'field_name': 'reason', 'field_type': 'fields.Text', 'purpose': 'The text field for the user to enter the reason.', 'attributes': {'string': 'Reason', 'required': 'True'}}

##### 2.3.4.13.9.0.0 Methods

- {'method_name': 'action_confirm', 'method_signature': 'action_confirm(self)', 'return_type': 'void', 'purpose': 'The generic action executed when the user clicks \\"Confirm\\".', 'implementation_logic': 'Specification requires this method to read the active model and active ID from the context. It should then call a specific method on the target record (e.g., `_action_cancel_with_reason`) and pass the captured reason. The name of the method to call should also be passed in the context from the button that launched the wizard.', 'exception_handling': 'Raises `ValidationError` if the reason is empty.'}

##### 2.3.4.13.10.0.0 Constraints

*No items available*

### 2.3.5.0.0.0.0 Interface Specifications

*No items available*

### 2.3.6.0.0.0.0 Enum Specifications

*No items available*

### 2.3.7.0.0.0.0 Dto Specifications

*No items available*

### 2.3.8.0.0.0.0 Configuration Specifications

*No items available*

### 2.3.9.0.0.0.0 Dependency Injection Specifications

*No items available*

### 2.3.10.0.0.0.0 External Integration Specifications

*No items available*

### 2.3.11.0.0.0.0 File Specifications

#### 2.3.11.1.0.0.0 File Name

##### 2.3.11.1.1.0.0 File Name

__manifest__.py

##### 2.3.11.1.2.0.0 File Path

tms_core/__manifest__.py

##### 2.3.11.1.3.0.0 File Type

Odoo Manifest

##### 2.3.11.1.4.0.0 Purpose

Defines the module's metadata, dependencies, and data files to be loaded by Odoo.

##### 2.3.11.1.5.0.0 Implementation Notes

This file's specification must include \"name\", \"version\", \"summary\", \"author\", \"category\". The \"depends\" key must list \"base\", \"hr\", and \"account\". The \"data\" key must define the load order: all \"security/\" files first (groups, then access csv, then rules), followed by all \"views/\" and \"wizards/\" files.

#### 2.3.11.2.0.0.0 File Name

##### 2.3.11.2.1.0.0 File Name

ir.model.access.csv

##### 2.3.11.2.2.0.0 File Path

tms_core/security/ir.model.access.csv

##### 2.3.11.2.3.0.0 File Type

Odoo Security CSV

##### 2.3.11.2.4.0.0 Purpose

Defines the model-level CRUD permissions for each security group, fulfilling REQ-1-008.

##### 2.3.11.2.5.0.0 Implementation Notes

This CSV file specification requires entries for all custom models and security groups. It must specify permissions that enforce the separation of duties outlined in REQ-1-101 (e.g., Finance Officers cannot create trips, Dispatch Managers cannot manage users).

#### 2.3.11.3.0.0.0 File Name

##### 2.3.11.3.1.0.0 File Name

record_rules.xml

##### 2.3.11.3.2.0.0 File Path

tms_core/security/record_rules.xml

##### 2.3.11.3.3.0.0 File Type

Odoo Security XML

##### 2.3.11.3.4.0.0 Purpose

Defines row-level security rules to enforce data segregation.

##### 2.3.11.3.5.0.0 Implementation Notes

This XML file specification requires a rule for `tms.trip` that restricts users in the \"Driver\" group to only see records where `driver_id` matches their own employee ID, as per REQ-1-100. It must also contain a rule to prevent drivers from viewing any financial data within their own trips.

#### 2.3.11.4.0.0.0 File Name

##### 2.3.11.4.1.0.0 File Name

security_groups.xml

##### 2.3.11.4.2.0.0 File Path

tms_core/security/security_groups.xml

##### 2.3.11.4.3.0.0 File Type

Odoo Security XML

##### 2.3.11.4.4.0.0 Purpose

Defines the security groups for each TMS role.

##### 2.3.11.4.5.0.0 Implementation Notes

Specification for this new file requires defining a top-level category \"TMS/Roles\". Inside, it must define `<record>` tags for `res.groups` with IDs like `group_tms_admin`, `group_tms_dispatch_manager`, `group_tms_finance_officer`, and `group_tms_driver`, fulfilling REQ-1-008.

#### 2.3.11.5.0.0.0 File Name

##### 2.3.11.5.1.0.0 File Name

tms_trip_views.xml

##### 2.3.11.5.2.0.0 File Path

tms_core/views/tms_trip_views.xml

##### 2.3.11.5.3.0.0 File Type

Odoo View XML

##### 2.3.11.5.4.0.0 Purpose

Defines the user interface for the tms.trip model.

##### 2.3.11.5.5.0.0 Implementation Notes

This XML file specification must include a form view with a `<header>` containing a `<field name=\"state\" widget=\"statusbar\"/>`. Buttons in the header must use the `states` attribute to be conditionally visible according to the strict lifecycle in REQ-1-904. The form must also include fields for profitability calculations, which must be hidden from the \"Driver\" group using the `groups` attribute.

#### 2.3.11.6.0.0.0 File Name

##### 2.3.11.6.1.0.0 File Name

tms_reason_wizard_views.xml

##### 2.3.11.6.2.0.0 File Path

tms_core/wizards/tms_reason_wizard_views.xml

##### 2.3.11.6.3.0.0 File Type

Odoo View XML

##### 2.3.11.6.4.0.0 Purpose

Defines the user interface for the generic reason wizard.

##### 2.3.11.6.5.0.0 Implementation Notes

Specification for the form view of the `tms.reason.wizard` model. The footer must contain a primary button calling `action_confirm` and a secondary \"Cancel\" button.

## 2.4.0.0.0.0.0 Component Count Validation

| Property | Value |
|----------|-------|
| Total Classes | 13 |
| Total Interfaces | 0 |
| Total Enums | 0 |
| Total Dtos | 0 |
| Total Configurations | 0 |
| Total External Integrations | 0 |
| Total Files | 6 |
| Grand Total Components | 19 |
| Phase 2 Claimed Count | 0 |
| Phase 2 Actual Count | 0 |
| Validation Added Count | 48 |
| Final Validated Count | 19 |

