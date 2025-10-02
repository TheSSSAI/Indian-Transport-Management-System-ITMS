# 1 Overview

## 1.1 Diagram Id

SEQ-BP-017

## 1.2 Name

Dispatch Manager Resolves an 'On Hold' Trip

## 1.3 Description

A Dispatch Manager reviews a trip that is in the 'On Hold' status, investigates the reason, and takes action to resolve the issue, returning the trip to 'In-Transit' status.

## 1.4 Type

🔹 BusinessProcess

## 1.5 Purpose

To manage operational disruptions by providing a formal process for managers to resolve issues and resume paused trips.

## 1.6 Complexity

Medium

## 1.7 Priority

🔴 High

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- Manager is notified of an 'On Hold' trip via the dashboard alert.
- Manager opens the trip record and reviews the event log to understand the reason.
- After taking corrective action offline (e.g., contacting the driver), the manager clicks the 'Resume Trip' button.
- The system prompts for a mandatory resolution comment.
- Manager enters the comment and confirms.
- REPO-TMS-CORE updates the trip status from 'On Hold' back to 'In-Transit'.
- The resolution comment is added to the trip's event history.

## 1.11 Triggers

- A trip is in 'On Hold' status requiring managerial review.

## 1.12 Outcomes

- The operational issue is resolved and documented.
- The trip continues its journey towards delivery.

## 1.13 Business Rules

- REQ-FNC-002: A Dispatch Manager can change the status of an 'On Hold' trip.
- REQ-FNC-002: Changing status from 'On Hold' requires a mandatory comment.

## 1.14 Error Scenarios

- A user without the 'Dispatch Manager' role attempts to resume the trip and is denied.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-BP-017

## 2.2 Name

Implementation: Dispatch Manager Resolves 'On Hold' Trip

## 2.3 Description

Technical sequence for a user with the 'Dispatch Manager' role resolving an operational disruption. The sequence covers the user interaction, business rule validation, atomic state transition from 'On Hold' to 'In-Transit', and the creation of an immutable audit record for the resolution.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

User-Actor

#### 2.4.1.2 Display Name

Dispatch Manager

#### 2.4.1.3 Type

🔹 Actor

#### 2.4.1.4 Technology

Human User (Web Browser)

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #E6E6E6 |
| Stereotype | User |

### 2.4.2.0 UI

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

Odoo Presentation Layer (UI)

#### 2.4.2.3 Type

🔹 UI

#### 2.4.2.4 Technology

Odoo 18 Views (XML), OWL 2.0

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | rectangle |
| Color | #C8E6C9 |
| Stereotype | Odoo UI |

### 2.4.3.0 BusinessLogic

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

Odoo Business Logic Layer

#### 2.4.3.3 Type

🔹 BusinessLogic

#### 2.4.3.4 Technology

Odoo 18, Python 3.11

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | rectangle |
| Color | #FFD54F |
| Stereotype | Odoo Controller/Model |

### 2.4.4.0 DataAccess

#### 2.4.4.1 Repository Id

REPO-TMS-CORE

#### 2.4.4.2 Display Name

Odoo Data Access Layer (ORM/DB)

#### 2.4.4.3 Type

🔹 DataAccess

#### 2.4.4.4 Technology

Odoo 18 ORM, PostgreSQL 16

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #B3E5FC |
| Stereotype | PostgreSQL |

## 2.5.0.0 Interactions

### 2.5.1.0 User Interaction

#### 2.5.1.1 Source Id

User-Actor

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

1. User, having identified an 'On Hold' trip from the dashboard, clicks the 'Resume Trip' button on the Trip form view.

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

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | UI Event (Click) |
| Parameters | trip.id |
| Authentication | User Session Cookie |
| Error Handling | N/A |
| Performance | Immediate UI response |

### 2.5.2.0 UI Rendering

#### 2.5.2.1 Source Id

REPO-TMS-CORE

#### 2.5.2.2 Target Id

REPO-TMS-CORE

#### 2.5.2.3 Message

2. Renders and displays an OWL-based wizard/modal, prompting for a mandatory 'Resolution Comment'.

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 UI Rendering

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message



#### 2.5.2.8 Has Return

❌ No

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal JS Call |
| Method | new Dialog(...).open() |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | JS errors logged to console. |
| Performance | < 100ms |

