output "replication_group_id" {
  description = "The ID of the ElastiCache replication group."
  value       = aws_elasticache_replication_group.tms_redis.id
}

output "primary_endpoint_address" {
  description = "The connection endpoint for the primary Redis node in the replication group."
  value       = aws_elasticache_replication_group.tms_redis.primary_endpoint_address
}

output "auth_token_secret_arn" {
  description = "The ARN of the secret in AWS Secrets Manager that stores the Redis AUTH token."
  value       = aws_secretsmanager_secret.redis_auth_token.arn
  sensitive   = true
}