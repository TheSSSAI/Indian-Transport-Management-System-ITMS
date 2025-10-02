# outputs.tf for API Gateway Module

output "api_gateway_id" {
  description = "The ID of the created API Gateway REST API."
  value       = aws_api_gateway_rest_api.tms_api.id
}

output "api_gateway_execution_arn" {
  description = "The execution ARN of the API Gateway, used for invoking it from other AWS services."
  value       = aws_api_gateway_rest_api.tms_api.execution_arn
}

output "api_gateway_invoke_url" {
  description = "The public URL to invoke the API Gateway stage. This is the main endpoint for clients."
  value       = aws_api_gateway_stage.tms_api_stage.invoke_url
}

output "vpc_link_id" {
  description = "The ID of the VPC Link used to connect to the backend NLB."
  value       = aws_api_gateway_vpc_link.tms_vpc_link.id
}