# main.tf for API Gateway Module
# This module creates an AWS API Gateway with a VPC Link integration to proxy requests
# to a private Network Load Balancer (NLB), typically fronting a service in EKS.
# It aligns with REQ-1-400, REQ-1-402, and the microservice architecture REQ-1-013.

resource "aws_api_gateway_rest_api" "tms_api" {
  name        = "${var.project_name}-${var.environment}-gps-gateway"
  description = "API Gateway for the TMS GPS Ingestion Microservice"

  endpoint_configuration {
    types = ["REGIONAL"]
  }

  tags = merge(
    var.tags,
    {
      "Name" = "${var.project_name}-${var.environment}-gps-gateway"
    }
  )
}

# VPC Link to securely connect API Gateway to resources in the VPC (like an NLB)
resource "aws_api_gateway_vpc_link" "tms_vpc_link" {
  name        = "${var.project_name}-${var.environment}-gps-nlb-link"
  description = "VPC Link to the NLB for the GPS microservice"
  target_arns = [var.target_nlb_arn]

  tags = merge(
    var.tags,
    {
      "Name" = "${var.project_name}-${var.environment}-gps-nlb-link"
    }
  )
}

# Define the resource path, e.g., /location
resource "aws_api_gateway_resource" "location_resource" {
  rest_api_id = aws_api_gateway_rest_api.tms_api.id
  parent_id   = aws_api_gateway_rest_api.tms_api.root_resource_id
  path_part   = "location"
}

# Define the method for the resource, e.g., POST /location
resource "aws_api_gateway_method" "post_location" {
  rest_api_id   = aws_api_gateway_rest_api.tms_api.id
  resource_id   = aws_api_gateway_resource.location_resource.id
  http_method   = "POST"
  authorization = "NONE" # Assuming authentication is handled by the service or a custom authorizer
}

# Define the integration between the method and the backend (NLB via VPC Link)
resource "aws_api_gateway_integration" "post_location_integration" {
  rest_api_id = aws_api_gateway_rest_api.tms_api.id
  resource_id = aws_api_gateway_resource.location_resource.id
  http_method = aws_api_gateway_method.post_location.http_method

  type                    = "HTTP_PROXY"
  integration_http_method = "POST"
  uri                     = "http://${var.nlb_dns_name}/location" # The NLB listener must be HTTP
  connection_type         = "VPC_LINK"
  connection_id           = aws_api_gateway_vpc_link.tms_vpc_link.id

  # Passthrough behavior ensures the request is forwarded as-is to the backend.
  request_parameters = {
    "integration.request.header.Content-Type" = "'application/json'"
  }
}

# A deployment is required to make the API callable
resource "aws_api_gateway_deployment" "tms_api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.tms_api.id

  # This ensures a new deployment is triggered when the API structure changes.
  triggers = {
    redeployment = sha1(jsonencode([
      aws_api_gateway_resource.location_resource.id,
      aws_api_gateway_method.post_location.id,
      aws_api_gateway_integration.post_location_integration.id,
    ]))
  }

  lifecycle {
    create_before_destroy = true
  }
}

# A stage represents a snapshot of the deployment, e.g., 'v1'
resource "aws_api_gateway_stage" "tms_api_stage" {
  deployment_id = aws_api_gateway_deployment.tms_api_deployment.id
  rest_api_id   = aws_api_gateway_rest_api.tms_api.id
  stage_name    = var.api_stage_name
}

# Configure CloudWatch logging for the API Gateway stage for monitoring and auditing.
resource "aws_api_gateway_method_settings" "all" {
  rest_api_id = aws_api_gateway_rest_api.tms_api.id
  stage_name  = aws_api_gateway_stage.tms_api_stage.stage_name
  method_path = "*/*"

  settings {
    metrics_enabled = true
    logging_level   = "INFO"
    data_trace_enabled = var.enable_api_data_tracing
  }
}

# IAM role for API Gateway to write logs to CloudWatch
resource "aws_iam_role" "api_gateway_cloudwatch_role" {
  name = "${var.project_name}-${var.environment}-api-gateway-cw-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "",
      "Effect": "Allow",
      "Principal": {
        "Service": "apigateway.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}

resource "aws_iam_role_policy" "api_gateway_cloudwatch_policy" {
  name = "${var.project_name}-${var.environment}-api-gateway-cw-policy"
  role = aws_iam_role.api_gateway_cloudwatch_role.id

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:PutLogEvents",
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}

resource "aws_api_gateway_account" "current" {
  cloudwatch_role_arn = aws_iam_role.api_gateway_cloudwatch_role.arn
}