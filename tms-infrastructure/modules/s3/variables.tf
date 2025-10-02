variable "bucket_name" {
  description = "The name of the S3 bucket. Must be globally unique."
  type        = string
}

variable "enable_versioning" {
  description = "A boolean flag to enable/disable versioning of the S3 bucket."
  type        = bool
  default     = true
}

variable "log_bucket_name" {
  description = "The name of the S3 bucket to send access logs to. If empty, logging is disabled."
  type        = string
  default     = ""
}

variable "enable_lifecycle_policy" {
  description = "A boolean flag to enable/disable the default lifecycle policy."
  type        = bool
  default     = false
}

variable "tags" {
  description = "A map of tags to assign to the bucket."
  type        = map(string)
  default     = {}
}