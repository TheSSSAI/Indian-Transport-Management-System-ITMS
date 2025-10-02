variable "project_name" {
  description = "The name of the project."
  type        = string
}

variable "environment" {
  description = "The environment name (e.g., 'dev', 'staging', 'prod')."
  type        = string
}

variable "private_subnet_ids" {
  description = "A list of private subnet IDs where the ElastiCache nodes will be deployed."
  type        = list(string)
}

variable "security_group_id" {
  description = "The ID of the security group to associate with the ElastiCache cluster."
  type        = string
}

variable "cluster_id" {
  description = "A unique identifier for the ElastiCache replication group."
  type        = string
  default     = "tms-redis-cluster"
}

variable "node_type" {
  description = "The instance type for the Redis cache nodes (e.g., 'cache.t3.small')."
  type        = string
  default     = "cache.t3.small"
}

variable "num_cache_nodes" {
  description = "The number of cache nodes in the Redis replication group. Should be >= 2 for Multi-AZ."
  type        = number
  default     = 2
}

variable "redis_version" {
  description = "The version of the Redis engine to use."
  type        = string
  default     = "7.0"
}

variable "multi_az_enabled" {
  description = "Flag to enable Multi-AZ with automatic failover for high availability (REQ-1-502)."
  type        = bool
  default     = false
}

variable "tags" {
  description = "A map of tags to apply to all resources."
  type        = map(string)
  default     = {}
}