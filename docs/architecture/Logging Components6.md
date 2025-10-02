# 1 System Overview

## 1.1 Analysis Date

2025-09-27

## 1.2 Technology Stack

- Odoo 18
- Python 3.11
- FastAPI
- PostgreSQL 16
- RabbitMQ
- Docker
- Amazon EKS
- Fluentbit
- OpenSearch
- Prometheus
- Grafana

## 1.3 Monitoring Requirements

- REQ-1-602: Mandates use of Prometheus, Fluentbit, OpenSearch, Grafana, and Alertmanager.
- REQ-1-680: Requires all application logs to be in a structured JSON format.
- REQ-1-501: Requires measurement of end-to-end latency for GPS data points (< 10s), necessitating log correlation.
- REQ-1-301: Requires monitoring and alerting for Dead-Letter Queues (DLQ).
- REQ-1-207: Differentiates operational logging from the business audit trail stored in the primary database.

## 1.4 System Architecture

Hybrid: A Modular Monolith (Odoo Addon) for core logic and a Decoupled Microservice (FastAPI) for high-volume GPS ingestion, running on AWS EKS.

## 1.5 Environment

production

# 2.0 Log Level And Category Strategy

## 2.1 Default Log Level

INFO

## 2.2 Environment Specific Levels

### 2.2.1 Environment

#### 2.2.1.1 Environment

staging

#### 2.2.1.2 Log Level

DEBUG

#### 2.2.1.3 Justification

Enables detailed tracing and debugging during pre-production testing cycles without impacting production performance or cost.

### 2.2.2.0 Environment

#### 2.2.2.1 Environment

production

#### 2.2.2.2 Log Level

INFO

#### 2.2.2.3 Justification

Provides a balance of operational insight and performance, capturing all significant business events and errors without excessive verbosity.

## 2.3.0.0 Component Categories

### 2.3.1.0 Component

#### 2.3.1.1 Component

Odoo Addon

#### 2.3.1.2 Category

🔹 tms.integration.gsp

#### 2.3.1.3 Log Level

INFO

#### 2.3.1.4 Verbose Logging

❌ No

#### 2.3.1.5 Justification

Logs all attempts, successes, failures, and retries for critical GST e-invoicing API calls.

### 2.3.2.0 Component

#### 2.3.2.1 Component

Odoo Addon

#### 2.3.2.2 Category

🔹 tms.trip.lifecycle

#### 2.3.2.3 Log Level

INFO

#### 2.3.2.4 Verbose Logging

❌ No

#### 2.3.2.5 Justification

Tracks all state transitions and significant events for a trip.

### 2.3.3.0 Component

#### 2.3.3.1 Component

GPS Ingestion Microservice

#### 2.3.3.2 Category

🔹 gps.ingestion

#### 2.3.3.3 Log Level

INFO

#### 2.3.3.4 Verbose Logging

❌ No

#### 2.3.3.5 Justification

Logs successful data reception, validation failures, and publishing activity. Subject to sampling to manage volume.

### 2.3.4.0 Component

#### 2.3.4.1 Component

Odoo GPS Consumer

#### 2.3.4.2 Category

🔹 gps.consumer

#### 2.3.4.3 Log Level

WARN

#### 2.3.4.4 Verbose Logging

❌ No

#### 2.3.4.5 Justification

Logs only warnings or errors by default. Successful message processing is considered a metric, not a log event, to reduce noise.

## 2.4.0.0 Sampling Strategies

- {'component': 'GPS Ingestion Microservice', 'samplingRate': '10%', 'condition': "Log level is INFO and event is 'Successful Ingestion'", 'reason': 'Reduces log volume and cost from a high-frequency component while ensuring all errors and a representative sample of successful operations are captured.'}

## 2.5.0.0 Logging Approach

### 2.5.1.0 Structured

✅ Yes

### 2.5.2.0 Format

JSON

### 2.5.3.0 Standard Fields

- timestamp
- level
- message
- serviceName
- correlationId
- podName
- k8sNamespace

### 2.5.4.0 Custom Fields

- tripId
- vehicleId
- userId
- gspTransactionId
- durationMs

# 3.0.0.0 Log Aggregation Architecture

## 3.1.0.0 Collection Mechanism

### 3.1.1.0 Type

🔹 agent

### 3.1.2.0 Technology

Fluentbit

### 3.1.3.0 Configuration

