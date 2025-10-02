# outputs.tf in modules/rds
# Defines the output contract of the RDS module.

output "instance_endpoint" {
  description = "The connection endpoint for the RDS instance."
  value       = aws_db_instance.main.endpoint
}

output "instance_address" {
  description = "The address of the RDS instance."
  value       = aws_db_instance.main.address
}

output "instance_port" {
  description = "The port of the RDS instance."
  value       = aws_db_instance.main.port
}

output "instance_arn" {
  description = "The ARN of the RDS instance."
  value       = aws_db_instance.main.arn
}

output "master_username" {
  description = "The master username for the database."
  value       = aws_db_instance.main.username
}

output "master_password_secret_arn" {
  description = "The ARN of the secret in AWS Secrets Manager containing the master password."
  value       = var.master_password_secret_arn
}