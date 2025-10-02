# 1 System Overview

## 1.1 Analysis Date

2025-06-13

## 1.2 Technology Stack

- Odoo 18
- Python 3.11
- FastAPI
- PostgreSQL 16
- RabbitMQ
- Redis
- Docker
- Amazon EKS

## 1.3 Architecture Patterns

- Modular Monolith
- Microservice
- Event-Driven (for GPS)
- Request-Reply

## 1.4 Resource Needs

- Container Orchestration (EKS)
- Managed Database (RDS)
- Managed Message Broker (Amazon MQ)
- Managed Cache (ElastiCache)
- Object Storage (S3)

## 1.5 Performance Expectations

95% of requests < 200ms (REQ-1-500), GPS data latency < 10s (REQ-1-501), supports 100 concurrent users.

## 1.6 Data Processing Volumes

High-volume, low-latency GPS data ingestion; moderate-volume transactional data for trips and financials.

# 2.0 Workload Characterization

## 2.1 Processing Resource Consumption

### 2.1.1 Operation

#### 2.1.1.1 Operation

Odoo Application Server

#### 2.1.1.2 Cpu Pattern

bursty

#### 2.1.1.3 Cpu Utilization

| Property | Value |
|----------|-------|
| Baseline | 10-15% |
| Peak | 60-80% |
| Average | 25% |

#### 2.1.1.4 Memory Pattern

steady

#### 2.1.1.5 Memory Requirements

| Property | Value |
|----------|-------|
| Baseline | 4GB per pod |
| Peak | 8GB per pod |
| Growth | low |

#### 2.1.1.6 Io Characteristics

| Property | Value |
|----------|-------|
| Disk Iops | Moderate (DB heavy) |
| Network Throughput | Moderate |
| Io Pattern | mixed |

### 2.1.2.0 Operation

#### 2.1.2.1 Operation

GPS Ingestion Microservice

#### 2.1.2.2 Cpu Pattern

cyclic

#### 2.1.2.3 Cpu Utilization

| Property | Value |
|----------|-------|
| Baseline | 5% |
| Peak | 30% |
| Average | 10% |

#### 2.1.2.4 Memory Pattern

steady

#### 2.1.2.5 Memory Requirements

| Property | Value |
|----------|-------|
| Baseline | 256MB per pod |
| Peak | 512MB per pod |
| Growth | none |

#### 2.1.2.6 Io Characteristics

| Property | Value |
|----------|-------|
| Disk Iops | Low |
| Network Throughput | High (outbound to RabbitMQ) |
| Io Pattern | sequential |

## 2.2.0.0 Concurrency Requirements

### 2.2.1.0 Operation

#### 2.2.1.1 Operation

Standard User Operations

#### 2.2.1.2 Max Concurrent Jobs

100

#### 2.2.1.3 Thread Pool Size

0

#### 2.2.1.4 Connection Pool Size

150

#### 2.2.1.5 Queue Depth

0

### 2.2.2.0 Operation

#### 2.2.2.1 Operation

GPS Data Consumption

#### 2.2.2.2 Max Concurrent Jobs

0

#### 2.2.2.3 Thread Pool Size

0

#### 2.2.2.4 Connection Pool Size

0

#### 2.2.2.5 Queue Depth

5,000

## 2.3.0.0 Database Access Patterns

- {'accessType': 'mixed', 'connectionRequirements': 'Persistent connections from Odoo ORM', 'queryComplexity': 'mixed', 'transactionVolume': 'Moderate', 'cacheHitRatio': '>80% target for Odoo cache'}

## 2.4.0.0 Frontend Resource Demands

- {'component': 'Odoo Web UI (OWL)', 'renderingLoad': 'moderate', 'staticContentSize': 'Medium', 'dynamicContentVolume': 'High', 'userConcurrency': '100'}

## 2.5.0.0 Load Patterns

- {'pattern': 'peak-trough', 'description': 'Load is expected to be highest during standard Indian business hours (9 AM - 6 PM IST) and lower during nights and weekends.', 'frequency': 'daily', 'magnitude': '3-4x peak vs. off-peak', 'predictability': 'high'}

# 3.0.0.0 Scaling Strategy Design

## 3.1.0.0 Scaling Approaches

### 3.1.1.0 Component

#### 3.1.1.1 Component

TMS Odoo Addon

#### 3.1.1.2 Primary Strategy

horizontal

#### 3.1.1.3 Justification

