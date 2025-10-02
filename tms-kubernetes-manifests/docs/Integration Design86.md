# 1 Integration Specifications

## 1.1 Extraction Metadata

| Property | Value |
|----------|-------|
| Repository Id | REPO-TMS-K8S |
| Extraction Timestamp | 2024-07-27T11:00:00Z |
| Mapping Validation Score | 100% |
| Context Completeness Score | 100% |
| Implementation Readiness Level | Ready for Implementation |

## 1.2 Relevant Requirements

### 1.2.1 Requirement Id

#### 1.2.1.1 Requirement Id

REQ-1-014

#### 1.2.1.2 Requirement Text

The system's deployment environment shall be hosted on AWS and orchestrated using containers. The application components (Odoo, microservice) must be packaged as Docker images. The production environment shall be a high-availability Amazon EKS cluster, utilizing Amazon RDS for PostgreSQL 16 for the database and Amazon S3 for storing all file attachments (e.g., receipts, PODs).

#### 1.2.1.3 Validation Criteria

- Verify the existence of Dockerfiles for all application components.
- Confirm the deployment scripts and configuration target an AWS EKS cluster.
- Verify that the application's database connection string points to an Amazon RDS for PostgreSQL 16 instance.
- Upload a file attachment and confirm it is stored in the designated Amazon S3 bucket, not in the database or on the local filesystem.

#### 1.2.1.4 Implementation Implications

- This repository must contain Kubernetes manifest files (Deployments, Services, Ingress, etc.) to define how application containers run on EKS.
- Manifests must include mechanisms (e.g., ConfigMaps, Secrets) to inject external configuration like RDS connection strings and S3 bucket names into the application pods.
- Deployment manifests must specify the Docker image URIs for each application component, which are consumed from a container registry.
- The repository should use a templating engine like Helm to manage configurations across different environments (dev, staging, prod).

#### 1.2.1.5 Extraction Reasoning

This requirement is the primary driver for the existence of the tms-kubernetes-manifests repository. The repository's sole purpose is to provide the Kubernetes configuration that orchestrates the containerized application on the specified AWS EKS cluster.

### 1.2.2.0 Requirement Id

#### 1.2.2.1 Requirement Id

REQ-1-502

#### 1.2.2.2 Requirement Text

The system must be highly available and recoverable. It shall achieve a minimum uptime of 99.9% during defined business hours, excluding pre-announced maintenance windows. For disaster recovery, the Recovery Point Objective (RPO), representing the maximum acceptable data loss, is 15 minutes. The Recovery Time Objective (RTO), representing the maximum time to restore service, is 4 hours.

#### 1.2.2.3 Validation Criteria

- Configure uptime monitoring (e.g., AWS CloudWatch) and review reports to confirm 99.9% availability is met.
- Verify that the database is configured for Point-In-Time-Recovery (PITR) with a granularity that supports a 15-minute RPO.
- Conduct a disaster recovery drill by simulating a regional failure and measure the time taken to restore the application and database in another region, ensuring it is under the 4-hour RTO.

#### 1.2.2.4 Implementation Implications

- Kubernetes Deployment manifests must be configured with multiple replicas for high availability.
- Pod Anti-Affinity rules must be defined to ensure replicas are scheduled across different nodes/availability zones.
- A PodDisruptionBudget must be defined for each critical application component to prevent voluntary disruptions from taking down the service.

#### 1.2.2.5 Extraction Reasoning

This NFR directly translates to specific Kubernetes configurations that must be defined within this repository to ensure application-level high availability.

### 1.2.3.0 Requirement Id

#### 1.2.3.1 Requirement Id

REQ-1-503

#### 1.2.3.2 Requirement Text

The system must enforce strict security for secrets management. All sensitive credentials, including but not limited to database passwords, GSP API keys, and GPS provider tokens, shall be stored in AWS Secrets Manager. These secrets must be dynamically injected into the application's runtime environment and must never be hardcoded in the source code, committed to version control, or stored in plain-text configuration files.

#### 1.2.3.3 Validation Criteria

- Review the application's source code and configuration files to confirm the absence of any hardcoded credentials.
- Inspect the Kubernetes deployment configuration and verify that it is configured to mount secrets from AWS Secrets Manager into the application pods as environment variables or files.

#### 1.2.3.4 Implementation Implications

