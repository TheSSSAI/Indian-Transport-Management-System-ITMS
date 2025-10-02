# 1 Overview

## 1.1 Diagram Id

SEQ-RF-016

## 1.2 Name

Database Point-In-Time-Recovery Process

## 1.3 Description

In response to a data corruption event, an SRE initiates a Point-In-Time-Recovery (PITR) for the Amazon RDS for PostgreSQL database to a state just before the incident occurred.

## 1.4 Type

🔹 RecoveryFlow

## 1.5 Purpose

To restore the production database to a known-good state, minimizing data loss and downtime in a disaster scenario, fulfilling REQ-NFR-002.

## 1.6 Complexity

High

## 1.7 Priority

🚨 Critical

## 1.8 Frequency

OnDemand

## 1.9 Participants

*No items available*

## 1.10 Key Interactions

- A critical data corruption is detected and an incident is declared.
- The application is put into maintenance mode.
- SRE navigates to the AWS RDS console and selects the production database.
- SRE chooses the 'Restore to point in time' option.
- SRE specifies the target timestamp, just prior to the corruption event.
- RDS provisions a new database instance and restores the data from automated snapshots and transaction logs.
- After validation, application connection strings are updated to point to the new, restored database instance.
- The application is taken out of maintenance mode.

## 1.11 Triggers

- A major data loss or corruption incident.

## 1.12 Outcomes

- The database is restored with minimal data loss (within RPO of 15 mins).
- Normal system operation is resumed.

## 1.13 Business Rules

- REQ-NFR-002: RPO is 15 minutes, RTO is 4 hours.

## 1.14 Error Scenarios

- The required transaction logs are unavailable for the target time.
- The restored database fails validation checks.

## 1.15 Integration Points

- Cloud Service: Amazon RDS for PostgreSQL

# 2.0 Details

## 2.1 Diagram Id

SEQ-RF-016

## 2.2 Name

SRE-Initiated RDS Point-In-Time-Recovery (PITR)

## 2.3 Description

Technical sequence for a Site Reliability Engineer (SRE) performing a manual Point-In-Time-Recovery of the production AWS RDS for PostgreSQL database following a critical data corruption incident. This flow details the steps from alert to service restoration, adhering to the system's RTO and RPO as defined in REQ-NFR-002.

## 2.4 Participants

### 2.4.1 Human Actor

#### 2.4.1.1 Repository Id

Actor:SRE

#### 2.4.1.2 Display Name

SRE (Site Reliability Engineer)

#### 2.4.1.3 Type

🔹 Human Actor

#### 2.4.1.4 Technology

IAM User with required permissions

#### 2.4.1.5 Order

1

#### 2.4.1.6 Style

| Property | Value |
|----------|-------|
| Shape | actor |
| Color | #990000 |
| Stereotype | Human |

### 2.4.2.0 Monitoring Service

#### 2.4.2.1 Repository Id

REPO-MON-PROMETHEUS

#### 2.4.2.2 Display Name

Prometheus / Alertmanager

#### 2.4.2.3 Type

🔹 Monitoring Service

#### 2.4.2.4 Technology

Prometheus, Alertmanager

#### 2.4.2.5 Order

2

#### 2.4.2.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #FF9900 |
| Stereotype | Monitoring |

### 2.4.3.0 Application Service

#### 2.4.3.1 Repository Id

REPO-TMS-CORE

#### 2.4.3.2 Display Name

TMS Application (Odoo)

#### 2.4.3.3 Type

🔹 Application Service

#### 2.4.3.4 Technology

Odoo 18, Python 3.11

#### 2.4.3.5 Order

3

#### 2.4.3.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #1E90FF |
| Stereotype | Service |

### 2.4.4.0 Container Orchestrator

#### 2.4.4.1 Repository Id

INFRA-AWS-EKS

#### 2.4.4.2 Display Name

Amazon EKS Control Plane

#### 2.4.4.3 Type

🔹 Container Orchestrator

#### 2.4.4.4 Technology

Kubernetes

#### 2.4.4.5 Order

4

#### 2.4.4.6 Style

| Property | Value |
|----------|-------|
| Shape | component |
| Color | #232F3E |
| Stereotype | Infrastructure |

### 2.4.5.0 Secrets Store

#### 2.4.5.1 Repository Id

INFRA-AWS-SECRETS-MANAGER

#### 2.4.5.2 Display Name

AWS Secrets Manager

#### 2.4.5.3 Type

🔹 Secrets Store

#### 2.4.5.4 Technology

AWS Service

#### 2.4.5.5 Order

5

#### 2.4.5.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #232F3E |
| Stereotype | Infrastructure |

### 2.4.6.0 Database

#### 2.4.6.1 Repository Id

INFRA-AWS-RDS-PRIMARY

#### 2.4.6.2 Display Name