Required to handle concurrent user load and ensure high availability (REQ-NFR-002) by running multiple replicas.

#### 3.1.1.4 Limitations

- Odoo's performance is heavily tied to database performance, which scales vertically.
- Session management might require sticky sessions at the load balancer level.

#### 3.1.1.5 Implementation

Kubernetes Horizontal Pod Autoscaler (HPA) on EKS.

### 3.1.2.0 Component

#### 3.1.2.1 Component

GPS Ingestion Service

#### 3.1.2.2 Primary Strategy

horizontal

#### 3.1.2.3 Justification

The service is stateless and designed to scale out easily to handle increases in the number of GPS devices or polling frequency.

#### 3.1.2.4 Limitations

- Limited by the throughput of the downstream message broker (RabbitMQ).

#### 3.1.2.5 Implementation

Kubernetes Horizontal Pod Autoscaler (HPA) on EKS.

## 3.2.0.0 Instance Specifications

### 3.2.1.0 Workload Type

#### 3.2.1.1 Workload Type

Odoo Application

#### 3.2.1.2 Instance Family

Memory Optimized (e.g., AWS r6g)

#### 3.2.1.3 Instance Size

medium/large

#### 3.2.1.4 V Cpus

4

#### 3.2.1.5 Memory Gb

16

#### 3.2.1.6 Storage Type

EBS gp3

#### 3.2.1.7 Network Performance

Moderate

#### 3.2.1.8 Optimization

memory

### 3.2.2.0 Workload Type

#### 3.2.2.1 Workload Type

GPS Ingestion Service

#### 3.2.2.2 Instance Family

General Purpose (e.g., AWS t4g)

#### 3.2.2.3 Instance Size

small

#### 3.2.2.4 V Cpus

2

#### 3.2.2.5 Memory Gb

4

#### 3.2.2.6 Storage Type

EBS gp3

#### 3.2.2.7 Network Performance

Moderate

#### 3.2.2.8 Optimization

balanced

### 3.2.3.0 Workload Type

#### 3.2.3.1 Workload Type

Database

#### 3.2.3.2 Instance Family

Memory Optimized (e.g., AWS db.r6g)

#### 3.2.3.3 Instance Size

large+

#### 3.2.3.4 V Cpus

4

#### 3.2.3.5 Memory Gb

32

#### 3.2.3.6 Storage Type

Provisioned IOPS SSD

#### 3.2.3.7 Network Performance

High

#### 3.2.3.8 Optimization

storage

## 3.3.0.0 Multithreading Considerations

*No items available*

## 3.4.0.0 Specialized Hardware

*No items available*

## 3.5.0.0 Storage Scaling

### 3.5.1.0 Storage Type

#### 3.5.1.1 Storage Type

database

#### 3.5.1.2 Scaling Method

vertical

#### 3.5.1.3 Performance

High (Provisioned IOPS)

#### 3.5.1.4 Consistency

Strong

### 3.5.2.0 Storage Type

#### 3.5.2.1 Storage Type

object

#### 3.5.2.2 Scaling Method

horizontal

#### 3.5.2.3 Performance

N/A (Managed by S3)

#### 3.5.2.4 Consistency

Eventual

## 3.6.0.0 Licensing Implications

- {'software': 'Odoo 18 Enterprise', 'licensingModel': 'per-user', 'scalingImpact': 'None. The number of application pods can be scaled independently of the number of licensed users.', 'costOptimization': 'N/A'}

# 4.0.0.0 Auto Scaling Trigger Metrics

## 4.1.0.0 Cpu Utilization Triggers

### 4.1.1.0 Component

#### 4.1.1.1 Component

TMS Odoo Addon

#### 4.1.1.2 Scale Up Threshold

75

#### 4.1.1.3 Scale Down Threshold

40

#### 4.1.1.4 Evaluation Periods

2

#### 4.1.1.5 Data Points

2

#### 4.1.1.6 Justification

Primary indicator of load on the application servers from user requests and background jobs.

### 4.1.2.0 Component

#### 4.1.2.1 Component

GPS Ingestion Service

#### 4.1.2.2 Scale Up Threshold

70

#### 4.1.2.3 Scale Down Threshold

30

#### 4.1.2.4 Evaluation Periods

3

#### 4.1.2.5 Data Points

2

#### 4.1.2.6 Justification

CPU is the main resource consumed during the poll-validate-publish cycle of the microservice.

## 4.2.0.0 Memory Consumption Triggers

*No items available*