- This repository must define the Kubernetes mechanism for fetching secrets from AWS Secrets Manager.
- This will be implemented using the AWS Secrets Store CSI Driver and associated `SecretProviderClass` custom resources.
- Deployment manifests will reference these resources to securely mount secrets into application pods.
- This repository must not contain any plaintext secrets.

#### 1.2.3.5 Extraction Reasoning

This critical security requirement dictates the secret management strategy at the deployment layer, which is a core responsibility of this repository.

### 1.2.4.0 Requirement Id

#### 1.2.4.1 Requirement Id

REQ-1-602

#### 1.2.4.2 Requirement Text

The system shall implement a comprehensive monitoring and logging stack. Prometheus shall be used to scrape metrics from application and infrastructure endpoints. Fluentbit shall be deployed to collect logs from all containers and forward them to a centralized OpenSearch cluster...

#### 1.2.4.3 Validation Criteria

- Verify that Prometheus is successfully scraping metrics from the Odoo and microservice pods.

#### 1.2.4.4 Implementation Implications

- Deployment manifests for application components must include Prometheus-specific annotations (e.g., `prometheus.io/scrape: 'true'`) to enable metric scraping.
- Service manifests must expose the metrics port.
- Manifests will also define how observability configurations from REPO-TMS-OBS are mounted into the monitoring tool pods.

#### 1.2.4.5 Extraction Reasoning

This requirement mandates that the application deployments defined in this repository are compatible with and discoverable by the cluster's monitoring stack.

## 1.3.0.0 Relevant Components

### 1.3.1.0 Component Name

#### 1.3.1.1 Component Name

Helm Charts

#### 1.3.1.2 Component Specification

A collection of templated Kubernetes manifest files that together define a complete application or service (Odoo, GPS Service). It allows for managing the complexity of Kubernetes applications and provides a standardized way to configure and deploy them across different environments using values files.

#### 1.3.1.3 Implementation Requirements

- Define a parent Helm chart for the entire TMS application.
- Create sub-charts for each deployable service (e.g., Odoo, GPS microservice).
- Use a values.yaml file to manage environment-specific configurations.
- Implement health checks (liveness and readiness probes) within the deployment templates.

#### 1.3.1.4 Architectural Context

Infrastructure & Operations Layer. This is the primary packaging and deployment unit for the GitOps methodology.

#### 1.3.1.5 Extraction Reasoning

The repository is explicitly described as being structured with Helm charts, making this the central component.

### 1.3.2.0 Component Name

#### 1.3.2.1 Component Name

Kubernetes Deployment

#### 1.3.2.2 Component Specification

Defines the desired state for a set of application pods, including the container image to use, the number of replicas, resource requests/limits, and update strategies. Kubernetes continuously works to maintain this desired state.

#### 1.3.2.3 Implementation Requirements

- Create a Deployment manifest for each microservice and the Odoo application.
- Specify container images, ports, environment variables, and volume mounts for secrets and configurations.
- Define appropriate resource requests and limits to ensure stable performance.
- Configure rolling update strategies to enable zero-downtime deployments.

#### 1.3.2.4 Architectural Context

Infrastructure & Operations Layer. This is the core Kubernetes object for managing stateless application workloads.

#### 1.3.2.5 Extraction Reasoning

This is a fundamental Kubernetes object that must be defined within this repository to run the containerized applications on EKS.

### 1.3.3.0 Component Name

#### 1.3.3.1 Component Name

Kubernetes Ingress

#### 1.3.3.2 Component Specification

Manages external access to the services in a cluster, typically HTTP and HTTPS. It can provide load balancing, SSL termination, and name-based virtual hosting.

#### 1.3.3.3 Implementation Requirements

- Define Ingress rules to route external traffic (e.g., from the internet) to the correct services based on hostname and path.
- Configure TLS termination using certificates managed by AWS Certificate Manager.
- Use an Ingress controller like the AWS Load Balancer Controller to provision an Application Load Balancer.

#### 1.3.3.4 Architectural Context

Infrastructure & Operations Layer. This is the primary entry point for external traffic into the Kubernetes cluster.

#### 1.3.3.5 Extraction Reasoning

Required to expose the web-based Odoo application and any public API endpoints to users and external systems.

### 1.3.4.0 Component Name

#### 1.3.4.1 Component Name

SecretProviderClass Manifest