### 2.5.3.0 User Interaction

#### 2.5.3.1 Source Id

User-Actor

#### 2.5.3.2 Target Id

REPO-TMS-CORE

#### 2.5.3.3 Message

3. Enters resolution comment and clicks 'Confirm'.

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 User Interaction

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message



#### 2.5.3.8 Has Return

❌ No

#### 2.5.3.9 Is Activation

❌ No

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | UI Event (Click) |
| Parameters | resolution_comment: string |
| Authentication | User Session Cookie |
| Error Handling | N/A |
| Performance | Immediate UI response |

### 2.5.4.0 RPC Call

#### 2.5.4.1 Source Id

REPO-TMS-CORE

#### 2.5.4.2 Target Id

REPO-TMS-CORE

#### 2.5.4.3 Message

4. Executes Odoo model method `action_resume_trip` via JSON-RPC call.

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 RPC Call

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message

13. Odoo Action dictionary for UI refresh or success/error notification.

#### 2.5.4.8 Has Return

✅ Yes

#### 2.5.4.9 Is Activation

✅ Yes

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | JSON-RPC |
| Method | call_kw('tms.trip', 'action_resume_trip', ...) |
| Parameters | trip_id: int, resolution_comment: string |
| Authentication | User Session ID |
| Error Handling | Handles Odoo `UserError`, `ValidationError`, `Acce... |
| Performance | Target < 500ms for entire backend process. |

#### 2.5.4.11 Nested Interactions

##### 2.5.4.11.1 Security Validation

###### 2.5.4.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.4.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.4.11.1.3 Message

5. [Security Checkpoint] Verify user role.

###### 2.5.4.11.1.4 Sequence Number

5

###### 2.5.4.11.1.5 Type

🔹 Security Validation

###### 2.5.4.11.1.6 Is Synchronous

✅ Yes

###### 2.5.4.11.1.7 Return Message

Success or AccessError exception.

###### 2.5.4.11.1.8 Has Return

✅ Yes

###### 2.5.4.11.1.9 Is Activation

❌ No

###### 2.5.4.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Python Call |
| Method | self.env.user.has_group('tms.group_dispatch_manage... |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | Raises `odoo.exceptions.AccessError` if check fail... |
| Performance | < 10ms |

##### 2.5.4.11.2.0 Data Validation

###### 2.5.4.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.4.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.4.11.2.3 Message

6. [Business Rule] Validate mandatory comment.

###### 2.5.4.11.2.4 Sequence Number

6

###### 2.5.4.11.2.5 Type

🔹 Data Validation

###### 2.5.4.11.2.6 Is Synchronous

✅ Yes

###### 2.5.4.11.2.7 Return Message

Success or ValidationError exception.

###### 2.5.4.11.2.8 Has Return

✅ Yes

###### 2.5.4.11.2.9 Is Activation

❌ No

###### 2.5.4.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Python Call |
| Method | if not resolution_comment: raise ValidationError(.... |
| Parameters | resolution_comment: string |
| Authentication | N/A |
| Error Handling | Raises `odoo.exceptions.ValidationError` as per RE... |
| Performance | < 1ms |

##### 2.5.4.11.3.0 Database Operation

###### 2.5.4.11.3.1 Source Id

REPO-TMS-CORE

###### 2.5.4.11.3.2 Target Id

REPO-TMS-CORE

###### 2.5.4.11.3.3 Message

7. Initiate database transaction.

###### 2.5.4.11.3.4 Sequence Number

7

###### 2.5.4.11.3.5 Type

🔹 Database Operation

###### 2.5.4.11.3.6 Is Synchronous

✅ Yes

###### 2.5.4.11.3.7 Return Message



###### 2.5.4.11.3.8 Has Return

❌ No

###### 2.5.4.11.3.9 Is Activation

✅ Yes

###### 2.5.4.11.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM Transaction |
| Method | @api.model |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | Any subsequent failure will trigger a transaction ... |
| Performance | N/A |

##### 2.5.4.11.4.0 Data Write

###### 2.5.4.11.4.1 Source Id

REPO-TMS-CORE

###### 2.5.4.11.4.2 Target Id

REPO-TMS-CORE

###### 2.5.4.11.4.3 Message

8. Update trip status via ORM.

###### 2.5.4.11.4.4 Sequence Number

8

###### 2.5.4.11.4.5 Type

🔹 Data Write

###### 2.5.4.11.4.6 Is Synchronous

✅ Yes

###### 2.5.4.11.4.7 Return Message

10. DB operation successful.

###### 2.5.4.11.4.8 Has Return

✅ Yes

###### 2.5.4.11.4.9 Is Activation

❌ No

###### 2.5.4.11.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM |
| Method | trip_record.write({'state': 'in_transit'}) |
| Parameters | Dictionary of fields to update. |
| Authentication | N/A |
| Error Handling | Database errors (e.g., lock timeout) will raise an... |
| Performance | < 50ms |

##### 2.5.4.11.5.0 Audit Logging

###### 2.5.4.11.5.1 Source Id

REPO-TMS-CORE

###### 2.5.4.11.5.2 Target Id

REPO-TMS-CORE

###### 2.5.4.11.5.3 Message

9. [Audit Trail] Post resolution comment to trip's chatter.

###### 2.5.4.11.5.4 Sequence Number

9

###### 2.5.4.11.5.5 Type

🔹 Audit Logging

###### 2.5.4.11.5.6 Is Synchronous

✅ Yes

###### 2.5.4.11.5.7 Return Message

11. DB operation successful.

###### 2.5.4.11.5.8 Has Return

✅ Yes

###### 2.5.4.11.5.9 Is Activation

❌ No

###### 2.5.4.11.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM |
| Method | trip_record.message_post(body=resolution_comment, ... |
| Parameters | body: string, subtype_id: int |
| Authentication | N/A |
| Error Handling | Database errors will raise an exception and trigge... |
| Performance | < 100ms (involves creating multiple related record... |

##### 2.5.4.11.6.0 Database Operation

###### 2.5.4.11.6.1 Source Id

REPO-TMS-CORE

###### 2.5.4.11.6.2 Target Id

REPO-TMS-CORE

###### 2.5.4.11.6.3 Message

12. Commit transaction.

###### 2.5.4.11.6.4 Sequence Number

12

###### 2.5.4.11.6.5 Type

🔹 Database Operation

###### 2.5.4.11.6.6 Is Synchronous

✅ Yes

###### 2.5.4.11.6.7 Return Message



###### 2.5.4.11.6.8 Has Return

❌ No

###### 2.5.4.11.6.9 Is Activation

❌ No

###### 2.5.4.11.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM Transaction |
| Method | Automatic on successful method execution |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | < 20ms |

### 2.5.5.0.0.0 UI Update

#### 2.5.5.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.5.2.0.0 Target Id

User-Actor

#### 2.5.5.3.0.0 Message

14. UI closes the modal and refreshes the trip form, displaying the new 'In-Transit' status and the new comment in the history.

#### 2.5.5.4.0.0 Sequence Number

14

#### 2.5.5.5.0.0 Type

🔹 UI Update

#### 2.5.5.6.0.0 Is Synchronous

❌ No

#### 2.5.5.7.0.0 Return Message



#### 2.5.5.8.0.0 Has Return

❌ No

#### 2.5.5.9.0.0 Is Activation

❌ No

#### 2.5.5.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | DOM Update |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | < 200ms |

## 2.6.0.0.0.0 Notes

### 2.6.1.0.0.0 Content

#### 2.6.1.1.0.0 Content

This entire business process (steps 5-12) MUST be executed within a single, atomic database transaction. A failure at any point must roll back all changes, leaving the trip in the 'On Hold' state.

#### 2.6.1.2.0.0 Position

bottom

#### 2.6.1.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.1.4.0.0 Sequence Number

7

### 2.6.2.0.0.0 Content

#### 2.6.2.1.0.0 Content

The check `has_group` is critical for enforcing the separation of duties outlined in REQ-FNC-001 and REQ-FNC-002.

#### 2.6.2.2.0.0 Position

right

#### 2.6.2.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.2.4.0.0 Sequence Number

5

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The `action_resume_trip` method on the `tms.trip` ... |
| Performance Targets | The end-to-end backend processing time for this op... |
| Error Handling Strategy | 1. **Access Denied:** If the security check fails,... |
| Testing Considerations | - **Happy Path:** A test case must verify that a D... |
| Monitoring Requirements | Log an INFO level message with `tripId` and `userI... |
| Deployment Considerations | This feature modifies a core business model. The c... |