## 4.3.0.0 Database Connection Triggers

*No items available*

## 4.4.0.0 Queue Length Triggers

- {'queueType': 'message', 'scaleUpThreshold': 1000, 'scaleDownThreshold': 100, 'ageThreshold': '60s', 'priority': 'high'}

## 4.5.0.0 Response Time Triggers

*No items available*

## 4.6.0.0 Custom Metric Triggers

- {'metricName': 'rabbitmq_queue_messages_ready{queue="gps_location_updates"}', 'description': 'Number of unprocessed messages in the GPS data queue.', 'scaleUpThreshold': 1000, 'scaleDownThreshold': 100, 'calculation': 'A custom metric exposed via the RabbitMQ exporter.', 'businessJustification': 'If the queue is backing up, it means the Odoo consumers are too slow or have failed. Scaling up the Odoo application pods (which host the consumers) can increase processing throughput.'}

## 4.7.0.0 Disk Iotriggers

*No items available*

# 5.0.0.0 Scaling Limits And Safeguards

## 5.1.0.0 Instance Limits

### 5.1.1.0 Component

#### 5.1.1.1 Component

TMS Odoo Addon

#### 5.1.1.2 Min Instances

3

#### 5.1.1.3 Max Instances

10

#### 5.1.1.4 Justification

Minimum of 3 for high availability across AZs. Maximum of 10 to control costs and prevent runaway scaling.

#### 5.1.1.5 Cost Implication

Sets a predictable ceiling on compute costs for the main application.

### 5.1.2.0 Component

#### 5.1.2.1 Component

GPS Ingestion Service

#### 5.1.2.2 Min Instances

2

#### 5.1.2.3 Max Instances

5

#### 5.1.2.4 Justification

Minimum of 2 for HA. Maximum is sufficient for the expected number of vehicles.

#### 5.1.2.5 Cost Implication

Low, as the service is lightweight.

## 5.2.0.0 Cooldown Periods

### 5.2.1.0 Action

#### 5.2.1.1 Action

scale-up

#### 5.2.1.2 Duration

180s

#### 5.2.1.3 Reasoning

Allows new pods to become fully operational and start processing traffic before another scale-up is considered.

#### 5.2.1.4 Component

TMS Odoo Addon

### 5.2.2.0 Action

#### 5.2.2.1 Action

scale-down

#### 5.2.2.2 Duration

300s

#### 5.2.2.3 Reasoning

Prevents premature scaling down during brief lulls in traffic, avoiding thrashing.

#### 5.2.2.4 Component

TMS Odoo Addon

## 5.3.0.0 Scaling Step Sizes

- {'component': 'TMS Odoo Addon', 'scaleUpStep': 1, 'scaleDownStep': 1, 'stepType': 'fixed', 'rationale': 'A gradual, one-pod-at-a-time scaling approach is sufficient for the expected load patterns and prevents sudden cost spikes.'}

## 5.4.0.0 Runaway Protection

- {'safeguard': 'max-scaling-rate', 'implementation': 'The `maxInstances` setting in the HPA acts as the primary safeguard.', 'trigger': 'Scaling beyond the defined maximum.', 'action': 'Prevent scaling.'}

## 5.5.0.0 Graceful Degradation

*No items available*

## 5.6.0.0 Resource Quotas

### 5.6.1.0 Environment

#### 5.6.1.1 Environment

production

#### 5.6.1.2 Quota Type

cpu

#### 5.6.1.3 Limit

50 vCPU

#### 5.6.1.4 Enforcement

hard

### 5.6.2.0 Environment

#### 5.6.2.1 Environment

production

#### 5.6.2.2 Quota Type

memory

#### 5.6.2.3 Limit

200 GiB

#### 5.6.2.4 Enforcement

hard

## 5.7.0.0 Workload Prioritization

*No items available*

# 6.0.0.0 Cost Optimization Strategy

## 6.1.0.0 Instance Right Sizing

*No items available*

## 6.2.0.0 Time Based Scaling

### 6.2.1.0 Schedule

#### 6.2.1.1 Schedule

0 1 * * *

#### 6.2.1.2 Timezone

Asia/Kolkata

#### 6.2.1.3 Scale Action

down

#### 6.2.1.4 Instance Count

3

#### 6.2.1.5 Justification

Scale down Odoo application to minimum HA replicas during off-peak night hours.

### 6.2.2.0 Schedule

#### 6.2.2.1 Schedule

0 8 * * *

