# 1 System Overview

## 1.1 Analysis Date

2025-06-13

## 1.2 Technology Stack

- Odoo 18
- Python 3.11
- FastAPI
- PostgreSQL 16
- RabbitMQ
- Docker
- Amazon EKS
- Prometheus
- Grafana

## 1.3 Monitoring Components

- Prometheus
- Alertmanager
- Grafana
- Fluentbit
- OpenSearch

## 1.4 Requirements

- REQ-1-500: <200ms p95 response time
- REQ-1-501: <10s GPS processing latency
- REQ-1-502: 99.9% uptime
- REQ-1-301: Asynchronous GPS ingestion via RabbitMQ with DLQ
- REQ-1-302: Synchronous GSP integration with async fallback
- REQ-1-602: Comprehensive monitoring with Prometheus stack

## 1.5 Environment

production

# 2.0 Standard System Metrics Selection

## 2.1 Hardware Utilization Metrics

### 2.1.1 container_cpu_usage_seconds_total

#### 2.1.1.1 Name

container_cpu_usage_seconds_total

#### 2.1.1.2 Type

🔹 counter

#### 2.1.1.3 Unit

seconds

#### 2.1.1.4 Description

Cumulative CPU time consumed by each container (Odoo, FastAPI, Nginx). Used to monitor resource usage and set requests/limits.

#### 2.1.1.5 Collection

##### 2.1.1.5.1 Interval

30s

##### 2.1.1.5.2 Method

Prometheus scrape (cAdvisor)

#### 2.1.1.6.0 Thresholds

##### 2.1.1.6.1 Warning

>80% of limit for 5m

##### 2.1.1.6.2 Critical

>95% of limit for 2m

#### 2.1.1.7.0 Justification

Essential for capacity planning, performance tuning, and ensuring application stability on EKS.

### 2.1.2.0.0 container_memory_working_set_bytes

#### 2.1.2.1.0 Name

container_memory_working_set_bytes

#### 2.1.2.2.0 Type

🔹 gauge

#### 2.1.2.3.0 Unit

bytes

#### 2.1.2.4.0 Description

Current memory usage for each container. Critical for detecting memory leaks and preventing OOMKilled events.

#### 2.1.2.5.0 Collection

##### 2.1.2.5.1 Interval

30s

##### 2.1.2.5.2 Method

Prometheus scrape (cAdvisor)

#### 2.1.2.6.0 Thresholds

##### 2.1.2.6.1 Warning

>85% of limit

##### 2.1.2.6.2 Critical

>95% of limit

#### 2.1.2.7.0 Justification

Directly supports system stability and performance monitoring on the container orchestration platform (EKS).

## 2.2.0.0.0 Runtime Metrics

- {'name': 'odoo_worker_process_count', 'type': 'gauge', 'unit': 'count', 'description': 'Number of active Odoo worker processes. Monitors if the worker pool is healthy and scaled correctly.', 'technology': 'Python', 'collection': {'interval': '60s', 'method': 'Custom exporter or process exporter'}, 'criticality': 'medium'}

## 2.3.0.0.0 Request Response Metrics

### 2.3.1.0.0 http_request_duration_seconds

#### 2.3.1.1.0 Name

http_request_duration_seconds

#### 2.3.1.2.0 Type

🔹 histogram

#### 2.3.1.3.0 Unit

seconds

#### 2.3.1.4.0 Description

Latency of HTTP requests processed by the ingress (Nginx), Odoo application, and FastAPI microservice.

#### 2.3.1.5.0 Dimensions

- path
- method
- status_code
- app

#### 2.3.1.6.0 Percentiles

- p95
- p99

#### 2.3.1.7.0 Collection

##### 2.3.1.7.1 Interval

30s

##### 2.3.1.7.2 Method

Prometheus scrape

### 2.3.2.0.0 http_requests_total

#### 2.3.2.1.0 Name

http_requests_total

#### 2.3.2.2.0 Type

🔹 counter

#### 2.3.2.3.0 Unit

count

#### 2.3.2.4.0 Description

Total number of HTTP requests, used for calculating request rate and error rate.

#### 2.3.2.5.0 Dimensions

- path
- method
- status_code
- app

#### 2.3.2.6.0 Percentiles

*No items available*

#### 2.3.2.7.0 Collection

##### 2.3.2.7.1 Interval

30s

##### 2.3.2.7.2 Method

