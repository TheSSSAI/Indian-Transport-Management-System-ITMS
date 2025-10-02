# 1 System Overview

## 1.1 Analysis Date

2025-06-13

## 1.2 Technology Stack

- Odoo 18
- Python 3.11
- FastAPI
- Docker
- Amazon EKS
- Terraform
- Pytest

## 1.3 Architecture Patterns

- Modular Monolith
- Microservice

## 1.4 Ci Cd Tool

GitHub Actions

## 1.5 Requirements Analyzed

- REQ-1-014
- REQ-1-402
- REQ-1-503
- REQ-1-504

# 2.0 Pipelines

## 2.1 TMS Odoo Addon CI/CD

### 2.1.1 Id

pl-odoo-001

### 2.1.2 Name

TMS Odoo Addon CI/CD

### 2.1.3 Description

Handles the continuous integration, quality analysis, and deployment of the core TMS Odoo addon. It builds a container image and deploys it to the EKS cluster.

### 2.1.4 Source Path

./odoo_addons/tms_management/

### 2.1.5 Trigger

| Property | Value |
|----------|-------|
| On Push To | main |
| On Tag Creation | v*.*.* |
| Manual Dispatch | ✅ |

### 2.1.6 Stages

#### 2.1.6.1 Static Analysis & Code Quality

##### 2.1.6.1.1 Name

Static Analysis & Code Quality

##### 2.1.6.1.2 Description

Performs static checks to enforce code quality and identify potential security issues early.

##### 2.1.6.1.3 Steps

###### 2.1.6.1.3.1 Checkout Code

####### 2.1.6.1.3.1.1 Name

Checkout Code

####### 2.1.6.1.3.1.2 Tool

git

####### 2.1.6.1.3.1.3 Script

```
actions/checkout@v4
```

###### 2.1.6.1.3.2.0 Lint Code

####### 2.1.6.1.3.2.1 Name

Lint Code

####### 2.1.6.1.3.2.2 Tool

Flake8

####### 2.1.6.1.3.2.3 Script

