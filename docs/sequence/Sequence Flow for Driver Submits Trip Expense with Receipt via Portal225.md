# 1 Overview

## 1.1 Diagram Id

SEQ-UJ-002

## 1.2 Name

Driver Submits Trip Expense with Receipt via Portal

## 1.3 Description

Details the user journey of a driver, using the mobile-friendly web portal, submitting a trip-related expense. The flow covers data entry for different expense types (e.g., Diesel), mandatory file upload, and initial system validation before the expense enters the approval workflow.

## 1.4 Type

🔹 UserJourney

## 1.5 Purpose

To provide a streamlined, digital method for drivers to submit expenses for reimbursement and to enable accurate, real-time trip cost tracking.

## 1.6 Complexity

Medium

## 1.7 Priority

🔴 High

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-DRV-UI
- REPO-TMS-CORE

## 1.10 Key Interactions

- Driver authenticates and selects an 'In-Transit' trip from their dashboard in REPO-DRV-UI.
- Driver navigates to the 'Submit Expense' feature.
- Driver enters expense details: type (Diesel, Toll, Food), amount, and uploads a receipt photo.
- If type is 'Diesel', driver provides fuel quantity and current vehicle odometer reading.
- REPO-DRV-UI submits the data to a REPO-TMS-CORE controller.
- REPO-TMS-CORE validates the submission (e.g., odometer reading > previous) and creates an expense record in a 'Submitted' state, linking it to the trip.

## 1.11 Triggers

- Driver incurs a cost (e.g., refueling, paying a toll) during an active trip.

## 1.12 Outcomes

- An expense record is successfully created and placed in the manager's approval queue.
- The uploaded receipt image is securely stored in the designated Amazon S3 bucket.
- An audit trail of the submission is created, linking the expense to the driver and trip.

## 1.13 Business Rules

- BR-009: The odometer reading submitted with a 'Diesel' expense must be greater than the previously recorded odometer reading for that vehicle.
- Uploaded receipt files must be in JPG, PNG, or PDF format and not exceed 5MB.

## 1.14 Error Scenarios

- User attempts to submit an odometer reading that is lower than the last recorded value, and receives a validation error.
- File upload fails due to an unsupported format or exceeding the size limit.
- The driver has no active 'In-Transit' trip to which an expense can be assigned.

## 1.15 Integration Points

- Cloud Service: Amazon S3 for receipt file storage.

# 2.0 Details

## 2.1 Diagram Id

SEQ-UJ-002

## 2.2 Name

Driver Submits Trip Expense with Receipt via Portal

## 2.3 Description

Provides a comprehensive technical specification for the user journey of a driver submitting a trip expense. This sequence details the interaction between the Odoo OWL frontend component (REPO-DRV-UI), the Odoo backend controller (REPO-TMS-CORE), and Amazon S3. The implementation pattern utilizes a secure, two-step submission process: first, obtaining a pre-signed URL from the backend for direct-to-S3 file upload, followed by a final submission of the expense form data, including the S3 file key, for server-side validation and persistence.

## 2.4 Participants

### 2.4.1 External Actor

#### 2.4.1.1 Repository Id

Driver (User)

#### 2.4.1.2 Display Name

Driver (User)

#### 2.4.1.3 Type

🔹 External Actor

#### 2.4.1.4 Technology

Human

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #999999 |
| Stereotype | User |

### 2.4.2.0 Frontend Component

#### 2.4.2.1 Repository Id

REPO-DRV-UI

#### 2.4.2.2 Display Name

Odoo Driver Portal (OWL)

#### 2.4.2.3 Type

🔹 Frontend Component

#### 2.4.2.4 Technology

Odoo 18, OWL 2.0, JavaScript

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #4285F4 |
| Stereotype | UI |

### 2.4.3.0 Backend Service

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

Odoo Core Business Logic

#### 2.4.3.3 Type

🔹 Backend Service

#### 2.4.3.4 Technology

Odoo 18, Python 3.11

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #34A853 |
| Stereotype | Backend |

### 2.4.4.0 Cloud Storage Service

