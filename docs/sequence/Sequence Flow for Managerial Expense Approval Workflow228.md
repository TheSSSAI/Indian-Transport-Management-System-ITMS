# 1 Overview

## 1.1 Diagram Id

SEQ-BP-005

## 1.2 Name

Managerial Expense Approval Workflow

## 1.3 Description

A Dispatch Manager or Finance Officer reviews a driver's submitted expense. They can view the expense details and attached receipt to either approve it for financial inclusion or reject it with a mandatory reason.

## 1.4 Type

🔹 BusinessProcess

## 1.5 Purpose

To ensure all trip-related expenses are valid, justified, and accurately accounted for before they are included in financial calculations like trip profitability.

## 1.6 Complexity

Low

## 1.7 Priority

🔴 High

## 1.8 Frequency

Daily

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- An approver (Dispatch Manager or Finance Officer) views a list of expenses with 'Submitted' status.
- The approver selects an expense to review its details, including the uploaded receipt image.
- **Approve Path:** The approver clicks 'Approve'. The expense record's status is updated to 'Approved'.
- **Reject Path:** The approver clicks 'Reject', which prompts for a mandatory reason for rejection. After submission, the status is updated to 'Rejected'.
- The system triggers a notification to the submitting driver informing them of the decision.

## 1.11 Triggers

- An expense record enters the 'Submitted' state after a driver submits it.

## 1.12 Outcomes

- The expense is marked as 'Approved' and is correctly included in the trip's profitability calculation.
- The expense is marked as 'Rejected' with a documented reason and is excluded from all financial calculations.

## 1.13 Business Rules

- Only expenses in the 'Approved' state shall be included in the trip's profitability calculation.
- Rejected expenses must include a reason for rejection, which is logged for audit purposes.

## 1.14 Error Scenarios

- An approver attempts to process an expense that has already been approved or rejected by another user.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-BP-005

## 2.2 Name

Implementation: Managerial Expense Approval Workflow

## 2.3 Description

Technical sequence for a user with approval rights (Dispatch Manager/Finance Officer) to review and process a driver-submitted expense within the Odoo framework. This diagram details the interactions between the UI, controller, and ORM layers, focusing on state management, business rule validation, security checks, and audit trail generation for both the approval and rejection paths.

## 2.4 Participants

### 2.4.1 External Actor

#### 2.4.1.1 Repository Id

*Not specified*

#### 2.4.1.2 Display Name

Approver (User)

#### 2.4.1.3 Type

🔹 External Actor

#### 2.4.1.4 Technology

Web Browser

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #999999 |
| Stereotype | User |

### 2.4.2.0 Presentation Layer

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

Odoo Web UI

#### 2.4.2.3 Type

🔹 Presentation Layer

#### 2.4.2.4 Technology

Odoo 18 Views, OWL 2.0

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | boundary |
| Color | #4CAF50 |
| Stereotype | UI |

### 2.4.3.0 Application Layer

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

Odoo Controller

#### 2.4.3.3 Type

🔹 Application Layer

#### 2.4.3.4 Technology

Odoo 18 HTTP Controller

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | control |
| Color | #FFC107 |
| Stereotype | Controller |

### 2.4.4.0 Business Logic Layer

#### 2.4.4.1 Repository Id

REPO-TMS-CORE

#### 2.4.4.2 Display Name

Odoo ORM (tms.expense)

#### 2.4.4.3 Type

🔹 Business Logic Layer

#### 2.4.4.4 Technology

Odoo 18 ORM, Python 3.11

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | entity |
| Color | #2196F3 |
| Stereotype | Model |

### 2.4.5.0 Utility Service

#### 2.4.5.1 Repository Id

REPO-TMS-CORE

#### 2.4.5.2 Display Name

Odoo Notification Service

#### 2.4.5.3 Type

🔹 Utility Service

#### 2.4.5.4 Technology

Odoo Mail Module (mail.thread)

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #E91E63 |
| Stereotype | Service |

## 2.5.0.0 Interactions

### 2.5.1.0 Request

#### 2.5.1.1 Source Id

*Not specified*

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

1. Navigates to Expense Approval view

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Request

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message

Displays list of expenses with 'Submitted' status

#### 2.5.1.8 Has Return

