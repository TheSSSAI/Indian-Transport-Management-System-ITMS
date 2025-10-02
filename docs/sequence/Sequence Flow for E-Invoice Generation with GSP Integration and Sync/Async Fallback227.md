# 1 Overview

## 1.1 Diagram Id

SEQ-IF-004

## 1.2 Name

E-Invoice Generation with GSP Integration and Sync/Async Fallback

## 1.3 Description

A Finance Officer generates a GST-compliant e-invoice for a completed trip. The system first attempts a real-time synchronous API call to the GSP. If this fails or times out, the task is seamlessly moved to a background job queue for automated retries, ensuring a resilient and non-blocking user experience.

## 1.4 Type

🔹 IntegrationFlow

## 1.5 Purpose

To generate legally compliant e-invoices by integrating with a GST Suvidha Provider (GSP), ensuring high availability through a robust synchronous-with-asynchronous-fallback mechanism.

## 1.6 Complexity

High

## 1.7 Priority

🚨 Critical

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE
- REPO-GSP-INT

## 1.10 Key Interactions

- Finance Officer triggers 'Generate E-Invoice' action for a 'Completed' trip in REPO-TMS-CORE.
- REPO-TMS-CORE prepares the invoice data, conforming to the GSP's required format.
- REPO-GSP-INT component is invoked, retrieving the GSP API key from AWS Secrets Manager.
- A synchronous HTTPS POST request is made to the GSP API.
- **Success Path:** GSP API responds with an HTTP 200 and IRN. The IRN is saved and the trip status becomes 'Invoiced'.
- **Failure Path:** The synchronous call fails (e.g., timeout, 5xx error). The task is enqueued in Odoo's background job queue, and the user is notified that processing is continuing in the background.
- The background job later retries the API call with exponential backoff.
- A system notification informs the user of the final success or permanent failure.

## 1.11 Triggers

- A user with the 'Finance Officer' role initiates the e-invoicing process for a trip.

## 1.12 Outcomes

- A valid Invoice Registration Number (IRN) is successfully generated and associated with the invoice in the system.
- After repeated failures, the invoice is flagged for manual intervention and a high-priority alert is generated for the Finance Officer.

## 1.13 Business Rules

- REQ-FNC-006: The system must integrate with a GSP to generate a valid IRN for e-invoicing.
- REQ-INT-003: The integration pattern must be a synchronous API call with an asynchronous fallback.
- REQ-BRC-002: E-invoicing functionality must comply with the Goods and Services Tax Act, 2017.

## 1.14 Error Scenarios

- The GSP API is temporarily down; the request is successfully moved to the background queue for later processing.
- The invoice data is invalid and rejected by the GSP; the background task fails permanently and alerts the user.
- AWS Secrets Manager is unreachable, preventing API key retrieval.

## 1.15 Integration Points

- External: GST Suvidha Provider (GSP) REST API
- Cloud Service: AWS Secrets Manager
- Internal: Odoo Background Job Queue

# 2.0 Details

## 2.1 Diagram Id

SEQ-IF-004-IMPL

## 2.2 Name

Implementation: E-Invoice Generation with GSP Sync/Async Fallback

## 2.3 Description

Provides the detailed technical sequence for generating a GST-compliant e-invoice. This sequence implements a resilient integration pattern by first attempting a synchronous API call to the GSP. Upon failure (e.g., timeout, 5xx error), the operation transparently falls back to an asynchronous background job for automated retries. This ensures a non-blocking user experience and guarantees eventual processing, fulfilling REQ-FNC-006 and REQ-INT-003.

## 2.4 Participants

### 2.4.1 Actor

#### 2.4.1.1 Repository Id

USER-FINANCE-OFFICER

#### 2.4.1.2 Display Name

User (Finance Officer)

#### 2.4.1.3 Type

🔹 Actor

#### 2.4.1.4 Technology

Web Browser (Odoo Web Client)

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #90A4AE |
| Stereotype | Human Actor |

### 2.4.2.0 Modular Monolith

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

TMS Core (Odoo Addon)

#### 2.4.2.3 Type

🔹 Modular Monolith

#### 2.4.2.4 Technology

Odoo 18, Python 3.11

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #42A5F5 |
| Stereotype | Business & Integration Logic |

### 2.4.3.0 Cloud Service

#### 2.4.3.1 Repository Id

AWS-SECRETS-MANAGER

#### 2.4.3.2 Display Name

AWS Secrets Manager

#### 2.4.3.3 Type

🔹 Cloud Service

#### 2.4.3.4 Technology

