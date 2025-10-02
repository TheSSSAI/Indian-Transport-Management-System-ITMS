# 1 Overview

## 1.1 Diagram Id

SEQ-EH-010

## 1.2 Name

Resilient GPS Message Processing with Dead-Letter Queue (DLQ)

## 1.3 Description

A GPS location message from RabbitMQ contains malformed data, causing the Odoo consumer to fail processing. After several failed retry attempts, the message is automatically routed to a Dead-Letter Queue (DLQ), which then triggers a critical operational alert.

## 1.4 Type

🔹 ErrorHandling

## 1.5 Purpose

To ensure the resilience of the asynchronous data processing pipeline by isolating un-processable 'poison' messages, preventing them from halting the entire flow, and immediately alerting operators for manual intervention.

## 1.6 Complexity

Medium

## 1.7 Priority

🔴 High

## 1.8 Frequency

OnDemand

## 1.9 Participants

- REPO-TMS-CORE
- REPO-GPS-CON

## 1.10 Key Interactions

- The REPO-TMS-CORE consumer fetches a message from the `q.tms.location_updates` queue.
- The message processing fails due to a persistent error (e.g., a `ValidationError` from malformed data).
- The consumer logic retries processing the message 3 times, but it continues to fail.
- After the final failed attempt, the consumer sends a negative acknowledgement (NACK) to RabbitMQ with the `requeue` flag set to false.
- RabbitMQ's dead-lettering policy on the main queue automatically routes the NACK'd message to the configured DLQ: `q.tms.location_updates.dlq`.
- A Prometheus alert, which constantly monitors the DLQ message count (`rabbitmq_queue_messages > 0`), fires.
- Alertmanager routes a critical notification to the on-call SRE team.

## 1.11 Triggers

- A message that cannot be successfully processed by the consumer logic is received.

## 1.12 Outcomes

- The main `q.tms.location_updates` processing queue remains unblocked, allowing valid messages to be processed.
- The problematic message is safely preserved in the DLQ for later analysis and potential reprocessing.
- System operators are immediately notified of a potential systemic issue requiring investigation.

## 1.13 Business Rules

- REQ-INT-003: The system shall implement a dead-letter queue (DLQ) for messages that repeatedly fail processing.

## 1.14 Error Scenarios

*No items available*

## 1.15 Integration Points

- Middleware: Amazon MQ for RabbitMQ
- Monitoring: Prometheus/Alertmanager

# 2.0 Details

## 2.1 Diagram Id

SEQ-EH-010-IMPL

## 2.2 Name

Implementation: Resilient GPS Message Processing via Dead-Letter Queue

## 2.3 Description

A comprehensive technical sequence detailing the handling of a poison-pill GPS message. This diagram illustrates the consumer's internal retry loop, the negative acknowledgement (NACK) mechanism, the automatic routing of the failed message to a Dead-Letter Queue (DLQ) by RabbitMQ, and the subsequent triggering of a critical alert via the Prometheus monitoring pipeline for operator intervention.

## 2.4 Participants

### 2.4.1 ApplicationLogic

#### 2.4.1.1 Repository Id

REPO-GPS-CON

#### 2.4.1.2 Display Name

Odoo GPS Consumer

#### 2.4.1.3 Type

🔹 ApplicationLogic

#### 2.4.1.4 Technology

Odoo 18, Python 3.11 (pika client)

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #1f77b4 |
| Stereotype | Odoo Scheduled Action |

### 2.4.2.0 MessageBroker

#### 2.4.2.1 Repository Id

Middleware-RabbitMQ

#### 2.4.2.2 Display Name

RabbitMQ Broker

#### 2.4.2.3 Type

🔹 MessageBroker

#### 2.4.2.4 Technology

Amazon MQ for RabbitMQ

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #ff7f0e |
| Stereotype | Middleware |

### 2.4.3.0 MonitoringSystem

#### 2.4.3.1 Repository Id

Monitoring-Prometheus

#### 2.4.3.2 Display Name

Prometheus

#### 2.4.3.3 Type

🔹 MonitoringSystem

#### 2.4.3.4 Technology

Prometheus

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #e377c2 |
| Stereotype | Monitoring |

### 2.4.4.0 AlertingSystem

#### 2.4.4.1 Repository Id