Prometheus scrape

## 2.4.0.0.0 Availability Metrics

- {'name': 'probe_success', 'type': 'gauge', 'unit': 'boolean', 'description': 'Indicates the health of key application endpoints (Odoo login page, FastAPI /health) via blackbox probing.', 'calculation': '1 for success, 0 for failure.', 'slaTarget': '99.9%'}

## 2.5.0.0.0 Scalability Metrics

- {'name': 'kube_deployment_status_replicas_available', 'type': 'gauge', 'unit': 'count', 'description': 'Tracks the number of available pods for each deployment (Odoo, FastAPI) to ensure the system is scaled to meet demand.', 'capacityThreshold': 'Minimum of 2 for HA', 'autoScalingTrigger': True}

# 3.0.0.0.0 Application Specific Metrics Design

## 3.1.0.0.0 Transaction Metrics

- {'name': 'tms_trip_creations_total', 'type': 'counter', 'unit': 'count', 'description': 'Counts the number of new trips created in the system. A key operational metric.', 'business_context': 'Trip Management', 'dimensions': ['customer_id', 'rate_type'], 'collection': {'interval': '30s', 'method': 'Custom instrumentation in Odoo'}, 'aggregation': {'functions': ['sum', 'rate'], 'window': '5m'}}

## 3.2.0.0.0 Cache Performance Metrics

### 3.2.1.0.0 redis_keyspace_hits_total

#### 3.2.1.1.0 Name

redis_keyspace_hits_total

#### 3.2.1.2.0 Type

🔹 counter

#### 3.2.1.3.0 Unit

count

#### 3.2.1.4.0 Description

Total number of successful key lookups in the Redis cache (from redis_exporter).

#### 3.2.1.5.0 Cache Type

Redis (Amazon ElastiCache)

#### 3.2.1.6.0 Hit Ratio Target

>90%

### 3.2.2.0.0 redis_keyspace_misses_total

#### 3.2.2.1.0 Name

redis_keyspace_misses_total

#### 3.2.2.2.0 Type

🔹 counter

#### 3.2.2.3.0 Unit

count

#### 3.2.2.4.0 Description

Total number of failed key lookups in the Redis cache (from redis_exporter). Used with hits to calculate cache hit ratio.

#### 3.2.2.5.0 Cache Type

Redis (Amazon ElastiCache)

#### 3.2.2.6.0 Hit Ratio Target

>90%

## 3.3.0.0.0 External Dependency Metrics

### 3.3.1.0.0 external_api_request_duration_seconds

#### 3.3.1.1.0 Name

external_api_request_duration_seconds

#### 3.3.1.2.0 Type

🔹 histogram

#### 3.3.1.3.0 Unit

seconds

#### 3.3.1.4.0 Description

Latency of API calls to third-party services (GPS Provider, GSP).

#### 3.3.1.5.0 Dependency

GSP API, GPS Provider API

#### 3.3.1.6.0 Circuit Breaker Integration

❌ No

#### 3.3.1.7.0 Sla

##### 3.3.1.7.1 Response Time

Varies by provider

##### 3.3.1.7.2 Availability

Varies by provider

### 3.3.2.0.0 rabbitmq_queue_messages

#### 3.3.2.1.0 Name

rabbitmq_queue_messages

#### 3.3.2.2.0 Type

🔹 gauge

#### 3.3.2.3.0 Unit

count

#### 3.3.2.4.0 Description

Current number of messages in RabbitMQ queues, especially gps_location_updates and the associated DLQ. A rising queue depth indicates a consumer problem.

#### 3.3.2.5.0 Dependency

Amazon MQ (RabbitMQ)

#### 3.3.2.6.0 Circuit Breaker Integration

❌ No

#### 3.3.2.7.0 Sla

##### 3.3.2.7.1 Response Time

N/A

##### 3.3.2.7.2 Availability

Managed by AWS

## 3.4.0.0.0 Error Metrics

- {'name': 'rabbitmq_messages_in_dlq_total', 'type': 'gauge', 'unit': 'count', 'description': 'The number of messages in the Dead-Letter Queue for GPS events. Any value > 0 requires immediate attention.', 'errorTypes': ['UnprocessableMessage'], 'dimensions': ['queue_name'], 'alertThreshold': '> 0 for 5m'}

## 3.5.0.0.0 Throughput And Latency Metrics