✅ Yes

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP |
| Method | GET /web#model=tms.expense&view_type=list&domain=[... |
| Parameters | Odoo view rendering request |
| Authentication | Odoo Session Cookie |
| Error Handling | Standard Odoo view loading error handling. |
| Performance | LCP < 3s as per REQ-NFR-001 |

#### 2.5.1.11 Nested Interactions

- {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '1.1. Request expense data', 'sequenceNumber': 1.1, 'type': 'Internal Call', 'isSynchronous': True, 'returnMessage': 'List of expense records', 'hasReturn': True, 'technicalDetails': {'protocol': 'Internal Method Call', 'method': "ORM.search_read([('state', '=', 'submitted')])", 'parameters': 'Domain, Fields', 'authentication': 'Odoo User Context', 'errorHandling': 'Odoo ORM exceptions (e.g., PSQLException).', 'performance': 'DB query execution < 200ms.'}}

### 2.5.2.0 Request

#### 2.5.2.1 Source Id

*Not specified*

#### 2.5.2.2 Target Id

REPO-TMS-CORE

#### 2.5.2.3 Message

2. Selects an expense to review details

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 Request

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

Displays expense form view with details and receipt

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP |
| Method | GET /web#model=tms.expense&id=<expense_id>&view_ty... |
| Parameters | Expense record ID |
| Authentication | Odoo Session Cookie |
| Error Handling | Handles invalid ID, displays 'Record does not exis... |
| Performance | Page load < 2s. |

### 2.5.3.0 Request

#### 2.5.3.1 Source Id

*Not specified*

#### 2.5.3.2 Target Id

REPO-TMS-CORE

#### 2.5.3.3 Message

3a. Clicks 'Approve' button

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 Request

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message

UI refreshes to show 'Approved' status

#### 2.5.3.8 Has Return

✅ Yes

#### 2.5.3.9 Is Activation

