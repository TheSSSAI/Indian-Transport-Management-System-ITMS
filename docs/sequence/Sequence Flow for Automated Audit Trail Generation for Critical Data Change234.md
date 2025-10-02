# 1 Overview

## 1.1 Diagram Id

SEQ-CF-011

## 1.2 Name

Automated Audit Trail Generation for Critical Data Change

## 1.3 Description

An Admin user modifies a critical field, such as the total amount, on an Invoice record. The system automatically and immutably creates an audit log entry that records the user, the timestamp, and the specific old and new values of the changed field.

## 1.4 Type

🔹 ComplianceFlow

## 1.5 Purpose

To maintain a non-repudiable, transparent history of all significant changes to critical data models, supporting security audits, regulatory compliance, and post-incident investigations.

## 1.6 Complexity

Low

## 1.7 Priority

🟡 Medium

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- An authenticated 'Admin' user opens an Invoice record in the UI.
- The user modifies a tracked field (e.g., `amount_total`) and clicks 'Save'.
- The `write` method of the Odoo ORM is called for the `account.move` model.
- Odoo's `mail.thread` mixin, which is inherited by the Invoice model, detects the change to a tracked field.
- A new `mail.message` record is created and linked to the Invoice record, containing a formatted string detailing the field changed, the old value, and the new value.
- This change log is immediately visible in the 'chatter' widget on the Invoice form view.

## 1.11 Triggers

- A Create, Update, or Delete (CRUD) operation is performed on a critical data model like Trip, Invoice, or Payment.

## 1.12 Outcomes

- A permanent, user-attributable, and timestamped audit log of the data modification is created.
- The log is easily accessible to other authorized users (Admins) for review.

## 1.13 Business Rules

- REQ-DAT-008: The system shall maintain an immutable audit trail for all create, update, and delete (CRUD) operations on critical data models.
- Audit logs shall be accessible only to users with the 'Admin' role.

## 1.14 Error Scenarios

*No items available*

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-CF-011

## 2.2 Name

Implementation of Automated Audit Trail for Critical Data Change in Odoo

## 2.3 Description

This sequence details the technical implementation of generating an immutable audit log when an Admin user modifies a tracked field on a critical Odoo model (e.g., Invoice). It leverages the built-in `mail.thread` mixin to automatically detect changes within the ORM `write` method, creates a `mail.message` record detailing the change, and commits both the data update and the audit log in a single atomic database transaction. This fulfills the compliance requirement REQ-DAT-008.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

user-actor-admin

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
| Color | #90A4AE |
| Stereotype | User |

### 2.4.2.0 Frontend UI

#### 2.4.2.1 Repository Id

temp-odoo-web-client

#### 2.4.2.2 Display Name

Odoo Web Client

#### 2.4.2.3 Type

🔹 Frontend UI

#### 2.4.2.4 Technology

Odoo Web Library (OWL) 2.0, JavaScript

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | boundary |
| Color | #4DD0E1 |
| Stereotype | UI |

### 2.4.3.0 Business Logic

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

TMS Core (Odoo Server)

#### 2.4.3.3 Type

🔹 Business Logic

#### 2.4.3.4 Technology

Odoo 18, Python 3.11

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #81C784 |
| Stereotype | Odoo Addon |

### 2.4.4.0 Database

#### 2.4.4.1 Repository Id

temp-postgresql-db

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
| Color | #7986CB |
| Stereotype | RDBMS |

## 2.5.0.0 Interactions

### 2.5.1.0 User Interaction

#### 2.5.1.1 Source Id

user-actor-admin

#### 2.5.1.2 Target Id

temp-odoo-web-client

#### 2.5.1.3 Message

1. Modifies tracked field (e.g., 'amount_total') on Invoice form and clicks 'Save'

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 User Interaction

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message



#### 2.5.1.8 Has Return

❌ No

#### 2.5.1.9 Is Activation

❌ No

#### 2.5.1.10 Technical Details

##### 2.5.1.10.1 Protocol

UI Event

##### 2.5.1.10.2 Method

on-click

##### 2.5.1.10.3 Parameters

- Event object

##### 2.5.1.10.4 Authentication

N/A

##### 2.5.1.10.5 Error Handling

Standard UI form validation.

##### 2.5.1.10.6 Performance

###### 2.5.1.10.6.1 Latency

<100ms

### 2.5.2.0.0.0 HTTP Request

#### 2.5.2.1.0.0 Source Id

temp-odoo-web-client

#### 2.5.2.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.2.3.0.0 Message

2. RPC Call: execute_kw('account.move', 'write', [invoice_id], {'amount_total': new_value})

#### 2.5.2.4.0.0 Sequence Number

2

#### 2.5.2.5.0.0 Type

🔹 HTTP Request

#### 2.5.2.6.0.0 Is Synchronous

✅ Yes