```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

####### 2.1.6.1.3.2.4 Justification

REQ-1-402 specifies Flake8 for linting.

###### 2.1.6.1.3.3.0 Format & Sort Imports

####### 2.1.6.1.3.3.1 Name

Format & Sort Imports

####### 2.1.6.1.3.3.2 Tool

Black, isort

####### 2.1.6.1.3.3.3 Script

```
black . --check
isort . --check-only
```

####### 2.1.6.1.3.3.4 Justification

REQ-1-402 specifies Black and isort for formatting.

###### 2.1.6.1.3.4.0 Static Application Security Testing (SAST)

####### 2.1.6.1.3.4.1 Name

Static Application Security Testing (SAST)

####### 2.1.6.1.3.4.2 Tool

Bandit

####### 2.1.6.1.3.4.3 Script

```
bandit -r . -ll -ii
```

####### 2.1.6.1.3.4.4 Justification

REQ-1-503 requires mitigation of common vulnerabilities.

###### 2.1.6.1.3.5.0 Dependency Vulnerability Scan

####### 2.1.6.1.3.5.1 Name

Dependency Vulnerability Scan

####### 2.1.6.1.3.5.2 Tool

pip-audit

####### 2.1.6.1.3.5.3 Script

```
pip-audit -r requirements.txt
```

####### 2.1.6.1.3.5.4 Justification

REQ-1-503 requires mitigation of vulnerabilities, including dependencies.

##### 2.1.6.1.4.0.0 Quality Gates

- All linting, formatting, and security checks must pass.

#### 2.1.6.2.0.0.0 Unit Test & Coverage

##### 2.1.6.2.1.0.0 Name

Unit Test & Coverage

##### 2.1.6.2.2.0.0 Description

Executes unit tests and enforces the minimum code coverage requirement.

##### 2.1.6.2.3.0.0 Steps

###### 2.1.6.2.3.1.0 Run Unit Tests with Coverage

####### 2.1.6.2.3.1.1 Name

Run Unit Tests with Coverage

####### 2.1.6.2.3.1.2 Tool

Pytest

####### 2.1.6.2.3.1.3 Script

```
pytest --cov=./ --cov-report=xml
```

####### 2.1.6.2.3.1.4 Justification

REQ-1-402 and REQ-1-504 specify Pytest for testing.

###### 2.1.6.2.3.2.0 Validate Coverage Threshold

####### 2.1.6.2.3.2.1 Name

Validate Coverage Threshold

####### 2.1.6.2.3.2.2 Tool

coverage.py

####### 2.1.6.2.3.2.3 Script

```
coverage report --fail-under=80
```

####### 2.1.6.2.3.2.4 Justification

REQ-1-504 mandates a minimum of 80% unit test coverage.

##### 2.1.6.2.4.0.0 Quality Gates

- All unit tests must pass.
- Code coverage must be >= 80%.

#### 2.1.6.3.0.0.0 Package & Scan Artifact

##### 2.1.6.3.1.0.0 Name

Package & Scan Artifact

##### 2.1.6.3.2.0.0 Description

Builds the Odoo application into an immutable Docker image, pushes it to the container registry, and scans it for vulnerabilities.

##### 2.1.6.3.3.0.0 Steps

###### 2.1.6.3.3.1.0 Build Docker Image

####### 2.1.6.3.3.1.1 Name

Build Docker Image

####### 2.1.6.3.3.1.2 Tool

Docker

####### 2.1.6.3.3.1.3 Script

```
docker build -t $ECR_REGISTRY/$IMAGE_NAME:$IMAGE_TAG .
```

###### 2.1.6.3.3.2.0 Push Docker Image to ECR

####### 2.1.6.3.3.2.1 Name

Push Docker Image to ECR

####### 2.1.6.3.3.2.2 Tool

AWS CLI

####### 2.1.6.3.3.2.3 Script

```
docker push $ECR_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
```

###### 2.1.6.3.3.3.0 Scan Container Image

####### 2.1.6.3.3.3.1 Name

Scan Container Image

####### 2.1.6.3.3.3.2 Tool

AWS ECR Scan (Trivy)

####### 2.1.6.3.3.3.3 Script

```
aws ecr start-image-scan ...
```

####### 2.1.6.3.3.3.4 Justification

REQ-1-503 requires periodic automated vulnerability scanning.

##### 2.1.6.3.4.0.0 Artifacts Produced

- Docker Image

##### 2.1.6.3.5.0.0 Quality Gates

- Image build and push must succeed.
- Image scan must report zero 'CRITICAL' severity vulnerabilities.

#### 2.1.6.4.0.0.0 Deploy to Staging

##### 2.1.6.4.1.0.0 Name

Deploy to Staging

##### 2.1.6.4.2.0.0 Description

Deploys the containerized application to the production-like staging environment for UAT and integration testing.

##### 2.1.6.4.3.0.0 Environment

staging

##### 2.1.6.4.4.0.0 Steps

###### 2.1.6.4.4.1.0 Deploy to EKS Staging Cluster

####### 2.1.6.4.4.1.1 Name

Deploy to EKS Staging Cluster

####### 2.1.6.4.4.1.2 Tool

kubectl

####### 2.1.6.4.4.1.3 Script

```
kubectl apply -k ./kube/staging
```

####### 2.1.6.4.4.1.4 Justification

REQ-1-014 specifies EKS as the deployment target.

###### 2.1.6.4.4.2.0 Verify Deployment Health

####### 2.1.6.4.4.2.1 Name

Verify Deployment Health

####### 2.1.6.4.4.2.2 Tool

kubectl

####### 2.1.6.4.4.2.3 Script

```
kubectl rollout status deployment/tms-odoo
```

#### 2.1.6.5.0.0.0 Integration Test

##### 2.1.6.5.1.0.0 Name

Integration Test

##### 2.1.6.5.2.0.0 Description

Runs a suite of automated integration tests against the newly deployed staging environment.

##### 2.1.6.5.3.0.0 Environment

staging

##### 2.1.6.5.4.0.0 Steps

- {'name': 'Execute Integration Test Suite', 'tool': 'Pytest', 'script': 'pytest tests/integration/', 'justification': 'REQ-1-504 requires a suite of automated integration tests.'}

##### 2.1.6.5.5.0.0 Quality Gates

- All integration tests must pass.

#### 2.1.6.6.0.0.0 Production Approval

##### 2.1.6.6.1.0.0 Name

Production Approval

##### 2.1.6.6.2.0.0 Description

A manual gate requiring explicit approval from a designated stakeholder before proceeding to production.

##### 2.1.6.6.3.0.0 Environment

production

##### 2.1.6.6.4.0.0 Type

🔹 ManualApproval

##### 2.1.6.6.5.0.0 Approvers

- Project Lead
- DevOps Lead

##### 2.1.6.6.6.0.0 Justification

REQ-TRN-004 implies a controlled, deliberate cutover process requiring human oversight.

#### 2.1.6.7.0.0.0 Deploy to Production

##### 2.1.6.7.1.0.0 Name

Deploy to Production

##### 2.1.6.7.2.0.0 Description

Promotes the validated image from staging to the production environment.

##### 2.1.6.7.3.0.0 Environment

production

##### 2.1.6.7.4.0.0 Steps

###### 2.1.6.7.4.1.0 Deploy to EKS Production Cluster

####### 2.1.6.7.4.1.1 Name

Deploy to EKS Production Cluster

####### 2.1.6.7.4.1.2 Tool

kubectl

####### 2.1.6.7.4.1.3 Script

```
kubectl apply -k ./kube/production
```

####### 2.1.6.7.4.1.4 Justification

REQ-1-014 specifies EKS as the deployment target.

###### 2.1.6.7.4.2.0 Verify Production Deployment Health

####### 2.1.6.7.4.2.1 Name

Verify Production Deployment Health

####### 2.1.6.7.4.2.2 Tool

kubectl

####### 2.1.6.7.4.2.3 Script

```
kubectl rollout status deployment/tms-odoo
```

## 2.2.0.0.0.0.0 GPS Ingestion Service CI/CD

### 2.2.1.0.0.0.0 Id

pl-gps-001

### 2.2.2.0.0.0.0 Name

GPS Ingestion Service CI/CD

### 2.2.3.0.0.0.0 Description

Handles the continuous integration, quality analysis, and deployment of the FastAPI microservice for GPS data ingestion.

### 2.2.4.0.0.0.0 Source Path

./gps_ingestion_service/

### 2.2.5.0.0.0.0 Trigger

| Property | Value |
|----------|-------|
| On Push To | main |
| On Tag Creation | v*.*.* |
| Manual Dispatch | ✅ |

### 2.2.6.0.0.0.0 Stages

#### 2.2.6.1.0.0.0 Static Analysis & Code Quality

##### 2.2.6.1.1.0.0 Name

Static Analysis & Code Quality

##### 2.2.6.1.2.0.0 Description

Performs static checks to enforce code quality and identify potential security issues early.

##### 2.2.6.1.3.0.0 Steps

###### 2.2.6.1.3.1.0 Checkout Code

####### 2.2.6.1.3.1.1 Name

Checkout Code

####### 2.2.6.1.3.1.2 Tool

git

####### 2.2.6.1.3.1.3 Script

```
actions/checkout@v4
```

###### 2.2.6.1.3.2.0 Lint Code

####### 2.2.6.1.3.2.1 Name

Lint Code

####### 2.2.6.1.3.2.2 Tool

Flake8

####### 2.2.6.1.3.2.3 Script

```
flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
```

####### 2.2.6.1.3.2.4 Justification

REQ-1-402 specifies Flake8 for linting.

###### 2.2.6.1.3.3.0 Format & Sort Imports

####### 2.2.6.1.3.3.1 Name

Format & Sort Imports

####### 2.2.6.1.3.3.2 Tool

Black, isort

####### 2.2.6.1.3.3.3 Script

```
black . --check
isort . --check-only
```

####### 2.2.6.1.3.3.4 Justification

REQ-1-402 specifies Black and isort for formatting.

###### 2.2.6.1.3.4.0 Static Application Security Testing (SAST)

####### 2.2.6.1.3.4.1 Name

Static Application Security Testing (SAST)

####### 2.2.6.1.3.4.2 Tool

Bandit

####### 2.2.6.1.3.4.3 Script

```
bandit -r . -ll -ii
```

####### 2.2.6.1.3.4.4 Justification

REQ-1-503 requires mitigation of common vulnerabilities.

###### 2.2.6.1.3.5.0 Dependency Vulnerability Scan

####### 2.2.6.1.3.5.1 Name

Dependency Vulnerability Scan

####### 2.2.6.1.3.5.2 Tool

pip-audit

####### 2.2.6.1.3.5.3 Script

```
pip-audit -r requirements.txt
```

####### 2.2.6.1.3.5.4 Justification

REQ-1-503 requires mitigation of vulnerabilities, including dependencies.

##### 2.2.6.1.4.0.0 Quality Gates

- All linting, formatting, and security checks must pass.

#### 2.2.6.2.0.0.0 Unit Test & Coverage

##### 2.2.6.2.1.0.0 Name

Unit Test & Coverage

##### 2.2.6.2.2.0.0 Description

Executes unit tests and enforces the minimum code coverage requirement.

##### 2.2.6.2.3.0.0 Steps

###### 2.2.6.2.3.1.0 Run Unit Tests with Coverage

####### 2.2.6.2.3.1.1 Name

Run Unit Tests with Coverage

####### 2.2.6.2.3.1.2 Tool

Pytest

####### 2.2.6.2.3.1.3 Script

```
pytest --cov=./ --cov-report=xml
```

####### 2.2.6.2.3.1.4 Justification

REQ-1-402 and REQ-1-504 specify Pytest for testing.

###### 2.2.6.2.3.2.0 Validate Coverage Threshold

####### 2.2.6.2.3.2.1 Name

Validate Coverage Threshold

####### 2.2.6.2.3.2.2 Tool

coverage.py

####### 2.2.6.2.3.2.3 Script

```
coverage report --fail-under=80
```

####### 2.2.6.2.3.2.4 Justification

REQ-1-504 mandates a minimum of 80% unit test coverage.

##### 2.2.6.2.4.0.0 Quality Gates

- All unit tests must pass.
- Code coverage must be >= 80%.

#### 2.2.6.3.0.0.0 Package & Scan Artifact

##### 2.2.6.3.1.0.0 Name

Package & Scan Artifact

##### 2.2.6.3.2.0.0 Description

Builds the FastAPI application into an immutable Docker image, pushes it to the container registry, and scans it for vulnerabilities.

##### 2.2.6.3.3.0.0 Steps

###### 2.2.6.3.3.1.0 Build Docker Image

####### 2.2.6.3.3.1.1 Name

Build Docker Image

####### 2.2.6.3.3.1.2 Tool

Docker

####### 2.2.6.3.3.1.3 Script

```
docker build -t $ECR_REGISTRY/$IMAGE_NAME:$IMAGE_TAG .
```

###### 2.2.6.3.3.2.0 Push Docker Image to ECR

####### 2.2.6.3.3.2.1 Name

Push Docker Image to ECR

####### 2.2.6.3.3.2.2 Tool

AWS CLI

####### 2.2.6.3.3.2.3 Script

```
docker push $ECR_REGISTRY/$IMAGE_NAME:$IMAGE_TAG
```

###### 2.2.6.3.3.3.0 Scan Container Image

####### 2.2.6.3.3.3.1 Name

Scan Container Image

####### 2.2.6.3.3.3.2 Tool

AWS ECR Scan (Trivy)

####### 2.2.6.3.3.3.3 Script

```
aws ecr start-image-scan ...
```

####### 2.2.6.3.3.3.4 Justification

REQ-1-503 requires periodic automated vulnerability scanning.

##### 2.2.6.3.4.0.0 Artifacts Produced

- Docker Image

##### 2.2.6.3.5.0.0 Quality Gates

- Image build and push must succeed.
- Image scan must report zero 'CRITICAL' severity vulnerabilities.

#### 2.2.6.4.0.0.0 Deploy to Staging

##### 2.2.6.4.1.0.0 Name

Deploy to Staging

##### 2.2.6.4.2.0.0 Description

Deploys the containerized microservice to the staging environment.

##### 2.2.6.4.3.0.0 Environment

staging

##### 2.2.6.4.4.0.0 Steps

###### 2.2.6.4.4.1.0 Deploy to EKS Staging Cluster

####### 2.2.6.4.4.1.1 Name

Deploy to EKS Staging Cluster

####### 2.2.6.4.4.1.2 Tool

kubectl

####### 2.2.6.4.4.1.3 Script

```
kubectl apply -k ./kube/staging
```

####### 2.2.6.4.4.1.4 Justification

REQ-1-014 specifies EKS as the deployment target.

###### 2.2.6.4.4.2.0 Verify Deployment Health

####### 2.2.6.4.4.2.1 Name

Verify Deployment Health

####### 2.2.6.4.4.2.2 Tool

kubectl

####### 2.2.6.4.4.2.3 Script

```
kubectl rollout status deployment/gps-ingestion-service
```

#### 2.2.6.5.0.0.0 Integration Test

##### 2.2.6.5.1.0.0 Name

Integration Test

##### 2.2.6.5.2.0.0 Description

Runs automated integration tests against the newly deployed staging environment.

##### 2.2.6.5.3.0.0 Environment

staging

##### 2.2.6.5.4.0.0 Steps

- {'name': 'Execute Integration Test Suite', 'tool': 'Pytest', 'script': 'pytest tests/integration/', 'justification': 'REQ-1-504 requires a suite of automated integration tests.'}

##### 2.2.6.5.5.0.0 Quality Gates

- All integration tests must pass.

#### 2.2.6.6.0.0.0 Production Approval

##### 2.2.6.6.1.0.0 Name

Production Approval

##### 2.2.6.6.2.0.0 Description

A manual gate requiring explicit approval from a designated stakeholder before proceeding to production.

##### 2.2.6.6.3.0.0 Environment

production

##### 2.2.6.6.4.0.0 Type

🔹 ManualApproval

##### 2.2.6.6.5.0.0 Approvers

- Project Lead
- DevOps Lead

#### 2.2.6.7.0.0.0 Deploy to Production

##### 2.2.6.7.1.0.0 Name

Deploy to Production

##### 2.2.6.7.2.0.0 Description

Promotes the validated image from staging to the production environment.

##### 2.2.6.7.3.0.0 Environment

production

##### 2.2.6.7.4.0.0 Steps

###### 2.2.6.7.4.1.0 Deploy to EKS Production Cluster

####### 2.2.6.7.4.1.1 Name

Deploy to EKS Production Cluster

####### 2.2.6.7.4.1.2 Tool

kubectl

####### 2.2.6.7.4.1.3 Script

```
kubectl apply -k ./kube/production
```

###### 2.2.6.7.4.2.0 Verify Production Deployment Health

####### 2.2.6.7.4.2.1 Name

Verify Production Deployment Health

####### 2.2.6.7.4.2.2 Tool

kubectl

####### 2.2.6.7.4.2.3 Script

```
kubectl rollout status deployment/gps-ingestion-service
```

# 3.0.0.0.0.0.0 Shared Configuration

## 3.1.0.0.0.0.0 Artifact Management

| Property | Value |
|----------|-------|
| Repository | AWS Elastic Container Registry (ECR) |
| Versioning Strategy | Git commit SHA for all builds; Git tags (e.g., v1.... |
| Immutability | Docker images are considered immutable. The same i... |
| Retention Policy | Keep last 20 images per repository; retain release... |

## 3.2.0.0.0.0.0 Rollback Strategy

| Property | Value |
|----------|-------|
| Mechanism | Automated Redeployment |
| Procedure | In case of failure, re-trigger the 'Deploy to Prod... |
| Trigger | Manual trigger by an authorized user upon observin... |

## 3.3.0.0.0.0.0 Secrets Management

| Property | Value |
|----------|-------|
| Tool | AWS Secrets Manager |
| Integration | Secrets are injected into the EKS pods at runtime ... |
| Justification | Fulfills REQ-1-503 by preventing secrets from bein... |

# 4.0.0.0.0.0.0 Implementation Priority

## 4.1.0.0.0.0.0 Component

### 4.1.1.0.0.0.0 Component

Odoo Addon Pipeline (pl-odoo-001)

### 4.1.2.0.0.0.0 Priority

🔴 high

### 4.1.3.0.0.0.0 Dependencies

*No items available*

### 4.1.4.0.0.0.0 Estimated Effort

Medium

### 4.1.5.0.0.0.0 Risk Level

low

## 4.2.0.0.0.0.0 Component

### 4.2.1.0.0.0.0 Component

GPS Service Pipeline (pl-gps-001)

### 4.2.2.0.0.0.0 Priority

🔴 high

### 4.2.3.0.0.0.0 Dependencies

*No items available*

### 4.2.4.0.0.0.0 Estimated Effort

Medium

### 4.2.5.0.0.0.0 Risk Level

low

# 5.0.0.0.0.0.0 Risk Assessment

## 5.1.0.0.0.0.0 Risk

### 5.1.1.0.0.0.0 Risk

Pipeline Flakiness

### 5.1.2.0.0.0.0 Impact

medium

### 5.1.3.0.0.0.0 Probability

medium

### 5.1.4.0.0.0.0 Mitigation

Ensure integration tests are robust and can be run idempotently. Use stable versions of actions and tools. Implement retry logic for transient network failures during deployments.

### 5.1.5.0.0.0.0 Contingency Plan

Provide clear documentation for manually running deployment steps if the pipeline fails for non-code-related reasons.

## 5.2.0.0.0.0.0 Risk

### 5.2.1.0.0.0.0 Risk

Inadequate Test Coverage

### 5.2.2.0.0.0.0 Impact

high

### 5.2.3.0.0.0.0 Probability

medium

### 5.2.4.0.0.0.0 Mitigation

Strictly enforce the 80% code coverage quality gate (REQ-1-504). Conduct regular reviews of test cases to ensure they cover critical business logic.

### 5.2.5.0.0.0.0 Contingency Plan

Block merges/deployments that fail the coverage check. Allocate developer time specifically for improving test coverage if it falls below the threshold.

# 6.0.0.0.0.0.0 Recommendations

## 6.1.0.0.0.0.0 Category

### 6.1.1.0.0.0.0 Category

🔹 Optimization

### 6.1.2.0.0.0.0 Recommendation

Implement build caching for Docker layers and Python dependencies within GitHub Actions.

### 6.1.3.0.0.0.0 Justification

Will significantly reduce pipeline execution time and cost, especially for the Odoo addon which may have numerous dependencies.

### 6.1.4.0.0.0.0 Priority

🟡 medium

### 6.1.5.0.0.0.0 Implementation Notes

Use `actions/cache` for dependencies and Docker's built-in layer caching.

## 6.2.0.0.0.0.0 Category

### 6.2.1.0.0.0.0 Category

🔹 Security

### 6.2.2.0.0.0.0 Recommendation

Integrate the CI/CD pipelines with GitHub's branch protection rules.

### 6.2.3.0.0.0.0 Justification

Enforces that all required status checks (linting, testing, scanning) must pass before code can be merged into the `main` branch, improving code quality and security posture.

### 6.2.4.0.0.0.0 Priority

🔴 high

### 6.2.5.0.0.0.0 Implementation Notes

Configure rules in GitHub settings to require all pipeline jobs to succeed for PRs targeting the main branch.

