variable "database_name" {
  description = "The name of the Timestream database."
  type        = string
}

variable "table_name" {
  description = "The name of the Timestream table."
  type        = string
}

variable "memory_retention_hours" {
  description = "The duration for which data must be stored in the memory store."
  type        = number
  default     = 24
}

variable "magnetic_retention_days" {
  description = "The duration for which data must be stored in the magnetic store."
  type        = number
  default     = 365
}

variable "kms_key_id" {
  description = "The ARN of the KMS key to use for encrypting the database. If not specified, a default AWS-managed key is used."
  type        = string
  default     = null
}

variable "tags" {
  description = "A map of tags to assign to the resources."
  type        = map(string)
  default     = {}
}