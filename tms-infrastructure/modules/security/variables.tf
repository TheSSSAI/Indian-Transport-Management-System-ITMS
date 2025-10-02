variable "project_name" {
  description = "The name of the project."
  type        = string
}

variable "environment" {
  description = "The environment name (e.g., 'dev', 'staging', 'prod')."
  type        = string
}

variable "aws_region" {
  description = "The AWS region where resources will be created."
  type        = string
}

variable "vpc_id" {
  description = "The ID of the VPC where security groups will be created."
  type        = string
}

variable "vpc_cidr" {
  description = "The CIDR block of the VPC."
  type        = string
}

variable "eks_cluster_oidc_provider_arn" {
  description = "The ARN of the OIDC provider for the EKS cluster, used for IAM Roles for Service Accounts (IRSA)."
  type        = string
}

variable "tms_app_namespace" {
  description = "The Kubernetes namespace where the TMS applications will be deployed."
  type        = string
  default     = "tms"
}

variable "s3_attachments_bucket_arn" {
  description = "The ARN of the S3 bucket used for storing attachments."
  type        = string
}

variable "tags" {
  description = "A map of tags to apply to all resources."
  type        = map(string)
  default     = {}
}