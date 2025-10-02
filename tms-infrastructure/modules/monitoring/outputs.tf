# outputs.tf in modules/monitoring
# Defines the output contract of the monitoring module.

output "opensearch_domain_endpoint" {
  description = "The endpoint for the OpenSearch domain."
  value       = aws_opensearch_domain.main.endpoint
}

output "opensearch_domain_arn" {
  description = "The ARN of the OpenSearch domain."
  value       = aws_opensearch_domain.main.arn
}

output "prometheus_workspace_id" {
  description = "The ID of the AWS Managed Prometheus workspace."
  value       = aws_prometheus_workspace.main.id
}

output "prometheus_workspace_endpoint" {
  description = "The endpoint of the AWS Managed Prometheus workspace."
  value       = aws_prometheus_workspace.main.prometheus_endpoint
}

output "grafana_workspace_id" {
  description = "The ID of the AWS Managed Grafana workspace."
  value       = aws_grafana_workspace.main.id
}

output "grafana_workspace_endpoint" {
  description = "The endpoint of the AWS Managed Grafana workspace."
  value       = aws_grafana_workspace.main.endpoint
}