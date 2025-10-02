# variables.tf in modules/rds
# Defines the input contract for the RDS module.

variable "project_name" {
  description = "The name of the project."
  type        = string
}

variable "environment" {
  description = "The environment name (e.g., dev, staging, prod)."
  type        = string
}

variable "tags" {
  description = "A map of tags to assign to all resources."
  type        = map(string)
  default     = {}
}

variable "db_subnet_ids" {
  description = "A list of private subnet IDs for the DB subnet group."
  type        = list(string)
  validation {
    condition     = length(var.db_subnet_ids) >= 2
    error_message = "At least two subnets in different AZs are required for Multi-AZ RDS."
  }
}

variable "vpc_security_group_id" {
  description = "The ID of the security group to associate with the RDS instance."
  type        = string
}

variable "instance_class" {
  description = "The instance class for the RDS database (e.g., 'db.t4g.medium')."
  type        = string
}

variable "allocated_storage" {
  description = "The initial allocated storage in GB."
  type        = number
  default     = 20
}

variable "storage_type" {
  description = "The storage type for the RDS instance (e.g., 'gp3', 'io1')."
  type        = string
  default     = "gp3"
}

variable "iops" {
  description = "The amount of provisioned IOPS. Only valid for 'io1' storage type."
  type        = number
  default     = 1000
}

variable "master_username" {
  description = "The master username for the database."
  type        = string
  default     = "postgres"
}

variable "master_password_secret_arn" {
  description = "The ARN of the secret in AWS Secrets Manager containing the master password."
  type        = string
}

variable "multi_az" {
  description = "Specifies if the RDS instance is multi-AZ. Required for prod/staging by REQ-1-502."
  type        = bool
  default     = false
}

variable "backup_retention_period" {
  description = "The number of days to retain backups for. Must be > 0 for PITR. Required by REQ-1-502."
  type        = number
  default     = 7
  validation {
    condition     = var.backup_retention_period >= 1
    error_message = "Backup retention period must be at least 1 day to enable Point-In-Time Recovery."
  }
}

variable "delete_automated_backups" {
  description = "Specifies if automated backups are deleted on instance termination. Should be false for prod."
  type        = bool
  default     = true
}

variable "apply_immediately" {
  description = "Specifies whether modifications are applied immediately or during the next maintenance window."
  type        = bool
  default     = true
}