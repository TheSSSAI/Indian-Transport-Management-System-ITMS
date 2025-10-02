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
- Terraform
- GitHub Actions

## 1.3 Architecture Patterns

- Hybrid (Modular Monolith with Decoupled Microservice)
- Event-Driven (for GPS data)
- Cloud-Native

## 1.4 Data Handling Needs

- Personally Identifiable Information (PII) for Drivers and Customers
- Financial Transactional Data (Invoices, Payments, Expenses)
- High-Volume Time-Series Location Data (GPS)
- File Attachments (PODs, Receipts)

## 1.5 Performance Expectations

High availability (99.9%), low latency for web requests (<200ms p95), and near real-time processing for GPS data (<10s end-to-end latency).

## 1.6 Regulatory Requirements

- Indian Goods and Services Tax Act, 2017 (for e-invoicing)
- Indian Digital Personal Data Protection Act (DPDPA), 2023
- Indian Motor Vehicles Act, 1988

# 2.0 Environment Strategy

## 2.1 Environment Types

### 2.1.1 Development

#### 2.1.1.1 Type

🔹 Development

#### 2.1.1.2 Purpose

Individual developer workspaces for feature development and unit testing.

#### 2.1.1.3 Usage Patterns

- Code development
- Unit testing
- Local debugging

#### 2.1.1.4 Isolation Level

partial

#### 2.1.1.5 Data Policy

Uses minimal, locally generated, or heavily anonymized seed data.

#### 2.1.1.6 Lifecycle Management

Ephemeral, created and destroyed on-demand by developers (e.g., Docker Compose).

### 2.1.2.0 Testing

#### 2.1.2.1 Type

🔹 Testing

#### 2.1.2.2 Purpose

Shared environment for the QA team to perform integration testing, regression testing, and validation of new features.

#### 2.1.2.3 Usage Patterns

- Automated integration tests
- Manual QA validation
- Regression suite execution

#### 2.1.2.4 Isolation Level

shared

#### 2.1.2.5 Data Policy

Uses a larger, more comprehensive set of anonymized/masked data, refreshed periodically.

#### 2.1.2.6 Lifecycle Management

Persistent, updated automatically by CI/CD pipeline on successful builds of feature branches.

### 2.1.3.0 Staging

#### 2.1.3.1 Type

🔹 Staging

#### 2.1.3.2 Purpose

A production-like environment for User Acceptance Testing (UAT), performance testing, and final pre-release validation.

#### 2.1.3.3 Usage Patterns

- UAT by business stakeholders
- Load and performance testing
- Data migration dry-runs (REQ-TRN-002)
- Pre-release validation

#### 2.1.3.4 Isolation Level

complete

#### 2.1.3.5 Data Policy

Uses a recently anonymized and masked full-scale copy of the production database.

#### 2.1.3.6 Lifecycle Management

Persistent, a stable replica of production. Updated by CI/CD only for release candidates.

### 2.1.4.0 Production

#### 2.1.4.1 Type

🔹 Production

#### 2.1.4.2 Purpose

The live environment used by all end-users to conduct business operations.

#### 2.1.4.3 Usage Patterns

- Live business transactions
- Real-time vehicle tracking
- Financial reporting

#### 2.1.4.4 Isolation Level

complete

#### 2.1.4.5 Data Policy

Live, real customer and operational data.

#### 2.1.4.6 Lifecycle Management

Highly controlled, persistent environment. Changes are only applied through a strict, audited CI/CD release process.

### 2.1.5.0 DR

#### 2.1.5.1 Type

🔹 DR

#### 2.1.5.2 Purpose

A disaster recovery environment to meet the RTO/RPO requirements in case of a full regional failure of the primary production site.

#### 2.1.5.3 Usage Patterns

- Failover target
- Periodic DR drills

#### 2.1.5.4 Isolation Level

complete

#### 2.1.5.5 Data Policy

Continuously replicated data from the production environment (e.g., cross-region DB replicas/snapshots).

#### 2.1.5.6 Lifecycle Management

Hot or Warm standby, defined via Infrastructure as Code (Terraform) for rapid provisioning.

## 2.2.0.0 Promotion Strategy

### 2.2.1.0 Workflow

Development -> Testing -> Staging -> Production. Code is merged from feature branches to a 'develop' branch for Testing, then to a 'release' branch for Staging, and finally to 'main' for Production deployment.

### 2.2.2.0 Approval Gates

- Automated tests must pass in Testing environment
- Manual QA sign-off in Testing
- Business stakeholder UAT sign-off in Staging
- Change Advisory Board (CAB) approval for Production release

### 2.2.3.0 Automation Level

automated

### 2.2.4.0 Rollback Procedure

