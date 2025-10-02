# variables.tf in modules/monitoring
# Defines the input contract for the monitoring module.

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

variable "private_subnet_ids" {
  description = "A list of private subnet IDs for deploying monitoring services."
  type        = list(string)
}

variable "vpc_cidr_blocks" {
  description = "List of CIDR blocks for the VPC to allow in OpenSearch access policy."
  type        = list(string)
}

variable "opensearch_security_group_id" {
  description = "The ID of the security group for the OpenSearch domain."
  type        = string
}

variable "grafana_security_group_id" {
  description = "The ID of the security group for the Grafana workspace."
  type        = string
}

variable "opensearch_instance_type" {
  description = "The instance type for OpenSearch data nodes."
  type        = string
  default     = "t3.small.search"
}

variable "opensearch_instance_count" {
  description = "The number of data nodes for the OpenSearch cluster."
  type        = number
  default     = 2
}

variable "opensearch_volume_size" {
  description = "The size in GB for the EBS volume attached to each OpenSearch data node."
  type        = number
  default     = 10
}

variable "opensearch_writer_iam_role_arns" {
  description = "A list of IAM Role ARNs that are allowed to write to the OpenSearch domain (e.g., Fluentbit's role)."
  type        = list(string)
  default     = []
}

variable "grafana_iam_role_arn" {
  description = "The ARN of the IAM role for the Grafana workspace to access data sources."
  type        = string
}