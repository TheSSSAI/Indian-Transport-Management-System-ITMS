variable "secret_name" {
  description = "The name of the secret to be created in AWS Secrets Manager."
  type        = string
}

variable "secret_string" {
  description = "The value of the secret. If not provided, a random password will be generated."
  type        = string
  default     = null
  sensitive   = true
}

variable "random_password_length" {
  description = "The length of the random password to generate if secret_string is not provided."
  type        = number
  default     = 32
}

variable "kms_key_id" {
  description = "The ARN of the KMS key to use for encrypting the secret. If not specified, a default AWS-managed key is used."
  type        = string
  default     = null
}

variable "recovery_window_in_days" {
  description = "The number of days that Secrets Manager waits before it can permanently delete this secret. 0 means immediate deletion."
  type        = number
  default     = 7
  validation {
    condition     = var.recovery_window_in_days >= 0 && var.recovery_window_in_days <= 30
    error_message = "The recovery window must be between 0 and 30 days."
  }
}

variable "tags" {
  description = "A map of tags to assign to the secret."
  type        = map(string)
  default     = {}
}