- {'name': 'gps_event_processing_latency_seconds', 'type': 'histogram', 'unit': 'seconds', 'description': 'End-to-end latency from GPS event publication by the microservice to its successful processing in Odoo.', 'percentiles': ['p95', 'p99'], 'buckets': ['1', '2.5', '5', '7.5', '10', '15'], 'slaTargets': {'p95': '< 10s', 'p99': '< 12s'}}

# 4.0.0.0.0 Business Kpi Identification

## 4.1.0.0.0 Critical Business Metrics

- {'name': 'tms_revenue_total', 'type': 'counter', 'unit': 'currency', 'description': "Tracks total revenue from invoiced trips. Corresponds to 'Total Revenue (MTD/YTD)' KPI from REQ-1-601.", 'businessOwner': 'Finance', 'calculation': "Sum of 'totalAmount' from newly 'Invoiced' status trips.", 'reportingFrequency': 'real-time', 'target': 'Growth'}

## 4.2.0.0.0 User Engagement Metrics

*No items available*

## 4.3.0.0.0 Conversion Metrics

*No items available*

## 4.4.0.0.0 Operational Efficiency Kpis

### 4.4.1.0.0 tms_trips_by_status

#### 4.4.1.1.0 Name

tms_trips_by_status

#### 4.4.1.2.0 Type

🔹 gauge

#### 4.4.1.3.0 Unit

count

#### 4.4.1.4.0 Description

Current number of trips in each status ('Pending Deliveries', 'Delayed Trips'). Corresponds to KPIs from REQ-1-601.

#### 4.4.1.5.0 Calculation

Count of trips grouped by 'status' field.

#### 4.4.1.6.0 Benchmark Target

Minimize 'Delayed' and 'On Hold' statuses.

### 4.4.2.0.0 tms_pending_payment_collections_amount

#### 4.4.2.1.0 Name

tms_pending_payment_collections_amount

#### 4.4.2.2.0 Type

🔹 gauge

#### 4.4.2.3.0 Unit

currency

#### 4.4.2.4.0 Description

Total value of outstanding invoices. Corresponds to 'Pending Payment Collections' KPI from REQ-1-601.

#### 4.4.2.5.0 Calculation

Sum of 'totalAmount' for invoices not in 'Paid' status.

#### 4.4.2.6.0 Benchmark Target

Minimize

## 4.5.0.0.0 Revenue And Cost Metrics

*No items available*

## 4.6.0.0.0 Customer Satisfaction Indicators

*No items available*

# 5.0.0.0.0 Collection Interval Optimization

## 5.1.0.0.0 Sampling Frequencies

### 5.1.1.0.0 Metric Category

#### 5.1.1.1.0 Metric Category

Infrastructure

#### 5.1.1.2.0 Interval

30s

#### 5.1.1.3.0 Justification

Provides a good balance of granularity and resource usage for system-level metrics like CPU/memory.

#### 5.1.1.4.0 Resource Impact

low

### 5.1.2.0.0 Metric Category

#### 5.1.2.1.0 Metric Category

Application

#### 5.1.2.2.0 Interval

30s

#### 5.1.2.3.0 Justification

Standard interval for application-level metrics like request rates and latencies.

#### 5.1.2.4.0 Resource Impact

low

### 5.1.3.0.0 Metric Category

#### 5.1.3.1.0 Metric Category

Business

#### 5.1.3.2.0 Interval

60s

#### 5.1.3.3.0 Justification

Slightly longer interval for business KPIs is acceptable as they change less frequently.

#### 5.1.3.4.0 Resource Impact

low

## 5.2.0.0.0 High Frequency Metrics

*No items available*

## 5.3.0.0.0 Cardinality Considerations

- {'metricName': 'http_request_duration_seconds', 'estimatedCardinality': 'medium', 'dimensionStrategy': 'Avoid high-cardinality dimensions like user IDs or trip IDs. Use path templates instead of raw URLs.', 'mitigationApproach': 'Use metric relabeling in Prometheus to drop high-cardinality labels or aggregate them.'}

## 5.4.0.0.0 Aggregation Periods

- {'metricType': 'Latency Histograms', 'periods': ['1m', '5m', '1h'], 'retentionStrategy': 'Prometheus recording rules will pre-aggregate percentiles over different time windows.'}

## 5.5.0.0.0 Collection Methods

- {'method': 'real-time', 'applicableMetrics': ['All Prometheus-scraped metrics'], 'implementation': 'Prometheus pull model.', 'performance': 'High'}

