# TMS Infrastructure - REPO-TMS-INFRA

This repository contains the Infrastructure as Code (IaC) for the Transport Management System (TMS) platform, managed with Terraform. It is the single source of truth for all AWS cloud infrastructure provisioning.

## Overview

The infrastructure is defined declaratively using HashiCorp Configuration Language (HCL) and is structured into reusable modules to promote maintainability, scalability, and consistency across environments. This repository is responsible for provisioning the foundational AWS environment, including:

-   **Networking**: VPC, public/private subnets, NAT gateways, and route tables.
-   **Compute**: Amazon EKS (Elastic Kubernetes Service) cluster and node groups.
-   **Databases**: Amazon RDS for PostgreSQL 16 and Amazon Timestream for telemetry.
-   **Storage**: Amazon S3 buckets for application attachments and Terraform state.
-   **Messaging & Caching**: Amazon MQ for RabbitMQ and Amazon ElastiCache for Redis.
-   **Security**: AWS Secrets Manager for credentials, IAM Roles (including IRSA), and Security Groups.
-   **Monitoring**: AWS Managed Services for Prometheus, Grafana, and Amazon OpenSearch.

This repository explicitly **excludes** application code, container images, and Kubernetes deployment manifests. It provides the target environment for those components.

## Repository Structure

-   `environments/`: Contains the root configuration for each deployment environment (e.g., `dev`, `staging`, `prod`). These configurations compose the reusable modules.
-   `modules/`: Contains reusable, versionable Terraform modules that encapsulate specific pieces of infrastructure (e.g., `network`, `eks`, `rds`).
-   `backend.tf`: Configures the remote state backend (S3).
-   `providers.tf`: Configures the AWS provider.
-   `versions.tf`: Pins the required Terraform and provider versions.
-   `CONTRACTS.md`: Documents the outputs (the public contract) exposed by this repository for consumption by other CI/CD pipelines.

## Prerequisites

-   [Terraform](https://developer.hashicorp.com/terraform/downloads) (version is pinned in `versions.tf`)
-   [AWS CLI](https://aws.amazon.com/cli/) configured with appropriate credentials.
-   [pre-commit](https://pre-commit.com/) for running quality checks before committing code.
-   [tflint](https://github.com/terraform-linters/tflint) for linting Terraform code.

To install pre-commit hooks:
```bash
pre-commit install
```

## Usage

All Terraform operations should be executed from within a specific environment's directory.

1.  **Navigate to the environment directory:**
    ```bash
    cd environments/dev
    ```

2.  **Initialize Terraform:**
    This will download the necessary providers and configure the backend.
    ```bash
t    erraform init
    ```

3.  **Plan the changes:**
    This command creates an execution plan, which lets you preview the changes Terraform plans to make to your infrastructure.
    ```bash
    terraform plan -var-file=terraform.tfvars
    ```

4.  **Apply the changes:**
    This command applies the changes required to reach the desired state of the configuration.
    ```bash
    terraform apply -var-file=terraform.tfvars
    ```

## CI/CD

Changes to infrastructure are managed via pull requests and applied automatically by a GitHub Actions pipeline defined in `.github/workflows/terraform-pipeline.yml`.

-   **On Pull Request**: The pipeline runs `terraform plan` to generate a plan for review.
-   **On Merge to `main`**: The pipeline runs `terraform apply` to provision the changes.