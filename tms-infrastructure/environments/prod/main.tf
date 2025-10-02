# /environments/prod/main.tf

# -----------------------------------------------------------------------------
# TMS PRODUCTION ENVIRONMENT - COMPOSITION ROOT
# -----------------------------------------------------------------------------
# This file defines the 'prod' environment, the live system for end-users.
# It is configured for maximum availability, resilience, and performance,
# strictly adhering to all NFRs including REQ-1-502 (99.9% uptime, Multi-AZ)
# and REQ-1-503 (Security).
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Module: Network
# Purpose: Provisions the foundational VPC, subnets, and routing for production.
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
# Purpose: Provisions the high-availability Kubernetes cluster for production.
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
# Purpose: Provisions the HA PostgreSQL 16 database for production.
# -----------------------------------------------------------------------------
module "rds" {
  source = "../../modules/rds"

  db_identifier               = "${var.project}-${var.environment}-db"
  db_name                     = var.rds_db_name
  db_username                 = var.rds_db_username
  db_instance_class           = var.rds_instance_class
  db_allocated_storage        = var.rds_allocated_storage
  db_engine_version           = var.rds_engine_version
  db_multi_az                 = var.rds_multi_az # true for production
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
# Purpose: Provisions the HA Redis cluster for caching.
# -----------------------------------------------------------------------------
module "elasticache" {
  source = "../../modules/elasticache"

  cluster_id                = "${var.project}-${var.environment}-redis"
  node_type                 = var.redis_node_type
  num_cache_nodes           = var.redis_num_cache_nodes # >= 2 for production HA
  engine_version            = var.redis_engine_version
  subnet_ids                = module.network.private_subnet_ids
  vpc_security_group_ids    = [module.security.elasticache_sg_id]
  environment               = var.environment
  project                   = var.project
  common_tags               = var.common_tags
}

# -----------------------------------------------------------------------------
# Module: MQ (RabbitMQ)
# Purpose: Provisions the HA RabbitMQ message broker.
# -----------------------------------------------------------------------------
module "mq" {
  source = "../../modules/mq"

  broker_name                   = "${var.project}-${var.environment}-broker"
  broker_instance_type          = var.mq_instance_type
  broker_deployment_mode        = var.mq_deployment_mode # CLUSTER_MULTI_AZ for production
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
  magnetic_store_retention_days = 365 * 2 # 2 years for prod
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
}