AWS SDK (HTTPS)

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #FF9800 |
| Stereotype | Secrets Store |

### 2.4.4.0 External Service

#### 2.4.4.1 Repository Id

EXT-GSP-API

#### 2.4.4.2 Display Name

External GSP API

#### 2.4.4.3 Type

🔹 External Service

#### 2.4.4.4 Technology

REST/JSON API (HTTPS)

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #EF5350 |
| Stereotype | Third-Party API |

### 2.4.5.0 Internal System

#### 2.4.5.1 Repository Id

SYS-ODOO-JOB-QUEUE

#### 2.4.5.2 Display Name

Odoo Job Queue

#### 2.4.5.3 Type

🔹 Internal System

#### 2.4.5.4 Technology

Odoo ORM, PostgreSQL

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | queue |
| Color | #66BB6A |
| Stereotype | Background Processor |

### 2.4.6.0 Internal System

#### 2.4.6.1 Repository Id

SYS-ODOO-NOTIFY

#### 2.4.6.2 Display Name

Odoo Notification Service

#### 2.4.6.3 Type

🔹 Internal System

#### 2.4.6.4 Technology

Odoo Bus

#### 2.4.6.5 Order

6

#### 2.4.6.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #AB47BC |
| Stereotype | Notification Service |

## 2.5.0.0 Interactions

### 2.5.1.0 User Interaction

#### 2.5.1.1 Source Id

USER-FINANCE-OFFICER

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

1. Triggers 'Generate E-Invoice' action for a 'Completed' trip.

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 User Interaction

#### 2.5.1.6 Is Synchronous

✅ Yes

#### 2.5.1.7 Return Message

Returns immediate UI feedback (success, queued, or error).

#### 2.5.1.8 Has Return

✅ Yes

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | POST (via Odoo Web Client) |
| Parameters | Odoo RPC call with `model='account.move'` and `met... |
| Authentication | Odoo User Session Cookie |
| Error Handling | Standard Odoo UI error dialogs for immediate valid... |
| Performance | User action, no strict SLA. |

### 2.5.2.0 Internal Logic

#### 2.5.2.1 Source Id

REPO-TMS-CORE

#### 2.5.2.2 Target Id

REPO-TMS-CORE

#### 2.5.2.3 Message

2. Validates preconditions: Trip status is 'Completed' and invoice contains all required fields (e.g., GSTIN).

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 Internal Logic

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

Validation success or raises `ValidationError`.

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | self._validate_einvoice_preconditions() |
| Parameters | invoice recordset |
| Authentication | N/A |
| Error Handling | If validation fails, raises an Odoo `ValidationErr... |
| Performance | <50ms |

### 2.5.3.0 Cloud Service Call

#### 2.5.3.1 Source Id

REPO-TMS-CORE

#### 2.5.3.2 Target Id

AWS-SECRETS-MANAGER

#### 2.5.3.3 Message

3. Retrieves GSP API Key from secure storage.

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 Cloud Service Call

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message

Returns secret string containing the API key.

#### 2.5.3.8 Has Return

✅ Yes

#### 2.5.3.9 Is Activation

