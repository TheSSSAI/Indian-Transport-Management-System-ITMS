# 1 Id

REPO-TMS-INFRA

# 2 Name

tms-infrastructure

# 3 Description

This repository is dedicated to Infrastructure as Code (IaC) and was preserved in its original, well-defined state. It contains all Terraform configurations required to provision and manage the entire cloud infrastructure on AWS. This includes the definition of the VPC, subnets, security groups, the Amazon EKS cluster, the Amazon RDS for PostgreSQL instance, Amazon S3 buckets, and all other necessary AWS resources. By managing infrastructure as code, the system's foundation is versionable, reproducible, and auditable. This repository is foundational to all other components, as it creates the environment in which they are deployed and run.

# 4 Type

🔹 Infrastructure

# 5 Namespace

tms.platform.infra

# 6 Output Path

terraform/aws

# 7 Framework

Terraform

# 8 Language

HCL

# 9 Technology

Terraform, AWS

# 10 Thirdparty Libraries

- AWS Terraform Provider

# 11 Layer Ids

- infrastructure-layer

# 12 Dependencies

*No items available*

# 13 Requirements

## 13.1 Requirement Id

### 13.1.1 Requirement Id

REQ-1-014

## 13.2.0 Requirement Id

### 13.2.1 Requirement Id

REQ-1-402

# 14.0.0 Generate Tests

❌ No

# 15.0.0 Generate Documentation

✅ Yes

# 16.0.0 Architecture Style

Infrastructure as Code

# 17.0.0 Architecture Map

- Infrastructure & Operations Layer

# 18.0.0 Components Map

*No items available*

# 19.0.0 Requirements Map

- REQ-1-014
- REQ-1-402

# 20.0.0 Decomposition Rationale

## 20.1.0 Operation Type

PRESERVED

## 20.2.0 Source Repository

tms-infrastructure

## 20.3.0 Decomposition Reasoning

This repository was preserved as it already represents a best-practice separation of concerns, isolating infrastructure definitions from application code and deployment configurations. Its scope is clear and focused.

## 20.4.0 Extracted Responsibilities

*No items available*

## 20.5.0 Reusability Scope

- The Terraform modules (e.g., for EKS or RDS) can be reused across other projects.

## 20.6.0 Development Benefits

- Enables GitOps workflows for infrastructure changes.
- Provides a safe, automated way to manage cloud resources.

# 21.0.0 Dependency Contracts

*No data available*

# 22.0.0 Exposed Contracts

## 22.1.0 Public Interfaces

*No items available*

# 23.0.0 Integration Patterns

| Property | Value |
|----------|-------|
| Dependency Injection | N/A |
| Event Communication | N/A |
| Data Flow | N/A |
| Error Handling | Terraform plan/apply lifecycle provides error feed... |
| Async Patterns | N/A |

# 24.0.0 Technology Guidance

| Property | Value |
|----------|-------|
| Framework Specific | Use Terraform workspaces to manage different envir... |
| Performance Considerations | N/A |
| Security Considerations | Follow the principle of least privilege when defin... |
| Testing Approach | Use 'terraform plan' for validation and tools like... |

# 25.0.0 Scope Boundaries

## 25.1.0 Must Implement

- All AWS resources required by the application.

## 25.2.0 Must Not Implement

- Application deployment logic (handled by REPO-TMS-K8S).
- Any application source code.

## 25.3.0 Extension Points

- New AWS resources can be added via new Terraform files.

## 25.4.0 Validation Rules

*No items available*

