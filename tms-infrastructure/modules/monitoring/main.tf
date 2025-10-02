# main.tf in modules/monitoring
# Provisions the monitoring and logging stack (OpenSearch, Prometheus, Grafana).
# Aligns with REQ-1-602.

# Amazon OpenSearch Service Domain for logging
resource "aws_opensearch_domain" "main" {
  domain_name    = "${var.project_name}-${var.environment}-logs"
  engine_version = "OpenSearch_2.11"

  cluster_config {
    instance_type          = var.opensearch_instance_type
    instance_count         = var.opensearch_instance_count
    dedicated_master_enabled = var.opensearch_instance_count >= 3
    zone_awareness_enabled = var.opensearch_instance_count >= 2
    zone_awareness_config {
      availability_zone_count = var.opensearch_instance_count >= 2 ? 2 : 1
    }
  }

  vpc_options {
    subnet_ids         = var.private_subnet_ids
    security_group_ids = [var.opensearch_security_group_id]
  }

  ebs_options {
    ebs_enabled = true
    volume_size = var.opensearch_volume_size
    volume_type = "gp3"
  }

  domain_endpoint_options {
    enforce_https = true
    tls_security_policy = "Policy-Min-TLS-1-2-2019-07"
  }

  encrypt_at_rest {
    enabled = true
  }

  node_to_node_encryption {
    enabled = true
  }

  access_policies = data.aws_iam_policy_document.opensearch_access_policy.json

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-logs"
  })
}

# Access policy for OpenSearch domain
data "aws_iam_policy_document" "opensearch_access_policy" {
  statement {
    effect = "Allow"
    principals {
      type        = "AWS"
      identifiers = ["*"]
    }
    actions = [
      "es:ESHttp*",
    ]
    resources = [
      "${aws_opensearch_domain.main.arn}/*",
    ]
    condition {
      test     = "IpAddress"
      variable = "aws:SourceIp"
      values   = var.vpc_cidr_blocks
    }
  }
  statement {
    effect = "Allow"
    principals {
      type        = "AWS"
      identifiers = var.opensearch_writer_iam_role_arns
    }
    actions = [
      "es:ESHttp*",
    ]
    resources = [
      "${aws_opensearch_domain.main.arn}/*",
    ]
  }
}

# AWS Managed Service for Prometheus (AMP)
resource "aws_prometheus_workspace" "main" {
  alias = "${var.project_name}-${var.environment}-metrics"
  tags  = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-metrics"
  })
}

# AWS Managed Service for Grafana
resource "aws_grafana_workspace" "main" {
  account_access_type      = "CURRENT_ACCOUNT"
  authentication_providers = ["AWS_SSO"]
  permission_type          = "SERVICE_MANAGED"
  role_arn                 = var.grafana_iam_role_arn
  name                     = "${var.project_name}-${var.environment}-dashboard"
  
  vpc_configuration {
    security_group_ids = [var.grafana_security_group_id]
    subnet_ids         = var.private_subnet_ids
  }
  
  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-dashboard"
  })
}

# Configure Grafana data sources
resource "aws_grafana_workspace_api_key" "main" {
  key_name         = "terraform-key"
  key_role         = "ADMIN"
  seconds_to_live  = 3600
  workspace_id     = aws_grafana_workspace.main.id
}

# This part would typically be handled by a Grafana provider, but for simplicity,
# we are only provisioning the workspace. The data source configuration would be done
# post-provisioning via Grafana's API or UI.
# The IAM role for Grafana (var.grafana_iam_role_arn) should have policies to read
# from the Prometheus workspace and OpenSearch domain.