# 1 System Overview

## 1.1 Analysis Date

2025-06-13

## 1.2 Technology Stack

- Odoo 18
- Python 3.11
- FastAPI
- PostgreSQL 16 (AWS RDS)
- RabbitMQ (Amazon MQ)
- Amazon EKS
- Docker

## 1.3 Metrics Configuration

- Prometheus for metrics collection from applications, middleware, and infrastructure.
- Alertmanager for alert routing, grouping, and notification.
- Fluentbit and OpenSearch for centralized log aggregation.

## 1.4 Monitoring Needs

- Ensure 99.9% uptime and adherence to performance SLOs (e.g., <200ms p95 API latency, <10s GPS processing latency).
- Detect and respond to integration failures with third-party services (GPS, GSP).
- Monitor the health of the asynchronous processing pipeline, including message queue depth and dead-letter queue status.
- Track infrastructure and application resource utilization to prevent capacity-related outages.

## 1.5 Environment

production

# 2.0 Alert Condition And Threshold Design

## 2.1 Critical Metrics Alerts

### 2.1.1 Metric

#### 2.1.1.1 Metric

probe_success

#### 2.1.1.2 Condition

== 0 for 1m

#### 2.1.1.3 Threshold Type

static

#### 2.1.1.4 Value

0

#### 2.1.1.5 Justification

REQ-1-502 requires 99.9% uptime. This alert detects when the primary application endpoint is completely unavailable.

#### 2.1.1.6 Business Impact

Critical: System is down, preventing all user operations.

### 2.1.2.0 Metric

#### 2.1.2.1 Metric

rabbitmq_queue_messages_ready

#### 2.1.2.2 Condition

> 0

#### 2.1.2.3 Threshold Type

static

#### 2.1.2.4 Value

0

#### 2.1.2.5 Justification

REQ-1-301 mandates a dead-letter queue (DLQ) for un-processable GPS messages. Any message in the DLQ indicates a persistent failure and potential data loss.

#### 2.1.2.6 Business Impact

Critical: Indicates a systemic issue with GPS data processing that requires manual intervention.

### 2.1.3.0 Metric

#### 2.1.3.1 Metric

http_request_duration_seconds_p95

#### 2.1.3.2 Condition

> 0.2s for 5m

#### 2.1.3.3 Threshold Type

static

#### 2.1.3.4 Value

0.2

#### 2.1.3.5 Justification

REQ-1-500 specifies that 95% of standard GET requests must complete in under 200ms. This alert detects SLO violations.

#### 2.1.3.6 Business Impact

High: Poor user experience, potential impact on operational efficiency.

### 2.1.4.0 Metric

#### 2.1.4.1 Metric

gsp_api_error_rate_5m

#### 2.1.4.2 Condition

> 10%

#### 2.1.4.3 Threshold Type

static

#### 2.1.4.4 Value

0.1

#### 2.1.4.5 Justification

REQ-1-302 defines a fallback mechanism for GSP integration failures. A high error rate indicates a problem with the provider or our integration, impacting the primary invoicing workflow.

#### 2.1.4.6 Business Impact

High: Delays in GST-compliant e-invoicing, requiring manual follow-up.

### 2.1.5.0 Metric

#### 2.1.5.1 Metric

kube_pod_container_resource_limits_cpu_throttling_seconds_total

#### 2.1.5.2 Condition

rate > 0.1

#### 2.1.5.3 Threshold Type

static

#### 2.1.5.4 Value

0.1

#### 2.1.5.5 Justification

Based on the EKS deployment model (REQ-1-014), CPU throttling indicates insufficient resources, which is a leading cause of latency and performance issues.

#### 2.1.5.6 Business Impact

Medium: Precursor to performance degradation and potential SLO violations.

## 2.2.0.0 Threshold Strategies

*No items available*

## 2.3.0.0 Baseline Deviation Alerts

*No items available*

## 2.4.0.0 Predictive Alerts

- {'metric': 'rabbitmq_queue_messages_ready{queue="q.tms.location_updates"}', 'predictionWindow': '1h', 'confidenceThreshold': '90%', 'algorithm': 'predict_linear', 'trainingPeriod': '1h'}

## 2.5.0.0 Compound Conditions

- {'name': 'OdooConsumerStalled', 'conditions': ['rabbitmq_queue_messages_ready{queue="q.tms.location_updates"} > 1000', 'rabbitmq_consumer_ack_rate{queue="q.tms.location_updates"} == 0'], 'logic': 'AND', 'timeWindow': '10m', 'justification': 'Detects a situation where the GPS data queue is backing up and the Odoo consumer is not processing any messages, indicating a complete stall.'}

