provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Project     = "tms"
      ManagedBy   = "Terraform"
      Environment = var.environment
    }
  }
}