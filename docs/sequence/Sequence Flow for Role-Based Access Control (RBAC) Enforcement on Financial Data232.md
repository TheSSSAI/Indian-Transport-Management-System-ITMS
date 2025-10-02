# 1 Overview

## 1.1 Diagram Id

SEQ-SC-009

## 1.2 Name

Role-Based Access Control (RBAC) Enforcement on Financial Data

## 1.3 Description

A sequence demonstrating how the system's security model prevents unauthorized access. A user with a 'Driver' role attempts to view a financial report and is explicitly denied access by Odoo's security layer based on their assigned role.

## 1.4 Type

🔹 SecurityFlow

## 1.5 Purpose

To ensure data confidentiality and enforce the principle of least privilege by strictly controlling access to sensitive data and system features based on a user's assigned role.

## 1.6 Complexity

Medium

## 1.7 Priority

🚨 Critical

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- A user authenticated with the 'Driver' role logs in.
- The user attempts to access a protected resource, such as the URL for a financial report.
- Odoo's access control layer intercepts the incoming request.
- It checks the user's security groups (linked to the 'Driver' role) against the Access Control List (ACL) defined for the target data model (e.g., `account.move`).
- The check fails because the 'Driver' security group lacks 'read' permissions for this model.
- The system raises an 'Access Denied' exception, preventing the data from being fetched and rendered.

## 1.11 Triggers

- Any user attempts to perform an action (read, write, create, delete) or access data.

## 1.12 Outcomes

- Unauthorized access to sensitive financial data is successfully prevented.
- The system's data integrity and confidentiality are maintained as per security requirements.

## 1.13 Business Rules

- REQ-FNC-001: A user assigned the 'Driver' role shall only be able to view trips assigned to them and shall not be able to view company financial data.
- Authorization shall be strictly enforced using Odoo's model-level permissions (`ir.model.access.csv`) and row-level security (`ir.rule`).

## 1.14 Error Scenarios

- A misconfiguration in the security rules (e.g., an overly permissive `ir.rule`) accidentally grants unintended access.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-IMP-SC-009

## 2.2 Name

Implementation: RBAC Enforcement for Financial Data Access

## 2.3 Description

A detailed technical sequence demonstrating Odoo's security model enforcing the principle of least privilege. An authenticated user with the 'Driver' role attempts to access a financial report. The request is intercepted by Odoo's security layer, which evaluates the user's security groups against the Access Control Lists (ACLs) for the 'account.move' model. The check fails as the driver's group lacks read permissions, resulting in an 'AccessError' exception and an HTTP 403 response, effectively preventing unauthorized data access before any database query is attempted.

## 2.4 Participants

### 2.4.1 External Actor

#### 2.4.1.1 Repository Id

USER_CLIENT

#### 2.4.1.2 Display Name

User Client (Browser)

#### 2.4.1.3 Type

🔹 External Actor

#### 2.4.1.4 Technology

Web Browser (Chrome, Safari)

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #E6E6E6 |
| Stereotype | User |

### 2.4.2.0 Application Logic

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

Odoo Web Layer (Controller)

#### 2.4.2.3 Type

🔹 Application Logic

#### 2.4.2.4 Technology

Odoo 18, Python 3.11

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #C9DAF8 |
| Stereotype | Controller |

### 2.4.3.0 Security Framework

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

Odoo Security Layer

#### 2.4.3.3 Type

🔹 Security Framework

#### 2.4.3.4 Technology

Odoo 18 ORM (ir.model.access, ir.rule)

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #F4CCCC |
| Stereotype | Security |

### 2.4.4.0 Data Access

#### 2.4.4.1 Repository Id

REPO-TMS-CORE

#### 2.4.4.2 Display Name

Odoo ORM (Data Access)

#### 2.4.4.3 Type

🔹 Data Access

#### 2.4.4.4 Technology

Odoo 18 ORM

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #D9EAD3 |
| Stereotype | ORM |

## 2.5.0.0 Interactions

### 2.5.1.0 Request

#### 2.5.1.1 Source Id

USER_CLIENT

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

1. GET /web/action/tms.financial_report_action

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Request

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message

8. HTTP/1.1 403 Forbidden

#### 2.5.1.8 Has Return

✅ Yes

#### 2.5.1.9 Is Activation

❌ No

#### 2.5.1.10 Technical Details

##### 2.5.1.10.1 Protocol

HTTP/1.1

##### 2.5.1.10.2 Method

GET

##### 2.5.1.10.3 Parameters

| Property | Value |
|----------|-------|
| Headers | {'Cookie': 'session_id=...'} |

##### 2.5.1.10.4 Authentication

Odoo Session Cookie (session_id) for user authentication.

##### 2.5.1.10.5 Error Handling

Receives and renders a standard 'Access Denied' page.

##### 2.5.1.10.6 Performance

###### 2.5.1.10.6.1 Sla

User feedback (<200ms)

### 2.5.2.0.0.0 Internal Call

#### 2.5.2.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.2.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.2.3.0.0 Message

2. Pre-fetch check: Controller invokes security check before accessing data.

#### 2.5.2.4.0.0 Sequence Number

2