# 3.0.0.0 Severity Level Classification

## 3.1.0.0 Severity Definitions

### 3.1.1.0 Level

#### 3.1.1.1 Level

🚨 Critical

#### 3.1.1.2 Criteria

Complete service unavailability, critical data integrity risk (e.g., DLQ), or major security breach. Requires immediate, automated wake-up notification and response.

#### 3.1.1.3 Business Impact

System-wide operational halt, significant revenue loss, regulatory non-compliance.

#### 3.1.1.4 Customer Impact

All users unable to access the system.

#### 3.1.1.5 Response Time

<5 minutes

#### 3.1.1.6 Escalation Required

✅ Yes

### 3.1.2.0 Level

#### 3.1.2.1 Level

🔴 High

#### 3.1.2.2 Criteria

Core business function significantly degraded (e.g., GSP integration failing), or SLO violation is occurring. Requires immediate attention during business hours.

#### 3.1.2.3 Business Impact

Impact on a key business process, risk of financial penalty, poor user experience.

#### 3.1.2.4 Customer Impact

A specific, critical workflow is failing or unusably slow.

#### 3.1.2.5 Response Time

<15 minutes

#### 3.1.2.6 Escalation Required

✅ Yes

### 3.1.3.0 Level

#### 3.1.3.1 Level

🟡 Medium

#### 3.1.3.2 Criteria

System performance is degrading, or a component is approaching resource limits. Indicates a potential future problem. Does not require immediate action.

#### 3.1.3.3 Business Impact

Potential for future service degradation if left unaddressed.

#### 3.1.3.4 Customer Impact

No direct customer impact, or minor intermittent issues.

#### 3.1.3.5 Response Time

<1 hour

#### 3.1.3.6 Escalation Required

❌ No

### 3.1.4.0 Level

#### 3.1.4.1 Level

⚠️ Warning

#### 3.1.4.2 Criteria

Informational alert about a non-critical condition, such as a scheduled job failing to run once or a resource reaching a soft limit.

#### 3.1.4.3 Business Impact

Low.

#### 3.1.4.4 Customer Impact

None.

#### 3.1.4.5 Response Time

Best Effort (24 hours)

#### 3.1.4.6 Escalation Required

❌ No

## 3.2.0.0 Business Impact Matrix

*No items available*

## 3.3.0.0 Customer Impact Criteria

*No items available*

## 3.4.0.0 Sla Violation Severity

*No items available*

## 3.5.0.0 System Health Severity

*No items available*

# 4.0.0.0 Notification Channel Strategy

## 4.1.0.0 Channel Configuration

### 4.1.1.0 Channel

#### 4.1.1.1 Channel

pagerduty

#### 4.1.1.2 Purpose

On-call alerting for critical, automated wake-up notifications.

#### 4.1.1.3 Applicable Severities

- Critical

#### 4.1.1.4 Time Constraints

24/7

#### 4.1.1.5 Configuration

*No data available*

### 4.1.2.0 Channel

#### 4.1.2.1 Channel

slack

#### 4.1.2.2 Purpose

Real-time team communication for all alert severities, routed to different channels.

#### 4.1.2.3 Applicable Severities

- Critical
- High
- Medium
- Warning

#### 4.1.2.4 Time Constraints

24/7

#### 4.1.2.5 Configuration

*No data available*

### 4.1.3.0 Channel

#### 4.1.3.1 Channel

email

#### 4.1.3.2 Purpose

Daily summaries and non-urgent notifications.

#### 4.1.3.3 Applicable Severities

- Warning

#### 4.1.3.4 Time Constraints

N/A

#### 4.1.3.5 Configuration

*No data available*

## 4.2.0.0 Routing Rules

### 4.2.1.0 Condition

#### 4.2.1.1 Condition

severity == 'Critical'

#### 4.2.1.2 Severity

Critical

#### 4.2.1.3 Alert Type

Any

#### 4.2.1.4 Channels

- pagerduty
- slack-critical

#### 4.2.1.5 Priority

🔹 1

### 4.2.2.0 Condition

#### 4.2.2.1 Condition

severity == 'High'

#### 4.2.2.2 Severity

High

#### 4.2.2.3 Alert Type

Any

#### 4.2.2.4 Channels

- slack-critical

#### 4.2.2.5 Priority

🔹 2

### 4.2.3.0 Condition

