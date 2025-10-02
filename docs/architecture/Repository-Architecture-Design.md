# TMS Solution - Enterprise Architecture Documentation

## Executive Summary
This document outlines the enterprise architecture for the Transport Management System (TMS), a cloud-native solution designed to modernize transport operations. The system is a hybrid architecture, combining a core **Odoo 18 Modular Monolith** for robust business logic with a high-performance **FastAPI Microservice** for real-time GPS data ingestion. The primary architectural driver was the strategic decomposition of the initial Odoo monolith into smaller, focused repositories. This decision enhances modularity, enables parallel development streams, and isolates external dependencies, leading to a more resilient, maintainable, and scalable system. Deployed on **Amazon EKS** and managed via **Infrastructure as Code (Terraform)** and **GitOps (Helm)**, the TMS solution delivers significant business value by reducing the support load on administrative staff, improving driver proficiency through self-service tools, and providing a stable, observable platform for future growth.

## Solution Architecture Overview

### Technology Stack
The TMS solution is built on a modern, cloud-native technology stack designed for performance, scalability, and reliability:
- **Backend Frameworks**: Odoo 18 (Python 3.11) for the core monolith, FastAPI (Python 3.11) for the GPS microservice.
- **Frontend Framework**: Odoo Web Library (OWL) 2.0 for the responsive, mobile-first Driver Portal.
- **Database**: Amazon RDS for PostgreSQL 16 (primary transactional DB) and Amazon ElastiCache for Redis (caching).
- **Infrastructure**: Amazon EKS for container orchestration, Docker for containerization, and Amazon S3 for file storage.
- **Integration**: RabbitMQ (Amazon MQ) for asynchronous messaging, and REST/HTTP for synchronous API communication.
- **DevOps & IaC**: Terraform for Infrastructure as Code, GitHub Actions for CI/CD, and Helm for Kubernetes deployments.
- **Observability**: A complete stack comprising Prometheus, Grafana, Fluent Bit, and OpenSearch for metrics, dashboards, and logging.

### Architectural Patterns
The architecture is founded on several key patterns:
- **Hybrid Architecture (Modular Monolith + Microservice)**: Leverages the rapid development capabilities of the Odoo framework for complex business workflows while isolating the high-throughput, I/O-bound task of GPS data ingestion into a specialized, independently scalable microservice.
- **Event-Driven Integration**: Decouples the GPS microservice from the Odoo monolith via a RabbitMQ message queue. This asynchronous pattern provides resilience and acts as a buffer, ensuring that high volumes of telemetry data do not impact the performance of the core transactional system.
- **Adapter Pattern**: Specialized integration repositories (`tms-gsp-integration-client`, `tms-gps-data-consumer`) act as adapters, encapsulating the logic for communicating with external services or message brokers. This isolates third-party dependencies and simplifies maintenance.

### Integration Approach
System integration is managed through well-defined contracts:
- **Asynchronous (GPS Telemetry)**: The GPS microservice polls an external API and publishes a standardized `VehicleLocationUpdated` event to RabbitMQ. A dedicated consumer within the Odoo application subscribes to these events to update vehicle status in near real-time.
- **Synchronous with Async Fallback (GSP E-Invoicing)**: For critical financial operations like e-invoicing, the system makes a primary synchronous REST API call to provide immediate user feedback. If this call fails or times out, the task is automatically enqueued into a background job processor for retries with exponential backoff, ensuring eventual consistency without blocking the user.

## Repository Architecture Strategy

### Decomposition Approach
The architecture evolved from a single monolithic Odoo addon repository to a set of eight focused repositories. The decomposition was driven by separating concerns along natural architectural boundaries:
1.  **Core vs. UI**: The specialized OWL-based Driver Portal (`tms-driver-portal-ui`) was separated from the core backend logic (`tms-core-business-logic`).
2.  **Core vs. Integration**: Logic for handling external integrations was extracted into dedicated repositories (`tms-gsp-integration-client` for the GSP API and `tms-gps-data-consumer` for the RabbitMQ consumer).
3.  **Application vs. Platform**: Code was strictly separated from its configuration. Application source code resides in service/addon repositories, while platform configurations (Infrastructure, Kubernetes, Observability) are managed in their own dedicated 'as-Code' repositories.