#### 6.2.2.2 Timezone

Asia/Kolkata

#### 6.2.2.3 Scale Action

up

#### 6.2.2.4 Instance Count

4

#### 6.2.2.5 Justification

Pre-warm the application by scaling up before the start of business hours.

## 6.3.0.0 Instance Termination Policies

- {'policy': 'availability-zone-balanced', 'component': 'TMS Odoo Addon', 'implementation': 'Kubernetes Descheduler can be configured to maintain AZ balance during scale-down.', 'statefulConsiderations': []}

## 6.4.0.0 Spot Instance Strategies

- {'component': 'GPS Ingestion Service', 'spotPercentage': 50, 'fallbackStrategy': 'If Spot instances are unavailable, the EKS node group will provision On-Demand instances.', 'interruptionHandling': 'The stateless nature of the service means a terminated pod can be replaced without data loss.', 'costSavings': 'Potentially 40-60% on compute for this component.'}

## 6.5.0.0 Reserved Instance Planning

### 6.5.1.0 Instance Type

#### 6.5.1.1 Instance Type

AWS RDS db.r6g.large

#### 6.5.1.2 Reservation Term

1-year

#### 6.5.1.3 Utilization Forecast

Constant 24/7 usage

#### 6.5.1.4 Baseline Instances

1

#### 6.5.1.5 Payment Option

no-upfront

### 6.5.2.0 Instance Type

#### 6.5.2.1 Instance Type

AWS EKS Managed Node (r6g.large)

#### 6.5.2.2 Reservation Term

1-year

#### 6.5.2.3 Utilization Forecast

Constant 24/7 usage for baseline capacity

#### 6.5.2.4 Baseline Instances

3

#### 6.5.2.5 Payment Option

no-upfront

## 6.6.0.0 Resource Tracking

- {'trackingMethod': 'tags', 'granularity': 'daily', 'optimization': 'Use tags like `Project: TMS`, `Environment: Production`, `Component: Odoo-App` for detailed cost allocation reports.', 'alerting': True}

## 6.7.0.0 Cleanup Policies

*No items available*

# 7.0.0.0 Load Testing And Validation

## 7.1.0.0 Baseline Metrics

### 7.1.1.0 Metric

#### 7.1.1.1 Metric

p95 API Response Time

#### 7.1.1.2 Baseline Value

<200ms

#### 7.1.1.3 Acceptable Variation

10%

#### 7.1.1.4 Measurement Method

Prometheus

### 7.1.2.0 Metric

#### 7.1.2.1 Metric

CPU Utilization at 100 Concurrent Users

#### 7.1.2.2 Baseline Value

<60%

#### 7.1.2.3 Acceptable Variation

15%

#### 7.1.2.4 Measurement Method

Prometheus

## 7.2.0.0 Validation Procedures

- {'procedure': 'Execute a suite of automated load tests in the staging environment before each major release.', 'frequency': 'pre-release', 'successCriteria': ['SLOs are met.', 'Scaling policies trigger correctly.', 'No resource exhaustion occurs.'], 'failureActions': ['Block release.', 'Create performance tickets for remediation.']}

## 7.3.0.0 Synthetic Load Scenarios

- {'scenario': 'Business Day Simulation', 'loadPattern': 'ramp-up', 'duration': '4 hours', 'targetMetrics': ['API response time', 'Pod count', 'CPU utilization'], 'expectedBehavior': 'System should scale out as load ramps up from 0 to 120 users, and scale back in as load decreases, while maintaining performance SLOs.'}

## 7.4.0.0 Scaling Event Monitoring

*No items available*

## 7.5.0.0 Policy Refinement

*No items available*

## 7.6.0.0 Effectiveness Kpis

*No items available*

## 7.7.0.0 Feedback Mechanisms

*No items available*

# 8.0.0.0 Project Specific Scaling Policies

## 8.1.0.0 Policies

### 8.1.1.0 hpa-tms-odoo-app

#### 8.1.1.1 Id

hpa-tms-odoo-app

#### 8.1.1.2 Type

🔹 Horizontal

#### 8.1.1.3 Component

TMS Odoo Addon

#### 8.1.1.4 Rules

- {'metric': 'kubernetes.io/pod/cpu/utilization', 'threshold': 75, 'operator': 'GREATER_THAN', 'scaleChange': 1, 'cooldown': {'scaleUpSeconds': 180, 'scaleDownSeconds': 300}, 'evaluationPeriods': 2, 'dataPointsToAlarm': 2}

