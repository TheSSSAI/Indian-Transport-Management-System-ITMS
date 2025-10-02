# variables.tf for API Gateway Module

variable "project_name" {
  description = "The name of the project, used for naming and tagging resources."
  type        = string
}

variable "environment" {
  description = "The deployment environment (e.g., 'dev', 'staging', 'prod')."
  type        = string
}

variable "tags" {
  description = "A map of tags to apply to all resources."
  type        = map(string)
  default     = {}
}

variable "target_nlb_arn" {
  description = "The ARN of the Network Load Balancer that the API Gateway will proxy requests to."
  type        = string
}

variable "nlb_dns_name" {
  description = "The DNS name of the Network Load Balancer. Required for the integration URI."
  type        = string
}

variable "api_stage_name" {
  description = "The name of the API Gateway deployment stage (e.g., 'v1', 'dev')."
  type        = string
  default     = "v1"
}

variable "enable_api_data_tracing" {
  description = "Flag to enable detailed API request/response logging to CloudWatch. Should be false in production for performance and cost reasons."
  type        = bool
  default     = false
}