### Optimization Benefits
This decomposed structure provides numerous advantages:
- **Independent Development & Deployment**: Teams can work on different components (e.g., Driver UI, GPS service, Core Logic) in parallel with minimal friction, leading to faster delivery cycles.
- **Clear Ownership & Expertise**: Each repository has a single, well-defined responsibility, fostering clear ownership and allowing teams to build specialized expertise.
- **Improved Maintainability**: Isolating external dependencies means that a change in a third-party API only requires updates to a single, small repository, rather than the entire core application.
- **Enhanced Reusability**: Platform-level repositories like `tms-infrastructure` and `tms-observability-config` contain modules and configurations that are reusable across other projects.

### Development Workflow
The repository structure enables a modern GitOps workflow. Development teams for each service/addon work independently in their respective repositories. Their CI pipelines are responsible for running tests and publishing versioned Docker image artifacts. The platform team manages the `tms-kubernetes-manifests` repository, which consumes these images. A change to a Helm chart in this repository automatically triggers a deployment to the EKS cluster, ensuring a consistent and auditable path to production.

## System Architecture Diagrams

### Repository Dependency Architecture
This diagram illustrates the final decomposed repository structure, their primary responsibilities, and the key dependencies and data flows between them. It shows a clear separation between the Odoo Application Layer, the independent Application Services, and the foundational Platform as Code layer.

### Component Integration Patterns
This diagram details the primary communication patterns between the services, highlighting the synchronous and asynchronous data exchange mechanisms. It clarifies the role of RabbitMQ as a message broker and the nature of API calls between the frontend and backend.

## Repository Catalog

- **tms-core-business-logic**: The core Odoo addon containing foundational data models, business logic, and back-office UI. It is the central authority for all business rules and data.
  - *Technology*: Odoo 18, Python 3.11
  - *Dependencies*: None
- **tms-driver-portal-ui**: A dedicated Odoo addon for the mobile-first Driver Portal frontend, built with the OWL 2.0 framework.
  - *Technology*: OWL 2.0, JavaScript
  - *Dependencies*: `tms-core-business-logic` (for APIs)
- **tms-gsp-integration-client**: An adapter addon that encapsulates all logic for communicating with the external GSP e-invoicing API.
  - *Technology*: Python 3.11, Odoo Job Queue
  - *Dependencies*: `tms-core-business-logic` (for invoice data)
- **tms-gps-data-consumer**: An adapter addon that contains the RabbitMQ consumer logic for processing incoming vehicle location events.
  - *Technology*: Python 3.11, RabbitMQ (pika)
  - *Dependencies*: `tms-core-business-logic` (to update vehicles)
- **tms-gps-ingestion-service**: A standalone FastAPI microservice that polls the third-party GPS API and publishes events to RabbitMQ.
  - *Technology*: FastAPI, Python 3.11, Docker
  - *Dependencies*: None
- **tms-infrastructure**: Contains all Terraform code to provision the AWS infrastructure (EKS, RDS, S3, etc.).
  - *Technology*: Terraform, HCL
  - *Dependencies*: None
- **tms-kubernetes-manifests**: Contains all Helm charts for deploying the applications and platform services to the EKS cluster.
  - *Technology*: Kubernetes, Helm, YAML
  - *Dependencies*: Consumes Docker images from all application repositories.
- **tms-observability-config**: Stores all configurations for the observability stack, including Prometheus rules and Grafana dashboards.
  - *Technology*: YAML, JSON
  - *Dependencies*: None

## Integration Architecture

### Interface Contracts
- **Odoo RPC API**: Exposed by `tms-core-business-logic` and consumed by `tms-driver-portal-ui`. This is a synchronous, request-response contract over HTTP/JSON-RPC for all frontend-backend interactions.
- **Odoo ORM API**: A Python-level API used internally by `tms-gsp-integration-client` and `tms-gps-data-consumer` to interact with the core data models.
- **AMQP Event Contract**: The `tms-gps-ingestion-service` produces a `VehicleLocationUpdated` event with a strict JSON schema. `tms-gps-data-consumer` is the consumer of this event. This is an asynchronous contract mediated by RabbitMQ.

