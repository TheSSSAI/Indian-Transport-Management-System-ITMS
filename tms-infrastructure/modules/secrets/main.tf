locals {
  is_random_password = var.secret_string == null
}

resource "random_password" "generated" {
  count = local.is_random_password ? 1 : 0

  length           = var.random_password_length
  special          = true
  override_special = "!@#$%&*()-_=+[]{}<>:?"
}

resource "aws_secretsmanager_secret" "main" {
  name       = var.secret_name
  kms_key_id = var.kms_key_id
  
  recovery_window_in_days = var.recovery_window_in_days

  tags = var.tags
}

resource "aws_secretsmanager_secret_version" "main" {
  secret_id     = aws_secretsmanager_secret.main.id
  secret_string = local.is_random_password ? random_password.generated[0].result : var.secret_string
  
  lifecycle {
    ignore_changes = [secret_string]
  }
}