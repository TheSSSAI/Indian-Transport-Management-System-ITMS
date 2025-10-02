output "secret_id" {
  description = "The ID of the secret."
  value       = aws_secretsmanager_secret.main.id
}

output "secret_arn" {
  description = "The ARN of the secret."
  value       = aws_secretsmanager_secret.main.arn
}

output "secret_version_id" {
  description = "The version ID of the secret."
  value       = aws_secretsmanager_secret_version.main.version_id
}