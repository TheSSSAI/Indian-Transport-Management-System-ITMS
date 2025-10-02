# 1 Id

REPO-TMS-CORE

# 2 Name

tms-core-business-logic

# 3 Description

This repository is the core of the Transport Management System, extracted from the original 'tms-odoo-addon' monolith. It contains the fundamental Odoo 18 modules that define the data models (e.g., Trip, Vehicle, Driver), core business logic, workflow state machines, and access control rules (RBAC). It also includes the standard back-office user interface views (Form, List, Kanban) for administrative and management roles. This component serves as the central business engine, providing the foundational data and services upon which all other specialized components, such as the driver portal and external integrations, depend. Its primary responsibility is to maintain the integrity and logic of the core transport operations domain, acting as the single source of truth for business data.

# 4 Type

🔹 Business Logic

# 5 Namespace

odoo.addons.tms_core

# 6 Output Path

addons/tms_core

# 7 Framework

Odoo 18

# 8 Language

Python

# 9 Technology

Odoo 18, Python 3.11, PostgreSQL 16

# 10 Thirdparty Libraries

*No items available*

# 11 Layer Ids

- business-logic-layer
- data-access-layer

# 12 Dependencies

*No items available*

# 13 Requirements

## 13.1 Requirement Id

### 13.1.1 Requirement Id

REQ-1-003

## 13.2.0 Requirement Id

### 13.2.1 Requirement Id

REQ-1-004

## 13.3.0 Requirement Id

### 13.3.1 Requirement Id

REQ-1-103

## 13.4.0 Requirement Id

### 13.4.1 Requirement Id

REQ-1-904

# 14.0.0 Generate Tests

✅ Yes

# 15.0.0 Generate Documentation

✅ Yes

# 16.0.0 Architecture Style

Modular Monolith

# 17.0.0 Architecture Map

- Odoo Business Logic Layer (Models & Controllers)

# 18.0.0 Components Map

- tms-odoo-addon-001

# 19.0.0 Requirements Map

- REQ-1-003
- REQ-1-004
- REQ-1-103
- REQ-1-904

# 20.0.0 Decomposition Rationale

## 20.1.0 Operation Type

NEW_DECOMPOSED

## 20.2.0 Source Repository

tms-odoo-addon

## 20.3.0 Decomposition Reasoning

This component was extracted to isolate the foundational business logic from UI and integration concerns. By creating a core repository, we establish a stable base that other components can depend on, reducing code entanglement within the original monolith and clarifying the primary responsibility of managing the core business domain.

## 20.4.0 Extracted Responsibilities

- Core data model definitions (Trip, Vehicle, etc.)
- Business rule and state machine implementation
- Back-office user interface views (XML)
- Role-Based Access Control (RBAC) definitions

## 20.5.0 Reusability Scope

- Serves as the foundational library for all other Odoo addons in the TMS ecosystem.

## 20.6.0 Development Benefits

- Allows the core business logic team to focus on domain rules without being impacted by UI or integration changes.
- Provides a clear, stable API (via Odoo ORM) for other components to consume.

# 21.0.0 Dependency Contracts

*No data available*

# 22.0.0 Exposed Contracts

## 22.1.0 Public Interfaces

- {'interface': 'Odoo ORM API (tms.trip, tms.vehicle, etc.)', 'methods': ['create(vals)', 'search([domain])', 'write(vals)', 'read([fields])'], 'events': [], 'properties': ['Odoo Model Fields (e.g., tms.trip.state)'], 'consumers': ['REPO-DRV-UI', 'REPO-GSP-INT', 'REPO-GPS-CON']}

# 23.0.0 Integration Patterns

| Property | Value |
|----------|-------|
| Dependency Injection | N/A (Uses Odoo's registry for service lookups) |
| Event Communication | Internal Odoo bus for model-level events. |
| Data Flow | Primary CRUD operations against the PostgreSQL dat... |
| Error Handling | Standard Odoo exceptions (UserError, ValidationErr... |
| Async Patterns | Utilizes Odoo scheduled actions for background tas... |

# 24.0.0 Technology Guidance

| Property | Value |
|----------|-------|
| Framework Specific | All code must adhere to Odoo development best prac... |
| Performance Considerations | Optimize ORM queries to avoid N+1 problems. Use ap... |
| Security Considerations | All data access must be protected by Odoo's securi... |
| Testing Approach | Focus on unit and integration tests for business l... |

# 25.0.0 Scope Boundaries

## 25.1.0 Must Implement

- All master data models.
- The complete trip lifecycle logic.
- Financial calculations like profitability.

## 25.2.0 Must Not Implement

- Custom frontend UI components (handled by REPO-DRV-UI).
- Direct communication logic with external third-party APIs (handled by integration repositories).

## 25.3.0 Extension Points

- Models are extensible via Odoo's inheritance mechanism.

## 25.4.0 Validation Rules

- Enforces all business rules like vehicle capacity (BR-007) and expired licenses (BR-003).

