# variables.tf in modules/mq
# Defines the input contract for the Amazon MQ module.

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
  description = "A list of private subnet IDs for the MQ broker."
  type        = list(string)
}

variable "vpc_security_group_id" {
  description = "The ID of the security group to associate with the MQ broker."
  type        = string
}

variable "broker_instance_type" {
  description = "The instance type for the MQ broker (e.g., 'mq.t3.micro')."
  type        = string
  default     = "mq.t3.micro"
}

variable "broker_engine_version" {
  description = "The RabbitMQ engine version."
  type        = string
  default     = "3.11.28"
}

variable "multi_az" {
  description = "Specifies if the MQ broker is multi-AZ. Required for prod/staging by REQ-1-502."
  type        = bool
  default     = false
}

variable "mq_username_secret_arn" {
  description = "The ARN of the secret in AWS Secrets Manager containing the MQ master username."
  type        = string
}

variable "mq_password_secret_arn" {
  description = "The ARN of the secret in AWS Secrets Manager containing the MQ master password."
  type        = string
}