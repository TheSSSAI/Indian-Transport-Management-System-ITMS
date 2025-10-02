# .tflint.hcl
# This file configures the TFLint linter for Terraform.

config {
  # Enable the AWS ruleset and set it as the default
  plugin "aws" {
    enabled = true
    version = "0.28.0"
    source  = "github.com/terraform-linters/tflint-ruleset-aws"
  }

  # Set default severity for issues. Can be "error", "warning", or "info".
  # Setting to "error" will cause pre-commit hooks and CI/CD pipelines to fail.
  force = false
  # You can also configure specific rules here if needed, for example:
  # rule "aws_instance_invalid_type" {
  #   enabled = true
  # }
}