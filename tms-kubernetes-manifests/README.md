# TMS Kubernetes Manifests

This repository contains the Kubernetes manifests for deploying the Transport Management System (TMS) application. It follows GitOps principles, where this repository is the single source of truth for the application's deployed state on the Amazon EKS cluster.

This repository fulfills the deployment requirements outlined in **REQ-1-014**, orchestrating the containerized Odoo monolith and FastAPI microservice as specified in the system architecture (**REQ-1-013**).

## Repository Structure

The repository uses a hybrid approach of Helm and Kustomize to manage application deployments across different environments.

```
.
├── .github/                # GitHub Actions CI workflows
│   └── workflows/
│       └── ci.yaml         # CI pipeline for linting and validation
├── base/                   # Kustomize base configuration
│   ├── kustomization.yaml  # Defines common resources and Helm chart rendering
│   ├── namespace.yaml      # Defines the 'tms' namespace
│   └── network-policies/   # Defines network security rules
├── charts/                 # Reusable Helm charts for application components
│   ├── tms-gps-service/    # Helm chart for the FastAPI GPS microservice
│   └── tms-odoo/           # Helm chart for the Odoo monolith application
├── crds/                   # Custom Resource Definitions required by the cluster
│   └── ...                 # e.g., SecretProviderClass CRD for AWS Secrets Manager integration
├── overlays/               # Environment-specific Kustomize overlays
│   └── production/         # Production environment configuration
│       ├── kustomization.yaml
│       ├── prod-values.yaml
│       └── patches/
├── scripts/                # Utility scripts for local validation and CI
│   ├── lint.sh             # Lints YAML files and Helm charts
│   └── validate.sh         # Validates that Kustomize overlays can be built
└── README.md               # This file
```

- **`charts/`**: Contains the packaged, reusable definitions for each application (Odoo and GPS Service). These charts are environment-agnostic.
- **`base/`**: The Kustomize base that renders the Helm charts with common, shared configuration. It also defines cluster-wide resources like the namespace and default network policies.
- **`overlays/`**: Contains environment-specific configurations (e.g., `production`). These overlays apply patches and provide custom values to the base, managing differences in replicas, resource limits, hostnames, etc.
- **`crds/`**: Stores Custom Resource Definitions that must be applied to the cluster before the Helm charts can be deployed.
- **`scripts/`**: Holds helper scripts for quality assurance, which are also used in the CI pipeline.

## Prerequisites

To work with this repository locally, you will need the following tools installed:

- **Helm**: `v3.14.0` or later
- **Kustomize**: `v5.3.0` or later
- **yamllint**: For YAML style checking
- **kubectl**: For interacting with a Kubernetes cluster

## Local Validation

Before pushing changes, you should run the validation scripts to ensure your changes are valid.

### 1. Linting

This script checks all YAML files for style and syntax correctness and validates Helm charts against best practices.

```bash
./scripts/lint.sh
```

### 2. Validation

This script attempts to build all Kustomize overlays. A successful run indicates that your configuration can be rendered into valid Kubernetes manifests.

```bash
./scripts/validate.sh
```

## Deployment Strategy (GitOps)

This repository is designed to be used with a GitOps controller (e.g., ArgoCD, Flux) running in the EKS cluster.

1.  **Code Change**: A developer merges a change into an application repository (e.g., `tms-core-service`).
2.  **CI & Build**: The application's CI pipeline builds a new Docker image and pushes it to Amazon ECR.
3.  **Update Manifests**: The CI pipeline then automatically updates the `image.tag` in the relevant `values.yaml` file in this repository (e.g., in `overlays/production/prod-values.yaml`) and commits the change.
4.  **GitOps Sync**: The GitOps controller detects the change in this repository.
5.  **Deployment**: The controller runs `kustomize build` on the appropriate overlay and applies the resulting manifests to the EKS cluster, triggering a rolling update of the application.

## Configuration

- **Helm Charts**: The core application definition is in the `charts/` directory. The `values.yaml` file in each chart defines its "API" - the set of configurable parameters.
- **Environments**: Environment-specific configuration is managed in the `overlays/` directory. For example, `overlays/production/prod-values.yaml` contains overrides for the production environment, such as production hostnames and increased replica counts.

## Secrets Management

In compliance with **REQ-1-503**, no secrets are stored in this repository. Secrets are managed in **AWS Secrets Manager**.

This repository uses the **AWS Secrets Store CSI Driver**.
- A `SecretProviderClass` manifest is defined for each application that needs secrets.
- This resource tells the CSI driver which secrets to fetch from AWS Secrets Manager.
- The `deployment.yaml` templates mount a volume using the CSI driver, which makes the secrets available to the pod as files or environment variables.
- This ensures that secrets are dynamically injected at runtime and never exposed in Git.