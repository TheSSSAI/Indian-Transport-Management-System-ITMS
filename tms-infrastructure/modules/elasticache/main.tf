# This module provisions a highly available Amazon ElastiCache for Redis cluster.
# It supports Multi-AZ for production environments to meet REQ-1-502.
# It also creates a secret in AWS Secrets Manager to store the Redis AUTH token.

# Create a subnet group for the ElastiCache cluster
resource "aws_elasticache_subnet_group" "tms_redis" {
  name       = "${var.project_name}-${var.environment}-redis-subnet-group"
  subnet_ids = var.private_subnet_ids

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-redis-subnet-group"
  })
}

# Generate a random password for the Redis AUTH token
resource "random_password" "redis_auth_token" {
  length           = 32
  special          = true
  override_special = "!#$%&*()-_=+[]{}<>:?"
}

# Store the Redis AUTH token in AWS Secrets Manager
resource "aws_secretsmanager_secret" "redis_auth_token" {
  name        = "tms/${var.environment}/redis/auth-token"
  description = "Redis AUTH token for the TMS ElastiCache cluster in ${var.environment}."

  tags = merge(var.tags, {
    Name = "tms-${var.environment}-redis-auth-token"
  })
}

resource "aws_secretsmanager_secret_version" "redis_auth_token_version" {
  secret_id     = aws_secretsmanager_secret.redis_auth_token.id
  secret_string = random_password.redis_auth_token.result
}

# Create the ElastiCache for Redis replication group (cluster)
resource "aws_elasticache_replication_group" "tms_redis" {
  replication_group_id          = var.cluster_id
  description                   = "TMS Redis cluster for ${var.environment}"
  node_type                     = var.node_type
  number_cache_clusters         = var.num_cache_nodes # For Multi-AZ, this should be >= 2
  engine                        = "redis"
  engine_version                = var.redis_version
  port                          = 6379
  parameter_group_name          = "default.redis${var.redis_version}"
  subnet_group_name             = aws_elasticache_subnet_group.tms_redis.name
  security_group_ids            = [var.security_group_id]
  automatic_failover_enabled    = var.multi_az_enabled
  multi_az_enabled              = var.multi_az_enabled
  at_rest_encryption_enabled    = true
  transit_encryption_enabled    = true
  auth_token                    = random_password.redis_auth_token.result
  apply_immediately             = true
  auto_minor_version_upgrade    = true
  data_tiering_enabled          = false # Can be enabled for larger clusters to reduce cost

  # Snapshotting for backup and recovery, important for HA/DR (REQ-1-502)
  snapshot_retention_limit = var.multi_az_enabled ? 7 : 1
  snapshot_window          = "04:00-05:00"

  tags = merge(var.tags, {
    Name = var.cluster_id
  })

  lifecycle {
    ignore_changes = [
      # Omit auth_token from lifecycle to prevent Terraform from knowing the secret value after initial creation
      auth_token,
    ]
  }
}