#### 1.3.4.2 Component Specification

A Kubernetes Custom Resource that defines how to fetch secrets from AWS Secrets Manager and make them available to pods. It is the key component for secure, dynamic secret injection.

#### 1.3.4.3 Implementation Requirements

- Define one or more `SecretProviderClass` resources.
- Specify the AWS region and a list of secret ARNs to fetch.
- Configure the resource to sync the fetched secrets into a native Kubernetes `Secret` object for application consumption.

#### 1.3.4.4 Architectural Context

Infrastructure & Operations Layer. Implements the secure integration pattern with AWS Secrets Manager.

#### 1.3.4.5 Extraction Reasoning

This component is the direct implementation of the secure secret injection pattern mandated by REQ-1-503.

## 1.4.0.0 Architectural Layers

- {'layer_name': 'Infrastructure & Operations Layer', 'layer_responsibilities': 'This layer is responsible for defining the runtime environment and deployment configuration for all application services. For this repository, the scope is strictly limited to the Kubernetes-level configuration that runs on the provisioned EKS cluster.', 'layer_constraints': ['Must be compatible with Amazon EKS.', 'Must adhere to a GitOps workflow for deployments.', 'Must not contain any application source code or infrastructure provisioning code.'], 'implementation_patterns': ['GitOps', 'Infrastructure as Code (IaC) for application configuration', 'Templating (Helm)'], 'extraction_reasoning': 'This repository is a core component of the Infrastructure & Operations Layer, specifically handling the application deployment aspect, which is distinct from infrastructure provisioning.'}

## 1.5.0.0 Dependency Interfaces

### 1.5.1.0 Interface Name

#### 1.5.1.1 Interface Name

IInfrastructureOutputs

#### 1.5.1.2 Source Repository

REPO-TMS-INFRA

#### 1.5.1.3 Method Contracts

- {'method_name': 'Terraform Remote State', 'method_signature': 'data "terraform_remote_state" "infra" { backend = "s3" ... }', 'method_purpose': 'To consume the identifiers and endpoints of the provisioned AWS infrastructure (VPC, EKS cluster, RDS, S3, etc.) required for configuring the Kubernetes deployment.', 'integration_context': 'Consumed by the CI/CD pipeline responsible for applying the manifests in this repository, which needs to know where to deploy and how to configure connections to external services.'}

#### 1.5.1.4 Integration Pattern

Infrastructure Consumption via Remote State

#### 1.5.1.5 Communication Protocol

Terraform State Protocol

#### 1.5.1.6 Extraction Reasoning

This is the most critical dependency, as this repository cannot function without the target infrastructure defined and provisioned by REPO-TMS-INFRA.

### 1.5.2.0 Interface Name

#### 1.5.2.1 Interface Name

IContainerImageArtifact

#### 1.5.2.2 Source Repository

REPO-TMS-CORE, REPO-GPS-SVC

#### 1.5.2.3 Method Contracts

- {'method_name': 'Image URI', 'method_signature': "string (e.g., '123456789012.dkr.ecr.ap-south-1.amazonaws.com/tms-core:1.2.3')", 'method_purpose': 'To provide the specific, versioned Docker image artifact to be deployed.', 'integration_context': "The image URI is consumed and specified in the `image.repository` and `image.tag` fields within the Helm chart's `values.yaml` file, which is then used by the Kubernetes Deployment manifest."}

#### 1.5.2.4 Integration Pattern

Artifact Consumption

#### 1.5.2.5 Communication Protocol

Docker Registry API

#### 1.5.2.6 Extraction Reasoning

This repository's purpose is to deploy application artifacts (Docker images) produced by the CI/CD pipelines of the application repositories.

### 1.5.3.0 Interface Name

#### 1.5.3.1 Interface Name

IObservabilityConfiguration

#### 1.5.3.2 Source Repository

REPO-TMS-OBS

#### 1.5.3.3 Method Contracts

- {'method_name': 'Configuration Files', 'method_signature': 'YAML and JSON files (e.g., prometheus/rules/*.yml, grafana/dashboards/*.json)', 'method_purpose': 'To provide the declarative configurations for Prometheus, Grafana, and other observability tools.', 'integration_context': 'The manifests in this repository will define ConfigMaps and volume mounts for the monitoring tool pods, which will be populated with the contents of the files from REPO-TMS-OBS via a GitOps controller or CI pipeline.'}

