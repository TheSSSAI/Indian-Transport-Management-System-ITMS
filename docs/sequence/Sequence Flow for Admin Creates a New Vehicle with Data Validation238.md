# 1 Overview

## 1.1 Diagram Id

SEQ-FF-015

## 1.2 Name

Admin Creates a New Vehicle with Data Validation

## 1.3 Description

An Admin user navigates to the Vehicle Master screen and creates a new vehicle record. The system performs server-side validation to ensure data integrity, specifically checking for the uniqueness of the truck number.

## 1.4 Type

🔹 FeatureFlow

## 1.5 Purpose

To add a new vehicle to the system's master data while enforcing critical business rules and data constraints.

## 1.6 Complexity

Low

## 1.7 Priority

🔴 High

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- Admin fills out the 'New Vehicle' form, including the Truck Number.
- Admin clicks 'Save'.
- REPO-TMS-CORE's ORM `create` method is invoked.
- A database query is executed to check if the provided Truck Number already exists.
- If unique, the new vehicle record is committed to the database.
- If not unique, a ValidationError is raised and displayed to the Admin.

## 1.11 Triggers

- A new vehicle is procured by the company.

## 1.12 Outcomes

- A new, valid vehicle record is added to the system.
- Data integrity is maintained.

## 1.13 Business Rules

- BR-002: The 'Truck Number' for each vehicle must be unique.

## 1.14 Error Scenarios

- Admin enters a duplicate truck number.
- Admin enters a truck number in an invalid format.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-FF-015

## 2.2 Name

Admin Creates Vehicle with Server-Side Uniqueness Validation

## 2.3 Description

Technical sequence for an Admin user creating a new vehicle record via the Odoo Web UI. The sequence details the JSON-RPC call to the Odoo server, which then enforces the business rule BR-002 (unique truck number) through an indexed database query before committing the new record. It covers both the successful creation path and the exception handling path for validation failures.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

USER-ADMIN

#### 2.4.1.2 Display Name

User (Admin)

#### 2.4.1.3 Type

🔹 Actor

#### 2.4.1.4 Technology

Human

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #999999 |
| Stereotype | <<Human>> |

### 2.4.2.0 Client

#### 2.4.2.1 Repository Id

ODOO-WEB-UI

#### 2.4.2.2 Display Name

Odoo Web UI (Browser)

#### 2.4.2.3 Type

🔹 Client

#### 2.4.2.4 Technology

Odoo Web Library (OWL), JavaScript

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | participant |
| Color | #4285F4 |
| Stereotype | <<Client>> |

### 2.4.3.0 Application

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

TMS Core (Odoo Server)

#### 2.4.3.3 Type

🔹 Application

#### 2.4.3.4 Technology

Odoo 18, Python 3.11

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | participant |
| Color | #34A853 |
| Stereotype | <<Application>> |

### 2.4.4.0 Database

#### 2.4.4.1 Repository Id

POSTGRESQL-DB

#### 2.4.4.2 Display Name

PostgreSQL Database

#### 2.4.4.3 Type

🔹 Database

#### 2.4.4.4 Technology

PostgreSQL 16

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #DB4437 |
| Stereotype | <<Database>> |

## 2.5.0.0 Interactions

### 2.5.1.0 UserInteraction

#### 2.5.1.1 Source Id

USER-ADMIN

#### 2.5.1.2 Target Id

ODOO-WEB-UI

#### 2.5.1.3 Message

1. Fills 'New Vehicle' form with data (e.g., Truck Number, Model) and clicks 'Save'.

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 UserInteraction

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message



#### 2.5.1.8 Has Return

❌ No

#### 2.5.1.9 Is Activation