#### 8.1.1.5 Safeguards

| Property | Value |
|----------|-------|
| Min Instances | 3 |
| Max Instances | 10 |
| Max Scaling Rate | 1 pod per 3 minutes |
| Cost Threshold | *N/A* |

#### 8.1.1.6 Schedule

##### 8.1.1.6.1 Enabled

✅ Yes

##### 8.1.1.6.2 Timezone

Asia/Kolkata

##### 8.1.1.6.3 Rules

###### 8.1.1.6.3.1 Time

####### 8.1.1.6.3.1.1 Time

0 1 * * *

####### 8.1.1.6.3.1.2 Action

scale-to

####### 8.1.1.6.3.1.3 Instance Count

3

###### 8.1.1.6.3.2.0 Time

####### 8.1.1.6.3.2.1 Time

0 8 * * *

####### 8.1.1.6.3.2.2 Action

scale-to

####### 8.1.1.6.3.2.3 Instance Count

4

### 8.1.2.0.0.0.0 hpa-gps-ingestion-service

#### 8.1.2.1.0.0.0 Id

hpa-gps-ingestion-service

#### 8.1.2.2.0.0.0 Type

🔹 Horizontal

#### 8.1.2.3.0.0.0 Component

GPS Ingestion Service

#### 8.1.2.4.0.0.0 Rules

- {'metric': 'kubernetes.io/pod/cpu/utilization', 'threshold': 70, 'operator': 'GREATER_THAN', 'scaleChange': 1, 'cooldown': {'scaleUpSeconds': 120, 'scaleDownSeconds': 300}, 'evaluationPeriods': 3, 'dataPointsToAlarm': 2}

#### 8.1.2.5.0.0.0 Safeguards

| Property | Value |
|----------|-------|
| Min Instances | 2 |
| Max Instances | 5 |
| Max Scaling Rate | 1 pod per 2 minutes |
| Cost Threshold | *N/A* |

#### 8.1.2.6.0.0.0 Schedule

##### 8.1.2.6.1.0.0 Enabled

❌ No

##### 8.1.2.6.2.0.0 Timezone



##### 8.1.2.6.3.0.0 Rules

*No items available*

## 8.2.0.0.0.0.0 Configuration

### 8.2.1.0.0.0.0 Min Instances

2

### 8.2.2.0.0.0.0 Max Instances

10

### 8.2.3.0.0.0.0 Default Timeout

300

### 8.2.4.0.0.0.0 Region

ap-south-1

### 8.2.5.0.0.0.0 Resource Group

tms-prod

### 8.2.6.0.0.0.0 Notification Endpoint

Alertmanager Webhook

### 8.2.7.0.0.0.0 Logging Level

INFO

### 8.2.8.0.0.0.0 Vpc Id

vpc-tms-prod

### 8.2.9.0.0.0.0 Instance Type

Mixed (r6g, t4g)

### 8.2.10.0.0.0.0 Enable Detailed Monitoring

true

### 8.2.11.0.0.0.0 Scaling Mode

hybrid

### 8.2.12.0.0.0.0 Cost Optimization

| Property | Value |
|----------|-------|
| Spot Instances Enabled | ✅ |
| Spot Percentage | 50 |
| Reserved Instances Planned | ✅ |

### 8.2.13.0.0.0.0 Performance Targets

| Property | Value |
|----------|-------|
| Response Time | <200ms (p95) |
| Throughput | 100 concurrent users |
| Availability | 99.9% |

## 8.3.0.0.0.0.0 Environment Specific Policies

### 8.3.1.0.0.0.0 Environment

#### 8.3.1.1.0.0.0 Environment

production

#### 8.3.1.2.0.0.0 Scaling Enabled

✅ Yes

#### 8.3.1.3.0.0.0 Aggressiveness

moderate

#### 8.3.1.4.0.0.0 Cost Priority

balanced

### 8.3.2.0.0.0.0 Environment

#### 8.3.2.1.0.0.0 Environment

staging

#### 8.3.2.2.0.0.0 Scaling Enabled

✅ Yes

#### 8.3.2.3.0.0.0 Aggressiveness

conservative

#### 8.3.2.4.0.0.0 Cost Priority

cost-optimized

### 8.3.3.0.0.0.0 Environment

#### 8.3.3.1.0.0.0 Environment

development

#### 8.3.3.2.0.0.0 Scaling Enabled

❌ No