#### 1.5.3.4 Integration Pattern

Configuration Consumption via GitOps

#### 1.5.3.5 Communication Protocol

Git

#### 1.5.3.6 Extraction Reasoning

The Kubernetes deployments for the observability stack, defined here, are consumers of the version-controlled configurations from REPO-TMS-OBS to ensure a fully code-driven monitoring setup.

## 1.6.0.0 Exposed Interfaces

### 1.6.1.0 Interface Name

#### 1.6.1.1 Interface Name

IHelmValuesAPI

#### 1.6.1.2 Consumer Repositories

- REPO-TMS-CORE
- REPO-GPS-SVC

#### 1.6.1.3 Method Contracts

- {'method_name': 'Helm Values Structure', 'method_signature': "YAML file structure (e.g., 'tmsOdoo.image.tag', 'gpsService.image.tag')", 'method_purpose': 'Provides a stable, version-controlled contract for CI/CD pipelines to update the image tags for deployed applications, triggering a new release via the GitOps workflow.', 'implementation_requirements': 'The `values.yaml` files within this repository must be well-structured and documented to serve as a clear API for the CI/CD processes of other repositories.'}

#### 1.6.1.4 Service Level Requirements

- The structure of the values files should be considered a stable API; breaking changes require coordination.

#### 1.6.1.5 Implementation Constraints

- CI/CD pipelines from consumer repositories must have write access (via a deploy key or token) to this Git repository to update image tags.

#### 1.6.1.6 Extraction Reasoning

This repository exposes a declarative API to the rest of the system's CI/CD infrastructure, defining how new application versions are promoted into the deployment pipeline.

### 1.6.2.0 Interface Name

#### 1.6.2.1 Interface Name

IApplicationEndpoints

#### 1.6.2.2 Consumer Repositories

- End-Users (via Browser)
- External Systems

#### 1.6.2.3 Method Contracts

- {'method_name': 'HTTP/HTTPS Endpoints', 'method_signature': "Public DNS hostnames (e.g., 'tms.example.com', 'api.tms.example.com')", 'method_purpose': 'To expose the running Odoo application and FastAPI microservice APIs to the internet.', 'implementation_requirements': 'Endpoints must be defined using Kubernetes Ingress resources, managed by the AWS Load Balancer Controller, and secured with TLS certificates.'}

#### 1.6.2.4 Service Level Requirements

- High availability as defined in the target EKS cluster configuration.
- Secure communication via HTTPS with TLS termination.

#### 1.6.2.5 Implementation Constraints

- Endpoints must be defined using Kubernetes Ingress objects.
- The Ingress must be managed by an appropriate Ingress controller (e.g., AWS Load Balancer Controller).

#### 1.6.2.6 Extraction Reasoning

While this repository does not contain code that implements an interface, it is directly responsible for defining and exposing the network endpoints through which the running application is accessed by all consumers.

## 1.7.0.0 Technology Context

### 1.7.1.0 Framework Requirements

The repository must contain valid Kubernetes manifests, structured using either Helm or Kustomize for templating and environment management. The primary language is YAML.

### 1.7.2.0 Integration Technologies

- Kubernetes
- Helm
- Docker
- Amazon EKS
- AWS Secrets Manager (via AWS Secrets Store CSI Driver)

### 1.7.3.0 Performance Constraints

Manifests must define appropriate resource requests and limits for all containers to ensure proper scheduling by Kubernetes and to prevent resource contention or exhaustion on the cluster nodes. Horizontal Pod Autoscalers should be used for stateless, high-load services.

### 1.7.4.0 Security Requirements

Manifests should define NetworkPolicies to enforce least-privilege communication between pods. Secret management must not involve storing plain-text secrets in this Git repository; a secure provider for AWS Secrets Manager must be used. ServiceAccounts must be configured with IAM Roles for Service Accounts (IRSA) for secure access to AWS resources.

## 1.8.0.0 Extraction Validation

| Property | Value |
|----------|-------|
| Mapping Completeness Check | The repository mapping is complete and directly ad... |
| Cross Reference Validation | The repository's responsibilities and dependencies... |
| Implementation Readiness Assessment | The repository context is fully implementation-rea... |
| Quality Assurance Confirmation | The extraction has been systematically validated. ... |

