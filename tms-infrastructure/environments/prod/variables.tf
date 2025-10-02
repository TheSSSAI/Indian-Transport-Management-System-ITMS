# variables.tf for the 'prod' environment
# This file declares all variables needed to compose the full 'prod' infrastructure.
# The structure is identical to dev/variables.tf to maintain consistency.

# General Project Variables
variable "project_name" {
  description = "The name of the project."
  type        = string
  default     = "tms"
}

variable "aws_region" {
  description = "The AWS region to deploy resources into."
  type        = string
  default     = "ap-south-1"
}

variable "tags" {
  description = "Common tags to apply to all resources."
  type        = map(string)
  default     = {}
}

# Network Module Variables
variable "vpc_cidr" {
  description = "The CIDR block for the VPC."
  type        = string
}

variable "public_subnets_cidr" {
  description = "List of CIDR blocks for public subnets."
  type        = list(string)
}

variable "private_subnets_cidr" {
  description = "List of CIDR blocks for private subnets."
  type        = list(string)
}

# EKS Module Variables
variable "eks_cluster_version" {
  description = "The Kubernetes version for the EKS cluster."
  type        = string
}

variable "eks_node_instance_type" {
  description = "The EC2 instance type for EKS worker nodes."
  type        = string
}

variable "eks_min_nodes" {
  description = "Minimum number of EKS worker nodes."
  type        = number
}

variable "eks_max_nodes" {
  description = "Maximum number of EKS worker nodes."
  type        = number
}

variable "eks_desired_nodes" {
  description = "Desired number of EKS worker nodes."
  type        = number
}

# RDS Module Variables
variable "rds_instance_class" {
  description = "The instance class for the RDS PostgreSQL database."
  type        = string
}

variable "rds_allocated_storage" {
  description = "Allocated storage in GB for the RDS instance."
  type        = number
}

variable "rds_multi_az" {
  description = "Flag to enable Multi-AZ deployment for RDS. Per REQ-1-502, must be true for prod."
  type        = bool
}

variable "rds_backup_retention_period" {
  description = "The number of days to retain backups for. Per REQ-1-502, must be > 0 to enable PITR."
  type        = number
}

# S3 Module Variables
variable "s3_attachments_bucket_name" {
  description = "The name of the S3 bucket for storing file attachments."
  type        = string
}

# ElastiCache (Redis) Module Variables
variable "redis_node_type" {
  description = "The node type for the Redis cluster."
  type        = string
}

variable "redis_num_nodes" {
  description = "The number of nodes in the Redis cluster."
  type        = number
}

# MQ (RabbitMQ) Module Variables
variable "mq_broker_instance_type" {
  description = "The instance type for the RabbitMQ broker."
  type        = string
}

variable "mq_deployment_mode" {
  description = "The deployment mode for RabbitMQ (SINGLE_INSTANCE or CLUSTER_MULTI_AZ)."
  type        = string
}

# API Gateway Module Variables
variable "api_gateway_stage_name" {
  description = "The stage name for the API Gateway deployment."
  type        = string
}

variable "api_gateway_enable_data_tracing" {
  description = "Flag to enable detailed API tracing in CloudWatch."
  type        = bool
}

# Secrets Module Variables
variable "db_master_username" {
  description = "The master username for the RDS database."
  type        = string
}

variable "mq_master_username" {
  description = "The master username for the RabbitMQ broker."
  type        = string
}

# Timestream Module Variables
variable "timestream_db_name" {
  description = "The name of the Timestream database for GPS data."
  type        = string
}

variable "timestream_table_name" {
  description = "The name of the Timestream table for GPS data."
  type        = string
}

# Monitoring Module Variables
variable "opensearch_domain_name" {
  description = "The name of the Amazon OpenSearch domain for logs."
  type        = string
}

variable "opensearch_instance_type" {
  description = "The instance type for OpenSearch data nodes."
  type        = string
}

variable "opensearch_instance_count" {
  description = "The number of data nodes in the OpenSearch cluster."
  type        = number
}