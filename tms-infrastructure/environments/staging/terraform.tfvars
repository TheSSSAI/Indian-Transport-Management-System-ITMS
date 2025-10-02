# terraform.tfvars for the 'staging' environment
# Provides values that mirror production architecture but at a reduced scale for UAT and pre-prod testing.

# General
project_name = "tms"
aws_region   = "ap-south-1"

# Network
vpc_cidr             = "10.20.0.0/16"
public_subnets_cidr  = ["10.20.1.0/24", "10.20.2.0/24"]
private_subnets_cidr = ["10.20.10.0/24", "10.20.11.0/24"]

# EKS
eks_cluster_version    = "1.28"
eks_node_instance_type = "t3.large"
eks_min_nodes          = 2
eks_max_nodes          = 5
eks_desired_nodes      = 2

# RDS (PostgreSQL 16)
rds_instance_class          = "db.t3.medium"
rds_allocated_storage       = 100
rds_multi_az                = true # Mirror production HA setup per REQ-1-502
rds_backup_retention_period = 14   # Enable PITR with longer retention

# S3
s3_attachments_bucket_name = "tms-staging-attachments-bucket-unique-name"

# ElastiCache (Redis)
redis_node_type = "cache.t3.small"
redis_num_nodes = 2 # Multi-AZ for staging

# MQ (RabbitMQ)
mq_broker_instance_type = "mq.t3.micro"
mq_deployment_mode      = "CLUSTER_MULTI_AZ" # Mirror production HA setup

# API Gateway
api_gateway_stage_name          = "staging"
api_gateway_enable_data_tracing = true # Enable for staging debugging

# Secrets
db_master_username = "tmsadmin"
mq_master_username = "tmsmqadmin"

# Timestream
timestream_db_name    = "tms-staging-telemetry"
timestream_table_name = "vehicle_locations"

# Monitoring
opensearch_domain_name    = "tms-staging-logs"
opensearch_instance_type  = "t3.medium.search"
opensearch_instance_count = 2