# 1 Id

REPO-TMS-K8S

# 2 Name

tms-kubernetes-manifests

# 3 Description

This repository was preserved and contains all Kubernetes configuration manifests, likely structured as Helm charts or Kustomize overlays. It defines how the containerized applications (Odoo monolith, FastAPI microservice) are deployed, configured, and managed on the EKS cluster. Responsibilities include defining Deployments, Services, Ingress rules, ConfigMaps, and the mechanism for injecting secrets from AWS Secrets Manager. This repository acts as the bridge between the application build artifacts (Docker images) and the running infrastructure, embodying the principles of GitOps for application deployment.

# 4 Type

🔹 Infrastructure

# 5 Namespace

tms.platform.deploy

# 6 Output Path

kubernetes/manifests

# 7 Framework

Helm/Kustomize

# 8 Language

YAML

# 9 Technology

Kubernetes, Helm

# 10 Thirdparty Libraries

*No items available*

# 11 Layer Ids

- infrastructure-layer

# 12 Dependencies

- REPO-TMS-CORE
- REPO-DRV-UI
- REPO-GSP-INT
- REPO-GPS-CON
- REPO-GPS-SVC

# 13 Requirements

- {'requirementId': 'REQ-1-014'}

# 14 Generate Tests

❌ No

# 15 Generate Documentation

✅ Yes

# 16 Architecture Style

GitOps

# 17 Architecture Map

- Infrastructure & Operations Layer

# 18 Components Map

*No items available*

# 19 Requirements Map

- REQ-1-014

# 20 Decomposition Rationale

## 20.1 Operation Type

PRESERVED

## 20.2 Source Repository

tms-kubernetes-manifests

## 20.3 Decomposition Reasoning

This repository was preserved because it correctly separates the application deployment and runtime configuration from the application source code. This is a critical separation for enabling GitOps and clear ownership between development and operations teams.

## 20.4 Extracted Responsibilities

*No items available*

## 20.5 Reusability Scope

- The Helm chart structure can be templated and reused for other applications.

## 20.6 Development Benefits

- Provides a single source of truth for how the application runs in production.
- Automates and standardizes the deployment process.

# 21.0 Dependency Contracts

## 21.1 Repo-Tms-Core

### 21.1.1 Required Interfaces

- {'interface': 'Docker Image', 'methods': [], 'events': [], 'properties': ['Image tag/digest']}

### 21.1.2 Integration Pattern

Consumes the container image artifact produced by the CI pipeline of the application repository.

### 21.1.3 Communication Protocol

Docker Registry API

# 22.0.0 Exposed Contracts

## 22.1.0 Public Interfaces

*No items available*

# 23.0.0 Integration Patterns

| Property | Value |
|----------|-------|
| Dependency Injection | Injects configuration and secrets into pods via Co... |
| Event Communication | N/A |
| Data Flow | N/A |
| Error Handling | Relies on Kubernetes' self-healing capabilities (e... |
| Async Patterns | N/A |

# 24.0.0 Technology Guidance

| Property | Value |
|----------|-------|
| Framework Specific | Use Helm for templating to manage configuration ac... |
| Performance Considerations | Define appropriate resource requests and limits fo... |
| Security Considerations | Define NetworkPolicies to restrict pod-to-pod comm... |
| Testing Approach | Lint Helm charts and use tools like 'helm template... |

# 25.0.0 Scope Boundaries

## 25.1.0 Must Implement

- Deployment configurations for all services.
- Service exposure via Ingress.
- Configuration and secrets management.

## 25.2.0 Must Not Implement

- Infrastructure provisioning (handled by REPO-TMS-INFRA).
- Building Docker images (handled by application CI pipelines).

## 25.3.0 Extension Points

- New services can be added by creating new Helm charts.

## 25.4.0 Validation Rules

*No items available*

