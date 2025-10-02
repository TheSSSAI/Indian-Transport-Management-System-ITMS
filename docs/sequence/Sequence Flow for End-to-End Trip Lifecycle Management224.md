# 1 Overview

## 1.1 Diagram Id

SEQ-BP-001

## 1.2 Name

End-to-End Trip Lifecycle Management

## 1.3 Description

Orchestrates the entire business process of a trip from initial planning, through execution and delivery, to financial settlement and payment completion. This sequence enforces all state transitions as defined in business rule BR-004, ensuring a consistent and auditable workflow for every transport job.

## 1.4 Type

🔹 BusinessProcess

## 1.5 Purpose

To manage and track the complete lifecycle of a transport job, ensuring full operational and financial closure.

## 1.6 Complexity

High

## 1.7 Priority

🚨 Critical

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE
- REPO-DRV-UI

## 1.10 Key Interactions

- Dispatch Manager creates a 'Planned' trip in REPO-TMS-CORE.
- Trip record is updated to 'Assigned' with a validated vehicle and driver.
- Driver, via REPO-DRV-UI, starts the trip, triggering a status update to 'In-Transit'.
- Driver uploads Proof of Delivery (POD) via REPO-DRV-UI; system updates status to 'Delivered'.
- Dispatch Manager verifies POD and trip details, promoting status to 'Completed'.
- Finance Officer generates an invoice; system updates status to 'Invoiced'.
- Finance Officer records customer payment; system updates status to 'Paid'.

## 1.11 Triggers

- A customer places a new transport order, initiating trip creation.

## 1.12 Outcomes

- A trip is successfully executed, invoiced, and paid in full.
- All operational and financial data for the trip is accurately recorded.
- The final profitability for the trip is calculated and available for reporting.

## 1.13 Business Rules

- BR-004: Trip status lifecycle must follow the defined path: Planned -> Assigned -> In-Transit -> Delivered -> Completed -> Invoiced -> Paid.
- BR-006: A new trip cannot be saved without a valid Customer, Source, and Destination.
- BR-007: The specified trip weight shall not exceed the assigned vehicle's registered capacity.
- BR-010: An invoice can only be generated for a trip that is in the 'Completed' state.

## 1.14 Error Scenarios

- A trip is marked as 'Canceled' at any stage before 'Delivered'.
- A driver cannot be assigned to a trip due to an expired license, blocking the transition to 'Assigned'.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-BP-001

## 2.2 Name

Implementation: End-to-End Trip Lifecycle Management

## 2.3 Description

Provides a detailed technical specification for orchestrating the entire business process of a trip, from initial creation by a Dispatch Manager to final payment recording by a Finance Officer. This sequence diagram details the specific ORM method calls, business rule validations, state transitions, and user interactions required to implement the trip lifecycle as defined in business rule BR-004. It serves as a blueprint for developers to implement the state machine and associated logic within the Odoo framework.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

Actor_Dispatch_Manager

#### 2.4.1.2 Display Name

Dispatch Manager

#### 2.4.1.3 Type

🔹 Actor

#### 2.4.1.4 Technology

Human User

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #E6F3FF |
| Stereotype | User Role |

### 2.4.2.0 Actor

#### 2.4.2.1 Repository Id

Actor_Driver

#### 2.4.2.2 Display Name

Driver

#### 2.4.2.3 Type

🔹 Actor

#### 2.4.2.4 Technology

Human User

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #E6F3FF |
| Stereotype | User Role |

### 2.4.3.0 Actor

#### 2.4.3.1 Repository Id

Actor_Finance_Officer

#### 2.4.3.2 Display Name

Finance Officer

#### 2.4.3.3 Type

🔹 Actor

#### 2.4.3.4 Technology

Human User

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #E6F3FF |
| Stereotype | User Role |

### 2.4.4.0 UI Component

#### 2.4.4.1 Repository Id

REPO-DRV-UI

#### 2.4.4.2 Display Name

Driver Portal UI (OWL)

#### 2.4.4.3 Type

🔹 UI Component

#### 2.4.4.4 Technology

Odoo OWL 2.0, JavaScript

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #D1E8D1 |
| Stereotype | Frontend |

### 2.4.5.0 Business Logic

#### 2.4.5.1 Repository Id

REPO-TMS-CORE

#### 2.4.5.2 Display Name

TMS Core Business Logic

#### 2.4.5.3 Type

🔹 Business Logic

#### 2.4.5.4 Technology