❌ No

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | UI Event |
| Method | onSubmit |
| Parameters | Form field values |
| Authentication | N/A |
| Error Handling | Client-side format validation (e.g., for truck num... |
| Performance | N/A |

### 2.5.2.0 Request

#### 2.5.2.1 Source Id

ODOO-WEB-UI

#### 2.5.2.2 Target Id

REPO-TMS-CORE

#### 2.5.2.3 Message

2. [RPC] call('tms.vehicle', 'create', [vals])

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 Request

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

8. [RPC Response] Success with new record ID OR Validation Error

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

✅ Yes

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | JSON-RPC over HTTPS |
| Method | POST /jsonrpc |
| Parameters | payload: { model: 'tms.vehicle', method: 'create',... |
| Authentication | Odoo 'session_id' cookie required and validated. |
| Error Handling | Handles HTTP errors (4xx, 5xx) and RPC-level fault... |
| Performance | Network latency is a factor. Request/response size... |

#### 2.5.2.11 Nested Interactions

##### 2.5.2.11.1 SecurityCheck

###### 2.5.2.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.2.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.2.11.1.3 Message

3. Verify user has 'create' access rights for 'tms.vehicle' model.

###### 2.5.2.11.1.4 Sequence Number

3

###### 2.5.2.11.1.5 Type

🔹 SecurityCheck

###### 2.5.2.11.1.6 Is Synchronous

✅ Yes

###### 2.5.2.11.1.7 Return Message

Access granted or denied.

###### 2.5.2.11.1.8 Has Return

✅ Yes

###### 2.5.2.11.1.9 Is Activation

❌ No

###### 2.5.2.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | self.check_access_rights('create') |
| Parameters | N/A |
| Authentication | Internal context user |
| Error Handling | If check fails, raises odoo.exceptions.AccessError... |
| Performance | Cached for performance. |

##### 2.5.2.11.2.0 Query

###### 2.5.2.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.2.11.2.2 Target Id

POSTGRESQL-DB

###### 2.5.2.11.2.3 Message

4. [SQL] SELECT 1 FROM tms_vehicle WHERE truck_number = $1

###### 2.5.2.11.2.4 Sequence Number

4

###### 2.5.2.11.2.5 Type

🔹 Query

###### 2.5.2.11.2.6 Is Synchronous

✅ Yes

###### 2.5.2.11.2.7 Return Message

5. [SQL Result] Returns 0 rows (Unique) or 1 row (Duplicate).

###### 2.5.2.11.2.8 Has Return

✅ Yes

###### 2.5.2.11.2.9 Is Activation

✅ Yes

###### 2.5.2.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL Wire Protocol |
| Method | SELECT |
| Parameters | truck_number value |
| Authentication | DB connection credentials from Odoo config. |
| Error Handling | Handles potential DB connection errors. |
| Performance | Critical path. Requires a UNIQUE index on the `tru... |

##### 2.5.2.11.3.0 Command

###### 2.5.2.11.3.1 Source Id

REPO-TMS-CORE

###### 2.5.2.11.3.2 Target Id

POSTGRESQL-DB

###### 2.5.2.11.3.3 Message

6. [ALT: Success] [SQL] INSERT INTO tms_vehicle (truck_number, ...) VALUES ($1, ...)

###### 2.5.2.11.3.4 Sequence Number

6

###### 2.5.2.11.3.5 Type

🔹 Command

###### 2.5.2.11.3.6 Is Synchronous

✅ Yes

###### 2.5.2.11.3.7 Return Message

7. [SQL Result] Commit successful, returns new record ID.

###### 2.5.2.11.3.8 Has Return

✅ Yes

###### 2.5.2.11.3.9 Is Activation

❌ No

###### 2.5.2.11.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL Wire Protocol |
| Method | INSERT |
| Parameters | All validated vehicle data. |
| Authentication | DB connection credentials. |
| Error Handling | The UNIQUE constraint on the `truck_number` column... |
| Performance | Standard INSERT performance. |

##### 2.5.2.11.4.0 Exception

###### 2.5.2.11.4.1 Source Id

REPO-TMS-CORE

###### 2.5.2.11.4.2 Target Id

REPO-TMS-CORE

###### 2.5.2.11.4.3 Message

6a. [ALT: Failure] Raise ValidationError('Truck Number must be unique.')

###### 2.5.2.11.4.4 Sequence Number

6.1

###### 2.5.2.11.4.5 Type

🔹 Exception

###### 2.5.2.11.4.6 Is Synchronous

✅ Yes

###### 2.5.2.11.4.7 Return Message

Error object is prepared for RPC response.

###### 2.5.2.11.4.8 Has Return

✅ Yes

###### 2.5.2.11.4.9 Is Activation

❌ No

###### 2.5.2.11.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Python Exception |
| Method | raise odoo.exceptions.ValidationError |
| Parameters | User-friendly error message. |
| Authentication | N/A |
| Error Handling | This exception is caught by the Odoo RPC dispatche... |
| Performance | N/A |

### 2.5.3.0.0.0 UIUpdate

#### 2.5.3.1.0.0 Source Id

ODOO-WEB-UI

#### 2.5.3.2.0.0 Target Id

USER-ADMIN

#### 2.5.3.3.0.0 Message

9. [ALT: Success] Display success notification and redirect to the new vehicle's form view.

#### 2.5.3.4.0.0 Sequence Number

9

#### 2.5.3.5.0.0 Type

🔹 UIUpdate

#### 2.5.3.6.0.0 Is Synchronous

✅ Yes

#### 2.5.3.7.0.0 Return Message



#### 2.5.3.8.0.0 Has Return

❌ No

#### 2.5.3.9.0.0 Is Activation

❌ No

#### 2.5.3.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | DOM Update |
| Method | N/A |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | UI rendering should be immediate. |

### 2.5.4.0.0.0 UIUpdate

#### 2.5.4.1.0.0 Source Id

ODOO-WEB-UI

#### 2.5.4.2.0.0 Target Id

USER-ADMIN

#### 2.5.4.3.0.0 Message

9a. [ALT: Failure] Display validation error message next to the 'Truck Number' field.

#### 2.5.4.4.0.0 Sequence Number

9.1

#### 2.5.4.5.0.0 Type

🔹 UIUpdate

#### 2.5.4.6.0.0 Is Synchronous

✅ Yes

#### 2.5.4.7.0.0 Return Message



#### 2.5.4.8.0.0 Has Return

❌ No

#### 2.5.4.9.0.0 Is Activation

❌ No

#### 2.5.4.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | DOM Update |
| Method | N/A |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | UI rendering should be immediate. |

## 2.6.0.0.0.0 Notes

- {'content': 'Business Rule BR-002 is enforced at two levels: programmatically by the SELECT query, and structurally by the database UNIQUE constraint to prevent race conditions.', 'position': 'bottom', 'participantId': 'REPO-TMS-CORE', 'sequenceNumber': 4}

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The 'tms.vehicle' Odoo model must have Access Cont... |
| Performance Targets | The entire create operation (sequence 2-8) must ha... |
| Error Handling Strategy | If the `truck_number` is a duplicate (violating BR... |
| Testing Considerations | 1. **Unit Test**: Test the `create` method of the ... |
| Monitoring Requirements | 1. **Metrics**: Monitor the rate of `ValidationErr... |
| Deployment Considerations | The database migration script that creates the `tm... |