### Data Flows
- **Transactional Flow**: A user interaction in the Driver Portal (`tms-driver-portal-ui`) triggers an RPC call to `tms-core-business-logic`, which performs business logic and commits data to the PostgreSQL database.
- **Real-time GPS Flow**: The `tms-gps-ingestion-service` polls an external API, publishes an event to RabbitMQ, which is then consumed by `tms-gps-data-consumer` and written to the PostgreSQL database via the `tms-core-business-logic` ORM.

## Technology Implementation Framework
- **Odoo Development**: Logic must be implemented in model methods to ensure reusability. Security is enforced via security groups and record rules. ORM queries must be optimized to prevent performance issues.
- **FastAPI Development**: Services must be stateless and utilize Pydantic for strict data validation. Asynchronous programming (`async/await`) is used for all I/O-bound operations.
- **Frontend Development**: The OWL framework's component-based architecture and state management must be used. All backend communication is done via asynchronous RPC calls.
- **Security**: All secrets and credentials for the entire system are managed by AWS Secrets Manager and securely injected into the runtime environments, never stored in code.

## Performance & Scalability Architecture
- **Asymmetric Scaling**: The architecture allows for independent scaling. The `tms-gps-ingestion-service` can be scaled horizontally by adding more pods based on telemetry volume, while the core Odoo application is scaled based on concurrent user load.
- **Critical Paths**: The end-to-end latency of the GPS pipeline (<10s) is managed through the high-performance FastAPI service and batch processing by the consumer. The core application's API response time (<200ms) is supported by Redis caching and optimized database queries.
- **Resilience**: RabbitMQ acts as a critical buffer, absorbing spikes in GPS data and allowing the core application to process updates at its own pace. The async fallback for GSP integration ensures that failures in external services do not halt internal workflows.

## Development & Deployment Strategy
- **CI/CD**: Each application repository has a dedicated GitHub Actions pipeline that automates testing, code quality checks, and the building/publishing of versioned Docker images to Amazon ECR.
- **GitOps**: The `tms-kubernetes-manifests` repository serves as the single source of truth for deployments. Changes merged to this repository (e.g., updating an image tag in a Helm chart) trigger an automated workflow that applies the changes to the EKS cluster, ensuring a fully auditable and automated deployment process.
- **Infrastructure Management**: All cloud infrastructure is managed declaratively via Terraform in the `tms-infrastructure` repository. Changes are reviewed via `terraform plan` in pull requests before being applied.

## Architecture Decision Records

- **ADR-001: Adopt a Hybrid (Monolith + Microservice) Architecture**
  - **Decision**: To use a core Odoo monolith for business logic and a separate FastAPI microservice for GPS ingestion.
  - **Rationale**: This leverages Odoo's strength for rapid development of complex business workflows while isolating the performance-critical, high-throughput GPS data processing to a specialized service. This prevents the monolith from being impacted by telemetry volume and allows for independent scaling.

- **ADR-002: Decompose the Monolithic Odoo Addon Repository**
  - **Decision**: To break the single `tms-odoo-addon` repository into four distinct, responsibility-focused repositories: `tms-core-business-logic`, `tms-driver-portal-ui`, `tms-gsp-integration-client`, and `tms-gps-data-consumer`.
  - **Rationale**: The original monolith violated the single-responsibility principle. This decomposition separates concerns (core logic, UI, integrations), enables parallel development, isolates external dependencies, and improves overall code maintainability and team autonomy.

- **ADR-003: Utilize an Asynchronous, Event-Driven Pipeline for GPS Data**
  - **Decision**: To use RabbitMQ as a message broker to decouple the GPS ingestion microservice from the Odoo application.
  - **Rationale**: A synchronous approach would tightly couple the services and make the core application vulnerable to latency or failure in the ingestion pipeline. The asynchronous queue-based approach provides a resilient, scalable, and fault-tolerant mechanism for handling high-volume, non-critical data.

- **ADR-004: Mandate Infrastructure as Code (IaC) and GitOps**
  - **Decision**: All cloud infrastructure will be defined in Terraform (`tms-infrastructure`), and all application deployments will be defined as Kubernetes manifests in Git (`tms-kubernetes-manifests`).
  - **Rationale**: This ensures that the entire system, from infrastructure to application configuration, is versioned, auditable, and reproducible. It enables automation, reduces manual errors, and provides a clear, declarative state of the production environment.