Primary RDS DB (Corrupted)

#### 2.4.6.3 Type

🔹 Database

#### 2.4.6.4 Technology

PostgreSQL 16

#### 2.4.6.5 Order

6

#### 2.4.6.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #D9534F |
| Stereotype | Database |

### 2.4.7.0 External System Interface

#### 2.4.7.1 Repository Id

EXT-AWS-CONSOLE

#### 2.4.7.2 Display Name

AWS Management Console

#### 2.4.7.3 Type

🔹 External System Interface

#### 2.4.7.4 Technology

Web Application

#### 2.4.7.5 Order

7

#### 2.4.7.6 Style

| Property | Value |
|----------|-------|
| Shape | boundary |
| Color | #5A6B86 |
| Stereotype | External |

### 2.4.8.0 Database

#### 2.4.8.1 Repository Id

INFRA-AWS-RDS-RESTORED

#### 2.4.8.2 Display Name

Restored RDS DB

#### 2.4.8.3 Type

🔹 Database

#### 2.4.8.4 Technology

PostgreSQL 16

#### 2.4.8.5 Order

8

#### 2.4.8.6 Style

| Property | Value |
|----------|-------|
| Shape | database |
| Color | #5CB85C |
| Stereotype | Database |

## 2.5.0.0 Interactions

### 2.5.1.0 Notification

#### 2.5.1.1 Source Id

REPO-MON-PROMETHEUS

#### 2.5.1.2 Target Id

Actor:SRE

#### 2.5.1.3 Message

Fire Critical Alert: 'Data Corruption Detected' or 'High DB Error Rate'

#### 2.5.1.4 Sequence Number

1

#### 2.5.1.5 Type

🔹 Notification

#### 2.5.1.6 Is Synchronous

❌ No

#### 2.5.1.7 Return Message



#### 2.5.1.8 Has Return

❌ No

#### 2.5.1.9 Is Activation

✅ Yes

#### 2.5.1.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PagerDuty/Slack/Email |
| Method | SendNotification |
| Parameters | Alert details, severity, runbook link |
| Authentication | N/A |
| Error Handling | Alertmanager escalation policies |
| Performance | Latency < 1 minute |

### 2.5.2.0 CLI Command

#### 2.5.2.1 Source Id

Actor:SRE

#### 2.5.2.2 Target Id

INFRA-AWS-EKS

#### 2.5.2.3 Message

Enable Maintenance Mode (e.g., apply config map, scale down deployment)

#### 2.5.2.4 Sequence Number

2

#### 2.5.2.5 Type

🔹 CLI Command

#### 2.5.2.6 Is Synchronous

✅ Yes

#### 2.5.2.7 Return Message

Deployment scaled / ConfigMap applied

#### 2.5.2.8 Has Return

✅ Yes

#### 2.5.2.9 Is Activation

❌ No

#### 2.5.2.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Kubernetes API |
| Method | kubectl apply -f maintenance-config.yaml |
| Parameters | Namespace, deployment name |
| Authentication | Kubeconfig file with valid IAM credentials |
| Error Handling | CLI returns error if command fails. |
| Performance | Latency < 30 seconds |

### 2.5.3.0 User Interaction

#### 2.5.3.1 Source Id

Actor:SRE

#### 2.5.3.2 Target Id

EXT-AWS-CONSOLE

#### 2.5.3.3 Message

Initiate 'Restore to point in time'

#### 2.5.3.4 Sequence Number

3

#### 2.5.3.5 Type

🔹 User Interaction

#### 2.5.3.6 Is Synchronous

✅ Yes

#### 2.5.3.7 Return Message

Restore configuration UI

#### 2.5.3.8 Has Return

✅ Yes

#### 2.5.3.9 Is Activation

✅ Yes

#### 2.5.3.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | GUI Navigation |
| Parameters | Database instance identifier |
| Authentication | MFA-authenticated IAM user session |
| Error Handling | UI displays errors if instance not found or permis... |
| Performance | Standard web UI latency |

### 2.5.4.0 API Call

#### 2.5.4.1 Source Id

EXT-AWS-CONSOLE

#### 2.5.4.2 Target Id

INFRA-AWS-RDS-PRIMARY

#### 2.5.4.3 Message

aws rds restore-db-instance-to-point-in-time

#### 2.5.4.4 Sequence Number

4

#### 2.5.4.5 Type

🔹 API Call

#### 2.5.4.6 Is Synchronous

✅ Yes

#### 2.5.4.7 Return Message

Restore task initiated

#### 2.5.4.8 Has Return

✅ Yes

#### 2.5.4.9 Is Activation

✅ Yes