#### 2.5.2.5.0.0 Type

🔹 Internal Call

#### 2.5.2.6.0.0 Is Synchronous

✅ Yes

#### 2.5.2.7.0.0 Return Message

7. Propagate AccessError exception

#### 2.5.2.8.0.0 Has Return

✅ Yes

#### 2.5.2.9.0.0 Is Activation

✅ Yes

#### 2.5.2.10.0.0 Technical Details

##### 2.5.2.10.1.0 Protocol

Internal Method Call

##### 2.5.2.10.2.0 Method

self.env['account.move'].check_access_rights('read')

##### 2.5.2.10.3.0 Parameters

| Property | Value |
|----------|-------|
| Operation | 'read' |
| Raise Exception | True (default) |

##### 2.5.2.10.4.0 Authentication

Internal user context (self.env.user) is used.

##### 2.5.2.10.5.0 Error Handling

Catches the AccessError from the Security Layer and translates it into an HTTP 403 response.

##### 2.5.2.10.6.0 Performance

###### 2.5.2.10.6.1 Sla

Internal processing (<150ms)

#### 2.5.2.11.0.0 Nested Interactions

- {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '3. Security Layer receives request to check model-level access.', 'sequenceNumber': 3, 'type': 'Security Check', 'isSynchronous': True, 'returnMessage': "6. raise AccessError('...you are not allowed to access this document.')", 'hasReturn': True, 'isActivation': True, 'technicalDetails': {'protocol': 'Internal Method Call', 'method': '_check_model_access(model_name, mode)', 'parameters': {'model_name': "'account.move'", 'mode': "'read'"}, 'authentication': "Operates on the authenticated user's ID and groups from the environment context.", 'errorHandling': 'If checks fail, raises an `odoo.exceptions.AccessError`.', 'performance': {'sla': 'Permission checks must be sub-10ms, typically cached.'}}, 'nestedInteractions': [{'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': "4. Load user's security groups from context.", 'sequenceNumber': 4, 'type': 'Data Lookup', 'isSynchronous': True, 'returnMessage': "Returns user's groups (e.g., ['tms_management.group_tms_driver'])", 'hasReturn': True, 'isActivation': False, 'technicalDetails': {'protocol': 'Internal Property Access', 'method': 'self.env.user.groups_id', 'parameters': {}, 'authentication': 'N/A', 'errorHandling': 'N/A', 'performance': {'sla': 'Cached in memory.'}}}, {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '5. Evaluate ACLs defined in `ir.model.access.csv`.', 'sequenceNumber': 5, 'type': 'Policy Evaluation', 'isSynchronous': True, 'returnMessage': "Evaluation result: `perm_read` is FALSE for user's group.", 'hasReturn': True, 'isActivation': False, 'technicalDetails': {'protocol': 'Internal Logic', 'method': 'Searches `ir_model_access` table.', 'parameters': {'model_name': "'account.move'", 'group_id': "IN (user's group IDs)", 'perm_read': 'True'}, 'authentication': 'N/A', 'errorHandling': 'If no matching rule is found, access defaults to denied.', 'performance': {'sla': 'Cached in memory per session.'}}}]}

## 2.6.0.0.0.0 Notes

### 2.6.1.0.0.0 Content

#### 2.6.1.1.0.0 Content

Defense in Depth: The security check is performed at the application logic layer BEFORE any attempt is made to invoke the ORM for data retrieval.

#### 2.6.1.2.0.0 Position

top-right

#### 2.6.1.3.0.0 Participant Id

*Not specified*

#### 2.6.1.4.0.0 Sequence Number

2

### 2.6.2.0.0.0 Content

#### 2.6.2.1.0.0 Content

Zero Trust Principle: The system does not trust the authenticated user's intent. Every operation on a protected resource requires explicit permission verification against defined ACLs.

#### 2.6.2.2.0.0 Position

bottom-left

#### 2.6.2.3.0.0 Participant Id

*Not specified*

#### 2.6.2.4.0.0 Sequence Number

3

### 2.6.3.0.0.0 Content

#### 2.6.3.1.0.0 Content

Because the model-level access check (`ir.model.access`) fails, the system does not proceed to evaluate more granular row-level security rules (`ir.rule`). This is a performance optimization.

#### 2.6.3.2.0.0 Position

middle-right

#### 2.6.3.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.3.4.0.0 Sequence Number

5

### 2.6.4.0.0.0 Content

#### 2.6.4.1.0.0 Content

The ORM and the underlying PostgreSQL database are never touched during this interaction, preventing any potential for data leakage through low-level errors.

#### 2.6.4.2.0.0 Position

bottom-right

#### 2.6.4.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.4.4.0.0 Sequence Number

6

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | ACLs in `ir.model.access.csv` must be defined with... |
| Performance Targets | Security checks are on the critical path of most r... |
| Error Handling Strategy | The `odoo.exceptions.AccessError` is the standard ... |
| Testing Considerations | A comprehensive test suite must be created to vali... |
| Monitoring Requirements | All `AccessError` events must be logged with a `WA... |
| Deployment Considerations | Security definitions (`ir.model.access.csv`, `ir.r... |