Automated rollback via CI/CD pipeline to redeploy the previous stable version. Database changes require a manual, pre-scripted rollback procedure or restore from backup.

## 2.3.0.0 Isolation Strategies

### 2.3.1.0 Environment

#### 2.3.1.1 Environment

Production

#### 2.3.1.2 Isolation Type

complete

#### 2.3.1.3 Implementation

Dedicated AWS account or a dedicated VPC with strict network ACLs and Security Groups. Separate IAM roles, KMS keys, and database instances.

#### 2.3.1.4 Justification

Protects live customer and financial data from unauthorized access and prevents non-production activities from impacting business operations.

### 2.3.2.0 Environment

#### 2.3.2.1 Environment

Staging

#### 2.3.2.2 Isolation Type

complete

#### 2.3.2.3 Implementation

Dedicated VPC, separate from Production and other non-production environments to ensure performance tests are accurate and security posture mirrors production.

#### 2.3.2.4 Justification

Ensures a high-fidelity testing environment that accurately reflects production performance and security characteristics.

### 2.3.3.0 Environment

#### 2.3.3.1 Environment

Development/Testing

#### 2.3.3.2 Isolation Type

network

#### 2.3.3.3 Implementation

A shared VPC for all development and testing workloads, with separation enforced by Security Groups and Kubernetes namespaces.

#### 2.3.3.4 Justification

Balances isolation needs with cost-effectiveness for non-critical, pre-production environments.

## 2.4.0.0 Scaling Approaches

### 2.4.1.0 Environment

#### 2.4.1.1 Environment

Production

#### 2.4.1.2 Scaling Type

auto

#### 2.4.1.3 Triggers

- CPU Utilization > 70%
- Memory Utilization > 75%
- RabbitMQ Queue Depth > 1000

#### 2.4.1.4 Limits

Configurable min/max replica counts for EKS deployments.

### 2.4.2.0 Environment

#### 2.4.2.1 Environment

Staging

#### 2.4.2.2 Scaling Type

horizontal

#### 2.4.2.3 Triggers

- Manual scaling for performance tests

#### 2.4.2.4 Limits

Sized to handle 1.5x expected production load for stress testing.

### 2.4.3.0 Environment

#### 2.4.3.1 Environment

Testing

#### 2.4.3.2 Scaling Type

vertical

#### 2.4.3.3 Triggers

- Fixed size, manually adjusted if needed

#### 2.4.3.4 Limits

Sufficient to run all automated tests and support a small number of concurrent QA users.

## 2.5.0.0 Provisioning Automation