❌ No

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AWS SDK (HTTPS) |
| Method | boto3.client('secretsmanager').get_secret_value(Se... |
| Parameters | SecretId |
| Authentication | IAM Role for Service Account (IRSA) for the EKS po... |
| Error Handling | If call fails, a `ClientError` is caught. A critic... |
| Performance | <100ms |

### 2.5.4.0 Cloud Service Response

#### 2.5.4.1 Source Id

AWS-SECRETS-MANAGER

#### 2.5.4.2 Target Id

REPO-TMS-CORE

#### 2.5.4.3 Message

4. Returns GSP API Key.

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 Cloud Service Response

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message



#### 2.5.4.8 Has Return

❌ No

#### 2.5.4.9 Is Activation

❌ No

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AWS SDK (HTTPS) |
| Method |  |
| Parameters | JSON payload `{ 'SecretString': '...' }` |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.5.0 Data Transformation

#### 2.5.5.1 Source Id

REPO-TMS-CORE

#### 2.5.5.2 Target Id

REPO-TMS-CORE

#### 2.5.5.3 Message

5. Transforms Odoo invoice record into the required GSP JSON format.

#### 2.5.5.4 Sequence Number

5

#### 2.5.5.5 Type

🔹 Data Transformation

#### 2.5.5.6 Is Synchronous

✅ Yes

#### 2.5.5.7 Return Message

Returns JSON-serializable Python dictionary.

#### 2.5.5.8 Has Return

✅ Yes

#### 2.5.5.9 Is Activation

❌ No

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | self._prepare_gsp_payload() |
| Parameters | invoice recordset |
| Authentication | N/A |
| Error Handling | Internal validation ensures all required fields ar... |
| Performance | <50ms |

### 2.5.6.0 API Call

#### 2.5.6.1 Source Id

REPO-TMS-CORE

#### 2.5.6.2 Target Id

EXT-GSP-API

#### 2.5.6.3 Message

6. [Sync Attempt] Submits e-invoice generation request.

#### 2.5.6.4 Sequence Number

6

#### 2.5.6.5 Type

🔹 API Call

#### 2.5.6.6 Is Synchronous

✅ Yes

#### 2.5.6.7 Return Message

Returns HTTP status and JSON response.

#### 2.5.6.8 Has Return

✅ Yes

#### 2.5.6.9 Is Activation

✅ Yes

#### 2.5.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | POST /v1.03/invoice |
| Parameters | Body: GSP JSON payload. Headers: `Authorization: B... |
| Authentication | Bearer token authentication with retrieved API key... |
| Error Handling | Handles HTTP status codes (2xx, 4xx, 5xx) and conn... |
| Performance | Request timeout set to 8 seconds. Per REQ-NFR-001,... |

#### 2.5.6.11 Nested Interactions

##### 2.5.6.11.1 API Response

###### 2.5.6.11.1.1 Source Id

EXT-GSP-API

###### 2.5.6.11.1.2 Target Id

REPO-TMS-CORE

###### 2.5.6.11.1.3 Message

7. [Success Path] Responds with 200 OK and IRN.

###### 2.5.6.11.1.4 Sequence Number

7

###### 2.5.6.11.1.5 Type

🔹 API Response

###### 2.5.6.11.1.6 Is Synchronous

✅ Yes

###### 2.5.6.11.1.7 Return Message



###### 2.5.6.11.1.8 Has Return

❌ No

###### 2.5.6.11.1.9 Is Activation

❌ No

###### 2.5.6.11.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method |  |
| Parameters | JSON payload `{ 'status': 1, 'data': { 'Irn': '...... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

##### 2.5.6.11.2.0 Database Transaction

###### 2.5.6.11.2.1 Source Id

REPO-TMS-CORE

###### 2.5.6.11.2.2 Target Id

REPO-TMS-CORE

###### 2.5.6.11.2.3 Message

8. [Success Path] Persists IRN and updates invoice & trip status.

###### 2.5.6.11.2.4 Sequence Number

8

###### 2.5.6.11.2.5 Type

🔹 Database Transaction

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
| Protocol | Odoo ORM |
| Method | invoice.write({'gsp_irn': '...', 'state': 'posted'... |
| Parameters | Field values for invoice and trip records. |
| Authentication | N/A |
| Error Handling | Database transaction ensures atomicity. |
| Performance | <100ms |

##### 2.5.6.11.3.0 UI Update

###### 2.5.6.11.3.1 Source Id

REPO-TMS-CORE

###### 2.5.6.11.3.2 Target Id

USER-FINANCE-OFFICER

###### 2.5.6.11.3.3 Message

9. [Success Path] Displays success message and updated invoice status in UI.

###### 2.5.6.11.3.4 Sequence Number

9

###### 2.5.6.11.3.5 Type

🔹 UI Update

###### 2.5.6.11.3.6 Is Synchronous

✅ Yes

###### 2.5.6.11.3.7 Return Message



###### 2.5.6.11.3.8 Has Return

❌ No

###### 2.5.6.11.3.9 Is Activation

❌ No

###### 2.5.6.11.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | Odoo Web Client render |
| Parameters | Updated view data |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.7.0.0.0 API Response (Failure)

#### 2.5.7.1.0.0 Source Id

EXT-GSP-API

#### 2.5.7.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.7.3.0.0 Message

7a. [Failure Path] Responds with 5xx error or times out.

#### 2.5.7.4.0.0 Sequence Number

10

#### 2.5.7.5.0.0 Type

🔹 API Response (Failure)

#### 2.5.7.6.0.0 Is Synchronous

✅ Yes

#### 2.5.7.7.0.0 Return Message



#### 2.5.7.8.0.0 Has Return

❌ No

#### 2.5.7.9.0.0 Is Activation

❌ No

#### 2.5.7.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method |  |
| Parameters | HTTP 503 Service Unavailable, or connection timeou... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.8.0.0.0 Job Enqueue

#### 2.5.8.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.8.2.0.0 Target Id

SYS-ODOO-JOB-QUEUE

#### 2.5.8.3.0.0 Message

8a. [Failure Path] Enqueues background job for async processing.

#### 2.5.8.4.0.0 Sequence Number

11

#### 2.5.8.5.0.0 Type

🔹 Job Enqueue

#### 2.5.8.6.0.0 Is Synchronous

✅ Yes

#### 2.5.8.7.0.0 Return Message



#### 2.5.8.8.0.0 Has Return

❌ No

#### 2.5.8.9.0.0 Is Activation

✅ Yes

#### 2.5.8.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM |
| Method | self.with_delay(eta=..., retry_pattern=...)._proce... |
| Parameters | Job details: invoice ID, ETA for first run, retry ... |
| Authentication | N/A |
| Error Handling | If the queue itself is down, a critical error is l... |
| Performance | <50ms |

### 2.5.9.0.0.0 UI Update

#### 2.5.9.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.9.2.0.0 Target Id

USER-FINANCE-OFFICER

#### 2.5.9.3.0.0 Message

9a. [Failure Path] Displays message: 'E-invoice queued for background processing.'

#### 2.5.9.4.0.0 Sequence Number

12

#### 2.5.9.5.0.0 Type

🔹 UI Update

#### 2.5.9.6.0.0 Is Synchronous

✅ Yes

#### 2.5.9.7.0.0 Return Message



#### 2.5.9.8.0.0 Has Return

❌ No

#### 2.5.9.9.0.0 Is Activation

❌ No

#### 2.5.9.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | Odoo Web Client render |
| Parameters | View data with notification banner. |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.10.0.0.0 Job Execution

#### 2.5.10.1.0.0 Source Id

SYS-ODOO-JOB-QUEUE

#### 2.5.10.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.10.3.0.0 Message

10. [Async Path] Executes job from queue.

#### 2.5.10.4.0.0 Sequence Number

13

#### 2.5.10.5.0.0 Type

🔹 Job Execution

#### 2.5.10.6.0.0 Is Synchronous

✅ Yes

#### 2.5.10.7.0.0 Return Message

Job completion status.

#### 2.5.10.8.0.0 Has Return

✅ Yes

#### 2.5.10.9.0.0 Is Activation

✅ Yes

#### 2.5.10.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Method Call |
| Method | _process_einvoice_async(invoice_id) |
| Parameters | invoice ID |
| Authentication | N/A |
| Error Handling | The job runner handles exceptions, retries, and pe... |
| Performance | Depends on external API calls. |

### 2.5.11.0.0.0 API Call

#### 2.5.11.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.11.2.0.0 Target Id

EXT-GSP-API

#### 2.5.11.3.0.0 Message

11. [Async Path] Retries e-invoice generation request.

#### 2.5.11.4.0.0 Sequence Number

14

#### 2.5.11.5.0.0 Type

🔹 API Call

#### 2.5.11.6.0.0 Is Synchronous

✅ Yes

#### 2.5.11.7.0.0 Return Message

Returns HTTP status and JSON response.

#### 2.5.11.8.0.0 Has Return

✅ Yes

#### 2.5.11.9.0.0 Is Activation

✅ Yes

#### 2.5.11.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | POST /v1.03/invoice |
| Parameters | Same as step 6. |
| Authentication | Bearer token authentication. |
| Error Handling | If this call fails, the job queue will reschedule ... |
| Performance | Timeout set to 15 seconds for background jobs. |

### 2.5.12.0.0.0 API Response

#### 2.5.12.1.0.0 Source Id

EXT-GSP-API

#### 2.5.12.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.12.3.0.0 Message

12. [Async Success] Responds with 200 OK and IRN.

#### 2.5.12.4.0.0 Sequence Number

15

#### 2.5.12.5.0.0 Type

🔹 API Response

#### 2.5.12.6.0.0 Is Synchronous

✅ Yes

#### 2.5.12.7.0.0 Return Message



#### 2.5.12.8.0.0 Has Return

❌ No

#### 2.5.12.9.0.0 Is Activation

❌ No

#### 2.5.12.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method |  |
| Parameters | JSON payload `{ 'status': 1, 'data': { 'Irn': '...... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.13.0.0.0 Notification

#### 2.5.13.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.13.2.0.0 Target Id

SYS-ODOO-NOTIFY

#### 2.5.13.3.0.0 Message

13. [Async Success] Sends success notification to user.

#### 2.5.13.4.0.0 Sequence Number

16

#### 2.5.13.5.0.0 Type

🔹 Notification

#### 2.5.13.6.0.0 Is Synchronous

❌ No

#### 2.5.13.7.0.0 Return Message



#### 2.5.13.8.0.0 Has Return

❌ No

#### 2.5.13.9.0.0 Is Activation

✅ Yes

#### 2.5.13.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo Bus (WebSocket) |
| Method | self.env['bus.bus']._sendone(channel, message_type... |
| Parameters | User's channel, notification type, and content: 'E... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.14.0.0.0 API Response (Failure)

#### 2.5.14.1.0.0 Source Id

EXT-GSP-API

#### 2.5.14.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.14.3.0.0 Message

12a. [Async Failure] Responds with 400 Bad Request after all retries.

#### 2.5.14.4.0.0 Sequence Number

17

#### 2.5.14.5.0.0 Type

🔹 API Response (Failure)

#### 2.5.14.6.0.0 Is Synchronous

✅ Yes

#### 2.5.14.7.0.0 Return Message



#### 2.5.14.8.0.0 Has Return

❌ No

#### 2.5.14.9.0.0 Is Activation

❌ No

#### 2.5.14.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method |  |
| Parameters | HTTP 400 with error details in body. |
| Authentication | N/A |
| Error Handling | This response marks the job for permanent failure. |
| Performance | N/A |

### 2.5.15.0.0.0 State Update

#### 2.5.15.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.15.2.0.0 Target Id

REPO-TMS-CORE

#### 2.5.15.3.0.0 Message

13a. [Async Failure] Marks invoice for manual intervention.

#### 2.5.15.4.0.0 Sequence Number

18

#### 2.5.15.5.0.0 Type

🔹 State Update

#### 2.5.15.6.0.0 Is Synchronous

✅ Yes

#### 2.5.15.7.0.0 Return Message



#### 2.5.15.8.0.0 Has Return

❌ No

#### 2.5.15.9.0.0 Is Activation

❌ No

#### 2.5.15.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo ORM |
| Method | invoice.write({'einvoice_status': 'failed', 'einvo... |
| Parameters | Updates a status field on the invoice and logs the... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

### 2.5.16.0.0.0 Notification

#### 2.5.16.1.0.0 Source Id

REPO-TMS-CORE

#### 2.5.16.2.0.0 Target Id

SYS-ODOO-NOTIFY

#### 2.5.16.3.0.0 Message

14a. [Async Failure] Sends high-priority failure alert to user.

#### 2.5.16.4.0.0 Sequence Number

19

#### 2.5.16.5.0.0 Type

🔹 Notification

#### 2.5.16.6.0.0 Is Synchronous

❌ No

#### 2.5.16.7.0.0 Return Message



#### 2.5.16.8.0.0 Has Return

❌ No

#### 2.5.16.9.0.0 Is Activation

✅ Yes

#### 2.5.16.10.0.0 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Odoo Bus (WebSocket) & Email |
| Method | self.env['bus.bus']._sendone(...) |
| Parameters | User's channel, notification type, and content: 'C... |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | N/A |

## 2.6.0.0.0.0 Notes

### 2.6.1.0.0.0 Content

#### 2.6.1.1.0.0 Content

Data Transformation Logic (Step 5): Maps fields from Odoo models (`account.move`, `res.partner`, `account.move.line`) to the GSP's nested JSON structure. This includes calculating tax totals per HSN code and validating formats.

#### 2.6.1.2.0.0 Position

right

#### 2.6.1.3.0.0 Participant Id

REPO-TMS-CORE

#### 2.6.1.4.0.0 Sequence Number

5

### 2.6.2.0.0.0 Content

#### 2.6.2.1.0.0 Content

Background Job Retry Policy (Step 8a): Configured with 5 retries. Delays: 5m, 15m, 1h, 4h, 12h. This exponential backoff avoids overwhelming a temporarily unavailable GSP API.

#### 2.6.2.2.0.0 Position

bottom

#### 2.6.2.3.0.0 Participant Id

SYS-ODOO-JOB-QUEUE

#### 2.6.2.4.0.0 Sequence Number

11

## 2.7.0.0.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The EKS pod running the Odoo application must be g... |
| Performance Targets | The initial synchronous attempt must provide feedb... |
| Error Handling Strategy | The core of the strategy is the synchronous-to-asy... |
| Testing Considerations | 1. **Integration Testing:** Use a mocking library ... |
| Monitoring Requirements | 1. **Metrics (Prometheus):** Create metrics for `g... |
| Deployment Considerations | The Odoo Job Queue worker must be configured and r... |

