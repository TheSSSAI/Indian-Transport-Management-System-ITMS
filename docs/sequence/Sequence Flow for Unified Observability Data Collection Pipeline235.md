# 1 Overview

## 1.1 Diagram Id

SEQ-OP-012

## 1.2 Name

Unified Observability Data Collection Pipeline

## 1.3 Description

An operational flow demonstrating how structured logs and time-series metrics are collected from application pods running in EKS and aggregated into the central observability platform (Prometheus and OpenSearch) for unified monitoring.

## 1.4 Type

🔹 OperationalFlow

## 1.5 Purpose

To provide a holistic, real-time view of system health, application performance, and operational behavior, fulfilling the comprehensive monitoring requirements.

## 1.6 Complexity

High

## 1.7 Priority

🔴 High

## 1.8 Frequency

Hourly

## 1.9 Participants

*No items available*

## 1.10 Key Interactions

- The Odoo application pod writes a structured JSON log message to `stdout`.
- Fluentbit, running as a DaemonSet on the EKS node, tails the container's log file.
- Fluentbit enriches the log with Kubernetes metadata (e.g., pod name, namespace, labels).
- Fluentbit forwards the enriched log record via HTTPS to the OpenSearch cluster for indexing.
- Concurrently, the central Prometheus server scrapes the `/metrics` HTTP endpoint exposed by the Odoo pod.
- Prometheus ingests the exposed time-series metrics (e.g., request latency, error counts) into its TSDB.
- An SRE uses a Grafana dashboard that queries both Prometheus (for metrics) and OpenSearch (for logs) to investigate an issue.

## 1.11 Triggers

- An application event occurs, which generates a log message and updates a metric counter.

## 1.12 Outcomes

- Application logs are indexed and searchable in OpenSearch within seconds of being generated.
- Application and infrastructure metrics are queryable in Prometheus within the defined scrape interval (e.g., 30s).
- System health can be visualized in real-time on unified Grafana dashboards.

## 1.13 Business Rules

- REQ-REP-003: The system shall use Prometheus for metrics, Fluentbit for log collection, OpenSearch for log storage, and Grafana for visualization.
- REQ-REP-003: Application logs shall be written in a structured JSON format to facilitate efficient parsing and analysis.

## 1.14 Error Scenarios

- Fluentbit loses connection to OpenSearch; it buffers logs on local disk and retries, preventing data loss.
- Prometheus fails to scrape a target pod; the target is marked as 'down' in the UI and an alert can be triggered.

## 1.15 Integration Points

- Orchestration: Amazon EKS
- Log Storage: OpenSearch
- Metrics Storage: Prometheus

# 2.0 Details

## 2.1 Diagram Id

SEQ-OP-012

## 2.2 Name

Unified Observability Data Collection and Visualization Pipeline

## 2.3 Description

Technical sequence demonstrating the parallel collection of structured JSON logs and time-series metrics from an application pod within Amazon EKS. Logs are collected by a Fluentbit agent, enriched with Kubernetes metadata, and forwarded to an OpenSearch cluster. Metrics are scraped from a `/metrics` endpoint by a Prometheus server. The flow culminates with a Site Reliability Engineer (SRE) utilizing a Grafana dashboard to query both data sources for unified system analysis, fulfilling REQ-REP-003.

## 2.4 Participants

### 2.4.1 Human Actor

#### 2.4.1.1 Repository Id

actor-sre

#### 2.4.1.2 Display Name

SRE

#### 2.4.1.3 Type

🔹 Human Actor

#### 2.4.1.4 Technology

Web Browser

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #90CAF9 |
| Stereotype | User |

### 2.4.2.0 Observability Platform

#### 2.4.2.1 Repository Id

infra-grafana

#### 2.4.2.2 Display Name

Grafana

#### 2.4.2.3 Type

🔹 Observability Platform

#### 2.4.2.4 Technology

Grafana 11.1.x

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #FFAB00 |
| Stereotype | Visualization |

### 2.4.3.0 Log Aggregation Store

#### 2.4.3.1 Repository Id

infra-opensearch

#### 2.4.3.2 Display Name

OpenSearch Cluster

#### 2.4.3.3 Type

🔹 Log Aggregation Store

#### 2.4.3.4 Technology

AWS Managed OpenSearch 2.15.x

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #00BFA5 |
| Stereotype | Log Store |

### 2.4.4.0 Metrics Store

#### 2.4.4.1 Repository Id

infra-prometheus

#### 2.4.4.2 Display Name

Prometheus Server

#### 2.4.4.3 Type

🔹 Metrics Store

#### 2.4.4.4 Technology

Prometheus 2.53.x

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #E65100 |
| Stereotype | TSDB |

### 2.4.5.0 Log Collector

#### 2.4.5.1 Repository Id

infra-fluentbit

#### 2.4.5.2 Display Name

Fluentbit Agent

#### 2.4.5.3 Type

🔹 Log Collector

#### 2.4.5.4 Technology

Fluentbit 3.0.x (DaemonSet)

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #4CAF50 |
| Stereotype | Agent |

