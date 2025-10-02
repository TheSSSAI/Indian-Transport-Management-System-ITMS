# 1 Pipelines

## 1.1 TMS Odoo Addon CI/CD Pipeline

### 1.1.1 Id

pipeline-tms-odoo-addon

### 1.1.2 Name

TMS Odoo Addon CI/CD Pipeline

### 1.1.3 Description

Builds, tests, and deploys the core TMS Odoo addon to staging and production EKS environments. REQ-1-402, REQ-1-504.

### 1.1.4 Stages

#### 1.1.4.1 Code Quality & Static Analysis

##### 1.1.4.1.1 Name

Code Quality & Static Analysis

##### 1.1.4.1.2 Steps

- echo "Running linter and formatters..."
- flake8 .
- black --check .
- isort --check-only .

##### 1.1.4.1.3 Environment

###### 1.1.4.1.3.1 Python Version

3.11

##### 1.1.4.1.4.0 Quality Gates

- {'name': 'Code Formatting & Linting', 'criteria': ['Flake8 passes with zero errors', 'Black check passes', 'isort check passes'], 'blocking': True}

#### 1.1.4.2.0.0 Unit Testing & Coverage

##### 1.1.4.2.1.0 Name

Unit Testing & Coverage

##### 1.1.4.2.2.0 Steps

- echo "Running unit tests..."
- pytest --cov=. --cov-fail-under=80

##### 1.1.4.2.3.0 Environment

###### 1.1.4.2.3.1 Python Version

3.11

##### 1.1.4.2.4.0 Quality Gates

- {'name': 'Test Coverage Check', 'criteria': ['Unit test coverage >= 80%'], 'blocking': True}

#### 1.1.4.3.0.0 Dependency Security Scan

##### 1.1.4.3.1.0 Name

Dependency Security Scan

##### 1.1.4.3.2.0 Steps

- echo "Scanning for vulnerabilities..."
- pip install safety
- safety check

##### 1.1.4.3.3.0 Environment

###### 1.1.4.3.3.1 Fail On Critical

true

##### 1.1.4.3.4.0 Quality Gates

- {'name': 'Vulnerability Check', 'criteria': ['No known critical vulnerabilities in dependencies'], 'blocking': True}

#### 1.1.4.4.0.0 Build & Push Docker Image

##### 1.1.4.4.1.0 Name

Build & Push Docker Image

##### 1.1.4.4.2.0 Steps

- echo "Building and pushing Docker image..."
- docker build -t $ECR_REPOSITORY_URL/tms-odoo-addon:$IMAGE_TAG .
- docker push $ECR_REPOSITORY_URL/tms-odoo-addon:$IMAGE_TAG

##### 1.1.4.4.3.0 Environment

###### 1.1.4.4.3.1 Ecr Repository Url

from-secrets

###### 1.1.4.4.3.2 Image Tag

git-commit-sha

#### 1.1.4.5.0.0 Deploy to Staging

##### 1.1.4.5.1.0 Name

Deploy to Staging

##### 1.1.4.5.2.0 Steps

- echo "Deploying to staging EKS cluster..."
- kubectl apply -f k8s/staging/deployment.yaml --namespace staging

##### 1.1.4.5.3.0 Environment

###### 1.1.4.5.3.1 Kube Context

staging-eks-cluster

###### 1.1.4.5.3.2 Image Tag To Deploy

git-commit-sha

#### 1.1.4.6.0.0 Manual Approval for Production

##### 1.1.4.6.1.0 Name

Manual Approval for Production

##### 1.1.4.6.2.0 Steps

- echo "Waiting for manual approval to deploy to production."

##### 1.1.4.6.3.0 Environment

###### 1.1.4.6.3.1 Approvers

Project-Leads-Group

##### 1.1.4.6.4.0 Quality Gates

- {'name': 'Production Go/No-Go', 'criteria': ['UAT passed in staging (REQ-1-504)', 'Data migration plan is ready (REQ-TRN-002)', 'Cutover plan is approved (REQ-TRN-004)'], 'blocking': True}

#### 1.1.4.7.0.0 Deploy to Production

##### 1.1.4.7.1.0 Name

Deploy to Production

##### 1.1.4.7.2.0 Steps

- echo "Deploying to production EKS cluster..."
- kubectl apply -f k8s/production/deployment.yaml --namespace production

##### 1.1.4.7.3.0 Environment

###### 1.1.4.7.3.1 Kube Context

production-eks-cluster

###### 1.1.4.7.3.2 Image Tag To Deploy

git-commit-sha

## 1.2.0.0.0.0 GPS Ingestion Microservice CI/CD Pipeline

### 1.2.1.0.0.0 Id

pipeline-gps-microservice

### 1.2.2.0.0.0 Name

GPS Ingestion Microservice CI/CD Pipeline