# 6.0.0.0.0 Aggregation Method Selection

## 6.1.0.0.0 Statistical Aggregations

- {'metricName': 'http_requests_total', 'aggregationFunctions': ['rate', 'sum'], 'windows': ['1m', '5m'], 'justification': 'Rate() is essential for calculating requests per second (RPS) and error rates from the raw counter.'}

## 6.2.0.0.0 Histogram Requirements

- {'metricName': 'http_request_duration_seconds', 'buckets': ['0.05', '0.1', '0.2', '0.5', '1.0', '2.5'], 'percentiles': ['p95', 'p99'], 'accuracy': 'High, to verify the <200ms SLO in REQ-1-500.'}

## 6.3.0.0.0 Percentile Calculations

- {'metricName': 'gps_event_processing_latency_seconds', 'percentiles': ['p95'], 'algorithm': 'histogram_quantile', 'accuracy': 'High, to verify the <10s SLO in REQ-1-501.'}

## 6.4.0.0.0 Metric Types

### 6.4.1.0.0 http_requests_total

#### 6.4.1.1.0 Name

http_requests_total

#### 6.4.1.2.0 Implementation

counter

#### 6.4.1.3.0 Reasoning

This is a monotonically increasing value representing total requests served. Best represented as a counter.

#### 6.4.1.4.0 Resets Handling

Prometheus rate() function automatically handles counter resets.

### 6.4.2.0.0 rabbitmq_queue_messages

#### 6.4.2.1.0 Name

rabbitmq_queue_messages

#### 6.4.2.2.0 Implementation

gauge

#### 6.4.2.3.0 Reasoning

This represents a point-in-time value that can go up or down. A gauge is the correct type.

#### 6.4.2.4.0 Resets Handling

N/A

## 6.5.0.0.0 Dimensional Aggregation

- {'metricName': 'http_requests_total', 'dimensions': ['status_code', 'app'], 'aggregationStrategy': 'sum(rate(http_requests_total{status_code=~"5.."}[5m])) by (app) / sum(rate(http_requests_total[5m])) by (app)', 'cardinalityImpact': 'Low'}

## 6.6.0.0.0 Derived Metrics

### 6.6.1.0.0 app_error_rate_percentage

#### 6.6.1.1.0 Name

app_error_rate_percentage

#### 6.6.1.2.0 Calculation

(Sum of 5xx responses) / (Total responses)

#### 6.6.1.3.0 Source Metrics

- http_requests_total

#### 6.6.1.4.0 Update Frequency

Every 30s (scrape interval)

### 6.6.2.0.0 cache_hit_ratio_percentage

#### 6.6.2.1.0 Name

cache_hit_ratio_percentage

#### 6.6.2.2.0 Calculation

redis_keyspace_hits_total / (redis_keyspace_hits_total + redis_keyspace_misses_total)

#### 6.6.2.3.0 Source Metrics

- redis_keyspace_hits_total
- redis_keyspace_misses_total

#### 6.6.2.4.0 Update Frequency

Every 30s (scrape interval)

# 7.0.0.0.0 Storage Requirements Planning

## 7.1.0.0.0 Retention Periods

### 7.1.1.0.0 Metric Type

#### 7.1.1.1.0 Metric Type

High-resolution raw metrics

#### 7.1.1.2.0 Retention Period

30 days

#### 7.1.1.3.0 Justification

Sufficient for short-term operational debugging and analysis.

#### 7.1.1.4.0 Compliance Requirement

None

### 7.1.2.0.0 Metric Type

#### 7.1.2.1.0 Metric Type

Aggregated metrics (via recording rules)

#### 7.1.2.2.0 Retention Period

1 year

#### 7.1.2.3.0 Justification

Required for long-term trending and capacity planning.

#### 7.1.2.4.0 Compliance Requirement

None

## 7.2.0.0.0 Data Resolution

### 7.2.1.0.0 Time Range

#### 7.2.1.1.0 Time Range

0-30 days

#### 7.2.1.2.0 Resolution

30s

#### 7.2.1.3.0 Query Performance

High

#### 7.2.1.4.0 Storage Optimization

None

### 7.2.2.0.0 Time Range

#### 7.2.2.1.0 Time Range

31 days - 1 year

#### 7.2.2.2.0 Resolution

5m

#### 7.2.2.3.0 Query Performance

