# Infrastructure Outputs Contract

This document defines the official contract of the `tms-infrastructure` repository. The outputs listed here are consumed by downstream systems, primarily the Kubernetes deployment repository (`REPO-TMS-K8S`), to configure and deploy applications.

**Any change to the name, type, or semantic meaning of these outputs is considered a breaking change and requires coordination with the consuming repositories.**

The consuming repository (`REPO-TMS-K8S`) will use the `terraform_remote_state` data source to read these values.

---

## Infrastructure Outputs

The following table details all outputs provided by the Terraform configuration for each environment (`dev`, `staging`, `prod`).

| Output Name                        | Data Type      | Description                                                                                             |
| ---------------------------------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| **Network**                        |                |                                                                                                         |
| `vpc_id`                           | `string`       | The ID of the provisioned Virtual Private Cloud (VPC).                                                  |
| `private_subnet_ids`               | `list(string)` | A list of subnet IDs for the private subnets where application workloads (EKS nodes) will run.          |
| `public_subnet_ids`                | `list(string)` | A list of subnet IDs for the public subnets used for load balancers and NAT gateways.                   |
| **Security**                       |                |                                                                                                         |
| `eks_node_sg_id`                   | `string`       | The ID of the security group attached to the EKS worker nodes.                                          |
| `rds_sg_id`                        | `string`       | The ID of the security group for the RDS database instance.                                             |
| **EKS (Kubernetes)**               |                |                                                                                                         |
| `eks_cluster_name`                 | `string`       | The name of the Amazon EKS cluster. Used by `kubectl` and other tools to target the cluster.            |
| `eks_cluster_endpoint`             | `string`       | The API server endpoint URL for the EKS cluster.                                                        |
| `eks_cluster_oidc_issuer_url`      | `string`       | The OIDC issuer URL for the cluster, required for configuring IAM Roles for Service Accounts (IRSA).      |
| `eks_cluster_ca_certificate`       | `string`       | The Base64 encoded Certificate Authority certificate for the EKS cluster. (Marked as sensitive)         |
| **RDS (PostgreSQL)**               |                |                                                                                                         |
| `rds_instance_endpoint`            | `string`       | The connection endpoint address for the RDS PostgreSQL instance.                                        |
| `rds_db_name`                      | `string`       | The name of the initial database created within the RDS instance.                                       |
| `rds_master_username`              | `string`       | The master username for the RDS instance.                                                               |
| `rds_master_password_secret_arn`   | `string`       | The ARN of the secret in AWS Secrets Manager containing the RDS master password. (Marked as sensitive)    |
| **S3 (Object Storage)**            |                |                                                                                                         |
| `s3_attachments_bucket_name`       | `string`       | The unique name of the S3 bucket used for storing application file attachments (e.g., PODs, receipts).    |
| `s3_attachments_bucket_arn`        | `string`       | The ARN of the S3 bucket for attachments, used for IAM policies.                                        |
| **ElastiCache (Redis)**            |                |                                                                                                         |
| `redis_primary_endpoint`           | `string`       | The primary connection endpoint for the Redis (ElastiCache) cluster.                                    |
| `redis_auth_token_secret_arn`      | `string`       | The ARN of the secret in AWS Secrets Manager containing the Redis AUTH token. (Marked as sensitive)       |
| **MQ (RabbitMQ)**                  |                |                                                                                                         |
| `rabbitmq_broker_endpoints`        | `list(string)` | The list of AMQP endpoints for connecting to the RabbitMQ broker cluster.                               |
| `rabbitmq_username_secret_arn`     | `string`       | The ARN of the secret in AWS Secrets Manager containing the RabbitMQ master username. (Marked as sensitive) |
| `rabbitmq_password_secret_arn`     | `string`       | The ARN of the secret in AWS Secrets Manager containing the RabbitMQ master password. (Marked as sensitive) |
| **API Gateway**                    |                |                                                                                                         |
| `api_gateway_invoke_url`           | `string`       | The invoke URL for the API Gateway stage that exposes the GPS ingestion microservice.                   |
| **Timestream (Telemetry)**         |                |                                                                                                         |
| `timestream_database_name`         | `string`       | The name of the Amazon Timestream database for high-volume GPS telemetry data.                          |
| `timestream_table_name`            | `string`       | The name of the Amazon Timestream table for storing GPS location points.                                |
| **Monitoring**                     |                |                                                                                                         |
| `grafana_workspace_endpoint`       | `string`       | The public URL endpoint for accessing the managed Grafana workspace.                                    |
| `prometheus_workspace_endpoint`    | `string`       | The remote write URL for the managed Prometheus workspace, used by in-cluster collectors.               |
| `opensearch_domain_endpoint`       | `string`       | The endpoint for the managed OpenSearch domain, used by log forwarders (Fluentbit).                     |