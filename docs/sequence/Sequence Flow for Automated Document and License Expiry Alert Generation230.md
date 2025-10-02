# 1 Overview

## 1.1 Diagram Id

SEQ-OP-007

## 1.2 Name

Automated Document and License Expiry Alert Generation

## 1.3 Description

A daily scheduled background job automatically scans all active vehicle and driver records. It checks for documents (e.g., Vehicle Insurance, Driver's License) that are nearing their expiry date and generates system alerts for responsible managers.

## 1.4 Type

🔹 OperationalFlow

## 1.5 Purpose

To proactively manage fleet and driver compliance by providing timely warnings about expiring documents, thus mitigating legal and operational risks.

## 1.6 Complexity

Low

## 1.7 Priority

🟡 Medium

## 1.8 Frequency

Daily

## 1.9 Participants

- REPO-TMS-CORE

## 1.10 Key Interactions

- Odoo's central scheduler triggers the 'Check Document Expiry' scheduled action (cron job).
- The job queries all 'Active' vehicle and driver records from the database.
- It iterates through each record, comparing document 'Expiry Date' fields against the current date plus the defined alert thresholds (e.g., 30, 15, and 7 days).
- For each upcoming expiry, it creates or updates a notification record in the system.
- These notifications are then visible in the 'Alerts Panel' on the manager's dashboard and trigger email notifications if configured.

## 1.11 Triggers

- A daily automated scheduler (cron) fires at a pre-configured time (e.g., midnight).

## 1.12 Outcomes

- Dispatch Managers and Admins are proactively notified of impending document and license expiries.
- Compliance risks associated with using vehicles or drivers with invalid documents are significantly mitigated.

## 1.13 Business Rules

- REQ-DAT-001: System shall automatically generate an alert 30, 15, and 7 days before a vehicle document's expiry date.
- REQ-DAT-002: System shall automatically generate an alert 30, 15, and 7 days before a driver's license expiry date.

## 1.14 Error Scenarios

- The scheduled job fails to execute, causing a one-day delay in notifications.
- A document record has a missing or invalid expiry date, causing it to be skipped by the check.

## 1.15 Integration Points

*No items available*

# 2.0 Details

## 2.1 Diagram Id

SEQ-OP-007-IMPL

## 2.2 Name

Implementation: Daily Document & License Expiry Check Cron Job

## 2.3 Description

Provides a detailed technical specification for the daily scheduled job (Odoo ir.cron) that scans active vehicle and driver records for impending document expiries. This operational flow is a core compliance feature, implementing business rules REQ-DAT-001 and REQ-DAT-002. The job queries the PostgreSQL database, processes records in batches, creates system alerts for relevant managers, and emits metrics to the observability platform for monitoring system health and operational effectiveness.

## 2.4 Participants

### 2.4.1 System Actor

#### 2.4.1.1 Repository Id

SYSTEM-SCHEDULER

#### 2.4.1.2 Display Name

Odoo Scheduler

#### 2.4.1.3 Type

🔹 System Actor

#### 2.4.1.4 Technology

Odoo 18 Base Scheduler (ir.cron)

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #999999 |
| Stereotype | <<Timer>> |

### 2.4.2.0 Odoo Addon

#### 2.4.2.1 Repository Id

REPO-TMS-CORE

#### 2.4.2.2 Display Name

TMS Core Business Logic

#### 2.4.2.3 Type

🔹 Odoo Addon

#### 2.4.2.4 Technology

Odoo 18, Python 3.11

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | participant |
| Color | #1f77b4 |
| Stereotype | <<Service>> |

### 2.4.3.0 Database

#### 2.4.3.1 Repository Id

INFRA-DB-RDS

#### 2.4.3.2 Display Name

PostgreSQL Database

#### 2.4.3.3 Type

🔹 Database

#### 2.4.3.4 Technology

Amazon RDS for PostgreSQL 16

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #ff7f0e |
| Stereotype | <<DataStore>> |

### 2.4.4.0 Monitoring & Logging

#### 2.4.4.1 Repository Id

INFRA-OBSERVABILITY

#### 2.4.4.2 Display Name

Observability Platform

#### 2.4.4.3 Type

🔹 Monitoring & Logging

#### 2.4.4.4 Technology

Prometheus, OpenSearch, Grafana

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | boundary |
| Color | #2ca02c |
| Stereotype | <<Monitoring>> |

## 2.5.0.0 Interactions

### 2.5.1.0 Scheduled Execution

#### 2.5.1.1 Source Id

SYSTEM-SCHEDULER

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

1. Trigger Scheduled Action: _cron_check_document_expiries()

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Scheduled Execution

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
| Protocol | Odoo RPC |
| Method | model._cron_check_document_expiries() |
| Parameters | None. Triggered based on `ir.cron` schedule defini... |
| Authentication | Executes as the special Odoo 'admin' user defined ... |
| Error Handling | If the job fails to lock or execute, Odoo's base s... |
| Performance | Triggering mechanism has negligible latency. |

### 2.5.2.0 Logging

#### 2.5.2.1 Source Id

REPO-TMS-CORE

#### 2.5.2.2 Target Id

INFRA-OBSERVABILITY

#### 2.5.2.3 Message

2. Log Job Start

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 Logging

#### 2.5.2.6 Is Synchronous

❌ No

#### 2.5.2.7 Return Message



#### 2.5.2.8 Has Return

❌ No

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | stdout (JSON) |
| Method | logging.info() |
| Parameters | {'message': 'Starting document expiry check job', ... |
| Authentication | N/A |
| Error Handling | Logs are collected by Fluentbit DaemonSet. |
| Performance | Asynchronous, sub-millisecond operation. |

### 2.5.3.0 Database Query

#### 2.5.3.1 Source Id

REPO-TMS-CORE

#### 2.5.3.2 Target Id

INFRA-DB-RDS

#### 2.5.3.3 Message

3. Query for Active Driver Licenses Nearing Expiry

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 Database Query

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message

4. Return Driver Records

#### 2.5.3.8 Has Return

✅ Yes

#### 2.5.3.9 Is Activation

✅ Yes

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | SQL over psycopg2 |
| Method | ORM: env['hr.employee'].search(domain) |
| Parameters | SQL: SELECT id, name, license_expiry_date FROM hr_... |
| Authentication | Uses pooled DB connection credentials from Odoo co... |
| Error Handling | Odoo ORM raises `psycopg2.Error`. Job will catch, ... |
| Performance | Requires an index on `hr_employee(active, license_... |

### 2.5.4.0 Database Query

#### 2.5.4.1 Source Id

REPO-TMS-CORE

#### 2.5.4.2 Target Id

INFRA-DB-RDS

#### 2.5.4.3 Message

5. Query for Active Vehicle Documents Nearing Expiry

#### 2.5.4.4 Sequence Number

5

#### 2.5.4.5 Type

🔹 Database Query

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message

6. Return Vehicle Document Records

#### 2.5.4.8 Has Return

✅ Yes

#### 2.5.4.9 Is Activation

✅ Yes

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | SQL over psycopg2 |
| Method | ORM: env['tms.vehicle.document'].search(domain) |
| Parameters | SQL: SELECT doc.id, doc.name, doc.expiry_date, doc... |
| Authentication | Uses pooled DB connection credentials. |
| Error Handling | Odoo ORM raises `psycopg2.Error`. Job will catch, ... |
| Performance | Requires indexes on `tms_vehicle(active)` and `tms... |

### 2.5.5.0 Internal Processing Loop

#### 2.5.5.1 Source Id

REPO-TMS-CORE

#### 2.5.5.2 Target Id

REPO-TMS-CORE

#### 2.5.5.3 Message

7. Process records and build list of alerts to create

#### 2.5.5.4 Sequence Number

7

#### 2.5.5.5 Type

🔹 Internal Processing Loop

#### 2.5.5.6 Is Synchronous

✅ Yes

#### 2.5.5.7 Return Message



#### 2.5.5.8 Has Return

❌ No

#### 2.5.5.9 Is Activation

❌ No

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | In-Memory |
| Method | Python loop and date comparison |
| Parameters | Iterates through fetched records. Calculates `days... |
| Authentication | N/A |
| Error Handling | Handles `TypeError` for invalid or null dates by l... |
| Performance | Processing is done in memory. For large datasets (... |

### 2.5.6.0 Database Write

#### 2.5.6.1 Source Id

REPO-TMS-CORE

#### 2.5.6.2 Target Id

INFRA-DB-RDS

#### 2.5.6.3 Message

8. Create System Alert Records in Bulk

#### 2.5.6.4 Sequence Number

8

#### 2.5.6.5 Type

🔹 Database Write

#### 2.5.6.6 Is Synchronous

✅ Yes

#### 2.5.6.7 Return Message

9. Acknowledge Creation

#### 2.5.6.8 Has Return

✅ Yes

#### 2.5.6.9 Is Activation

✅ Yes

#### 2.5.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | SQL over psycopg2 |
| Method | ORM: env['tms.system_alert'].create(vals_list) |
| Parameters | SQL: INSERT INTO tms_system_alert (related_model, ... |
| Authentication | Uses pooled DB connection credentials. |
| Error Handling | A unique constraint on the alert record (e.g., on ... |
| Performance | Uses a single `create` call with a list of diction... |

### 2.5.7.0 Metric Emission

#### 2.5.7.1 Source Id

REPO-TMS-CORE

#### 2.5.7.2 Target Id

INFRA-OBSERVABILITY

#### 2.5.7.3 Message

10. Emit Operational Metrics

#### 2.5.7.4 Sequence Number

10

#### 2.5.7.5 Type

🔹 Metric Emission

#### 2.5.7.6 Is Synchronous

❌ No

#### 2.5.7.7 Return Message



#### 2.5.7.8 Has Return

❌ No

#### 2.5.7.9 Is Activation

❌ No

#### 2.5.7.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Prometheus Exposition Format |
| Method | Update Prometheus client library gauges and counte... |
| Parameters | `tms_expiry_check_job_duration_seconds.set(job_dur... |
| Authentication | N/A |
| Error Handling | Metrics are exposed via a /metrics endpoint scrape... |
| Performance | In-memory operation with negligible overhead. |

### 2.5.8.0 Logging

#### 2.5.8.1 Source Id

REPO-TMS-CORE

#### 2.5.8.2 Target Id

INFRA-OBSERVABILITY

#### 2.5.8.3 Message

11. Log Job Completion

#### 2.5.8.4 Sequence Number

11

#### 2.5.8.5 Type

🔹 Logging

#### 2.5.8.6 Is Synchronous

❌ No

#### 2.5.8.7 Return Message



#### 2.5.8.8 Has Return

❌ No

#### 2.5.8.9 Is Activation

❌ No

#### 2.5.8.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | stdout (JSON) |
| Method | logging.info() |
| Parameters | {'message': 'Document expiry check job finished', ... |
| Authentication | N/A |
| Error Handling | Logs are collected by Fluentbit. |
| Performance | Asynchronous, sub-millisecond operation. |

## 2.6.0.0 Notes

- {'content': 'The entire process from step 2 to 11 is wrapped in a try/finally block to ensure that job completion (or failure) is always logged and final metrics are emitted.', 'position': 'bottom', 'participantId': 'REPO-TMS-CORE', 'sequenceNumber': 11}

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The Odoo `ir.cron` record must be configured to ru... |
| Performance Targets | The entire job must complete in under 10 minutes f... |
| Error Handling Strategy | Primary failure mode is DB unavailability. The job... |
| Testing Considerations | Unit tests must cover the date calculation logic f... |
| Monitoring Requirements | A dedicated Grafana dashboard will visualize key m... |
| Deployment Considerations | The `ir.cron` definition is an XML record deployed... |