Monitoring-Alertmanager

#### 2.4.4.2 Display Name

Alertmanager

#### 2.4.4.3 Type

🔹 AlertingSystem

#### 2.4.4.4 Technology

Alertmanager

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #d62728 |
| Stereotype | Alerting |

### 2.4.5.0 NotificationEndpoint

#### 2.4.5.1 Repository Id

SRE-OnCall-Platform

#### 2.4.5.2 Display Name

SRE On-Call Platform

#### 2.4.5.3 Type

🔹 NotificationEndpoint

#### 2.4.5.4 Technology

PagerDuty / Slack

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #9467bd |
| Stereotype | External |

## 2.5.0.0 Interactions

### 2.5.1.0 MessageDelivery

#### 2.5.1.1 Source Id

Middleware-RabbitMQ

#### 2.5.1.2 Target Id

REPO-GPS-CON

#### 2.5.1.3 Message

1. Deliver Malformed Message from 'q.tms.location_updates'

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 MessageDelivery

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
| Protocol | AMQP 0-9-1 |
| Method | basic.deliver |
| Parameters | payload: malformed JSON, delivery_tag: <unique_id> |
| Authentication | Uses credentials from AWS Secrets Manager. |
| Error Handling | N/A |
| Performance | Sub-millisecond delivery. |

#### 2.5.1.11 Nested Interactions

- {'sourceId': 'REPO-GPS-CON', 'targetId': 'REPO-GPS-CON', 'message': '2. [Loop: Retry Logic (3 attempts)] Attempt to process message', 'sequenceNumber': 2, 'type': 'InternalProcessing', 'isSynchronous': True, 'returnMessage': "Raise ValidationError('Invalid latitude format')", 'hasReturn': True, 'isActivation': False, 'technicalDetails': {'protocol': 'Internal Method Call', 'method': 'process_gps_message(payload)', 'parameters': 'payload from RabbitMQ message', 'authentication': 'N/A', 'errorHandling': 'A try/except block catches persistent exceptions like ValidationError, JSONDecodeError, etc. The loop counter is incremented on each failure.', 'performance': 'Processing should be < 100ms per attempt.'}}

### 2.5.2.0 Command

#### 2.5.2.1 Source Id

REPO-GPS-CON

#### 2.5.2.2 Target Id

Middleware-RabbitMQ

#### 2.5.2.3 Message

3. Send Negative Acknowledgement (NACK)

#### 2.5.2.4 Sequence Number

3

#### 2.5.2.5 Type

🔹 Command

#### 2.5.2.6 Is Synchronous

❌ No

#### 2.5.2.7 Return Message



#### 2.5.2.8 Has Return

❌ No

#### 2.5.2.9 Is Activation

✅ Yes

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AMQP 0-9-1 |
| Method | basic.nack |
| Parameters | delivery_tag: <from_step_1>, requeue: false |
| Authentication | N/A (existing channel) |
| Error Handling | If channel to RabbitMQ is closed, an exception is ... |
| Performance | Sub-millisecond. |

### 2.5.3.0 InternalPolicyExecution

#### 2.5.3.1 Source Id

Middleware-RabbitMQ

#### 2.5.3.2 Target Id

Middleware-RabbitMQ

#### 2.5.3.3 Message

4. Route message to Dead-Letter Queue (DLQ)

#### 2.5.3.4 Sequence Number

4

#### 2.5.3.5 Type

🔹 InternalPolicyExecution

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message

Message moved to 'q.tms.location_updates.dlq'

#### 2.5.3.8 Has Return

✅ Yes

#### 2.5.3.9 Is Activation

❌ No

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal Broker Logic |
| Method | Dead-Lettering Policy |
| Parameters | Based on 'x-dead-letter-exchange' and 'x-dead-lett... |
| Authentication | N/A |
| Error Handling | If DLQ is misconfigured (e.g., does not exist), th... |
| Performance | Near-instantaneous. |

### 2.5.4.0 DataRequest

#### 2.5.4.1 Source Id

Monitoring-Prometheus

#### 2.5.4.2 Target Id

Middleware-RabbitMQ

#### 2.5.4.3 Message

5. Scrape RabbitMQ Exporter for metrics

#### 2.5.4.4 Sequence Number

5

#### 2.5.4.5 Type

