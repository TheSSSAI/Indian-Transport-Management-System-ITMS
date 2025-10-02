# terraform.tfvars for the 'prod' environment
# Provides production-grade, highly-available, and performant values for all variables.

# General
project_name = "tms"
aws_region   = "ap-south-1"

# Network
vpc_cidr             = "10.30.0.0/16"
public_subnets_cidr  = ["10.30.1.0/24", "10.30.2.0/24", "10.30.3.0/24"] # 3 AZs for HA
private_subnets_cidr = ["10.30.10.0/24", "10.30.11.0/24", "10.30.12.0/24"] # 3 AZs for HA

# EKS
eks_cluster_version    = "1.28"
eks_node_instance_type = "m5.large" # General purpose production instances
eks_min_nodes          = 3
eks_max_nodes          = 10
eks_desired_nodes      = 3

# RDS (PostgreSQL 16)
rds_instance_class          = "db.m5.large" # Production-grade instance
rds_allocated_storage       = 200
rds_multi_az                = true # Mandatory for production HA per REQ-1-502
rds_backup_retention_period = 30   # Long retention for production DR

# S3
s3_attachments_bucket_name = "tms-prod-attachments-bucket-unique-name"

# ElastiCache (Redis)
redis_node_type = "cache.m5.large"
redis_num_nodes = 2 # Multi-AZ for high availability

# MQ (RabbitMQ)
mq_broker_instance_type = "mq.m5.large"
mq_deployment_mode      = "CLUSTER_MULTI_AZ" # Mandatory for production HA

# API Gateway
api_gateway_stage_name          = "prod"
api_gateway_enable_data_tracing = false # Disable for performance and cost in production

# Secrets
db_master_username = "tmsadmin"
mq_master_username = "tmsmqadmin"

# Timestream
timestream_db_name    = "tms-prod-telemetry"
timestream_table_name = "vehicle_locations"

# Monitoring
opensearch_domain_name    = "tms-prod-logs"
opensearch_instance_type  = "m6g.large.search" # Graviton instances for cost-performance
opensearch_instance_count = 3 # HA setup for logging