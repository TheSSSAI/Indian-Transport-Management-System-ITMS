# terraform.tfvars for the 'dev' environment
# Provides cost-optimized values for development and testing.

# General
project_name = "tms"
aws_region   = "ap-south-1"

# Network
vpc_cidr             = "10.10.0.0/16"
public_subnets_cidr  = ["10.10.1.0/24", "10.10.2.0/24"]
private_subnets_cidr = ["10.10.10.0/24", "10.10.11.0/24"]

# EKS
eks_cluster_version    = "1.28"
eks_node_instance_type = "t3.medium"
eks_min_nodes          = 1
eks_max_nodes          = 3
eks_desired_nodes      = 1

# RDS (PostgreSQL 16)
rds_instance_class          = "db.t3.small"
rds_allocated_storage       = 20
rds_multi_az                = false # Cost-saving for dev
rds_backup_retention_period = 7     # Enable PITR for dev testing

# S3
s3_attachments_bucket_name = "tms-dev-attachments-bucket-unique-name"

# ElastiCache (Redis)
redis_node_type = "cache.t3.micro"
redis_num_nodes = 1

# MQ (RabbitMQ)
mq_broker_instance_type = "mq.t3.micro"
mq_deployment_mode      = "SINGLE_INSTANCE" # Cost-saving for dev

# API Gateway
api_gateway_stage_name          = "dev"
api_gateway_enable_data_tracing = true # Enable for easier debugging in dev

# Secrets
db_master_username = "tmsadmin"
mq_master_username = "tmsmqadmin"

# Timestream
timestream_db_name    = "tms-dev-telemetry"
timestream_table_name = "vehicle_locations"

# Monitoring
opensearch_domain_name    = "tms-dev-logs"
opensearch_instance_type  = "t3.small.search"
opensearch_instance_count = 1