| Property | Value |
|----------|-------|
| Deployment | Kubernetes DaemonSet |
| Input | tail (from /var/log/containers/*.log) |
| Parser | docker-json |
| Filter | kubernetes (to add metadata) |

### 3.1.4.0 Justification

Mandated by REQ-1-602. A DaemonSet ensures all logs from all pods on every node in the EKS cluster are collected automatically and efficiently.

## 3.2.0.0 Strategy

| Property | Value |
|----------|-------|
| Approach | centralized |
| Reasoning | REQ-1-602 requires a centralized OpenSearch cluste... |
| Local Retention | 100MB per node |

## 3.3.0.0 Shipping Methods

- {'protocol': 'HTTP', 'destination': 'OpenSearch Cluster Endpoint', 'reliability': 'at-least-once', 'compression': True}

## 3.4.0.0 Buffering And Batching

| Property | Value |
|----------|-------|
| Buffer Size | 5MB |
| Batch Size | 0 |
| Flush Interval | 1s |
| Backpressure Handling | Fluentbit's built-in memory limits and retry logic... |

## 3.5.0.0 Transformation And Enrichment

- {'transformation': 'Kubernetes Metadata Enrichment', 'purpose': 'To automatically add context (pod name, namespace, labels) to every log record for precise filtering and analysis.', 'stage': 'collection'}

## 3.6.0.0 High Availability

| Property | Value |
|----------|-------|
| Required | ✅ |
| Redundancy | Multi-AZ OpenSearch cluster. |
| Failover Strategy | Fluentbit's internal buffering and retry mechanism... |

# 4.0.0.0 Retention Policy Design

## 4.1.0.0 Retention Periods

- {'logType': 'Application & Infrastructure Logs', 'retentionPeriod': '90 days', 'justification': 'Provides a 3-month window for troubleshooting operational issues, analyzing trends, and investigating security events.', 'complianceRequirement': 'None explicitly stated, but aligns with general best practices.'}

## 4.2.0.0 Compliance Requirements

*No items available*

## 4.3.0.0 Volume Impact Analysis

| Property | Value |
|----------|-------|
| Estimated Daily Volume | 10-20 GB/day |
| Storage Cost Projection | Based on AWS OpenSearch pricing for the chosen ins... |
| Compression Ratio | 10:1 (estimated) |

## 4.4.0.0 Storage Tiering

### 4.4.1.0 Hot Storage

| Property | Value |
|----------|-------|
| Duration | 14 days |
| Accessibility | immediate |
| Cost | high |

### 4.4.2.0 Warm Storage

| Property | Value |
|----------|-------|
| Duration | 76 days |
| Accessibility | seconds |
| Cost | medium |

### 4.4.3.0 Cold Storage

| Property | Value |
|----------|-------|
| Duration | 0 days |
| Accessibility | N/A |
| Cost | N/A |

## 4.5.0.0 Compression Strategy

| Property | Value |
|----------|-------|
| Algorithm | Default (LZ4/Zstandard) |
| Compression Level | Default |
| Expected Ratio | Varies by log content |

## 4.6.0.0 Anonymization Requirements

*No items available*

# 5.0.0.0 Search Capability Requirements

## 5.1.0.0 Essential Capabilities

### 5.1.1.0 Capability

#### 5.1.1.1 Capability

Cross-service tracing via a unique `correlationId`.

#### 5.1.1.2 Performance Requirement

< 5 seconds

#### 5.1.1.3 Justification

Required to measure end-to-end latency as per REQ-1-501 and for effective debugging in a distributed architecture.

### 5.1.2.0 Capability

#### 5.1.2.1 Capability

Filtering logs by `serviceName`, `level`, `podName`, `tripId`, and `vehicleId`.

#### 5.1.2.2 Performance Requirement

< 5 seconds

#### 5.1.2.3 Justification

Enables developers and SREs to quickly isolate logs related to a specific component, business transaction, or error condition.

## 5.2.0.0 Performance Characteristics

| Property | Value |
|----------|-------|
| Search Latency | < 5 seconds for indexed fields |
| Concurrent Users | 10 |
| Query Complexity | complex |
| Indexing Strategy | Default OpenSearch indexing with custom mapping fo... |

## 5.3.0.0 Indexed Fields

### 5.3.1.0 Field

#### 5.3.1.1 Field

correlationId

#### 5.3.1.2 Index Type

keyword

#### 5.3.1.3 Search Pattern

Exact match

#### 5.3.1.4 Frequency

high

### 5.3.2.0 Field

#### 5.3.2.1 Field

tripId

#### 5.3.2.2 Index Type

keyword

#### 5.3.2.3 Search Pattern

Exact match

#### 5.3.2.4 Frequency

medium

### 5.3.3.0 Field

#### 5.3.3.1 Field

level

#### 5.3.3.2 Index Type

keyword

#### 5.3.3.3 Search Pattern

Exact match

#### 5.3.3.4 Frequency

high

### 5.3.4.0 Field

#### 5.3.4.1 Field

serviceName

#### 5.3.4.2 Index Type

keyword

#### 5.3.4.3 Search Pattern

Exact match

#### 5.3.4.4 Frequency

high

## 5.4.0.0 Full Text Search

### 5.4.1.0 Required

✅ Yes

### 5.4.2.0 Fields

- message

### 5.4.3.0 Search Engine

OpenSearch

### 5.4.4.0 Relevance Scoring

✅ Yes

## 5.5.0.0 Correlation And Tracing

### 5.5.1.0 Correlation Ids

- correlationId

### 5.5.2.0 Trace Id Propagation

A `correlationId` must be generated at the edge (Nginx/API Gateway) or application entry point and propagated through all subsequent service calls and messages.

### 5.5.3.0 Span Correlation

❌ No

### 5.5.4.0 Cross Service Tracing

✅ Yes

## 5.6.0.0 Dashboard Requirements

### 5.6.1.0 Dashboard

#### 5.6.1.1 Dashboard

Application Error Dashboard (Grafana)

#### 5.6.1.2 Purpose

To visualize log error rates per service, top error messages, and trends over time.

#### 5.6.1.3 Refresh Interval

1m

#### 5.6.1.4 Audience

SRE, Developers

### 5.6.2.0 Dashboard

#### 5.6.2.1 Dashboard

GPS Pipeline Health (Grafana)

#### 5.6.2.2 Purpose

To visualize the flow of GPS data, including ingestion rate, processing latency (calculated from logs), and DLQ count.

#### 5.6.2.3 Refresh Interval

1m

#### 5.6.2.4 Audience

SRE

# 6.0.0.0 Storage Solution Selection

## 6.1.0.0 Selected Technology

### 6.1.1.0 Primary

OpenSearch

### 6.1.2.0 Reasoning

Mandated by REQ-1-602. It provides the required scalable, centralized search and analysis capabilities for structured log data.

### 6.1.3.0 Alternatives

- N/A (technology is specified in requirements)

## 6.2.0.0 Scalability Requirements

| Property | Value |
|----------|-------|
| Expected Growth Rate | 10% month-over-month |
| Peak Load Handling | Horizontally scalable by adding more OpenSearch no... |
| Horizontal Scaling | ✅ |

## 6.3.0.0 Cost Performance Analysis

- {'solution': 'AWS Managed OpenSearch', 'costPerGB': 'Variable (based on instance type and region)', 'queryPerformance': 'High (with appropriate indexing and node sizing)', 'operationalComplexity': 'low'}

## 6.4.0.0 Backup And Recovery

| Property | Value |
|----------|-------|
| Backup Frequency | Daily automated snapshots to S3 |
| Recovery Time Objective | 4 hours |
| Recovery Point Objective | 24 hours |
| Testing Frequency | Annually |

## 6.5.0.0 Geo Distribution

### 6.5.1.0 Required

❌ No

### 6.5.2.0 Regions

*No items available*

### 6.5.3.0 Replication Strategy



## 6.6.0.0 Data Sovereignty

- {'region': 'ap-south-1 (Mumbai)', 'requirements': ['All log data must be stored and processed within India.'], 'complianceFramework': "Implied by project context ('Indian Transport Management System')."}

# 7.0.0.0 Access Control And Compliance

## 7.1.0.0 Access Control Requirements

### 7.1.1.0 Role

#### 7.1.1.1 Role

SRE / DevOps

#### 7.1.1.2 Permissions

- read
- write
- admin

#### 7.1.1.3 Log Types

- All

#### 7.1.1.4 Justification

Responsible for managing and maintaining the observability platform.

### 7.1.2.0 Role

#### 7.1.2.1 Role

Developer

#### 7.1.2.2 Permissions

- read

#### 7.1.2.3 Log Types

- All

#### 7.1.2.4 Justification

Requires read-only access to logs in all environments for troubleshooting application issues.

## 7.2.0.0 Sensitive Data Handling

### 7.2.1.0 Data Type

#### 7.2.1.1 Data Type

Credentials (Passwords, API Keys, Tokens)

#### 7.2.1.2 Handling Strategy

exclude

#### 7.2.1.3 Fields

- N/A

#### 7.2.1.4 Compliance Requirement

REQ-1-503 mandates that secrets are never stored or logged. This must be enforced at the application level.

### 7.2.2.0 Data Type

#### 7.2.2.1 Data Type

PII (Personally Identifiable Information)

#### 7.2.2.2 Handling Strategy

mask

#### 7.2.2.3 Fields

- customer.contact.phone
- driver.name

#### 7.2.2.4 Compliance Requirement

General data protection best practices.

## 7.3.0.0 Encryption Requirements

### 7.3.1.0 In Transit

| Property | Value |
|----------|-------|
| Required | ✅ |
| Protocol | TLS 1.2+ |
| Certificate Management | AWS Certificate Manager (ACM) |

### 7.3.2.0 At Rest

| Property | Value |
|----------|-------|
| Required | ✅ |
| Algorithm | AES-256 |
| Key Management | AWS Key Management Service (KMS) |

## 7.4.0.0 Audit Trail

| Property | Value |
|----------|-------|
| Log Access | ✅ |
| Retention Period | 1 Year |
| Audit Log Location | AWS CloudTrail and OpenSearch audit logs |
| Compliance Reporting | ❌ |

## 7.5.0.0 Regulatory Compliance

*No items available*

## 7.6.0.0 Data Protection Measures

- {'measure': 'Role-Based Access Control (RBAC) for OpenSearch Dashboards', 'implementation': "Using OpenSearch's built-in security plugin to restrict access based on user roles.", 'monitoringRequired': True}

# 8.0.0.0 Project Specific Logging Config

## 8.1.0.0 Logging Config

### 8.1.1.0 Level

🔹 INFO

### 8.1.2.0 Retention

90 days

### 8.1.3.0 Aggregation

Centralized via Fluentbit to OpenSearch

### 8.1.4.0 Storage

AWS Managed OpenSearch

### 8.1.5.0 Configuration

*No data available*

## 8.2.0.0 Component Configurations

### 8.2.1.0 Component

#### 8.2.1.1 Component

Odoo Addon

#### 8.2.1.2 Log Level

INFO

#### 8.2.1.3 Output Format

JSON

#### 8.2.1.4 Destinations

- stdout

#### 8.2.1.5 Sampling

##### 8.2.1.5.1 Enabled

❌ No

##### 8.2.1.5.2 Rate



#### 8.2.1.6.0 Custom Fields

- tripId
- userId

### 8.2.2.0.0 Component

#### 8.2.2.1.0 Component

GPS Ingestion Microservice

#### 8.2.2.2.0 Log Level

INFO

#### 8.2.2.3.0 Output Format

JSON

#### 8.2.2.4.0 Destinations

- stdout

#### 8.2.2.5.0 Sampling

##### 8.2.2.5.1 Enabled

✅ Yes

##### 8.2.2.5.2 Rate

10% for successful ingestions

#### 8.2.2.6.0 Custom Fields

- vehicleId

## 8.3.0.0.0 Metrics

### 8.3.1.0.0 Custom Metrics

*No data available*

## 8.4.0.0.0 Alert Rules

### 8.4.1.0.0 DLQHasMessages

#### 8.4.1.1.0 Name

DLQHasMessages

#### 8.4.1.2.0 Condition

rabbitmq_queue_messages{queue="gps_location_dlq"} > 0

#### 8.4.1.3.0 Severity

Critical

#### 8.4.1.4.0 Actions

- {'type': 'Alertmanager', 'target': 'SRE Pager Channel', 'configuration': {}}

#### 8.4.1.5.0 Suppression Rules

*No items available*

#### 8.4.1.6.0 Escalation Path

*No items available*

### 8.4.2.0.0 GSPSyncApiHighErrorRate

#### 8.4.2.1.0 Name

GSPSyncApiHighErrorRate

#### 8.4.2.2.0 Condition

rate(gsp_api_errors_total[5m]) > 0.5

#### 8.4.2.3.0 Severity

High

#### 8.4.2.4.0 Actions

- {'type': 'Alertmanager', 'target': 'SRE Ticket Channel', 'configuration': {}}

#### 8.4.2.5.0 Suppression Rules

*No items available*

#### 8.4.2.6.0 Escalation Path

*No items available*

# 9.0.0.0.0 Implementation Priority

## 9.1.0.0.0 Component

### 9.1.1.0.0 Component

Structured Logging Implementation (Odoo & FastAPI)

### 9.1.2.0.0 Priority

🔴 high

### 9.1.3.0.0 Dependencies

*No items available*

### 9.1.4.0.0 Estimated Effort

Medium

### 9.1.5.0.0 Risk Level

low

## 9.2.0.0.0 Component

### 9.2.1.0.0 Component

Fluentbit -> OpenSearch Pipeline Setup

### 9.2.2.0.0 Priority

🔴 high

### 9.2.3.0.0 Dependencies

*No items available*

### 9.2.4.0.0 Estimated Effort

Medium

### 9.2.5.0.0 Risk Level

low

## 9.3.0.0.0 Component

### 9.3.1.0.0 Component

Critical Alerting Configuration (DLQ, Error Rates)

### 9.3.2.0.0 Priority

🔴 high

### 9.3.3.0.0 Dependencies

- Fluentbit -> OpenSearch Pipeline Setup

### 9.3.4.0.0 Estimated Effort

Low

### 9.3.5.0.0 Risk Level

low

## 9.4.0.0.0 Component

### 9.4.1.0.0 Component

Grafana Dashboard Creation

### 9.4.2.0.0 Priority

🟡 medium

### 9.4.3.0.0 Dependencies

- Fluentbit -> OpenSearch Pipeline Setup

### 9.4.4.0.0 Estimated Effort

Medium

### 9.4.5.0.0 Risk Level

low

# 10.0.0.0.0 Risk Assessment

## 10.1.0.0.0 Risk

### 10.1.1.0.0 Risk

Excessive log volume from the GPS microservice drives up costs.

### 10.1.2.0.0 Impact

medium

### 10.1.3.0.0 Probability

high

### 10.1.4.0.0 Mitigation

Implement log sampling for successful ingestion events at the source (FastAPI service). Set up cost alerts in AWS Budgets.

### 10.1.5.0.0 Contingency Plan

Adjust sampling rate or log level dynamically if costs exceed budget.

## 10.2.0.0.0 Risk

### 10.2.1.0.0 Risk

Sensitive PII or credentials are leaked into logs.

### 10.2.2.0.0 Impact

high

### 10.2.3.0.0 Probability

low

### 10.2.4.0.0 Mitigation

Enforce structured logging with a library that prevents logging of entire objects. Conduct code reviews focused on logging statements. Application-level masking of known PII fields.

### 10.2.5.0.0 Contingency Plan

Purge affected logs from OpenSearch immediately. Use OpenSearch's field masking capabilities as a secondary control. Trigger a security incident response process.

# 11.0.0.0.0 Recommendations

## 11.1.0.0.0 Category

### 11.1.1.0.0 Category

🔹 Observability

### 11.1.2.0.0 Recommendation

Enforce the generation and propagation of a `correlationId` for every transaction, starting at the edge (Nginx/API Gateway), through the application logic, and into any asynchronous messages (e.g., RabbitMQ headers).

### 11.1.3.0.0 Justification

This is the cornerstone of effective troubleshooting in this hybrid architecture and is essential for accurately measuring the end-to-end latency required by REQ-1-501.

### 11.1.4.0.0 Priority

🔴 high

### 11.1.5.0.0 Implementation Notes

Use Nginx's `$request_id` variable or a similar mechanism. In Python, use a context variable (`contextvars`) to implicitly carry the ID through the call stack.

## 11.2.0.0.0 Category

### 11.2.1.0.0 Category

🔹 Code Quality

### 11.2.2.0.0 Recommendation

Mandate the use of a dedicated structured logging library like `structlog` for all Python components (Odoo and FastAPI).

### 11.2.3.0.0 Justification

This ensures adherence to the JSON format (REQ-1-680), simplifies adding standard context fields (`correlationId`, `serviceName`), and reduces the risk of developers writing unstructured or improperly formatted log messages.

### 11.2.4.0.0 Priority

🔴 high

### 11.2.5.0.0 Implementation Notes

Create a shared logging configuration module that can be used by both the Odoo addon and the FastAPI service.

