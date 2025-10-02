terraform {
  backend "s3" {
    # These values will be dynamically configured during CI/CD initialization.
    # The key will be set to something like "environments/dev/terraform.tfstate"
    # to maintain state isolation per environment.
    # Example configuration (do not uncomment):
    # bucket         = "tms-terraform-state-backend-bucket"
    # key            = "path/to/my/key"
    # region         = "ap-south-1"
    # dynamodb_table = "tms-terraform-state-lock-table"
    # encrypt        = true
  }
}