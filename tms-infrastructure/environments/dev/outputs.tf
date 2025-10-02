# -----------------------------------------------------------------------------
# Outputs for the Development Environment
#
# This file defines the outputs of the Terraform configuration for the 'dev'
# environment. These outputs serve as the contract for other systems, such as
# the Kubernetes deployment repository, to consume infrastructure details.
# -----------------------------------------------------------------------------

# --- Network Outputs ---
output "vpc_id" {
  description = "The ID of the VPC for the dev environment."
  value       = module.network.vpc_id
}

output "private_subnet_ids" {
  description = "A list of IDs for the private subnets in the dev environment."
  value       = module.network.private_subnet_ids
}

output "public_subnet_ids" {
  description = "A list of IDs for the public subnets in the dev environment."
  value       = module.network.public_subnet_ids
}

# --- Security Outputs ---
output "eks_node_sg_id" {
  description = "The ID of the security group attached to the EKS worker nodes in dev."
  value       = module.security.eks_node_sg_id
}

output "rds_sg_id" {
  description = "The ID of the security group for the RDS instance in dev."
  value       = module.security.rds_sg_id
}

# --- EKS Outputs ---
output "eks_cluster_name" {
  description = "The name of the EKS cluster for the dev environment."
  value       = module.eks.cluster_name
}

output "eks_cluster_endpoint" {
  description = "The API server endpoint for the EKS cluster in dev."
  value       = module.eks.cluster_endpoint
}

output "eks_cluster_oidc_issuer_url" {
  description = "The OIDC issuer URL for the EKS cluster, required for IRSA."
  value       = module.eks.cluster_oidc_issuer_url
}

output "eks_cluster_ca_certificate" {
  description = "The Base64 encoded CA certificate for the EKS cluster."
  value       = module.eks.cluster_ca_certificate
  sensitive   = true
}

# --- RDS Outputs ---
output "rds_instance_endpoint" {
  description = "The connection endpoint for the RDS PostgreSQL instance in dev."
  value       = module.rds.instance_endpoint
}

output "rds_db_name" {
  description = "The name of the database created within the RDS instance for dev."
  value       = module.rds.db_name
}

output "rds_master_username" {
  description = "The master username for the RDS instance."
  value       = module.rds.master_username
}

output "rds_master_password_secret_arn" {
  description = "The ARN of the secret in AWS Secrets Manager containing the RDS master password for dev."
  value       = module.secrets.rds_master_password_secret_arn
  sensitive   = true
}

# --- S3 Outputs ---
output "s3_attachments_bucket_name" {
  description = "The name of the S3 bucket for storing application file attachments in dev."
  value       = module.s3_attachments.bucket_name
}

output "s3_attachments_bucket_arn" {
  description = "The ARN of the S3 bucket for storing application file attachments in dev."
  value       = module.s3_attachments.bucket_arn
}

# --- ElastiCache (Redis) Outputs ---
output "redis_primary_endpoint" {
  description = "The primary endpoint for the Redis (ElastiCache) cluster in dev."
  value       = module.elasticache_redis.primary_endpoint
}

output "redis_auth_token_secret_arn" {
  description = "The ARN of the secret containing the Redis AUTH token for dev."
  value       = module.secrets.redis_auth_token_secret_arn
  sensitive   = true
}

# --- MQ (RabbitMQ) Outputs ---
output "rabbitmq_broker_endpoints" {
  description = "The AMQP endpoints for the RabbitMQ broker in dev."
  value       = module.mq_rabbitmq.rabbitmq_broker_endpoints
}

output "rabbitmq_username_secret_arn" {
  description = "The ARN of the secret containing the RabbitMQ master username for dev."
  value       = module.secrets.rabbitmq_username_secret_arn
  sensitive   = true
}

output "rabbitmq_password_secret_arn" {
  description = "The ARN of the secret containing the RabbitMQ master password for dev."
  value       = module.secrets.rabbitmq_password_secret_arn
  sensitive   = true
}

# --- API Gateway Outputs ---
output "api_gateway_invoke_url" {
  description = "The invoke URL for the API Gateway stage exposing the GPS microservice in dev."
  value       = module.api_gateway.invoke_url
}

# --- Timestream Outputs ---
output "timestream_database_name" {
  description = "The name of the Timestream database for GPS telemetry in dev."
  value       = module.timestream.database_name
}

output "timestream_table_name" {
  description = "The name of the Timestream table for GPS telemetry in dev."
  value       = module.timestream.table_name
}

# --- Monitoring Outputs ---
output "grafana_workspace_endpoint" {
  description = "The URL for the Grafana workspace endpoint in dev."
  value       = module.monitoring.grafana_workspace_endpoint
}

output "prometheus_workspace_endpoint" {
  description = "The remote write URL for the Prometheus workspace in dev."
  value       = module.monitoring.prometheus_workspace_endpoint
}

output "opensearch_domain_endpoint" {
  description = "The endpoint for the OpenSearch domain in dev."
  value       = module.monitoring.opensearch_domain_endpoint
}