#### 2.4.4.1 Repository Id

Amazon S3

#### 2.4.4.2 Display Name

Amazon S3

#### 2.4.4.3 Type

🔹 Cloud Storage Service

#### 2.4.4.4 Technology

AWS S3

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #FF9900 |
| Stereotype | Storage |

## 2.5.0.0 Interactions

### 2.5.1.0 User Interaction

#### 2.5.1.1 Source Id

Driver (User)

#### 2.5.1.2 Target Id

REPO-DRV-UI

#### 2.5.1.3 Message

1. Fills expense form (Type, Amount, Odometer) and selects receipt file.

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 User Interaction

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Has Return

❌ No

#### 2.5.1.8 Is Activation

❌ No

#### 2.5.1.9 Technical Details

| Property | Value |
|----------|-------|
| Protocol | User Interface |
| Method | Form Input & File Selection |
| Parameters | Expense data fields, local file path. |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.2.0 Internal Process

#### 2.5.2.1 Source Id

REPO-DRV-UI

#### 2.5.2.2 Target Id

REPO-DRV-UI

#### 2.5.2.3 Message

2. Perform client-side validation (file type, size, required fields).

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 Internal Process

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Has Return

✅ Yes

#### 2.5.2.8 Return Message

Validation result (pass/fail).

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | JavaScript |
| Method | validateForm() |
| Parameters | Form state object. |
| Authentication | N/A |
| Error Handling | If validation fails, display inline error messages... |
| Performance | Must be near-instant (<50ms). |

### 2.5.3.0 User Interaction

#### 2.5.3.1 Source Id

Driver (User)

#### 2.5.3.2 Target Id

REPO-DRV-UI

#### 2.5.3.3 Message

3. Taps 'Submit' button.

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 User Interaction

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Has Return

❌ No

#### 2.5.3.8 Is Activation

✅ Yes

#### 2.5.3.9 Technical Details

| Property | Value |
|----------|-------|
| Protocol | UI Event |
| Method | onClick |
| Parameters | N/A |
| Authentication | N/A |
| Error Handling | Button should be in a disabled state until client-... |
| Performance | N/A |

### 2.5.4.0 API Call

#### 2.5.4.1 Source Id

REPO-DRV-UI

#### 2.5.4.2 Target Id

REPO-TMS-CORE

#### 2.5.4.3 Message

4. Request pre-signed URL for receipt upload.

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 API Call

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Has Return

✅ Yes

#### 2.5.4.8 Return Message

HTTP 200 OK with pre-signed URL data or HTTP 400 with validation error.

#### 2.5.4.9 Is Activation

