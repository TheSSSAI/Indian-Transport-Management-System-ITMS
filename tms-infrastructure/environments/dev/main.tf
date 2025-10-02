# /environments/dev/main.tf

# -----------------------------------------------------------------------------
# TMS DEVELOPMENT ENVIRONMENT - COMPOSITION ROOT
# -----------------------------------------------------------------------------
# This file defines the 'dev' environment by composing the reusable infrastructure
# modules from the /modules directory. It passes environment-specific variables
# (defined in terraform.tfvars) to configure the infrastructure for development
# purposes, prioritizing cost-effectiveness over high availability.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Module: Network
# Purpose: Provisions the foundational VPC, subnets, and routing for the dev env.
# -----------------------------------------------------------------------------
module "network" {
  source = "../../modules/network"

  vpc_cidr_block      = var.vpc_cidr_block
  availability_zones  = var.availability_zones
  environment         = var.environment
  project             = var.project
  common_tags         = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: S3
# Purpose: Provisions S3 buckets for application attachments and other storage.
# -----------------------------------------------------------------------------
module "s3" {
  source = "../../modules/s3"

  attachments_bucket_name = "${var.project}-${var.environment}-attachments"
  environment             = var.environment
  project                 = var.project
  common_tags             = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: Secrets
# Purpose: Manages AWS Secrets Manager secrets for various services.
# -----------------------------------------------------------------------------
module "secrets" {
  source = "../../modules/secrets"

  rds_master_password_secret_name = "${var.project}-${var.environment}-rds-master-password"
  mq_master_password_secret_name  = "${var.project}-${var.environment}-mq-master-password"
  mq_master_user                  = var.mq_master_user
  environment                     = var.environment
  project                         = var.project
  common_tags                     = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: EKS (Elastic Kubernetes Service)
# Purpose: Provisions the Kubernetes cluster for running containerized applications.
# -----------------------------------------------------------------------------
module "eks" {
  source = "../../modules/eks"

  cluster_name          = "${var.project}-${var.environment}-cluster"
  cluster_version       = var.eks_cluster_version
  vpc_id                = module.network.vpc_id
  private_subnet_ids    = module.network.private_subnet_ids
  node_instance_type    = var.eks_node_instance_type
  node_min_size         = var.eks_node_min_size
  node_desired_size     = var.eks_node_desired_size
  node_max_size         = var.eks_node_max_size
  environment           = var.environment
  project               = var.project
  common_tags           = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: Security
# Purpose: Provisions IAM roles, policies, and security groups.
# Depends on Network (for VPC) and EKS (for OIDC provider URL).
# -----------------------------------------------------------------------------
module "security" {
  source = "../../modules/security"

  vpc_id                         = module.network.vpc_id
  eks_cluster_name               = module.eks.cluster_name
  eks_cluster_oidc_issuer_url    = module.eks.cluster_oidc_issuer_url
  eks_cluster_oidc_provider_arn  = module.eks.cluster_oidc_provider_arn
  attachments_s3_bucket_arn      = module.s3.attachments_bucket_arn
  rds_master_password_secret_arn = module.secrets.rds_master_password_secret_arn
  mq_master_password_secret_arn  = module.secrets.mq_master_password_secret_arn
  environment                    = var.environment
  project                        = var.project
  common_tags                    = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: RDS (Relational Database Service)
# Purpose: Provisions the PostgreSQL 16 database.
# -----------------------------------------------------------------------------
module "rds" {
  source = "../../modules/rds"

  db_identifier               = "${var.project}-${var.environment}-db"
  db_name                     = var.rds_db_name
  db_username                 = var.rds_db_username
  db_instance_class           = var.rds_instance_class
  db_allocated_storage        = var.rds_allocated_storage
  db_engine_version           = var.rds_engine_version
  db_multi_az                 = var.rds_multi_az # false for dev
  db_backup_retention_period  = var.rds_backup_retention_period
  db_subnet_ids               = module.network.private_subnet_ids
  db_vpc_security_group_ids   = [module.security.rds_sg_id]
  db_master_password_secret_arn = module.secrets.rds_master_password_secret_arn
  environment                 = var.environment
  project                     = var.project
  common_tags                 = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: ElastiCache (Redis)
# Purpose: Provisions the Redis cluster for caching.
# -----------------------------------------------------------------------------
module "elasticache" {
  source = "../../modules/elasticache"

  cluster_id                = "${var.project}-${var.environment}-redis"
  node_type                 = var.redis_node_type
  num_cache_nodes           = var.redis_num_cache_nodes # 1 for dev
  engine_version            = var.redis_engine_version
  subnet_ids                = module.network.private_subnet_ids
  vpc_security_group_ids    = [module.security.elasticache_sg_id]
  environment               = var.environment
  project                   = var.project
  common_tags               = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: MQ (RabbitMQ)
# Purpose: Provisions the RabbitMQ message broker.
# -----------------------------------------------------------------------------
module "mq" {
  source = "../../modules/mq"

  broker_name                   = "${var.project}-${var.environment}-broker"
  broker_instance_type          = var.mq_instance_type
  broker_deployment_mode        = var.mq_deployment_mode # SINGLE_INSTANCE for dev
  broker_engine_version         = var.mq_engine_version
  broker_master_user            = var.mq_master_user
  broker_master_password_secret_arn = module.secrets.mq_master_password_secret_arn
  broker_subnet_ids             = module.network.private_subnet_ids
  broker_security_group_ids     = [module.security.mq_sg_id]
  environment                   = var.environment
  project                       = var.project
  common_tags                   = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: Timestream
# Purpose: Provisions the Timestream database for high-volume GPS data.
# -----------------------------------------------------------------------------
module "timestream" {
  source = "../../modules/timestream"

  database_name           = "${var.project}_${var.environment}_telemetry"
  vehicle_location_table_name = "vehicle_locations"
  geofence_event_table_name   = "geofence_events"
  memory_store_retention_hours = 24 * 7 # 7 days
  magnetic_store_retention_days = 365 # 1 year
  environment                 = var.environment
  project                     = var.project
  common_tags                 = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: Monitoring
# Purpose: Provisions the monitoring stack (OpenSearch, Managed Prometheus, etc.).
# -----------------------------------------------------------------------------
module "monitoring" {
  source = "../../modules/monitoring"

  opensearch_domain_name  = "${var.project}-${var.environment}-logs"
  opensearch_instance_type = var.opensearch_instance_type
  opensearch_instance_count = var.opensearch_instance_count
  vpc_id                  = module.network.vpc_id
  subnet_ids              = module.network.private_subnet_ids
  security_group_ids      = [module.security.monitoring_sg_id]
  environment             = var.environment
  project                 = var.project
  common_tags             = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: API Gateway
# Purpose: Provisions the API Gateway for the GPS microservice.
# -----------------------------------------------------------------------------
module "api_gateway" {
  source = "../../modules/api_gateway"

  api_name        = "${var.project}-${var.environment}-gps-api"
  stage_name      = var.environment
  environment     = var.environment
  project         = var.project
  common_tags     = var.common_tags
  
  # Note: The actual integration with the EKS service will be configured
  # via Kubernetes resources (Ingress) and not directly here. This module
  # sets up the gateway, custom domain, and basic configuration.
}