Odoo 18, Python 3.11, PostgreSQL 16

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #FADBD8 |
| Stereotype | Backend |

## 2.5.0.0 Interactions

### 2.5.1.0 UserAction

#### 2.5.1.1 Source Id

Actor_Dispatch_Manager

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

1. createTrip(vals: dict)

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 UserAction

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message

Returns new trip record ID

#### 2.5.1.8 Has Return

✅ Yes

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | tms.trip.create(vals) |
| Parameters | vals dictionary containing { 'customer_id', 'sourc... |
| Authentication | Odoo Session Cookie with Dispatch Manager permissi... |
| Error Handling | Raises Odoo UserError if BR-006 validation fails. |
| Performance | p99 < 500ms |

#### 2.5.1.11 Nested Interactions

##### 2.5.1.11.1 Validation

###### 2.5.1.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.1.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.1.11.1.3 Message

1.1. Validate required fields per BR-006 (Customer, Source, Destination).

###### 2.5.1.11.1.4 Sequence Number

1.1

###### 2.5.1.11.1.5 Type

🔹 Validation

###### 2.5.1.11.1.6 Is Synchronous

✅ Yes

###### 2.5.1.11.1.7 Return Message



###### 2.5.1.11.1.8 Has Return

❌ No

###### 2.5.1.11.1.9 Is Activation

❌ No

###### 2.5.1.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | _validate_creation_data(vals) |
| Parameters | vals dictionary |
| Authentication | N/A |
| Error Handling | Throws ValidationError on failure. |
| Performance | p99 < 50ms |

##### 2.5.1.11.2.0 DatabaseUpdate

###### 2.5.1.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.1.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.1.11.2.3 Message

1.2. Create tms.trip record with state = 'Planned'.

###### 2.5.1.11.2.4 Sequence Number

1.2

###### 2.5.1.11.2.5 Type

🔹 DatabaseUpdate

###### 2.5.1.11.2.6 Is Synchronous

✅ Yes

###### 2.5.1.11.2.7 Return Message

new_trip_id

###### 2.5.1.11.2.8 Has Return

✅ Yes

###### 2.5.1.11.2.9 Is Activation

❌ No

###### 2.5.1.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL INSERT |
| Method | ORM create() |
| Parameters | SQL INSERT statement |
| Authentication | N/A |
| Error Handling | Database transaction rollback on failure. |
| Performance | p99 < 100ms |

##### 2.5.1.11.3.0 Audit

###### 2.5.1.11.3.1 Source Id

REPO-TMS-CORE

###### 2.5.1.11.3.2 Target Id

REPO-TMS-CORE

###### 2.5.1.11.3.3 Message

1.3. Create audit trail entry for 'Trip Created'.

###### 2.5.1.11.3.4 Sequence Number

1.3

###### 2.5.1.11.3.5 Type

🔹 Audit

###### 2.5.1.11.3.6 Is Synchronous

✅ Yes

###### 2.5.1.11.3.7 Return Message



###### 2.5.1.11.3.8 Has Return

❌ No

###### 2.5.1.11.3.9 Is Activation

❌ No

###### 2.5.1.11.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | mail.thread.message_post() |
| Parameters | body='Trip created', author_id=user.id |
| Authentication | N/A |
| Error Handling | Logged via standard Odoo logging. |
| Performance | p99 < 80ms |

### 2.5.2.0.0.0 UserAction

#### 2.5.2.1.0.0 Source Id

Actor_Dispatch_Manager

#### 2.5.2.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.2.3.0.0 Message

2. assignVehicleAndDriver(trip_id, vehicle_id, driver_id)

#### 2.5.2.4.0.0 Sequence Number

2

#### 2.5.2.5.0.0 Type

🔹 UserAction

#### 2.5.2.6.0.0 Is Synchronous

✅ Yes

#### 2.5.2.7.0.0 Return Message

Returns success status

#### 2.5.2.8.0.0 Has Return

✅ Yes

#### 2.5.2.9.0.0 Is Activation

❌ No

#### 2.5.2.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | tms.trip.write(vals) |
| Parameters | vals = { 'vehicle_id': vehicle_id, 'driver_id': dr... |
| Authentication | Odoo Session Cookie |
| Error Handling | Raises Odoo UserError if BR-003 or BR-007 validati... |
| Performance | p99 < 600ms |

#### 2.5.2.11.0.0 Nested Interactions

##### 2.5.2.11.1.0 Validation

###### 2.5.2.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.2.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.2.11.1.3 Message

2.1. Validate vehicle capacity against trip weight (BR-007).

###### 2.5.2.11.1.4 Sequence Number

2.1

###### 2.5.2.11.1.5 Type

🔹 Validation

###### 2.5.2.11.1.6 Is Synchronous

✅ Yes

###### 2.5.2.11.1.7 Return Message



###### 2.5.2.11.1.8 Has Return

❌ No

###### 2.5.2.11.1.9 Is Activation

❌ No

###### 2.5.2.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | _check_vehicle_capacity() |
| Parameters | trip.weight, vehicle.capacity |
| Authentication | N/A |
| Error Handling | Throws ValidationError on failure. |
| Performance | p99 < 50ms |

##### 2.5.2.11.2.0 Validation

###### 2.5.2.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.2.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.2.11.2.3 Message

2.2. Validate driver's license expiry date (BR-003).

###### 2.5.2.11.2.4 Sequence Number

2.2

###### 2.5.2.11.2.5 Type

🔹 Validation

###### 2.5.2.11.2.6 Is Synchronous

✅ Yes

###### 2.5.2.11.2.7 Return Message



###### 2.5.2.11.2.8 Has Return

❌ No

###### 2.5.2.11.2.9 Is Activation

❌ No

###### 2.5.2.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | _check_driver_license() |
| Parameters | driver.license_expiry_date |
| Authentication | N/A |
| Error Handling | Throws ValidationError on failure. |
| Performance | p99 < 50ms |

##### 2.5.2.11.3.0 StateTransition

###### 2.5.2.11.3.1 Source Id

REPO-TMS-CORE

###### 2.5.2.11.3.2 Target Id

REPO-TMS-CORE

###### 2.5.2.11.3.3 Message

2.3. [State Transition] Update tms.trip record state from 'Planned' to 'Assigned'.

###### 2.5.2.11.3.4 Sequence Number

2.3

###### 2.5.2.11.3.5 Type

🔹 StateTransition

###### 2.5.2.11.3.6 Is Synchronous

✅ Yes

###### 2.5.2.11.3.7 Return Message



###### 2.5.2.11.3.8 Has Return

❌ No

###### 2.5.2.11.3.9 Is Activation

❌ No

###### 2.5.2.11.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL UPDATE |
| Method | ORM write({'state': 'Assigned'}) |
| Parameters | SQL UPDATE statement |
| Authentication | N/A |
| Error Handling | Database transaction rollback on failure. |
| Performance | p99 < 100ms |

### 2.5.3.0.0.0 UserAction

#### 2.5.3.1.0.0 Source Id

Actor_Driver

#### 2.5.3.2.0.0 Target Id

REPO-DRV-UI

#### 2.5.3.3.0.0 Message

3. Taps 'Start Trip' button

#### 2.5.3.4.0.0 Sequence Number

3

#### 2.5.3.5.0.0 Type

🔹 UserAction

#### 2.5.3.6.0.0 Is Synchronous

❌ No

#### 2.5.3.7.0.0 Return Message



#### 2.5.3.8.0.0 Has Return

❌ No

#### 2.5.3.9.0.0 Is Activation

✅ Yes

#### 2.5.3.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | UI Event |
| Method | onClick |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | UI displays loading indicator. |
| Performance | N/A |

### 2.5.4.0.0.0 APICall

#### 2.5.4.1.0.0 Source Id

REPO-DRV-UI

#### 2.5.4.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.4.3.0.0 Message

4. startTrip(trip_id)

#### 2.5.4.4.0.0 Sequence Number

4

#### 2.5.4.5.0.0 Type

🔹 APICall

#### 2.5.4.6.0.0 Is Synchronous

✅ Yes

#### 2.5.4.7.0.0 Return Message

Returns success status

#### 2.5.4.8.0.0 Has Return

✅ Yes

#### 2.5.4.9.0.0 Is Activation

❌ No

#### 2.5.4.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo Controller Call (HTTP POST) |
| Method | /tms/driver/trip/start |
| Parameters | { 'trip_id': trip_id } |
| Authentication | Odoo Session Cookie with Driver permissions |
| Error Handling | Returns JSON error response { 'error': 'Invalid st... |
| Performance | p99 < 500ms |

#### 2.5.4.11.0.0 Nested Interactions

- {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': "4.1. [State Transition] Update tms.trip state from 'Assigned' to 'In-Transit'.", 'sequenceNumber': 4.1, 'type': 'StateTransition', 'isSynchronous': True, 'returnMessage': '', 'hasReturn': False, 'isActivation': False, 'technicalDetails': {'protocol': 'PostgreSQL UPDATE', 'method': "ORM write({'state': 'In-Transit'})", 'parameters': 'SQL UPDATE statement', 'authentication': 'N/A', 'errorHandling': 'Database transaction rollback on failure.', 'performance': 'p99 < 100ms'}}

### 2.5.5.0.0.0 UserAction

#### 2.5.5.1.0.0 Source Id

Actor_Driver

#### 2.5.5.2.0.0 Target Id

REPO-DRV-UI

#### 2.5.5.3.0.0 Message

5. Uploads Proof of Delivery (POD)

#### 2.5.5.4.0.0 Sequence Number

5

#### 2.5.5.5.0.0 Type

🔹 UserAction

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
| Protocol | UI Event |
| Method | onFileUpload |
| Parameters | file object, recipient name |
| Authentication | N/A |
| Error Handling | UI displays upload progress. |
| Performance | N/A |

### 2.5.6.0.0.0 APICall

#### 2.5.6.1.0.0 Source Id

REPO-DRV-UI

#### 2.5.6.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.6.3.0.0 Message

6. submitPOD(trip_id, pod_file, recipient_name)

#### 2.5.6.4.0.0 Sequence Number

6

#### 2.5.6.5.0.0 Type

🔹 APICall

#### 2.5.6.6.0.0 Is Synchronous

✅ Yes

#### 2.5.6.7.0.0 Return Message

Returns success status

#### 2.5.6.8.0.0 Has Return

✅ Yes

#### 2.5.6.9.0.0 Is Activation

❌ No

#### 2.5.6.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo Controller Call (HTTP POST, multipart/form-da... |
| Method | /tms/driver/trip/pod |
| Parameters | trip_id, file data, recipient_name |
| Authentication | Odoo Session Cookie |
| Error Handling | Returns JSON error response. |
| Performance | p99 < 2000ms (includes S3 upload) |

#### 2.5.6.11.0.0 Nested Interactions

##### 2.5.6.11.1.0 Integration

###### 2.5.6.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.6.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.6.11.1.3 Message

6.1. Upload pod_file to Amazon S3 and create ir.attachment record.

###### 2.5.6.11.1.4 Sequence Number

6.1

###### 2.5.6.11.1.5 Type

🔹 Integration

###### 2.5.6.11.1.6 Is Synchronous

✅ Yes

###### 2.5.6.11.1.7 Return Message

s3_url

###### 2.5.6.11.1.8 Has Return

✅ Yes

###### 2.5.6.11.1.9 Is Activation

❌ No

###### 2.5.6.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | S3 Boto3 client upload_fileobj() |
| Parameters | file, bucket_name, object_name |
| Authentication | AWS IAM Role |
| Error Handling | Logged and raises exception. |
| Performance | Dependent on file size and network. |

##### 2.5.6.11.2.0 StateTransition

###### 2.5.6.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.6.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.6.11.2.3 Message

6.2. [State Transition] Update tms.trip state from 'In-Transit' to 'Delivered'.

###### 2.5.6.11.2.4 Sequence Number

6.2

###### 2.5.6.11.2.5 Type

🔹 StateTransition

###### 2.5.6.11.2.6 Is Synchronous

✅ Yes

###### 2.5.6.11.2.7 Return Message



###### 2.5.6.11.2.8 Has Return

❌ No

###### 2.5.6.11.2.9 Is Activation

❌ No

###### 2.5.6.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL UPDATE |
| Method | ORM write({'state': 'Delivered'}) |
| Parameters | SQL UPDATE statement |
| Authentication | N/A |
| Error Handling | Database transaction rollback. |
| Performance | p99 < 100ms |

### 2.5.7.0.0.0 UserAction

#### 2.5.7.1.0.0 Source Id

Actor_Dispatch_Manager

#### 2.5.7.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.7.3.0.0 Message

7. completeTrip(trip_id)

#### 2.5.7.4.0.0 Sequence Number

7

#### 2.5.7.5.0.0 Type

🔹 UserAction

#### 2.5.7.6.0.0 Is Synchronous

✅ Yes

#### 2.5.7.7.0.0 Return Message

Returns success status

#### 2.5.7.8.0.0 Has Return

✅ Yes

#### 2.5.7.9.0.0 Is Activation

❌ No

#### 2.5.7.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | tms.trip.action_complete() |
| Parameters | trip_id |
| Authentication | Odoo Session Cookie |
| Error Handling | Raises UserError on invalid state. |
| Performance | p99 < 500ms |

#### 2.5.7.11.0.0 Nested Interactions

- {'sourceId': 'REPO-TMS-CORE', 'targetId': 'REPO-TMS-CORE', 'message': "7.1. [State Transition] Update tms.trip state from 'Delivered' to 'Completed'.", 'sequenceNumber': 7.1, 'type': 'StateTransition', 'isSynchronous': True, 'returnMessage': '', 'hasReturn': False, 'isActivation': False, 'technicalDetails': {'protocol': 'PostgreSQL UPDATE', 'method': "ORM write({'state': 'Completed'})", 'parameters': 'SQL UPDATE statement', 'authentication': 'N/A', 'errorHandling': 'Database transaction rollback.', 'performance': 'p99 < 100ms'}}

### 2.5.8.0.0.0 UserAction

#### 2.5.8.1.0.0 Source Id

Actor_Finance_Officer

#### 2.5.8.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.8.3.0.0 Message

8. generateInvoice(trip_id)

#### 2.5.8.4.0.0 Sequence Number

8

#### 2.5.8.5.0.0 Type

🔹 UserAction

#### 2.5.8.6.0.0 Is Synchronous

✅ Yes

#### 2.5.8.7.0.0 Return Message

Returns new invoice record ID

#### 2.5.8.8.0.0 Has Return

✅ Yes

#### 2.5.8.9.0.0 Is Activation

❌ No

#### 2.5.8.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | tms.trip.action_create_invoice() |
| Parameters | trip_id |
| Authentication | Odoo Session Cookie with Finance Officer permissio... |
| Error Handling | Raises UserError if BR-010 validation fails. |
| Performance | p99 < 800ms |

#### 2.5.8.11.0.0 Nested Interactions

##### 2.5.8.11.1.0 Validation

###### 2.5.8.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.8.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.8.11.1.3 Message

8.1. Validate trip state is 'Completed' (BR-010).

###### 2.5.8.11.1.4 Sequence Number

8.1

###### 2.5.8.11.1.5 Type

🔹 Validation

###### 2.5.8.11.1.6 Is Synchronous

✅ Yes

###### 2.5.8.11.1.7 Return Message



###### 2.5.8.11.1.8 Has Return

❌ No

###### 2.5.8.11.1.9 Is Activation

❌ No

###### 2.5.8.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | _validate_invoice_creation() |
| Parameters | trip.state |
| Authentication | N/A |
| Error Handling | Throws ValidationError on failure. |
| Performance | p99 < 50ms |

##### 2.5.8.11.2.0 DatabaseUpdate

###### 2.5.8.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.8.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.8.11.2.3 Message

8.2. Create account.move record from trip data.

###### 2.5.8.11.2.4 Sequence Number

8.2

###### 2.5.8.11.2.5 Type

🔹 DatabaseUpdate

###### 2.5.8.11.2.6 Is Synchronous

✅ Yes

###### 2.5.8.11.2.7 Return Message

invoice_id

###### 2.5.8.11.2.8 Has Return

✅ Yes

###### 2.5.8.11.2.9 Is Activation

❌ No

###### 2.5.8.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL INSERT |
| Method | ORM account.move.create() |
| Parameters | SQL INSERT statement |
| Authentication | N/A |
| Error Handling | Database transaction rollback. |
| Performance | p99 < 200ms |

##### 2.5.8.11.3.0 StateTransition

###### 2.5.8.11.3.1 Source Id

REPO-TMS-CORE

###### 2.5.8.11.3.2 Target Id

REPO-TMS-CORE

###### 2.5.8.11.3.3 Message

8.3. [State Transition] Update tms.trip state from 'Completed' to 'Invoiced'.

###### 2.5.8.11.3.4 Sequence Number

8.3

###### 2.5.8.11.3.5 Type

🔹 StateTransition

###### 2.5.8.11.3.6 Is Synchronous

✅ Yes

###### 2.5.8.11.3.7 Return Message



###### 2.5.8.11.3.8 Has Return

❌ No

###### 2.5.8.11.3.9 Is Activation

❌ No

###### 2.5.8.11.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL UPDATE |
| Method | ORM write({'state': 'Invoiced'}) |
| Parameters | SQL UPDATE statement |
| Authentication | N/A |
| Error Handling | Database transaction rollback. |
| Performance | p99 < 100ms |

### 2.5.9.0.0.0 UserAction

#### 2.5.9.1.0.0 Source Id

Actor_Finance_Officer

#### 2.5.9.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.9.3.0.0 Message

9. recordPayment(invoice_id, payment_data)

#### 2.5.9.4.0.0 Sequence Number

9

#### 2.5.9.5.0.0 Type

🔹 UserAction

#### 2.5.9.6.0.0 Is Synchronous

✅ Yes

#### 2.5.9.7.0.0 Return Message

Returns success status

#### 2.5.9.8.0.0 Has Return

✅ Yes

#### 2.5.9.9.0.0 Is Activation

❌ No

#### 2.5.9.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM API |
| Method | account.payment.register() wizard |
| Parameters | invoice_id, journal_id, amount |
| Authentication | Odoo Session Cookie |
| Error Handling | Standard Odoo financial validation errors. |
| Performance | p99 < 800ms |

#### 2.5.9.11.0.0 Nested Interactions

##### 2.5.9.11.1.0 DatabaseUpdate

###### 2.5.9.11.1.1 Source Id

REPO-TMS-CORE

###### 2.5.9.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.9.11.1.3 Message

9.1. Reconcile payment and update invoice payment_state.

###### 2.5.9.11.1.4 Sequence Number

9.1

###### 2.5.9.11.1.5 Type

🔹 DatabaseUpdate

###### 2.5.9.11.1.6 Is Synchronous

✅ Yes

###### 2.5.9.11.1.7 Return Message



###### 2.5.9.11.1.8 Has Return

❌ No

###### 2.5.9.11.1.9 Is Activation

❌ No

###### 2.5.9.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL UPDATE |
| Method | ORM write() on account.move |
| Parameters | SQL UPDATE on account_move |
| Authentication | N/A |
| Error Handling | Database transaction rollback. |
| Performance | p99 < 150ms |

##### 2.5.9.11.2.0 StateTransition

###### 2.5.9.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.9.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.9.11.2.3 Message

9.2. IF all invoices for trip are paid, [State Transition] update tms.trip state from 'Invoiced' to 'Paid'.

###### 2.5.9.11.2.4 Sequence Number

9.2

###### 2.5.9.11.2.5 Type

🔹 StateTransition

###### 2.5.9.11.2.6 Is Synchronous

✅ Yes

###### 2.5.9.11.2.7 Return Message



###### 2.5.9.11.2.8 Has Return

❌ No

###### 2.5.9.11.2.9 Is Activation

❌ No

###### 2.5.9.11.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL UPDATE |
| Method | ORM write({'state': 'Paid'}) |
| Parameters | Conditional SQL UPDATE statement |
| Authentication | N/A |
| Error Handling | Database transaction rollback. |
| Performance | p99 < 150ms |

## 2.6.0.0.0.0 Notes

### 2.6.1.0.0.0 Content

#### 2.6.1.1.0.0 Content

Business Rule BR-004 is enforced by the sequence of state transitions implemented in the tms.trip model methods. Each action validates the current state before proceeding.

#### 2.6.1.2.0.0 Position

Top

#### 2.6.1.3.0.0 Participant Id

*Not specified*

#### 2.6.1.4.0.0 Sequence Number

*Not specified*

### 2.6.2.0.0.0 Content

#### 2.6.2.1.0.0 Content

All state transitions and critical financial operations (invoice/payment creation) must generate an immutable audit trail entry using Odoo's mail.thread mixin.

#### 2.6.2.2.0.0 Position

Bottom

#### 2.6.2.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.2.4.0.0 Sequence Number

*Not specified*

### 2.6.3.0.0.0 Content

#### 2.6.3.1.0.0 Content

Driver-facing actions are exposed via dedicated, simplified REST controllers, while back-office actions use standard Odoo ORM methods triggered by the web client.

#### 2.6.3.2.0.0 Position

Middle

#### 2.6.3.3.0.0 Participant Id

*Not specified*

#### 2.6.3.4.0.0 Sequence Number

4

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | Access to each action must be strictly controlled ... |
| Performance Targets | Individual state transitions must complete in unde... |
| Error Handling Strategy | Utilize Odoo's standard `UserError` and `Validatio... |
| Testing Considerations | End-to-end tests are critical. A single test case ... |
| Monitoring Requirements | A Grafana dashboard should monitor the volume of t... |
| Deployment Considerations | The state machine logic is a core part of the appl... |