🔹 DataRequest

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message

Return Metric Value: {queue='q.tms.location_updates.dlq', value=1}

#### 2.5.4.8 Has Return

✅ Yes

#### 2.5.4.9 Is Activation

❌ No

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP/GET |
| Method | /metrics |
| Parameters | None |
| Authentication | Scrape target configured with mTLS or within a sec... |
| Error Handling | Prometheus marks the target as 'down' if the scrap... |
| Performance | Scrape duration should be < 1s. |

### 2.5.5.0 InternalProcessing

#### 2.5.5.1 Source Id

Monitoring-Prometheus

#### 2.5.5.2 Target Id

Monitoring-Prometheus

#### 2.5.5.3 Message

6. Evaluate Alerting Rule: 'GpsDlqNotEmpty'

#### 2.5.5.4 Sequence Number

6

#### 2.5.5.5 Type

🔹 InternalProcessing

#### 2.5.5.6 Is Synchronous

✅ Yes

#### 2.5.5.7 Return Message

Rule condition met, alert state changes to 'Firing'

#### 2.5.5.8 Has Return

✅ Yes

#### 2.5.5.9 Is Activation

❌ No

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PromQL |
| Method | Rule Evaluation |
| Parameters | expr: rabbitmq_queue_messages{queue="q.tms.locatio... |
| Authentication | N/A |
| Error Handling | Errors in rule evaluation are logged by Prometheus... |
| Performance | Sub-second evaluation. |

### 2.5.6.0 Notification

#### 2.5.6.1 Source Id

Monitoring-Prometheus

#### 2.5.6.2 Target Id

Monitoring-Alertmanager

#### 2.5.6.3 Message

7. Fire Alert

#### 2.5.6.4 Sequence Number

7

#### 2.5.6.5 Type

🔹 Notification

#### 2.5.6.6 Is Synchronous

❌ No

#### 2.5.6.7 Return Message



#### 2.5.6.8 Has Return

❌ No

#### 2.5.6.9 Is Activation

❌ No

#### 2.5.6.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTP/POST |
| Method | /api/v2/alerts |
| Parameters | JSON payload containing alert labels (alertname, s... |
| Authentication | Configured via Prometheus static config or service... |
| Error Handling | Prometheus will retry sending alerts if Alertmanag... |
| Performance | < 1s. |

### 2.5.7.0 Notification

#### 2.5.7.1 Source Id

Monitoring-Alertmanager

#### 2.5.7.2 Target Id

SRE-OnCall-Platform

#### 2.5.7.3 Message

8. Route Critical Notification

#### 2.5.7.4 Sequence Number

8

#### 2.5.7.5 Type

🔹 Notification

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
| Protocol | HTTP/POST (Webhook) |
| Method | Varies by platform (e.g., PagerDuty Events API v2) |
| Parameters | Transformed alert payload matching the receiver's ... |
| Authentication | Secure webhook URL with token. |
| Error Handling | Alertmanager will retry notifications based on its... |
| Performance | Depends on the external platform's API latency. |

## 2.6.0.0 Notes

### 2.6.1.0 Content

#### 2.6.1.1 Content

The `requeue: false` parameter in the NACK call is critical. If set to `true`, it would create an infinite loop of redelivery and failure for a poison-pill message, blocking the queue.

#### 2.6.1.2 Position

bottom

#### 2.6.1.3 Participant Id

REPO-GPS-CON

#### 2.6.1.4 Sequence Number

3

### 2.6.2.0 Content

#### 2.6.2.1 Content

The `for: 1m` clause in the alerting rule prevents flapping alerts if a message enters and is quickly removed from the DLQ for any reason.

#### 2.6.2.2 Position

bottom

#### 2.6.2.3 Participant Id

Monitoring-Prometheus

#### 2.6.2.4 Sequence Number

6

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | RabbitMQ connection credentials and API keys for t... |
| Performance Targets | The entire alert pipeline from DLQ message arrival... |
| Error Handling Strategy | This sequence implements the Dead-Letter Channel p... |
| Testing Considerations | An integration test must be created that: 1. Publi... |
| Monitoring Requirements | The primary metric for this flow is `rabbitmq_queu... |
| Deployment Considerations | The RabbitMQ queue policies (`x-dead-letter-exchan... |