Medium

#### 7.2.2.4.0 Storage Optimization

Downsampling via recording rules

## 7.3.0.0.0 Downsampling Strategies

- {'sourceResolution': '30s', 'targetResolution': '5m', 'aggregationMethod': 'avg for gauges, sum for counters, preserving histogram buckets', 'triggerCondition': 'Prometheus recording rules evaluated at each scrape.'}

## 7.4.0.0.0 Storage Performance

| Property | Value |
|----------|-------|
| Write Latency | <100ms |
| Query Latency | <1s for typical dashboard queries |
| Throughput Requirements | Handle metrics from ~100 pods |
| Scalability Needs | Horizontal scalability using a Prometheus-compatib... |

## 7.5.0.0.0 Query Optimization

*No items available*

## 7.6.0.0.0 Cost Optimization

- {'strategy': 'Downsampling and Retention', 'implementation': 'Use Prometheus recording rules to create lower-resolution, long-term metrics and set a short retention for high-resolution raw data.', 'expectedSavings': 'Significant reduction in long-term storage costs.', 'tradeoffs': 'Loss of fine-grained historical data beyond 30 days.'}

# 8.0.0.0.0 Project Specific Metrics Config

## 8.1.0.0.0 Standard Metrics

### 8.1.1.0.0 http_request_duration_seconds

#### 8.1.1.1.0 Name

http_request_duration_seconds

#### 8.1.1.2.0 Type

🔹 histogram

#### 8.1.1.3.0 Unit

seconds

#### 8.1.1.4.0 Collection

##### 8.1.1.4.1 Interval

30s

##### 8.1.1.4.2 Method

Prometheus scrape

#### 8.1.1.5.0 Thresholds

##### 8.1.1.5.1 Warning

p95 > 180ms

##### 8.1.1.5.2 Critical

p95 > 200ms

#### 8.1.1.6.0 Dimensions

- app
- path
- status_code

### 8.1.2.0.0 rabbitmq_queue_messages

#### 8.1.2.1.0 Name

rabbitmq_queue_messages

#### 8.1.2.2.0 Type

🔹 gauge

#### 8.1.2.3.0 Unit

count

#### 8.1.2.4.0 Collection

##### 8.1.2.4.1 Interval

30s

##### 8.1.2.4.2 Method

RabbitMQ Exporter

#### 8.1.2.5.0 Thresholds

##### 8.1.2.5.1 Warning

>500 for 5m

##### 8.1.2.5.2 Critical

>1000 for 5m

#### 8.1.2.6.0 Dimensions

- queue

## 8.2.0.0.0 Custom Metrics

### 8.2.1.0.0 gps_event_processing_latency_seconds

#### 8.2.1.1.0 Name

gps_event_processing_latency_seconds

#### 8.2.1.2.0 Description

Measures end-to-end latency for GPS data pipeline to ensure REQ-1-501 is met.

#### 8.2.1.3.0 Calculation

Timestamp difference between event creation in FastAPI and event processing in Odoo.

#### 8.2.1.4.0 Type

🔹 histogram

#### 8.2.1.5.0 Unit

seconds

#### 8.2.1.6.0 Business Context

Real-time Vehicle Tracking

#### 8.2.1.7.0 Collection

##### 8.2.1.7.1 Interval

30s

##### 8.2.1.7.2 Method

Custom instrumentation

#### 8.2.1.8.0 Alerting

##### 8.2.1.8.1 Enabled

✅ Yes

##### 8.2.1.8.2 Conditions

- p95 > 10s for 5m

### 8.2.2.0.0 tms_trips_by_status

#### 8.2.2.1.0 Name

tms_trips_by_status

#### 8.2.2.2.0 Description

Provides data for the operational dashboard KPIs as per REQ-1-601.

#### 8.2.2.3.0 Calculation

Periodic SELECT COUNT(*) ... GROUP BY status on the trips table.

#### 8.2.2.4.0 Type

🔹 gauge

#### 8.2.2.5.0 Unit

count

#### 8.2.2.6.0 Business Context

Operational Dashboard

#### 8.2.2.7.0 Collection

##### 8.2.2.7.1 Interval

60s

##### 8.2.2.7.2 Method

Custom Odoo exporter

#### 8.2.2.8.0 Alerting

##### 8.2.2.8.1 Enabled

✅ Yes

##### 8.2.2.8.2 Conditions