#### 8.3.3.3.0.0.0 Aggressiveness

conservative

#### 8.3.3.4.0.0.0 Cost Priority

cost-optimized

# 9.0.0.0.0.0.0 Implementation Priority

## 9.1.0.0.0.0.0 Component

### 9.1.1.0.0.0.0 Component

Baseline Horizontal Pod Autoscaler for Odoo and FastAPI

### 9.1.2.0.0.0.0 Priority

🔴 high

### 9.1.3.0.0.0.0 Dependencies

- EKS Cluster Setup
- Prometheus Metrics Server Installation

### 9.1.4.0.0.0.0 Estimated Effort

Low

### 9.1.5.0.0.0.0 Risk Level

low

## 9.2.0.0.0.0.0 Component

### 9.2.1.0.0.0.0 Component

Scheduled Scaling Policies (CronHPA)

### 9.2.2.0.0.0.0 Priority

🟡 medium

### 9.2.3.0.0.0.0 Dependencies

- Baseline HPA

### 9.2.4.0.0.0.0 Estimated Effort

Low

### 9.2.5.0.0.0.0 Risk Level

low

## 9.3.0.0.0.0.0 Component

### 9.3.1.0.0.0.0 Component

Custom Metric Scaling (RabbitMQ Queue Length)

### 9.3.2.0.0.0.0 Priority

🟡 medium

### 9.3.3.0.0.0.0 Dependencies

- KEDA (Kubernetes Event-driven Autoscaling) installation
- RabbitMQ Exporter Setup

### 9.3.4.0.0.0.0 Estimated Effort

Medium

### 9.3.5.0.0.0.0 Risk Level

medium

# 10.0.0.0.0.0.0 Risk Assessment

## 10.1.0.0.0.0.0 Risk

### 10.1.1.0.0.0.0 Risk

Scaling Thrashing

### 10.1.2.0.0.0.0 Impact

medium

### 10.1.3.0.0.0.0 Probability

medium

### 10.1.4.0.0.0.0 Mitigation

Implement appropriate cooldown periods (e.g., 300 seconds for scale-down) and use a wider margin between scale-up and scale-down thresholds (e.g., 75% vs 40%).

### 10.1.5.0.0.0.0 Contingency Plan

Temporarily disable autoscaling for the affected component and manually set the replica count while investigating the trigger conditions.

## 10.2.0.0.0.0.0 Risk

### 10.2.1.0.0.0.0 Risk

Runaway Scaling Costs

### 10.2.2.0.0.0.0 Impact

high

### 10.2.3.0.0.0.0 Probability

low

### 10.2.4.0.0.0.0 Mitigation

Set a sensible `maxInstances` limit on all HPA configurations. Implement AWS budget alerts to notify stakeholders of cost anomalies.

### 10.2.5.0.0.0.0 Contingency Plan

Manually scale down the workload. Investigate the root cause, which could be a misconfigured metric, a bug causing high CPU, or a denial-of-service attack.

# 11.0.0.0.0.0.0 Recommendations

## 11.1.0.0.0.0.0 Category

### 11.1.1.0.0.0.0 Category

🔹 Policy Tuning

### 11.1.2.0.0.0.0 Recommendation

Start with conservative scaling policies and thresholds. Monitor system performance under real-world load for at least two weeks post-launch before making policies more aggressive.

### 11.1.3.0.0.0.0 Justification

Avoids premature or unnecessary scaling events by basing decisions on actual usage patterns rather than assumptions, which optimizes both cost and stability.

### 11.1.4.0.0.0.0 Priority

🔴 high

### 11.1.5.0.0.0.0 Implementation Notes

Use Grafana dashboards to visualize CPU/memory utilization against the HPA thresholds to identify if they are set appropriately.

## 11.2.0.0.0.0.0 Category

### 11.2.1.0.0.0.0 Category

🔹 Resilience

### 11.2.2.0.0.0.0 Recommendation

Implement Kubernetes Pod Disruption Budgets (PDBs) for all critical components (Odoo, FastAPI).

### 11.2.3.0.0.0.0 Justification

Ensures that a minimum number of replicas are always running during voluntary disruptions like node upgrades or deployments, which is crucial for maintaining the 99.9% availability requirement.

### 11.2.4.0.0.0.0 Priority

🔴 high

### 11.2.5.0.0.0.0 Implementation Notes

Set `minAvailable` to at least 2 for the Odoo application and 1 for the GPS service in their respective PDBs.

