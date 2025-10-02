output "database_name" {
  description = "The name of the Timestream database."
  value       = aws_timestreamwrite_database.main.database_name
}

output "database_arn" {
  description = "The ARN of the Timestream database."
  value       = aws_timestreamwrite_database.main.arn
}

output "table_name" {
  description = "The name of the Timestream table."
  value       = aws_timestreamwrite_table.main.table_name
}

output "table_arn" {
  description = "The ARN of the Timestream table."
  value       = aws_timestreamwrite_table.main.arn
}