#### 4.2.3.1 Condition

severity == 'Medium'

#### 4.2.3.2 Severity

Medium

#### 4.2.3.3 Alert Type

Any

#### 4.2.3.4 Channels

- slack-warnings

#### 4.2.3.5 Priority

🔹 3

## 4.3.0.0 Time Based Routing

*No items available*

## 4.4.0.0 Ticketing Integration

- {'system': 'jira', 'triggerConditions': ["severity == 'Critical'", "severity == 'High'"], 'ticketPriority': 'Highest for Critical, High for High', 'autoAssignment': True}

## 4.5.0.0 Emergency Notifications

*No items available*

## 4.6.0.0 Chat Platform Integration

*No items available*

# 5.0.0.0 Alert Correlation Implementation

## 5.1.0.0 Grouping Requirements

- {'groupingCriteria': 'alertname, cluster, namespace, service', 'timeWindow': '5m', 'maxGroupSize': 0, 'suppressionStrategy': 'Group alerts with the same labels into a single notification to reduce noise.'}

## 5.2.0.0 Parent Child Relationships

- {'parentCondition': 'Alert: AWSRDSUnavailable', 'childConditions': ['Alert: OdooDatabaseConnectionError'], 'suppressionDuration': 'While parent is active', 'propagationRules': 'If the database is down, suppress application-level connection errors as they are symptoms, not the root cause.'}

## 5.3.0.0 Topology Based Correlation

*No items available*

## 5.4.0.0 Time Window Correlation

*No items available*

## 5.5.0.0 Causal Relationship Detection

*No items available*

## 5.6.0.0 Maintenance Window Suppression

### 5.6.1.0 Maintenance Type

Scheduled Deployments, Database Maintenance

### 5.6.2.0 Suppression Scope

- service
- cluster

### 5.6.3.0 Automatic Detection

❌ No

### 5.6.4.0 Manual Override

✅ Yes

# 6.0.0.0 False Positive Mitigation

## 6.1.0.0 Noise Reduction Strategies

- {'strategy': "Use of 'for' clause in Prometheus", 'implementation': 'Require an alert condition to persist for a specified duration (e.g., 2-5 minutes) before firing.', 'applicableAlerts': ['HighApiLatency', 'HighResourceUsageEks'], 'effectiveness': 'High. Prevents alerts from transient spikes or brief network blips.'}

## 6.2.0.0 Confirmation Counts

*No items available*

## 6.3.0.0 Dampening And Flapping

*No items available*

## 6.4.0.0 Alert Validation

*No items available*

## 6.5.0.0 Smart Filtering

*No items available*

## 6.6.0.0 Quorum Based Alerting

*No items available*

# 7.0.0.0 On Call Management Integration

## 7.1.0.0 Escalation Paths

- {'severity': 'Critical', 'escalationLevels': [{'level': 1, 'recipients': ['Primary On-Call Engineer (via PagerDuty)'], 'escalationTime': '15m', 'requiresAcknowledgment': True}, {'level': 2, 'recipients': ['Secondary On-Call Engineer, Team Lead (via PagerDuty)'], 'escalationTime': '15m', 'requiresAcknowledgment': True}], 'ultimateEscalation': 'Engineering Manager'}

## 7.2.0.0 Escalation Timeframes

*No items available*

## 7.3.0.0 On Call Rotation

*No items available*

## 7.4.0.0 Acknowledgment Requirements

- {'severity': 'Critical', 'acknowledgmentTimeout': '15m', 'autoEscalation': True, 'requiresComment': False}

## 7.5.0.0 Incident Ownership

*No items available*

## 7.6.0.0 Follow The Sun Support

*No items available*

# 8.0.0.0 Project Specific Alerts Config

## 8.1.0.0 Alerts

### 8.1.1.0 WebAppUnresponsive

#### 8.1.1.1 Name

WebAppUnresponsive

#### 8.1.1.2 Description

The main TMS application web endpoint is not responding to HTTP probes.

#### 8.1.1.3 Condition

probe_success{job="blackbox-http", instance="https://tms.example.com"} == 0 for 1m

#### 8.1.1.4 Threshold

== 0

#### 8.1.1.5 Severity

Critical

#### 8.1.1.6 Channels

- pagerduty
- slack-critical

#### 8.1.1.7 Correlation

##### 8.1.1.7.1 Group Id

app-availability

##### 8.1.1.7.2 Suppression Rules

*No items available*

#### 8.1.1.8.0 Escalation