### 1.2.3.0.0.0 Description

Builds, tests, and deploys the FastAPI GPS ingestion microservice. REQ-1-401, REQ-1-402.

### 1.2.4.0.0.0 Stages

#### 1.2.4.1.0.0 Code Quality & Unit Testing

##### 1.2.4.1.1.0 Name

Code Quality & Unit Testing

##### 1.2.4.1.2.0 Steps

- flake8 .
- black --check .
- isort --check-only .
- pytest --cov=. --cov-fail-under=80

##### 1.2.4.1.3.0 Environment

###### 1.2.4.1.3.1 Python Version

3.11

##### 1.2.4.1.4.0 Quality Gates

- {'name': 'Static Analysis & Test Coverage', 'criteria': ['All linting and formatting checks pass', 'Unit test coverage >= 80%'], 'blocking': True}

#### 1.2.4.2.0.0 Build & Push Docker Image

##### 1.2.4.2.1.0 Name

Build & Push Docker Image

##### 1.2.4.2.2.0 Steps

- docker build -t $ECR_REPOSITORY_URL/gps-ingestion-service:$IMAGE_TAG .
- docker push $ECR_REPOSITORY_URL/gps-ingestion-service:$IMAGE_TAG

##### 1.2.4.2.3.0 Environment

###### 1.2.4.2.3.1 Ecr Repository Url

from-secrets

###### 1.2.4.2.3.2 Image Tag

git-commit-sha

#### 1.2.4.3.0.0 Deploy to Staging

##### 1.2.4.3.1.0 Name

Deploy to Staging

##### 1.2.4.3.2.0 Steps

- kubectl apply -f k8s/staging/gps-service.yaml --namespace staging

##### 1.2.4.3.3.0 Environment

###### 1.2.4.3.3.1 Kube Context

staging-eks-cluster

#### 1.2.4.4.0.0 Manual Approval for Production

##### 1.2.4.4.1.0 Name

Manual Approval for Production

##### 1.2.4.4.2.0 Steps

- echo "Waiting for manual approval to deploy to production."

##### 1.2.4.4.3.0 Environment

*No data available*

##### 1.2.4.4.4.0 Quality Gates

- {'name': 'Production Readiness Check', 'criteria': ['Staging environment tests passed'], 'blocking': True}

#### 1.2.4.5.0.0 Deploy to Production

##### 1.2.4.5.1.0 Name

Deploy to Production

##### 1.2.4.5.2.0 Steps

- kubectl apply -f k8s/production/gps-service.yaml --namespace production

##### 1.2.4.5.3.0 Environment

###### 1.2.4.5.3.1 Kube Context

production-eks-cluster

## 1.3.0.0.0.0 Infrastructure as Code (Terraform) Pipeline

### 1.3.1.0.0.0 Id

pipeline-iac-terraform

### 1.3.2.0.0.0 Name

Infrastructure as Code (Terraform) Pipeline

### 1.3.3.0.0.0 Description

Validates and applies infrastructure changes to AWS using Terraform. REQ-1-402, REQ-NFR-002.

### 1.3.4.0.0.0 Stages

#### 1.3.4.1.0.0 Validate & Plan

##### 1.3.4.1.1.0 Name

Validate & Plan

##### 1.3.4.1.2.0 Steps

- terraform init
- terraform validate
- terraform plan -out=tfplan

##### 1.3.4.1.3.0 Environment

###### 1.3.4.1.3.1 Terraform Version

1.8.x

##### 1.3.4.1.4.0 Quality Gates

- {'name': 'Terraform Validation', 'criteria': ['Terraform code is syntactically valid'], 'blocking': True}

#### 1.3.4.2.0.0 Review Plan & Approve

##### 1.3.4.2.1.0 Name

Review Plan & Approve

##### 1.3.4.2.2.0 Steps

- echo "Waiting for manual approval of Terraform plan."

##### 1.3.4.2.3.0 Environment

###### 1.3.4.2.3.1 Approvers

DevOps-Leads-Group

##### 1.3.4.2.4.0 Quality Gates

- {'name': 'Infrastructure Change Approval', 'criteria': ['Terraform plan has been reviewed and approved by an authorized user'], 'blocking': True}

#### 1.3.4.3.0.0 Apply Infrastructure Changes

##### 1.3.4.3.1.0 Name

Apply Infrastructure Changes

##### 1.3.4.3.2.0 Steps

- terraform apply "tfplan"

##### 1.3.4.3.3.0 Environment

###### 1.3.4.3.3.1 Aws Region

ap-south-1

# 2.0.0.0.0.0 Configuration

| Property | Value |
|----------|-------|
| Artifact Repository | Amazon ECR |
| Default Branch | main |
| Retention Policy | Keep artifacts for last 10 builds |
| Notification Channel | slack#tms-deployments |