### 2.4.6.0 Platform Infrastructure

#### 2.4.6.1 Repository Id

platform-eks-node

#### 2.4.6.2 Display Name

EKS Node / Container Runtime

#### 2.4.6.3 Type

🔹 Platform Infrastructure

#### 2.4.6.4 Technology

Amazon Linux 2 / containerd

#### 2.4.6.5 Order

6

#### 2.4.6.6 Style

| Property | Value |
|----------|-------|
| Shape | node |
| Color | #BDBDBD |
| Stereotype | Infrastructure |

### 2.4.7.0 Application Container

#### 2.4.7.1 Repository Id

REPO-TMS-CORE

#### 2.4.7.2 Display Name

Odoo Application Pod

#### 2.4.7.3 Type

🔹 Application Container

#### 2.4.7.4 Technology

Odoo 18 / Python 3.11

#### 2.4.7.5 Order

7

#### 2.4.7.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #7E57C2 |
| Stereotype | Application |

## 2.5.0.0 Interactions

### 2.5.1.0 Internal Processing

#### 2.5.1.1 Source Id

REPO-TMS-CORE

#### 2.5.1.2 Target Id

REPO-TMS-CORE

#### 2.5.1.3 Message

1. Application event occurs (e.g., Trip status changes).

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Internal Processing

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
| Protocol | In-Process |
| Method | handle_event() |
| Parameters | Event data object |
| Authentication | N/A |
| Error Handling | Standard try/except block. |
| Performance | Sub-millisecond latency. |

### 2.5.2.0 Log Output

#### 2.5.2.1 Source Id

REPO-TMS-CORE

#### 2.5.2.2 Target Id

platform-eks-node

#### 2.5.2.3 Message

2. Writes structured JSON log to stdout.

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 Log Output

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

Container runtime captures log.

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | File I/O (stdout stream) |
| Method | write() |
| Parameters | JSON string payload adhering to REQ-REP-003. e.g.,... |
| Authentication | N/A |
| Error Handling | Handled by container runtime. |
| Performance | High throughput, low latency. |

### 2.5.3.0 File Read

#### 2.5.3.1 Source Id

platform-eks-node

#### 2.5.3.2 Target Id

infra-fluentbit

#### 2.5.3.3 Message

3. Tailing container log file.

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 File Read

#### 2.5.3.6 Is Synchronous

❌ No

#### 2.5.3.7 Return Message



#### 2.5.3.8 Has Return

❌ No

#### 2.5.3.9 Is Activation

✅ Yes

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Filesystem (inotify) |
| Method | tail input plugin |
| Parameters | Path: `/var/log/containers/*.log`, Parser: `docker... |
| Authentication | Filesystem permissions. |
| Error Handling | Retries on read errors; tracks file offset to prev... |
| Performance | Optimized for low CPU/memory overhead. |

### 2.5.4.0 Data Enrichment

#### 2.5.4.1 Source Id

infra-fluentbit

#### 2.5.4.2 Target Id

infra-fluentbit

#### 2.5.4.3 Message

4. Enriches log with Kubernetes metadata.

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 Data Enrichment

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
| Protocol | In-Memory |
| Method | kubernetes filter plugin |
| Parameters | Adds labels like `pod_name`, `namespace`, `contain... |
| Authentication | ServiceAccount token to access Kube API server. |
| Error Handling | Caches metadata to reduce API server load and hand... |
| Performance | Sub-millisecond processing per record. |

### 2.5.5.0 Data Ingestion

#### 2.5.5.1 Source Id

infra-fluentbit

#### 2.5.5.2 Target Id

infra-opensearch

#### 2.5.5.3 Message

5. Forwards enriched log batch.

#### 2.5.5.4 Sequence Number

5

#### 2.5.5.5 Type

🔹 Data Ingestion

#### 2.5.5.6 Is Synchronous

✅ Yes

#### 2.5.5.7 Return Message

6. 200 OK

#### 2.5.5.8 Has Return

✅ Yes

#### 2.5.5.9 Is Activation

