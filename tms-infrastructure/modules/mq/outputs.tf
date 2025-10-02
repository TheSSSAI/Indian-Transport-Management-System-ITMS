# outputs.tf in modules/mq
# Defines the output contract of the Amazon MQ module.

output "broker_id" {
  description = "The ID of the MQ broker."
  value       = aws_mq_broker.main.id
}

output "broker_arn" {
  description = "The ARN of the MQ broker."
  value       = aws_mq_broker.main.arn
}

output "broker_amqp_endpoints" {
  description = "The AMQP endpoints for the RabbitMQ broker."
  value       = [for instance in aws_mq_broker.main.instances : instance.endpoints[0]]
  sensitive   = true
}

output "broker_console_url" {
  description = "The URL of the RabbitMQ Management Console."
  value       = one(aws_mq_broker.main.instances[*].console_url)
}