| Property | Value |
|----------|-------|
| Tool | Terraform |
| Templating | Uses Terraform modules for reusable components (e.... |
| State Management | Terraform Cloud or S3 backend with DynamoDB lockin... |
| Cicd Integration | ✅ |

# 3.0.0.0 Resource Requirements Analysis

## 3.1.0.0 Workload Analysis

### 3.1.1.0 Workload Type

#### 3.1.1.1 Workload Type

Odoo Monolith

#### 3.1.1.2 Expected Load

100 concurrent users performing transactional operations.

#### 3.1.1.3 Peak Capacity

150 concurrent users

#### 3.1.1.4 Resource Profile

balanced

### 3.1.2.0 Workload Type

#### 3.1.2.1 Workload Type

GPS Ingestion Microservice

#### 3.1.2.2 Expected Load

High volume of small, frequent API calls (e.g., 1000 vehicles polling every 60s).

#### 3.1.2.3 Peak Capacity

2000 vehicles polling every 30s

#### 3.1.2.4 Resource Profile

io-intensive

### 3.1.3.0 Workload Type

#### 3.1.3.1 Workload Type

Reporting & Analytics

#### 3.1.3.2 Expected Load

Periodic, intensive database queries for report generation.

#### 3.1.3.3 Peak Capacity

Multiple large reports generated simultaneously at month-end.

#### 3.1.3.4 Resource Profile

cpu-intensive

## 3.2.0.0 Compute Requirements

### 3.2.1.0 Environment

#### 3.2.1.1 Environment

Production

#### 3.2.1.2 Instance Type

EKS Node Group: m5.large; RDS: db.m5.xlarge (Multi-AZ)

#### 3.2.1.3 Cpu Cores

0

#### 3.2.1.4 Memory Gb

0

#### 3.2.1.5 Instance Count

0

#### 3.2.1.6 Auto Scaling

##### 3.2.1.6.1 Enabled

✅ Yes

##### 3.2.1.6.2 Min Instances

3

##### 3.2.1.6.3 Max Instances

8

##### 3.2.1.6.4 Scaling Triggers

- Cluster CPU/Memory pressure

#### 3.2.1.7.0 Justification

Meets 99.9% availability NFR (REQ-NFR-002) with multiple replicas and provides elasticity for varying loads. Multi-AZ RDS for database high availability.

### 3.2.2.0.0 Environment

#### 3.2.2.1.0 Environment

Staging

#### 3.2.2.2.0 Instance Type

EKS Node Group: m5.large; RDS: db.m5.large (Single-AZ)

#### 3.2.2.3.0 Cpu Cores

0

#### 3.2.2.4.0 Memory Gb

0

#### 3.2.2.5.0 Instance Count

0

#### 3.2.2.6.0 Auto Scaling

##### 3.2.2.6.1 Enabled

❌ No

##### 3.2.2.6.2 Min Instances

2

##### 3.2.2.6.3 Max Instances

2

##### 3.2.2.6.4 Scaling Triggers

*No items available*

#### 3.2.2.7.0 Justification

Provides a production-like environment for accurate UAT and performance testing at a reduced cost (Single-AZ DB).

### 3.2.3.0.0 Environment

#### 3.2.3.1.0 Environment

Testing

#### 3.2.3.2.0 Instance Type

EKS Node Group: t3.medium; RDS: db.t3.medium (Single-AZ)

#### 3.2.3.3.0 Cpu Cores

0

#### 3.2.3.4.0 Memory Gb

0

#### 3.2.3.5.0 Instance Count

0

#### 3.2.3.6.0 Auto Scaling

##### 3.2.3.6.1 Enabled

❌ No

##### 3.2.3.6.2 Min Instances

1

##### 3.2.3.6.3 Max Instances

1

##### 3.2.3.6.4 Scaling Triggers

*No items available*

#### 3.2.3.7.0 Justification

Cost-effective environment sufficient for running automated test suites and supporting a small QA team.

## 3.3.0.0.0 Storage Requirements

### 3.3.1.0.0 Environment

#### 3.3.1.1.0 Environment

Production

#### 3.3.1.2.0 Storage Type

block

#### 3.3.1.3.0 Capacity

Initial 500GB, auto-scaling enabled

#### 3.3.1.4.0 Iops Requirements

3000 provisioned IOPS

#### 3.3.1.5.0 Throughput Requirements

250 MB/s

#### 3.3.1.6.0 Redundancy

Multi-AZ

#### 3.3.1.7.0 Encryption

✅ Yes

### 3.3.2.0.0 Environment

#### 3.3.2.1.0 Environment

Production

#### 3.3.2.2.0 Storage Type

object

#### 3.3.2.3.0 Capacity

Scales on demand (Amazon S3)

#### 3.3.2.4.0 Iops Requirements

N/A

#### 3.3.2.5.0 Throughput Requirements

N/A

#### 3.3.2.6.0 Redundancy

Multi-AZ by default

#### 3.3.2.7.0 Encryption

✅ Yes

### 3.3.3.0.0 Environment

#### 3.3.3.1.0 Environment

Staging

#### 3.3.3.2.0 Storage Type

block

#### 3.3.3.3.0 Capacity

500GB fixed

#### 3.3.3.4.0 Iops Requirements

1000 provisioned IOPS

#### 3.3.3.5.0 Throughput Requirements

125 MB/s

#### 3.3.3.6.0 Redundancy

Single-AZ

#### 3.3.3.7.0 Encryption

✅ Yes

## 3.4.0.0.0 Special Hardware Requirements

*No items available*

## 3.5.0.0.0 Scaling Strategies

- {'environment': 'Production', 'strategy': 'reactive', 'implementation': 'Kubernetes Horizontal Pod Autoscaler (HPA) for application pods (Odoo, FastAPI) based on CPU/memory. AWS Cluster Autoscaler for EKS worker nodes.', 'costOptimization': 'Scale-to-zero for non-critical services during off-peak hours can be considered in the future.'}

# 4.0.0.0.0 Security Architecture

## 4.1.0.0.0 Authentication Controls

### 4.1.1.0.0 Method

#### 4.1.1.1.0 Method

mfa

#### 4.1.1.2.0 Scope

All users with access to Odoo UI, especially Admin roles.

#### 4.1.1.3.0 Implementation

Leverage Odoo's built-in multi-factor authentication capabilities (REQ-NFR-003).

#### 4.1.1.4.0 Environment

Staging, Production

### 4.1.2.0.0 Method

#### 4.1.2.1.0 Method

api-keys

#### 4.1.2.2.0 Scope

Programmatic access to third-party GSP and GPS APIs.

#### 4.1.2.3.0 Implementation

Securely stored and managed via AWS Secrets Manager and injected into the runtime environment (REQ-NFR-003).

#### 4.1.2.4.0 Environment

Production

## 4.2.0.0.0 Authorization Controls

### 4.2.1.0.0 Model

#### 4.2.1.1.0 Model

rbac

#### 4.2.1.2.0 Implementation

Strictly enforced using Odoo's native security model (ir.model.access.csv, ir.rule) as defined in REQ-FNC-001.

#### 4.2.1.3.0 Granularity

fine-grained

#### 4.2.1.4.0 Environment

Development, Testing, Staging, Production

### 4.2.2.0.0 Model

#### 4.2.2.1.0 Model

iam

#### 4.2.2.2.0 Implementation

AWS IAM Roles for Service Accounts (IRSA) to grant pods least-privilege access to AWS services like S3 and Secrets Manager.

#### 4.2.2.3.0 Granularity

fine-grained

#### 4.2.2.4.0 Environment

Development, Testing, Staging, Production

## 4.3.0.0.0 Certificate Management

| Property | Value |
|----------|-------|
| Authority | external |
| Rotation Policy | Annual rotation, automated. |
| Automation | ✅ |
| Monitoring | ✅ |

## 4.4.0.0.0 Encryption Standards

### 4.4.1.0.0 Scope

#### 4.4.1.1.0 Scope

data-in-transit

#### 4.4.1.2.0 Algorithm

TLS 1.2 or newer

#### 4.4.1.3.0 Key Management

AWS Certificate Manager (ACM)

#### 4.4.1.4.0 Compliance

*No items available*

### 4.4.2.0.0 Scope

#### 4.4.2.1.0 Scope

data-at-rest

#### 4.4.2.2.0 Algorithm

AES-256

#### 4.4.2.3.0 Key Management

AWS Key Management Service (KMS)

#### 4.4.2.4.0 Compliance

- DPDPA, 2023

## 4.5.0.0.0 Access Control Mechanisms

### 4.5.1.0.0 security-groups

#### 4.5.1.1.0 Type

🔹 security-groups

#### 4.5.1.2.0 Configuration

Stateful firewalls at the ENI level, configured with least-privilege rules (e.g., RDS only accepts traffic from EKS nodes on port 5432).

#### 4.5.1.3.0 Environment

All

#### 4.5.1.4.0 Rules

*No items available*

### 4.5.2.0.0 waf

#### 4.5.2.1.0 Type

🔹 waf

#### 4.5.2.2.0 Configuration

AWS WAF attached to the Application Load Balancer to protect against common web exploits (OWASP Top 10) as per REQ-NFR-003.

#### 4.5.2.3.0 Environment

Production

#### 4.5.2.4.0 Rules

- AWS Managed Rules for SQLi, XSS
- Rate-based rules

## 4.6.0.0.0 Data Protection Measures

- {'dataType': 'pii', 'protectionMethod': 'masking', 'implementation': 'Custom scripts will be used to mask or anonymize PII data (driver names, contact details, etc.) when refreshing non-production environments from production backups.', 'compliance': ['DPDPA, 2023']}

## 4.7.0.0.0 Network Security

- {'control': 'ids', 'implementation': 'AWS GuardDuty enabled for intelligent threat detection across the AWS account.', 'rules': [], 'monitoring': True}

## 4.8.0.0.0 Security Monitoring

### 4.8.1.0.0 vulnerability-scanning

#### 4.8.1.1.0 Type

🔹 vulnerability-scanning

#### 4.8.1.2.0 Implementation

Automated container image scanning (e.g., Trivy, AWS ECR Scan) integrated into the CI/CD pipeline. Periodic scans of the running EKS cluster.

#### 4.8.1.3.0 Frequency

On every code commit and weekly

#### 4.8.1.4.0 Alerting

✅ Yes

### 4.8.2.0.0 pen-testing

#### 4.8.2.1.0 Type

🔹 pen-testing

#### 4.8.2.2.0 Implementation

Third-party penetration test to be conducted before initial launch and annually thereafter (REQ-NFR-003).

#### 4.8.2.3.0 Frequency

Annually

#### 4.8.2.4.0 Alerting

❌ No

## 4.9.0.0.0 Backup Security

| Property | Value |
|----------|-------|
| Encryption | ✅ |
| Access Control | Restricted IAM policies for accessing backup data. |
| Offline Storage | ❌ |
| Testing Frequency | Quarterly |

## 4.10.0.0.0 Compliance Frameworks

- {'framework': 'dpdpa', 'applicableEnvironments': ['Production', 'Staging'], 'controls': ['Data encryption at rest', 'Data masking for non-prod', 'Strict RBAC'], 'auditFrequency': 'Annually'}

# 5.0.0.0.0 Network Design

## 5.1.0.0.0 Network Segmentation

### 5.1.1.0.0 Environment

#### 5.1.1.1.0 Environment

All

#### 5.1.1.2.0 Segment Type

private

#### 5.1.1.3.0 Purpose

Hosting EKS worker nodes, RDS database, ElastiCache, and Amazon MQ to prevent direct internet exposure.

#### 5.1.1.4.0 Isolation

virtual

### 5.1.2.0.0 Environment

#### 5.1.2.1.0 Environment

All

#### 5.1.2.2.0 Segment Type

public

#### 5.1.2.3.0 Purpose

Hosting Application Load Balancers and NAT Gateways for controlled ingress and egress traffic.

#### 5.1.2.4.0 Isolation

virtual

## 5.2.0.0.0 Subnet Strategy

### 5.2.1.0.0 Environment

#### 5.2.1.1.0 Environment

Production

#### 5.2.1.2.0 Subnet Type

private

#### 5.2.1.3.0 Cidr Block

10.0.1.0/24

#### 5.2.1.4.0 Availability Zone

ap-south-1a

#### 5.2.1.5.0 Routing Table

Route to NAT Gateway

### 5.2.2.0.0 Environment

#### 5.2.2.1.0 Environment

Production

#### 5.2.2.2.0 Subnet Type

private

#### 5.2.2.3.0 Cidr Block

10.0.2.0/24

#### 5.2.2.4.0 Availability Zone

ap-south-1b

#### 5.2.2.5.0 Routing Table

Route to NAT Gateway

### 5.2.3.0.0 Environment

#### 5.2.3.1.0 Environment

Production

#### 5.2.3.2.0 Subnet Type

public

#### 5.2.3.3.0 Cidr Block

10.0.101.0/24

#### 5.2.3.4.0 Availability Zone

ap-south-1a

#### 5.2.3.5.0 Routing Table

Route to Internet Gateway

## 5.3.0.0.0 Security Group Rules

### 5.3.1.0.0 Group Name

#### 5.3.1.1.0 Group Name

sg-rds-prod

#### 5.3.1.2.0 Direction

inbound

#### 5.3.1.3.0 Protocol

tcp

#### 5.3.1.4.0 Port Range

5432

#### 5.3.1.5.0 Source

sg-eks-nodes-prod

#### 5.3.1.6.0 Purpose

Allow database access only from the application tier.

### 5.3.2.0.0 Group Name

#### 5.3.2.1.0 Group Name

sg-eks-nodes-prod

#### 5.3.2.2.0 Direction

inbound

#### 5.3.2.3.0 Protocol

tcp

#### 5.3.2.4.0 Port Range

8069

#### 5.3.2.5.0 Source

sg-alb-prod

#### 5.3.2.6.0 Purpose

Allow traffic from the load balancer to the Odoo application.

### 5.3.3.0.0 Group Name

#### 5.3.3.1.0 Group Name

sg-alb-prod

#### 5.3.3.2.0 Direction

inbound

#### 5.3.3.3.0 Protocol

tcp

#### 5.3.3.4.0 Port Range

443

#### 5.3.3.5.0 Source

0.0.0.0/0

#### 5.3.3.6.0 Purpose

Allow HTTPS traffic from the internet to the application.

## 5.4.0.0.0 Connectivity Requirements

- {'source': 'EKS Pods (Private Subnet)', 'destination': 'Internet (GSP/GPS APIs)', 'protocol': 'https', 'bandwidth': '1 Gbps', 'latency': '<100ms'}

## 5.5.0.0.0 Network Monitoring

- {'type': 'flow-logs', 'implementation': 'VPC Flow Logs enabled and sent to a centralized logging solution for analysis and threat detection.', 'alerting': True, 'retention': '90 days'}

## 5.6.0.0.0 Bandwidth Controls

*No items available*

## 5.7.0.0.0 Service Discovery

| Property | Value |
|----------|-------|
| Method | dns |
| Implementation | Kubernetes native service discovery using CoreDNS ... |
| Health Checks | ✅ |

## 5.8.0.0.0 Environment Communication

*No items available*

# 6.0.0.0.0 Data Management Strategy

## 6.1.0.0.0 Data Isolation

### 6.1.1.0.0 Environment

#### 6.1.1.1.0 Environment

Production

#### 6.1.1.2.0 Isolation Level

complete

#### 6.1.1.3.0 Method

separate-instances

#### 6.1.1.4.0 Justification

Ensures absolute separation of live data, meeting security and compliance requirements.

### 6.1.2.0.0 Environment

#### 6.1.2.1.0 Environment

Staging

#### 6.1.2.2.0 Isolation Level

complete

#### 6.1.2.3.0 Method

separate-instances

#### 6.1.2.4.0 Justification

Required for accurate performance testing and to prevent any cross-contamination with production.

## 6.2.0.0.0 Backup And Recovery

- {'environment': 'Production', 'backupFrequency': 'Daily automated snapshots', 'retentionPeriod': '30 days', 'recoveryTimeObjective': '4 hours', 'recoveryPointObjective': '15 minutes', 'testingSchedule': 'Quarterly'}

## 6.3.0.0.0 Data Masking Anonymization

- {'environment': 'Staging, Testing', 'dataType': 'PII (Driver, Customer)', 'maskingMethod': 'static', 'coverage': 'complete', 'compliance': ['DPDPA, 2023']}

## 6.4.0.0.0 Migration Processes

- {'sourceEnvironment': 'Staging', 'targetEnvironment': 'Production', 'migrationMethod': 'dump-restore', 'validation': 'Mandatory dry-run in Staging, post-migration validation checklist (REQ-TRN-002).', 'rollbackPlan': 'Halt cutover and reschedule. Do not proceed if validation fails.'}

## 6.5.0.0.0 Retention Policies

### 6.5.1.0.0 Environment

#### 6.5.1.1.0 Environment

Production

#### 6.5.1.2.0 Data Type

Core transactional records (Trips, Invoices)

#### 6.5.1.3.0 Retention Period

7 years

#### 6.5.1.4.0 Archival Method

Retain in primary database; future consideration for archival to cold storage.

#### 6.5.1.5.0 Compliance Requirement

Financial regulations.

### 6.5.2.0.0 Environment

#### 6.5.2.1.0 Environment

Production

#### 6.5.2.2.0 Data Type

GPS location history

#### 6.5.2.3.0 Retention Period

12 months (online)

#### 6.5.2.4.0 Archival Method

Aggregate and archive to Amazon S3 Glacier after 12 months.

#### 6.5.2.5.0 Compliance Requirement

None

## 6.6.0.0.0 Data Classification

- {'classification': 'restricted', 'handlingRequirements': ['Encryption at rest and in transit', 'Strict access control'], 'accessControls': ['RBAC'], 'environments': ['Production']}

## 6.7.0.0.0 Disaster Recovery

- {'environment': 'Production', 'drSite': 'Different AWS Region (e.g., ap-southeast-1)', 'replicationMethod': 'asynchronous', 'failoverTime': '< 4 hours (RTO)', 'testingFrequency': 'Annually'}

# 7.0.0.0.0 Monitoring And Observability

## 7.1.0.0.0 Monitoring Components

### 7.1.1.0.0 Component

#### 7.1.1.1.0 Component

infrastructure

#### 7.1.1.2.0 Tool

Prometheus

#### 7.1.1.3.0 Implementation

Collects metrics from EKS, nodes, pods, RDS, RabbitMQ, and Redis via exporters.

#### 7.1.1.4.0 Environments

- Staging
- Production

### 7.1.2.0.0 Component

#### 7.1.2.1.0 Component

logs

#### 7.1.2.2.0 Tool

Fluentbit & OpenSearch

#### 7.1.2.3.0 Implementation

Centralized collection and analysis of structured JSON logs from all containers.

#### 7.1.2.4.0 Environments

- Staging
- Production

### 7.1.3.0.0 Component

#### 7.1.3.1.0 Component

visualization

#### 7.1.3.2.0 Tool

Grafana

#### 7.1.3.3.0 Implementation

Unified dashboards for metrics and logs.

#### 7.1.3.4.0 Environments

- Staging
- Production

### 7.1.4.0.0 Component

#### 7.1.4.1.0 Component

alerting

#### 7.1.4.2.0 Tool

Alertmanager

#### 7.1.4.3.0 Implementation

Handles alerting based on Prometheus rules, routes to appropriate channels.

#### 7.1.4.4.0 Environments

- Production

## 7.2.0.0.0 Environment Specific Thresholds

### 7.2.1.0.0 Environment

#### 7.2.1.1.0 Environment

Production

#### 7.2.1.2.0 Metric

p95 API Latency

#### 7.2.1.3.0 Warning Threshold

180ms

#### 7.2.1.4.0 Critical Threshold

200ms

#### 7.2.1.5.0 Justification

Aligned with NFR REQ-NFR-001.

### 7.2.2.0.0 Environment

#### 7.2.2.1.0 Environment

Production

#### 7.2.2.2.0 Metric

RabbitMQ DLQ Messages

#### 7.2.2.3.0 Warning Threshold

0

#### 7.2.2.4.0 Critical Threshold

0

#### 7.2.2.5.0 Justification

Any message in the DLQ indicates a persistent failure and requires immediate attention (REQ-INT-003).

### 7.2.3.0.0 Environment

#### 7.2.3.1.0 Environment

Staging

#### 7.2.3.2.0 Metric

p95 API Latency

#### 7.2.3.3.0 Warning Threshold

300ms

#### 7.2.3.4.0 Critical Threshold

500ms

#### 7.2.3.5.0 Justification

Higher tolerance in Staging as it's not a live environment, but still monitored for performance regressions.

## 7.3.0.0.0 Metrics Collection

- {'category': 'application', 'metrics': ['http_request_duration_seconds', 'http_requests_total', 'gps_processing_latency_seconds'], 'collectionInterval': '30s', 'retention': '30 days raw, 1 year aggregated'}

## 7.4.0.0.0 Health Check Endpoints

### 7.4.1.0.0 Component

#### 7.4.1.1.0 Component

Odoo Application

#### 7.4.1.2.0 Endpoint

/web/database/selector

#### 7.4.1.3.0 Check Type

liveness

#### 7.4.1.4.0 Timeout

10s

#### 7.4.1.5.0 Frequency

30s

### 7.4.2.0.0 Component

#### 7.4.2.1.0 Component

GPS Ingestion Service

#### 7.4.2.2.0 Endpoint

/health

#### 7.4.2.3.0 Check Type

liveness

#### 7.4.2.4.0 Timeout

5s

#### 7.4.2.5.0 Frequency

30s

## 7.5.0.0.0 Logging Configuration

### 7.5.1.0.0 Environment

#### 7.5.1.1.0 Environment

Production

#### 7.5.1.2.0 Log Level

INFO

#### 7.5.1.3.0 Destinations

- stdout (collected by Fluentbit)

#### 7.5.1.4.0 Retention

90 days in OpenSearch

#### 7.5.1.5.0 Sampling

10% for successful GPS ingestion events to manage volume.

### 7.5.2.0.0 Environment

#### 7.5.2.1.0 Environment

Staging

#### 7.5.2.2.0 Log Level

DEBUG

#### 7.5.2.3.0 Destinations

- stdout (collected by Fluentbit)

#### 7.5.2.4.0 Retention

30 days in OpenSearch

#### 7.5.2.5.0 Sampling

None

## 7.6.0.0.0 Escalation Policies

- {'environment': 'Production', 'severity': 'Critical', 'escalationPath': ['On-call Engineer (PagerDuty)', 'Engineering Lead', 'Head of Engineering'], 'timeouts': ['15m', '30m'], 'channels': ['PagerDuty', 'Slack']}

## 7.7.0.0.0 Dashboard Configurations

### 7.7.1.0.0 Dashboard Type

#### 7.7.1.1.0 Dashboard Type

operational

#### 7.7.1.2.0 Audience

Dispatch Manager, Finance Officer

#### 7.7.1.3.0 Refresh Interval

1m

#### 7.7.1.4.0 Metrics

- Pending Deliveries
- Delayed Trips
- Pending Payment Collections
- Total Revenue (MTD/YTD)

### 7.7.2.0.0 Dashboard Type

#### 7.7.2.1.0 Dashboard Type

technical

#### 7.7.2.2.0 Audience

SRE/DevOps

#### 7.7.2.3.0 Refresh Interval

30s

#### 7.7.2.4.0 Metrics

- API Latency (p95, p99)
- Error Rate (%)
- Pod CPU/Memory Usage
- DB Connections
- Queue Depth

# 8.0.0.0.0 Project Specific Environments

## 8.1.0.0.0 Environments

*No items available*

## 8.2.0.0.0 Configuration

*No data available*

## 8.3.0.0.0 Cross Environment Policies

*No items available*

# 9.0.0.0.0 Implementation Priority

## 9.1.0.0.0 Component

### 9.1.1.0.0 Component

Infrastructure as Code (Terraform) for Staging Environment

### 9.1.2.0.0 Priority

🔴 high

### 9.1.3.0.0 Dependencies

*No items available*

### 9.1.4.0.0 Estimated Effort

High

### 9.1.5.0.0 Risk Level

medium

## 9.2.0.0.0 Component

### 9.2.1.0.0 Component

CI/CD Pipeline (GitHub Actions) for Automated Deployments to Testing/Staging

### 9.2.2.0.0 Priority

🔴 high

### 9.2.3.0.0 Dependencies

- Terraform for Staging

### 9.2.4.0.0 Estimated Effort

High

### 9.2.5.0.0 Risk Level

medium

## 9.3.0.0.0 Component

### 9.3.1.0.0 Component

Core Observability Stack (Prometheus, Grafana, OpenSearch)

### 9.3.2.0.0 Priority

🔴 high

### 9.3.3.0.0 Dependencies

- Terraform for Staging

### 9.3.4.0.0 Estimated Effort

Medium

### 9.3.5.0.0 Risk Level

low

## 9.4.0.0.0 Component

### 9.4.1.0.0 Component

Production Environment Build-out and Hardening

### 9.4.2.0.0 Priority

🟡 medium

### 9.4.3.0.0 Dependencies

- CI/CD Pipeline
- Terraform for Staging

### 9.4.4.0.0 Estimated Effort

Medium

### 9.4.5.0.0 Risk Level

high

## 9.5.0.0.0 Component

### 9.5.1.0.0 Component

Disaster Recovery Site Configuration

### 9.5.2.0.0 Priority

🟢 low

### 9.5.3.0.0 Dependencies

- Production Environment Build-out

### 9.5.4.0.0 Estimated Effort

Medium

### 9.5.5.0.0 Risk Level

medium

# 10.0.0.0.0 Risk Assessment

## 10.1.0.0.0 Risk

### 10.1.1.0.0 Risk

Security misconfiguration in cloud environment leading to data breach.

### 10.1.2.0.0 Impact

high

### 10.1.3.0.0 Probability

medium

### 10.1.4.0.0 Mitigation

Strict adherence to Infrastructure as Code (Terraform), least-privilege IAM roles, regular automated security scanning, and third-party penetration testing.

### 10.1.5.0.0 Contingency Plan

Incident Response Plan, revoke compromised credentials, restore from backups to a clean environment.

## 10.2.0.0.0 Risk

### 10.2.1.0.0 Risk

Cost overruns due to inefficient resource allocation or uncontrolled scaling.

### 10.2.2.0.0 Impact

medium

### 10.2.3.0.0 Probability

high

### 10.2.4.0.0 Mitigation

Implement AWS Budgets and cost alerts, right-size instances based on monitoring data, use cost-effective instance types (e.g., Graviton, Spot for non-prod where applicable).

### 10.2.5.0.0 Contingency Plan

Quarterly resource optimization reviews, implement cost-saving measures like instance scheduling for non-prod environments.

## 10.3.0.0.0 Risk

### 10.3.1.0.0 Risk

Data migration failure during cutover, causing significant downtime.

### 10.3.2.0.0 Impact

high

### 10.3.3.0.0 Probability

medium

### 10.3.4.0.0 Mitigation

Mandatory, full-scale dry-run of migration in the Staging environment. Develop comprehensive validation scripts and a clear rollback plan (REQ-TRN-002, REQ-TRN-004).

### 10.3.5.0.0 Contingency Plan

Execute the documented rollback plan, which involves reverting user access to the legacy system and rescheduling the cutover.

# 11.0.0.0.0 Recommendations

## 11.1.0.0.0 Category

### 11.1.1.0.0 Category

🔹 Security

### 11.1.2.0.0 Recommendation

Implement IAM Roles for Service Accounts (IRSA) from day one. Avoid using EC2 instance profiles or long-lived credentials for pod-level access to AWS services.

### 11.1.3.0.0 Justification

Provides the most secure, least-privilege method for granting Kubernetes pods access to AWS resources, which is critical for protecting access to S3, RDS, and Secrets Manager.

### 11.1.4.0.0 Priority

🔴 high

### 11.1.5.0.0 Implementation Notes

This requires configuring an OIDC provider for the EKS cluster and creating specific IAM roles and policies for each service that needs AWS access.

## 11.2.0.0.0 Category

### 11.2.1.0.0 Category

🔹 Cost Optimization

### 11.2.2.0.0 Recommendation

Implement automated start/stop schedules for the Testing and Staging environments.

### 11.2.3.0.0 Justification

These environments are typically not needed 24/7. Shutting them down during off-hours (nights and weekends) can lead to significant cost savings (~60-70%).

### 11.2.4.0.0 Priority

🟡 medium

### 11.2.5.0.0 Implementation Notes

Use AWS Lambda functions triggered by EventBridge (CloudWatch Events) schedules to patch EKS node group desired counts to 0 and stop RDS instances.

## 11.3.0.0.0 Category

### 11.3.1.0.0 Category

🔹 Reliability

### 11.3.2.0.0 Recommendation

Conduct a mandatory Chaos Engineering exercise in the Staging environment before the first production go-live.

### 11.3.3.0.0 Justification

Proactively identifies weaknesses in the system's resilience by simulating failures (e.g., pod deletion, network latency, RDS failover), ensuring the system behaves as expected and meets its RTO/RPO targets.

### 11.3.4.0.0 Priority

🟡 medium

### 11.3.5.0.0 Implementation Notes

Use tools like the AWS Fault Injection Simulator (FIS) or open-source alternatives to inject controlled failures and observe the system's automated recovery capabilities.