❌ No

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | POST /_bulk |
| Parameters | Batch of NDJSON log records. `Content-Type: applic... |
| Authentication | AWS IAM role (IRSA) or SigV4 signing. |
| Error Handling | Implements exponential backoff on 5xx errors. Buff... |
| Performance | Batching improves throughput. Latency target < 2s ... |

### 2.5.6.0 Metrics Collection

#### 2.5.6.1 Source Id

infra-prometheus

#### 2.5.6.2 Target Id

REPO-TMS-CORE

#### 2.5.6.3 Message

7. Scrape metrics endpoint.

#### 2.5.6.4 Sequence Number

7

#### 2.5.6.5 Type

🔹 Metrics Collection

#### 2.5.6.6 Is Synchronous

✅ Yes

#### 2.5.6.7 Return Message

8. Prometheus exposition format text.

#### 2.5.6.8 Has Return

✅ Yes

#### 2.5.6.9 Is Activation

❌ No

#### 2.5.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP |
| Method | GET /metrics |
| Parameters | `Accept: application/openmetrics-text` header. |
| Authentication | Network policies restrict access to Prometheus nam... |
| Error Handling | If scrape fails, Prometheus marks the target as 'd... |
| Performance | Scrape interval: 30s. Scrape timeout: 10s. |

### 2.5.7.0 User Interaction

#### 2.5.7.1 Source Id

actor-sre

#### 2.5.7.2 Target Id

infra-grafana

#### 2.5.7.3 Message

9. Accesses 'TMS System Health' dashboard.

#### 2.5.7.4 Sequence Number

9

#### 2.5.7.5 Type

🔹 User Interaction

#### 2.5.7.6 Is Synchronous

✅ Yes

#### 2.5.7.7 Return Message

10. Renders dashboard UI.

#### 2.5.7.8 Has Return

✅ Yes

#### 2.5.7.9 Is Activation

✅ Yes

#### 2.5.7.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | GET /d/tms-health |
| Parameters | Time range parameters (e.g., `from=now-1h&to=now`)... |
| Authentication | SSO (e.g., OIDC, SAML). |
| Error Handling | Standard HTTP error pages. |
| Performance | Dashboard load time < 3s. |

### 2.5.8.0 Data Query

#### 2.5.8.1 Source Id

infra-grafana

#### 2.5.8.2 Target Id

infra-prometheus

#### 2.5.8.3 Message

11. Queries for metrics data.

#### 2.5.8.4 Sequence Number

11

#### 2.5.8.5 Type

🔹 Data Query

#### 2.5.8.6 Is Synchronous

✅ Yes

#### 2.5.8.7 Return Message

12. Time-series data (JSON).

#### 2.5.8.8 Has Return

✅ Yes

#### 2.5.8.9 Is Activation

❌ No

#### 2.5.8.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP |
| Method | POST /api/v1/query_range |
| Parameters | PromQL query, e.g., `rate(http_requests_total{job=... |
| Authentication | API token or internal service authentication. |
| Error Handling | Grafana displays query error in the panel if Prome... |
| Performance | Query latency target < 1s for typical dashboard qu... |

### 2.5.9.0 Data Query

#### 2.5.9.1 Source Id

infra-grafana

#### 2.5.9.2 Target Id

infra-opensearch

#### 2.5.9.3 Message

13. Queries for log data.

#### 2.5.9.4 Sequence Number

13

#### 2.5.9.5 Type

🔹 Data Query

#### 2.5.9.6 Is Synchronous

✅ Yes

#### 2.5.9.7 Return Message

14. Log documents (JSON).

#### 2.5.9.8 Has Return

✅ Yes

#### 2.5.9.9 Is Activation

❌ No

#### 2.5.9.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP |
| Method | POST /_msearch |
| Parameters | OpenSearch DSL or Lucene query, e.g., `kubernetes.... |
| Authentication | Grafana data source credentials (e.g., user/pass, ... |
| Error Handling | Grafana displays query error in the panel if OpenS... |
| Performance | Query latency target < 2s for indexed fields. |

### 2.5.10.0 Data Visualization

#### 2.5.10.1 Source Id

infra-grafana

#### 2.5.10.2 Target Id

actor-sre

#### 2.5.10.3 Message

15. Presents unified view with correlated logs and metrics.

#### 2.5.10.4 Sequence Number

15

#### 2.5.10.5 Type

🔹 Data Visualization

#### 2.5.10.6 Is Synchronous

❌ No

#### 2.5.10.7 Return Message



#### 2.5.10.8 Has Return

❌ No

#### 2.5.10.9 Is Activation

❌ No

#### 2.5.10.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS / WebSocket |
| Method | N/A |
| Parameters | JSON data models for charts and logs panels. |
| Authentication | N/A |
| Error Handling | UI gracefully handles partial data if one data sou... |
| Performance | Real-time updates with configurable refresh interv... |

## 2.6.0.0 Notes

### 2.6.1.0 Content

#### 2.6.1.1 Content

Log collection (Steps 2-6) and Metrics collection (Steps 7-8) happen concurrently and continuously in the background.

#### 2.6.1.2 Position

top

#### 2.6.1.3 Participant Id

*Not specified*

#### 2.6.1.4 Sequence Number

1

### 2.6.2.0 Content

#### 2.6.2.1 Content

REQ-REP-003 mandates this entire observability stack. Configuration is managed via IaC (Terraform) and GitOps.

#### 2.6.2.2 Position

bottom

#### 2.6.2.3 Participant Id

*Not specified*

#### 2.6.2.4 Sequence Number

15

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | Access to Grafana, OpenSearch, and Prometheus UIs ... |
| Performance Targets | Log ingestion latency (app write to OpenSearch ind... |
| Error Handling Strategy | Fluentbit MUST be configured with a persistent loc... |
| Testing Considerations | In staging, generate synthetic logs and metrics to... |
| Monitoring Requirements | Meta-monitoring is critical. A dedicated Grafana d... |
| Deployment Considerations | All observability components (Prometheus, Grafana,... |