✅ Yes

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP/JSON API |
| Method | POST /tms/expense/presign_url |
| Parameters | { filename: 'receipt.jpg', content_type: 'image/jp... |
| Authentication | Odoo session cookie (`session_id`) required and va... |
| Error Handling | Handle HTTP 4xx/5xx errors. On 400 (e.g., file typ... |
| Performance | SLA < 500ms. |

### 2.5.5.0 Internal Process

#### 2.5.5.1 Source Id

REPO-TMS-CORE

#### 2.5.5.2 Target Id

REPO-TMS-CORE

#### 2.5.5.3 Message

4a. Validate file metadata against business rules (type, size).

#### 2.5.5.4 Sequence Number

5

#### 2.5.5.5 Type

🔹 Internal Process

#### 2.5.5.6 Is Synchronous

✅ Yes

#### 2.5.5.7 Has Return

✅ Yes

#### 2.5.5.8 Return Message

Validation result.

#### 2.5.5.9 Is Activation

❌ No

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Python |
| Method | validate_upload_request() |
| Parameters | File metadata dict. |
| Authentication | N/A |
| Error Handling | If validation fails, raise an `odoo.exceptions.Val... |
| Performance | Immediate. |

### 2.5.6.0 SDK Call

#### 2.5.6.1 Source Id

REPO-TMS-CORE

#### 2.5.6.2 Target Id

Amazon S3

#### 2.5.6.3 Message

4b. Generate pre-signed POST URL using AWS SDK.

#### 2.5.6.4 Sequence Number

6

#### 2.5.6.5 Type

🔹 SDK Call

#### 2.5.6.6 Is Synchronous

✅ Yes

#### 2.5.6.7 Has Return

✅ Yes

#### 2.5.6.8 Return Message

Pre-signed URL object.

#### 2.5.6.9 Is Activation

❌ No

#### 2.5.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AWS SDK (boto3) |
| Method | s3_client.generate_presigned_post() |
| Parameters | Bucket name, object key, conditions (e.g., content... |
| Authentication | Via IAM Role assigned to the Odoo EKS pod. |
| Error Handling | SDK exceptions are caught and logged, returning an... |
| Performance | Typically < 200ms. |

### 2.5.7.0 File Upload

#### 2.5.7.1 Source Id

REPO-DRV-UI

#### 2.5.7.2 Target Id

Amazon S3

#### 2.5.7.3 Message

5. Upload receipt file directly using pre-signed URL.

#### 2.5.7.4 Sequence Number

7

#### 2.5.7.5 Type

🔹 File Upload

#### 2.5.7.6 Is Synchronous

✅ Yes

#### 2.5.7.7 Has Return

✅ Yes

#### 2.5.7.8 Return Message

HTTP 204 No Content (on success) or S3 error response.

#### 2.5.7.9 Is Activation

❌ No

#### 2.5.7.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | POST |
| Parameters | Multipart form data including the file and fields ... |
| Authentication | The pre-signed URL itself contains the temporary a... |
| Error Handling | The UI must handle upload failures (e.g., network ... |
| Performance | Dependent on user's network connection speed and f... |

### 2.5.8.0 API Call

#### 2.5.8.1 Source Id

REPO-DRV-UI

#### 2.5.8.2 Target Id

REPO-TMS-CORE

#### 2.5.8.3 Message

6. Submit final expense data with S3 file key.

#### 2.5.8.4 Sequence Number

8

#### 2.5.8.5 Type

🔹 API Call

#### 2.5.8.6 Is Synchronous

✅ Yes

#### 2.5.8.7 Has Return

✅ Yes

#### 2.5.8.8 Return Message

HTTP 201 Created with new expense ID, or HTTP 400 with validation errors.

#### 2.5.8.9 Is Activation

✅ Yes

#### 2.5.8.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP/JSON API |
| Method | POST /tms/expense/submit |
| Parameters | { trip_id: 123, type: 'Diesel', amount: 5000, quan... |
| Authentication | Odoo session cookie (`session_id`) required and va... |
| Error Handling | Handle HTTP 4xx/5xx errors. On 400, display specif... |
| Performance | SLA < 1000ms. |

### 2.5.9.0 Business Logic

#### 2.5.9.1 Source Id

REPO-TMS-CORE

#### 2.5.9.2 Target Id

REPO-TMS-CORE

#### 2.5.9.3 Message

6a. Perform server-side validation (BR-009).

#### 2.5.9.4 Sequence Number

9

#### 2.5.9.5 Type

🔹 Business Logic

#### 2.5.9.6 Is Synchronous

✅ Yes

#### 2.5.9.7 Has Return

❌ No

#### 2.5.9.8 Is Activation

❌ No

#### 2.5.9.9 Nested Interactions

##### 2.5.9.9.1 Database Query

###### 2.5.9.9.1.1 Source Id

REPO-TMS-CORE

###### 2.5.9.9.1.2 Target Id

REPO-TMS-CORE

###### 2.5.9.9.1.3 Message

Query database for last recorded odometer for the vehicle.

###### 2.5.9.9.1.4 Sequence Number

10

###### 2.5.9.9.1.5 Type

🔹 Database Query

###### 2.5.9.9.1.6 Is Synchronous

✅ Yes

###### 2.5.9.9.1.7 Has Return

✅ Yes

###### 2.5.9.9.1.8 Return Message

Last odometer value.

###### 2.5.9.9.1.9 Is Activation

❌ No

###### 2.5.9.9.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM |
| Method | self.env['tms.vehicle'].search_read([('id', '=', v... |
| Parameters | Vehicle ID. |
| Authentication | N/A |
| Error Handling | Handled by Odoo ORM. |
| Performance | Query should be indexed and take < 50ms. |

##### 2.5.9.9.2.0 Validation Check

###### 2.5.9.9.2.1 Source Id

REPO-TMS-CORE

###### 2.5.9.9.2.2 Target Id

REPO-TMS-CORE

###### 2.5.9.9.2.3 Message

Compare submitted odometer > last recorded odometer.

###### 2.5.9.9.2.4 Sequence Number

11

###### 2.5.9.9.2.5 Type

🔹 Validation Check

###### 2.5.9.9.2.6 Is Synchronous

✅ Yes

###### 2.5.9.9.2.7 Has Return

✅ Yes

###### 2.5.9.9.2.8 Return Message

Validation result.

###### 2.5.9.9.2.9 Is Activation

❌ No

###### 2.5.9.9.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Python |
| Method | if submitted_odometer <= last_odometer: |
| Parameters | Odometer values. |
| Authentication | N/A |
| Error Handling | If check fails, raise `odoo.exceptions.ValidationE... |
| Performance | Immediate. |

### 2.5.10.0.0.0 Database Write

#### 2.5.10.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.10.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.10.3.0.0 Message

7. Create `tms.expense` record in 'Submitted' state.

#### 2.5.10.4.0.0 Sequence Number

12

#### 2.5.10.5.0.0 Type

🔹 Database Write

#### 2.5.10.6.0.0 Is Synchronous

✅ Yes

#### 2.5.10.7.0.0 Has Return

✅ Yes

#### 2.5.10.8.0.0 Return Message

New record object.

#### 2.5.10.9.0.0 Is Activation

❌ No

#### 2.5.10.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM |
| Method | self.env['tms.expense'].create(vals) |
| Parameters | Dictionary of validated expense data, including tr... |
| Authentication | N/A |
| Error Handling | Database constraints or ORM errors are caught, log... |
| Performance | Typically < 200ms. |

### 2.5.11.0.0.0 UI Update

#### 2.5.11.1.0.0 Source Id

REPO-DRV-UI

#### 2.5.11.2.0.0 Target Id

Driver (User)

#### 2.5.11.3.0.0 Message

8. Display success confirmation to user.

#### 2.5.11.4.0.0 Sequence Number

13

#### 2.5.11.5.0.0 Type

🔹 UI Update

#### 2.5.11.6.0.0 Is Synchronous

✅ Yes

#### 2.5.11.7.0.0 Has Return

❌ No

#### 2.5.11.8.0.0 Is Activation

❌ No

#### 2.5.11.9.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | User Interface |
| Method | showToast('Expense submitted successfully!') |
| Parameters | Success message. |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | Immediate. |

## 2.6.0.0.0.0 Notes

### 2.6.1.0.0.0 Content

#### 2.6.1.1.0.0 Content

The pre-signed URL pattern offloads the file upload bandwidth from the application server to S3, improving performance and scalability.

#### 2.6.1.2.0.0 Position

top

#### 2.6.1.3.0.0 Participant Id

*Not specified*

#### 2.6.1.4.0.0 Sequence Number

4

### 2.6.2.0.0.0 Content

#### 2.6.2.1.0.0 Content

Server-side validation is critical and serves as the ultimate source of truth, even if client-side checks are in place.

#### 2.6.2.2.0.0 Position

bottom

#### 2.6.2.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.2.4.0.0 Sequence Number

9

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | Backend controllers must enforce Odoo's CSRF prote... |
| Performance Targets | The end-to-end user-perceived time from tapping 'S... |
| Error Handling Strategy | The UI must provide immediate, clear, and actionab... |
| Testing Considerations | Unit tests for the Odoo controller must cover all ... |
| Monitoring Requirements | Monitor the latency and error rates (4xx and 5xx) ... |
| Deployment Considerations | The Odoo application's IAM role in EKS must have `... |