##### 8.1.1.8.1 Enabled

✅ Yes

##### 8.1.1.8.2 Escalation Time

15m

##### 8.1.1.8.3 Escalation Path

- L1 On-call
- L2 On-call

#### 8.1.1.9.0 Suppression

| Property | Value |
|----------|-------|
| Maintenance Window | ✅ |
| Dependency Failure | ✅ |
| Manual Override | ✅ |

#### 8.1.1.10.0 Validation

##### 8.1.1.10.1 Confirmation Count

0

##### 8.1.1.10.2 Confirmation Window

1m

#### 8.1.1.11.0 Remediation

##### 8.1.1.11.1 Automated Actions

*No items available*

##### 8.1.1.11.2 Runbook Url

🔗 [https://runbooks.example.com/tms/webapp-unresponsive](https://runbooks.example.com/tms/webapp-unresponsive)

##### 8.1.1.11.3 Troubleshooting Steps

- Check EKS pod status for Odoo and Nginx.
- Verify AWS load balancer health checks.
- Inspect pod logs for crash loops or critical errors.

### 8.1.2.0.0 GpsDlqNotEmpty

#### 8.1.2.1.0 Name

GpsDlqNotEmpty

#### 8.1.2.2.0 Description

One or more messages are in the GPS data Dead-Letter Queue, indicating a persistent processing failure.

#### 8.1.2.3.0 Condition

rabbitmq_queue_messages_ready{queue="q.tms.location_updates.dlq"} > 0

#### 8.1.2.4.0 Threshold

> 0

#### 8.1.2.5.0 Severity

Critical

#### 8.1.2.6.0 Channels

- pagerduty
- slack-critical

#### 8.1.2.7.0 Correlation

##### 8.1.2.7.1 Group Id

gps-pipeline-failure

##### 8.1.2.7.2 Suppression Rules

*No items available*

#### 8.1.2.8.0 Escalation

##### 8.1.2.8.1 Enabled

✅ Yes

##### 8.1.2.8.2 Escalation Time

15m

##### 8.1.2.8.3 Escalation Path

- L1 On-call
- L2 On-call

#### 8.1.2.9.0 Suppression

| Property | Value |
|----------|-------|
| Maintenance Window | ✅ |
| Dependency Failure | ❌ |
| Manual Override | ✅ |

#### 8.1.2.10.0 Validation

##### 8.1.2.10.1 Confirmation Count

0

##### 8.1.2.10.2 Confirmation Window

0m

#### 8.1.2.11.0 Remediation

##### 8.1.2.11.1 Automated Actions

*No items available*

##### 8.1.2.11.2 Runbook Url

🔗 [https://runbooks.example.com/tms/gps-dlq-investigation](https://runbooks.example.com/tms/gps-dlq-investigation)

##### 8.1.2.11.3 Troubleshooting Steps

- Inspect message contents in the DLQ via RabbitMQ UI.
- Analyze Odoo consumer logs for the corresponding error.
- Identify root cause (e.g., malformed data, bug in consumer).
- Decide whether to discard, repair, or redrive the message.

### 8.1.3.0.0 HighApiLatency

#### 8.1.3.1.0 Name

HighApiLatency

#### 8.1.3.2.0 Description

The p95 request latency for the core Odoo application has exceeded the 200ms SLO.

#### 8.1.3.3.0 Condition

histogram_quantile(0.95, sum(rate(http_request_duration_seconds_bucket{service="odoo-monolith", job!="blackbox-http"}[5m])) by (le)) > 0.2 for 5m

#### 8.1.3.4.0 Threshold

> 0.2s

#### 8.1.3.5.0 Severity

High

#### 8.1.3.6.0 Channels

- slack-critical

#### 8.1.3.7.0 Correlation

##### 8.1.3.7.1 Group Id

app-performance

##### 8.1.3.7.2 Suppression Rules

- Suppress if AWSRDSUnavailable is firing.

#### 8.1.3.8.0 Escalation

##### 8.1.3.8.1 Enabled

❌ No

##### 8.1.3.8.2 Escalation Time



##### 8.1.3.8.3 Escalation Path

*No items available*

#### 8.1.3.9.0 Suppression

| Property | Value |
|----------|-------|
| Maintenance Window | ✅ |
| Dependency Failure | ✅ |
| Manual Override | ✅ |

#### 8.1.3.10.0 Validation

##### 8.1.3.10.1 Confirmation Count

0

##### 8.1.3.10.2 Confirmation Window

5m

#### 8.1.3.11.0 Remediation

##### 8.1.3.11.1 Automated Actions

*No items available*

##### 8.1.3.11.2 Runbook Url

🔗 [https://runbooks.example.com/tms/high-api-latency](https://runbooks.example.com/tms/high-api-latency)

##### 8.1.3.11.3 Troubleshooting Steps

- Check RDS CPU and active connections.
- Analyze slow query logs in PostgreSQL.
- Check Odoo pod CPU/Memory utilization and for throttling.

### 8.1.4.0.0 GspIntegrationErrorRateHigh

#### 8.1.4.1.0 Name

GspIntegrationErrorRateHigh

#### 8.1.4.2.0 Description

The error rate for API calls to the GSP for e-invoicing is over 10%.

#### 8.1.4.3.0 Condition

sum(rate(http_requests_total{job="odoo-monolith", handler="/gsp/invoice", code=~"5.."}[5m])) / sum(rate(http_requests_total{job="odoo-monolith", handler="/gsp/invoice"}[5m])) > 0.1 for 5m

#### 8.1.4.4.0 Threshold

> 10%

#### 8.1.4.5.0 Severity

High

#### 8.1.4.6.0 Channels

- slack-critical

#### 8.1.4.7.0 Correlation

##### 8.1.4.7.1 Group Id

external-integrations

##### 8.1.4.7.2 Suppression Rules

*No items available*

#### 8.1.4.8.0 Escalation

##### 8.1.4.8.1 Enabled

❌ No

##### 8.1.4.8.2 Escalation Time



##### 8.1.4.8.3 Escalation Path

*No items available*

#### 8.1.4.9.0 Suppression

| Property | Value |
|----------|-------|
| Maintenance Window | ✅ |
| Dependency Failure | ❌ |
| Manual Override | ✅ |

#### 8.1.4.10.0 Validation

##### 8.1.4.10.1 Confirmation Count

0

##### 8.1.4.10.2 Confirmation Window

5m

#### 8.1.4.11.0 Remediation

##### 8.1.4.11.1 Automated Actions

*No items available*

##### 8.1.4.11.2 Runbook Url

🔗 [https://runbooks.example.com/tms/gsp-integration-errors](https://runbooks.example.com/tms/gsp-integration-errors)

##### 8.1.4.11.3 Troubleshooting Steps

- Check the third-party GSP provider's status page.
- Inspect Odoo logs for specific error messages and payloads sent.
- Verify API keys and credentials in AWS Secrets Manager have not expired.

### 8.1.5.0.0 RabbitMqGpsQueueGrowing

#### 8.1.5.1.0 Name

RabbitMqGpsQueueGrowing

#### 8.1.5.2.0 Description

The GPS data queue is predicted to grow beyond 10,000 messages in the next hour, indicating a slow consumer.

#### 8.1.5.3.0 Condition

predict_linear(rabbitmq_queue_messages_ready{queue="q.tms.location_updates"}[1h], 3600) > 10000

#### 8.1.5.4.0 Threshold

> 10000 (predicted)

#### 8.1.5.5.0 Severity

Medium

#### 8.1.5.6.0 Channels

- slack-warnings

#### 8.1.5.7.0 Correlation

##### 8.1.5.7.1 Group Id

gps-pipeline-performance

##### 8.1.5.7.2 Suppression Rules

*No items available*

#### 8.1.5.8.0 Escalation

##### 8.1.5.8.1 Enabled

❌ No

##### 8.1.5.8.2 Escalation Time



##### 8.1.5.8.3 Escalation Path

*No items available*

#### 8.1.5.9.0 Suppression

| Property | Value |
|----------|-------|
| Maintenance Window | ✅ |
| Dependency Failure | ❌ |
| Manual Override | ✅ |

#### 8.1.5.10.0 Validation

##### 8.1.5.10.1 Confirmation Count

0

##### 8.1.5.10.2 Confirmation Window

0m

#### 8.1.5.11.0 Remediation

##### 8.1.5.11.1 Automated Actions

*No items available*

##### 8.1.5.11.2 Runbook Url

🔗 [https://runbooks.example.com/tms/rabbitmq-queue-growing](https://runbooks.example.com/tms/rabbitmq-queue-growing)

##### 8.1.5.11.3 Troubleshooting Steps

- Investigate Odoo consumer performance.
- Check for slow DB writes or resource contention on the Odoo pods.
- Consider scaling up the number of Odoo consumer workers if load is sustained.

## 8.2.0.0.0 Alert Groups

*No items available*

## 8.3.0.0.0 Notification Templates

*No items available*

# 9.0.0.0.0 Implementation Priority

## 9.1.0.0.0 Component

### 9.1.1.0.0 Component

Critical Alerts (WebAppUnresponsive, GpsDlqNotEmpty)

### 9.1.2.0.0 Priority

🔴 high

### 9.1.3.0.0 Dependencies

- Prometheus, Alertmanager, PagerDuty Integration

### 9.1.4.0.0 Estimated Effort

Medium

### 9.1.5.0.0 Risk Level

low

## 9.2.0.0.0 Component

### 9.2.1.0.0 Component

High Severity Alerts (HighApiLatency, GspIntegrationErrorRateHigh)

### 9.2.2.0.0 Priority

🔴 high

### 9.2.3.0.0 Dependencies

- Application-level metrics instrumentation

### 9.2.4.0.0 Estimated Effort

Medium

### 9.2.5.0.0 Risk Level

medium

## 9.3.0.0.0 Component

### 9.3.1.0.0 Component

Medium/Warning Alerts (RabbitMqGpsQueueGrowing)

### 9.3.2.0.0 Priority

🟡 medium

### 9.3.3.0.0 Dependencies

- RabbitMQ exporter setup

### 9.3.4.0.0 Estimated Effort

Low

### 9.3.5.0.0 Risk Level

low

# 10.0.0.0.0 Risk Assessment

## 10.1.0.0.0 Risk

### 10.1.1.0.0 Risk

Alert Fatigue

### 10.1.2.0.0 Impact

high

### 10.1.3.0.0 Probability

high

### 10.1.4.0.0 Mitigation

Strictly limit the number of waking alerts to only Critical severity. Use aggressive grouping, `for` clauses, and appropriate severities for all other conditions. Regularly review and tune noisy alerts.

### 10.1.5.0.0 Contingency Plan

If fatigue occurs, conduct an immediate audit of all firing alerts to raise thresholds, lengthen `for` durations, or downgrade severity.

## 10.2.0.0.0 Risk

### 10.2.1.0.0 Risk

Missed Critical Alert

### 10.2.2.0.0 Impact

high

### 10.2.3.0.0 Probability

low

### 10.2.4.0.0 Mitigation

Thoroughly test the entire notification pipeline from Prometheus to PagerDuty. Implement a 'dead man's switch' alert (e.g., Alertmanager's Watchdog) to ensure the alerting system itself is functional.

### 10.2.5.0.0 Contingency Plan

Establish a secondary, manual process for checking system health dashboards if the primary alerting system is suspected to be down.

# 11.0.0.0.0 Recommendations

## 11.1.0.0.0 Category

### 11.1.1.0.0 Category

🔹 Runbooks

### 11.1.2.0.0 Recommendation

Develop a detailed, version-controlled runbook for every configured alert.

### 11.1.3.0.0 Justification

Actionable alerts require clear, documented steps for diagnosis and remediation. This reduces Mean Time To Recovery (MTTR) and cognitive load on the on-call engineer.

### 11.1.4.0.0 Priority

🔴 high

### 11.1.5.0.0 Implementation Notes

Each runbook should link to relevant Grafana dashboards, logs, and provide step-by-step troubleshooting instructions.

## 11.2.0.0.0 Category

### 11.2.1.0.0 Category

🔹 Threshold Tuning

### 11.2.2.0.0 Recommendation

Schedule a recurring (quarterly) review of all alert thresholds and conditions.

### 11.2.3.0.0 Justification

System performance profiles change over time. Static thresholds set at launch may become too noisy or insensitive. Regular tuning ensures alerts remain effective.

### 11.2.4.0.0 Priority

🟡 medium

### 11.2.5.0.0 Implementation Notes

Use Grafana dashboards showing metrics against their alert thresholds to visually identify candidates for tuning.

## 11.3.0.0.0 Category

### 11.3.1.0.0 Category

🔹 Observability

### 11.3.2.0.0 Recommendation

Instrument the Odoo application with custom Prometheus metrics for key business operations (e.g., trips created, invoices generated).

### 11.3.3.0.0 Justification

While infrastructure and HTTP metrics are essential, business-level metrics provide deeper insight and allow for the creation of alerts that are more closely tied to business impact.

### 11.3.4.0.0 Priority

🟡 medium

### 11.3.5.0.0 Implementation Notes

Use a Python Prometheus client library within the Odoo TMS addon code to expose a `/metrics` endpoint.