✅ Yes

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP |
| Method | POST /tms/expense/<id>/approve |
| Parameters | Expense record ID |
| Authentication | Odoo Session Cookie, CSRF Token |
| Error Handling | Frontend displays error notification on failure (e... |
| Performance | Action completion < 500ms |

#### 2.5.3.11 Nested Interactions

- {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '3.1. Invoke approval business logic', 'sequenceNumber': 3.1, 'type': 'Internal Call', 'isSynchronous': True, 'returnMessage': 'Success/Failure', 'hasReturn': True, 'technicalDetails': {'protocol': 'Internal Method Call', 'method': 'ORM.action_approve()', 'parameters': 'self (expense recordset)', 'authentication': 'Odoo User Context', 'errorHandling': 'Raises UserError for validation failures, AccessError for permission issues.', 'performance': 'Method execution < 400ms'}, 'nestedInteractions': [{'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': "3.1.1. Security & State Check: Verify user role and state=='submitted'", 'sequenceNumber': 3.11, 'type': 'Validation', 'isSynchronous': True, 'returnMessage': 'Validation Pass/Fail', 'hasReturn': True, 'technicalDetails': {'protocol': 'Internal Logic', 'method': "self.env.user.has_group('...') and self.state == 'submitted'", 'parameters': 'None', 'authentication': 'N/A', 'errorHandling': "Raise AccessError if role check fails. Raise UserError if state is not 'submitted' (concurrent update).", 'performance': 'Negligible'}}, {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': "3.1.2. Update record state to 'Approved'", 'sequenceNumber': 3.12, 'type': 'Database Write', 'isSynchronous': True, 'returnMessage': 'None', 'hasReturn': False, 'technicalDetails': {'protocol': 'Internal ORM Call', 'method': "self.write({'state': 'approved'})", 'parameters': 'Dictionary of values to update.', 'authentication': 'N/A', 'errorHandling': 'Database transaction management by Odoo ORM.', 'performance': 'DB write operation < 100ms'}}, {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '3.1.3. Post notification to driver', 'sequenceNumber': 3.13, 'type': 'Internal Call', 'isSynchronous': False, 'returnMessage': 'None', 'hasReturn': False, 'technicalDetails': {'protocol': 'Internal Method Call', 'method': "self.message_post(body='...', partner_ids=[...])", 'parameters': 'Message body, recipient partner IDs.', 'authentication': 'N/A', 'errorHandling': 'Logged by Odoo mail queue if delivery fails.', 'performance': 'Queued immediately (< 10ms).'}}]}

### 2.5.4.0 Request

#### 2.5.4.1 Source Id

*Not specified*

#### 2.5.4.2 Target Id

REPO-TMS-CORE

#### 2.5.4.3 Message

3b. Clicks 'Reject', enters mandatory reason, and submits

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 Request

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message

UI refreshes to show 'Rejected' status

#### 2.5.4.8 Has Return

✅ Yes

#### 2.5.4.9 Is Activation

✅ Yes

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP |
| Method | POST /tms/expense/<id>/reject |
| Parameters | JSON Payload: { 'reason': '...' } |
| Authentication | Odoo Session Cookie, CSRF Token |
| Error Handling | Frontend displays error notification on failure (e... |
| Performance | Action completion < 500ms |

#### 2.5.4.11 Nested Interactions

- {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '4.1. Invoke rejection business logic', 'sequenceNumber': 4.1, 'type': 'Internal Call', 'isSynchronous': True, 'returnMessage': 'Success/Failure', 'hasReturn': True, 'technicalDetails': {'protocol': 'Internal Method Call', 'method': 'ORM.action_reject(reason)', 'parameters': 'self (expense recordset), reason (string)', 'authentication': 'Odoo User Context', 'errorHandling': 'Raises UserError for validation failures, AccessError for permission issues.', 'performance': 'Method execution < 400ms'}, 'nestedInteractions': [{'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '4.1.1. Security, State, & Reason Check: Verify role, state, and non-empty reason', 'sequenceNumber': 4.11, 'type': 'Validation', 'isSynchronous': True, 'returnMessage': 'Validation Pass/Fail', 'hasReturn': True, 'technicalDetails': {'protocol': 'Internal Logic', 'method': 'if not reason: raise UserError(...)', 'parameters': 'None', 'authentication': 'N/A', 'errorHandling': 'Raise UserError if reason is empty.', 'performance': 'Negligible'}}, {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': "4.1.2. Update record state to 'Rejected'", 'sequenceNumber': 4.12, 'type': 'Database Write', 'isSynchronous': True, 'returnMessage': 'None', 'hasReturn': False, 'technicalDetails': {'protocol': 'Internal ORM Call', 'method': "self.write({'state': 'rejected'})", 'parameters': 'Dictionary of values to update.', 'authentication': 'N/A', 'errorHandling': 'Database transaction management by Odoo ORM.', 'performance': 'DB write operation < 100ms'}}, {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': '4.1.3. Post notification and rejection reason to driver', 'sequenceNumber': 4.13, 'type': 'Internal Call', 'isSynchronous': False, 'returnMessage': 'None', 'hasReturn': False, 'technicalDetails': {'protocol': 'Internal Method Call', 'method': "self.message_post(body=f'Rejected: {reason}', ...)", 'parameters': 'Message body including reason, recipient partner IDs.', 'authentication': 'N/A', 'errorHandling': 'Logged by Odoo mail queue if delivery fails.', 'performance': 'Queued immediately (< 10ms).'}}]}

## 2.6.0.0 Notes

### 2.6.1.0 Content

#### 2.6.1.1 Content

Business Rule: Only expenses with state='approved' are included in trip profitability calculations. This logic is handled by the profitability reporting/calculation service, which filters expenses based on this state.

#### 2.6.1.2 Position

bottom

#### 2.6.1.3 Participant Id

REPO-TMS-CORE

#### 2.6.1.4 Sequence Number

*Not specified*

### 2.6.2.0 Content

#### 2.6.2.1 Content

Audit Trail: All state changes and posted messages (including rejection reasons) are automatically logged in the expense record's chatter by Odoo's 'mail.thread' mixin, satisfying audit requirements.

#### 2.6.2.2 Position

bottom

#### 2.6.2.3 Participant Id

REPO-TMS-CORE

#### 2.6.2.4 Sequence Number

*Not specified*

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | RBAC is critical. The `action_approve` and `action... |
| Performance Targets | The entire approval/rejection transaction, from us... |
| Error Handling Strategy | The primary error to handle is concurrent modifica... |
| Testing Considerations | Unit tests for the `tms.expense` model must cover:... |
| Monitoring Requirements | Create Prometheus metrics for `tms_expense_approva... |
| Deployment Considerations | Ensure the security groups ('tms.group_dispatch_ma... |