- tms_trips_by_status{status="Delayed"} > 10

## 8.3.0.0.0 Dashboard Metrics

### 8.3.1.0.0 Dashboard

#### 8.3.1.1.0 Dashboard

Application Overview

#### 8.3.1.2.0 Metrics

- app_error_rate_percentage
- http_request_duration_seconds_p95
- http_requests_per_second

#### 8.3.1.3.0 Refresh Interval

30s

#### 8.3.1.4.0 Audience

DevOps/SRE

### 8.3.2.0.0 Dashboard

#### 8.3.2.1.0 Dashboard

Business Operations

#### 8.3.2.2.0 Metrics

- tms_trips_by_status
- tms_revenue_total
- tms_pending_payment_collections_amount

#### 8.3.2.3.0 Refresh Interval

1m

#### 8.3.2.4.0 Audience

Dispatch Managers, Finance Officers

# 9.0.0.0.0 Implementation Priority

## 9.1.0.0.0 Component

### 9.1.1.0.0 Component

Standard Infrastructure Metrics (EKS, Nginx, RDS, RabbitMQ)

### 9.1.2.0.0 Priority

🔴 high

### 9.1.3.0.0 Dependencies

- Prometheus setup

### 9.1.4.0.0 Estimated Effort

Low (Standard exporters)

### 9.1.5.0.0 Risk Level

low

## 9.2.0.0.0 Component

### 9.2.1.0.0 Component

Core Application Metrics (HTTP Latency/Errors)

### 9.2.2.0.0 Priority

🔴 high

### 9.2.3.0.0 Dependencies

- Prometheus setup

### 9.2.4.0.0 Estimated Effort

Medium (Requires middleware instrumentation)

### 9.2.5.0.0 Risk Level

low

## 9.3.0.0.0 Component

### 9.3.1.0.0 Component

Critical Custom Metrics (GPS Latency, DLQ)

### 9.3.2.0.0 Priority

🔴 high

### 9.3.3.0.0 Dependencies

- Core Application Metrics

### 9.3.4.0.0 Estimated Effort

Medium

### 9.3.5.0.0 Risk Level

medium

## 9.4.0.0.0 Component

### 9.4.1.0.0 Component

Business KPI Metrics

### 9.4.2.0.0 Priority

🟡 medium

### 9.4.3.0.0 Dependencies

- Core Application Metrics

### 9.4.4.0.0 Estimated Effort

Medium

### 9.4.5.0.0 Risk Level

low

# 10.0.0.0.0 Risk Assessment

- {'risk': 'High Cardinality from metric dimensions (e.g., using Trip ID in a label) overwhelms Prometheus.', 'impact': 'high', 'probability': 'medium', 'mitigation': 'Enforce strict policies on label usage. Avoid user-generated content or unbounded IDs as labels. Use aggregation and relabeling rules.', 'contingencyPlan': 'Drop high-cardinality metrics at the scrape or aggregation level. Isolate problematic services.'}

# 11.0.0.0.0 Recommendations

## 11.1.0.0.0 Category

### 11.1.1.0.0 Category

🔹 Instrumentation

### 11.1.2.0.0 Recommendation

Use standard, well-supported Prometheus client libraries for both Python applications (prometheus-client for Odoo, prometheus-fastapi-instrumentator for FastAPI).

### 11.1.3.0.0 Justification

Reduces development effort, ensures best practices are followed, and simplifies maintenance.

### 11.1.4.0.0 Priority

🔴 high

### 11.1.5.0.0 Implementation Notes

Instrument FastAPI with the standard middleware. For Odoo, create a custom controller endpoint at /metrics that uses the Python client library to expose application and business metrics.

## 11.2.0.0.0 Category

### 11.2.1.0.0 Category

🔹 Alerting

### 11.2.2.0.0 Recommendation

Define all alerts in Prometheus as code and store them in version control. Focus on actionable, symptom-based alerts (e.g., high latency, high error rate) rather than cause-based alerts (e.g., high CPU).

### 11.2.3.0.0 Justification

Ensures alerting strategy is repeatable, versioned, and reviewed. Symptom-based alerts reduce noise and directly indicate user-facing impact.

### 11.2.4.0.0 Priority

🔴 high

### 11.2.5.0.0 Implementation Notes

Create a separate Git repository for monitoring configuration, including Prometheus rules and Alertmanager configuration. Link alerts back to runbooks for troubleshooting.