#### 2.5.2.7.0.0 Return Message

7. HTTP 200 OK Response with success status

#### 2.5.2.8.0.0 Has Return

✅ Yes

#### 2.5.2.9.0.0 Is Activation

✅ Yes

#### 2.5.2.10.0.0 Technical Details

##### 2.5.2.10.1.0 Protocol

HTTP/1.1

##### 2.5.2.10.2.0 Method

POST /jsonrpc

##### 2.5.2.10.3.0 Parameters

- JSON-RPC payload containing model, method, record ID, and updated values.

##### 2.5.2.10.4.0 Authentication

Odoo Session Cookie (`session_id`)

##### 2.5.2.10.5.0 Error Handling

Receives and displays RPC Error (e.g., 404, 500) from Odoo server if the transaction fails.

##### 2.5.2.10.6.0 Performance

###### 2.5.2.10.6.1 Latency

<500ms for typical write operations

### 2.5.3.0.0.0 Internal Method Call

#### 2.5.3.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.3.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.3.3.0.0 Message

3. Invoke ORM: `account_move.write({'amount_total': new_value})`

#### 2.5.3.4.0.0 Sequence Number

3

#### 2.5.3.5.0.0 Type

🔹 Internal Method Call

#### 2.5.3.6.0.0 Is Synchronous

✅ Yes

#### 2.5.3.7.0.0 Return Message

ORM write operation successful

#### 2.5.3.8.0.0 Has Return

✅ Yes

#### 2.5.3.9.0.0 Is Activation

❌ No

#### 2.5.3.10.0.0 Technical Details

##### 2.5.3.10.1.0 Protocol

Python

##### 2.5.3.10.2.0 Method

write()

##### 2.5.3.10.3.0 Parameters

- vals (dict): Dictionary of fields to update.

##### 2.5.3.10.4.0 Authentication

Odoo user context (`self.env.user`) is checked against model's Access Control Lists (ACLs).

##### 2.5.3.10.5.0 Error Handling

Propagates `ValidationError` or `UserError` to the JSON-RPC controller.

##### 2.5.3.10.6.0 Performance

###### 2.5.3.10.6.1 Latency

Dependent on database and number of fields being updated.

#### 2.5.3.11.0.0 Nested Interactions

##### 2.5.3.11.1.0 Internal Logic

###### 2.5.3.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.3.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.3.11.1.3 Message

3.1. [mail.thread] Detect change on field with `tracking=True`

###### 2.5.3.11.1.4 Sequence Number

3.1

###### 2.5.3.11.1.5 Type

🔹 Internal Logic

###### 2.5.3.11.1.6 Is Synchronous

✅ Yes

###### 2.5.3.11.1.7 Return Message

List of changes detected

###### 2.5.3.11.1.8 Has Return

✅ Yes

###### 2.5.3.11.1.9 Is Activation

❌ No

###### 2.5.3.11.1.10 Technical Details

####### 2.5.3.11.1.10.1 Protocol

Python

####### 2.5.3.11.1.10.2 Method

Inherited `write` method logic from `mail.thread` mixin.

####### 2.5.3.11.1.10.3 Parameters

*No items available*

####### 2.5.3.11.1.10.4 Authentication

N/A

####### 2.5.3.11.1.10.5 Error Handling

N/A

####### 2.5.3.11.1.10.6 Performance

######## 2.5.3.11.1.10.6.1 Latency

Minimal overhead, <10ms

##### 2.5.3.11.2.0.0.0 Internal Method Call

###### 2.5.3.11.2.1.0.0 Source Id

REPO-TMS-CORE

###### 2.5.3.11.2.2.0.0 Target Id

REPO-TMS-CORE

###### 2.5.3.11.2.3.0.0 Message

3.2. ORM Call: `self.env['mail.message'].create(...)`

###### 2.5.3.11.2.4.0.0 Sequence Number

3.2

###### 2.5.3.11.2.5.0.0 Type

🔹 Internal Method Call

###### 2.5.3.11.2.6.0.0 Is Synchronous

✅ Yes

###### 2.5.3.11.2.7.0.0 Return Message

New `mail.message` record object

###### 2.5.3.11.2.8.0.0 Has Return

✅ Yes

###### 2.5.3.11.2.9.0.0 Is Activation

❌ No

###### 2.5.3.11.2.10.0.0 Technical Details

####### 2.5.3.11.2.10.1.0 Protocol

Python

####### 2.5.3.11.2.10.2.0 Method

create()

####### 2.5.3.11.2.10.3.0 Parameters

- `vals` (dict): Includes `model='account.move'`, `res_id=invoice_id`, `author_id`, `body='<p>Amount Total: 1000 -> 1200</p>'`, `message_type='notification'`

####### 2.5.3.11.2.10.4.0 Authentication

N/A (system context)

####### 2.5.3.11.2.10.5.0 Error Handling