#### 2.5.4.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AWS SDK/API |
| Method | RestoreDBInstanceToPointInTime |
| Parameters | { SourceDBInstanceIdentifier, TargetDBInstanceIden... |
| Authentication | IAM role credentials from user session |
| Error Handling | API call returns InvalidParameterValueException, D... |
| Performance | Latency < 2 seconds |

### 2.5.5.0 Asynchronous Process

#### 2.5.5.1 Source Id

INFRA-AWS-RDS-PRIMARY

#### 2.5.5.2 Target Id

INFRA-AWS-RDS-RESTORED

#### 2.5.5.3 Message

Provision & Restore Data from Snapshots and Transaction Logs

#### 2.5.5.4 Sequence Number

5

#### 2.5.5.5 Type

🔹 Asynchronous Process

#### 2.5.5.6 Is Synchronous

❌ No

#### 2.5.5.7 Return Message



#### 2.5.5.8 Has Return

❌ No

#### 2.5.5.9 Is Activation

✅ Yes

#### 2.5.5.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal AWS Process |
| Method | Data Plane Restoration |
| Parameters | Target timestamp, backup data sources |
| Authentication | N/A |
| Error Handling | Process failure is reported in AWS Console/CloudWa... |
| Performance | Variable; can take minutes to hours depending on D... |

### 2.5.6.0 Status Update

#### 2.5.6.1 Source Id

INFRA-AWS-RDS-RESTORED

#### 2.5.6.2 Target Id

EXT-AWS-CONSOLE

#### 2.5.6.3 Message

Status: 'Available'

#### 2.5.6.4 Sequence Number

6

#### 2.5.6.5 Type

🔹 Status Update

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
| Protocol | AWS CloudWatch Events |
| Method | Event Notification |
| Parameters | New instance details, endpoint URL |
| Authentication | N/A |
| Error Handling | N/A |
| Performance | Near real-time |

### 2.5.7.0 Database Query

#### 2.5.7.1 Source Id

Actor:SRE

#### 2.5.7.2 Target Id

INFRA-AWS-RDS-RESTORED

#### 2.5.7.3 Message

Execute Data Validation Script

#### 2.5.7.4 Sequence Number

7

#### 2.5.7.5 Type

🔹 Database Query

#### 2.5.7.6 Is Synchronous

✅ Yes

#### 2.5.7.7 Return Message

Validation Result (OK / FAILED)

#### 2.5.7.8 Has Return

✅ Yes

#### 2.5.7.9 Is Activation

❌ No

#### 2.5.7.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL Wire Protocol |
| Method | psql -h <new-endpoint> -f validate.sql |
| Parameters | DB credentials (temporary access) |
| Authentication | Database user/password |
| Error Handling | Script fails if data integrity checks fail (e.g., ... |
| Performance | Latency dependent on query complexity |

### 2.5.8.0 API Call / CLI

#### 2.5.8.1 Source Id

Actor:SRE

#### 2.5.8.2 Target Id

INFRA-AWS-SECRETS-MANAGER

#### 2.5.8.3 Message

Update Database Connection Secret

#### 2.5.8.4 Sequence Number

8

#### 2.5.8.5 Type

🔹 API Call / CLI

#### 2.5.8.6 Is Synchronous

✅ Yes

#### 2.5.8.7 Return Message

Secret updated successfully

#### 2.5.8.8 Has Return

✅ Yes

#### 2.5.8.9 Is Activation

✅ Yes

#### 2.5.8.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | AWS SDK/API |
| Method | aws secretsmanager update-secret |
| Parameters | Secret ID, new secret string (with restored DB end... |
| Authentication | IAM credentials |
| Error Handling | API call fails if permissions are incorrect or sec... |
| Performance | Latency < 2 seconds |

### 2.5.9.0 CLI Command

#### 2.5.9.1 Source Id

Actor:SRE

#### 2.5.9.2 Target Id

INFRA-AWS-EKS

#### 2.5.9.3 Message

Trigger Rolling Restart of Application Deployment

#### 2.5.9.4 Sequence Number

9

#### 2.5.9.5 Type

🔹 CLI Command

#### 2.5.9.6 Is Synchronous

✅ Yes

#### 2.5.9.7 Return Message

Deployment restart triggered

#### 2.5.9.8 Has Return

✅ Yes

#### 2.5.9.9 Is Activation

✅ Yes

#### 2.5.9.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Kubernetes API |
| Method | kubectl rollout restart deployment/tms-app |
| Parameters | Deployment name, namespace |
| Authentication | Kubeconfig with IAM credentials |
| Error Handling | CLI returns error if deployment not found. |
| Performance | Latency < 5 seconds |

### 2.5.10.0 Orchestration

#### 2.5.10.1 Source Id

INFRA-AWS-EKS

#### 2.5.10.2 Target Id

REPO-TMS-CORE

#### 2.5.10.3 Message

Create New Pods; Pods fetch new secret

#### 2.5.10.4 Sequence Number

10

#### 2.5.10.5 Type

🔹 Orchestration

#### 2.5.10.6 Is Synchronous

❌ No

#### 2.5.10.7 Return Message



#### 2.5.10.8 Has Return

❌ No

#### 2.5.10.9 Is Activation

✅ Yes

#### 2.5.10.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Internal K8s/AWS Integration |
| Method | Pod Initialization |
| Parameters | Deployment spec, Secrets Store CSI driver config |
| Authentication | IAM Role for Service Account (IRSA) |
| Error Handling | Pod will fail to start and enter CrashLoopBackOff ... |
| Performance | Dependent on image pull time and app start time. |

### 2.5.11.0 Database Connection

#### 2.5.11.1 Source Id

REPO-TMS-CORE

#### 2.5.11.2 Target Id

INFRA-AWS-RDS-RESTORED

#### 2.5.11.3 Message

Establish Connection Pool

#### 2.5.11.4 Sequence Number

11

#### 2.5.11.5 Type

🔹 Database Connection

#### 2.5.11.6 Is Synchronous

✅ Yes

#### 2.5.11.7 Return Message

Connection successful

#### 2.5.11.8 Has Return

✅ Yes

#### 2.5.11.9 Is Activation

❌ No

#### 2.5.11.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | PostgreSQL Wire Protocol |
| Method | Connect() |
| Parameters | Host, Port, User, Password from secret |
| Authentication | Database credentials |
| Error Handling | Application logs connection errors; readiness prob... |
| Performance | Low latency required for fast startup. |

### 2.5.12.0 User Interaction

#### 2.5.12.1 Source Id

Actor:SRE

#### 2.5.12.2 Target Id

REPO-TMS-CORE

#### 2.5.12.3 Message

Perform Smoke Tests on Application

#### 2.5.12.4 Sequence Number

12

#### 2.5.12.5 Type

🔹 User Interaction

#### 2.5.12.6 Is Synchronous

✅ Yes

#### 2.5.12.7 Return Message

Smoke Tests Passed

#### 2.5.12.8 Has Return

✅ Yes

#### 2.5.12.9 Is Activation

❌ No

#### 2.5.12.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | HTTPS |
| Method | GET, POST requests |
| Parameters | Test user credentials, sample data |
| Authentication | Application-level user authentication |
| Error Handling | Investigate application logs and pod status if tes... |
| Performance | N/A |

### 2.5.13.0 CLI Command

#### 2.5.13.1 Source Id

Actor:SRE

#### 2.5.13.2 Target Id

INFRA-AWS-EKS

#### 2.5.13.3 Message

Disable Maintenance Mode

#### 2.5.13.4 Sequence Number

13

#### 2.5.13.5 Type

🔹 CLI Command

#### 2.5.13.6 Is Synchronous

✅ Yes

#### 2.5.13.7 Return Message

Maintenance mode disabled

#### 2.5.13.8 Has Return

✅ Yes

#### 2.5.13.9 Is Activation

❌ No

#### 2.5.13.10 Technical Details

| Property | Value |
|----------|-------|
| Protocol | Kubernetes API |
| Method | kubectl apply -f production-config.yaml |
| Parameters | Namespace, deployment name |
| Authentication | Kubeconfig with IAM credentials |
| Error Handling | CLI returns error if command fails. |
| Performance | Latency < 30 seconds |

## 2.6.0.0 Notes

### 2.6.1.0 Content

#### 2.6.1.1 Content

This entire process must be documented in a version-controlled runbook and tested via regular DR drills.

#### 2.6.1.2 Position

top

#### 2.6.1.3 Participant Id

*Not specified*

#### 2.6.1.4 Sequence Number

0

### 2.6.2.0 Content

#### 2.6.2.1 Content

Data loss is possible for transactions occurring between the last backup and the restore point. RPO is 15 minutes.

#### 2.6.2.2 Position

bottom

#### 2.6.2.3 Participant Id

INFRA-AWS-RDS-PRIMARY

#### 2.6.2.4 Sequence Number

4

### 2.6.3.0 Content

#### 2.6.3.1 Content

Validation is the most critical manual step. The script must be comprehensive to ensure business data consistency.

#### 2.6.3.2 Position

right

#### 2.6.3.3 Participant Id

Actor:SRE

#### 2.6.3.4 Sequence Number

7

## 2.7.0.0 Implementation Guidance

| Property | Value |
|----------|-------|
| Security Requirements | The SRE must operate under an IAM role with tightl... |
| Performance Targets | Recovery Time Objective (RTO) is 4 hours from inci... |
| Error Handling Strategy | If PITR fails (e.g., transaction logs unavailable)... |
| Testing Considerations | The entire recovery procedure must be tested quart... |
| Monitoring Requirements | During recovery, monitor the RDS restore progress ... |
| Deployment Considerations | This is a high-impact, manual procedure. The prima... |