Raises database exceptions on failure.

####### 2.5.3.11.2.10.6.0 Performance

######## 2.5.3.11.2.10.6.1 Latency

Dependent on database write speed.

### 2.5.4.0.0.0.0.0 Database Transaction

#### 2.5.4.1.0.0.0.0 Source Id

REPO-TMS-CORE

#### 2.5.4.2.0.0.0.0 Target Id

temp-postgresql-db

#### 2.5.4.3.0.0.0.0 Message

4. Execute SQL Transaction

#### 2.5.4.4.0.0.0.0 Sequence Number

4

#### 2.5.4.5.0.0.0.0 Type

🔹 Database Transaction

#### 2.5.4.6.0.0.0.0 Is Synchronous

✅ Yes

#### 2.5.4.7.0.0.0.0 Return Message

6. Transaction COMMIT successful

#### 2.5.4.8.0.0.0.0 Has Return

✅ Yes

#### 2.5.4.9.0.0.0.0 Is Activation

✅ Yes

#### 2.5.4.10.0.0.0.0 Technical Details

##### 2.5.4.10.1.0.0.0 Protocol

PostgreSQL Wire Protocol

##### 2.5.4.10.2.0.0.0 Method

BEGIN; UPDATE account_move ...; INSERT INTO mail_message ...; COMMIT;

##### 2.5.4.10.3.0.0.0 Parameters

- SQL statements with bound parameters.

##### 2.5.4.10.4.0.0.0 Authentication

Database connection credentials from Odoo config.

##### 2.5.4.10.5.0.0.0 Error Handling

On failure, the entire transaction is automatically rolled back, ensuring atomicity.

##### 2.5.4.10.6.0.0.0 Performance

###### 2.5.4.10.6.1.0.0 Latency

<50ms for indexed writes

### 2.5.5.0.0.0.0.0 UI Update

#### 2.5.5.1.0.0.0.0 Source Id

temp-odoo-web-client

#### 2.5.5.2.0.0.0.0 Target Id

user-actor-admin

#### 2.5.5.3.0.0.0.0 Message

8. Render updated Invoice view, displaying new value and audit log in chatter widget

#### 2.5.5.4.0.0.0.0 Sequence Number

8

#### 2.5.5.5.0.0.0.0 Type

🔹 UI Update

#### 2.5.5.6.0.0.0.0 Is Synchronous

✅ Yes

#### 2.5.5.7.0.0.0.0 Return Message



#### 2.5.5.8.0.0.0.0 Has Return

❌ No

#### 2.5.5.9.0.0.0.0 Is Activation

❌ No

#### 2.5.5.10.0.0.0.0 Technical Details

##### 2.5.5.10.1.0.0.0 Protocol

DOM Render

##### 2.5.5.10.2.0.0.0 Method

OWL component re-render

##### 2.5.5.10.3.0.0.0 Parameters

*No items available*

##### 2.5.5.10.4.0.0.0 Authentication

N/A

##### 2.5.5.10.5.0.0.0 Error Handling

N/A

##### 2.5.5.10.6.0.0.0 Performance

###### 2.5.5.10.6.1.0.0 Latency

<100ms

## 2.6.0.0.0.0.0.0 Notes

### 2.6.1.0.0.0.0.0 Content

#### 2.6.1.1.0.0.0.0 Content

Implementation Detail: The audit trail is enabled by inheriting the `mail.thread` mixin in the Python model definition (e.g., `_inherit = ['mail.thread']`) and adding the `tracking=True` attribute to specific fields (e.g., `amount_total = fields.Monetary(tracking=True)`). This is a configuration-driven approach using the Odoo framework.

#### 2.6.1.2.0.0.0.0 Position

bottom-left

#### 2.6.1.3.0.0.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.1.4.0.0.0.0 Sequence Number

3

### 2.6.2.0.0.0.0.0 Content

#### 2.6.2.1.0.0.0.0 Content

Compliance Requirement (REQ-DAT-008): The creation of the `mail.message` (audit log) and the update to `account.move` (invoice data) occur within the same atomic database transaction. This guarantees that a data change can never be committed without its corresponding audit log, ensuring immutability and consistency.

#### 2.6.2.2.0.0.0.0 Position

bottom-right

#### 2.6.2.3.0.0.0.0 Participant Id

temp-postgresql-db

#### 2.6.2.4.0.0.0.0 Sequence Number

4

## 2.7.0.0.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | Access to view the audit logs (the `mail.message` ... |
| Performance Targets | The overhead of tracking changes is minimal for si... |
| Error Handling Strategy | The primary error handling mechanism is the atomic... |
| Testing Considerations | 1. Create an E2E test where a test user modifies a... |
| Monitoring Requirements | No specific monitoring is required for this standa... |
| Deployment Considerations | This feature is enabled through code-level model d... |

