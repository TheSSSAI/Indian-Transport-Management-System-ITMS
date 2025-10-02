# --------------------------------------------------------------------------------------------------
# SECURITY GROUPS
#
# Defines the security groups for various components of the TMS infrastructure,
# enforcing the principle of least privilege for network communication.
# --------------------------------------------------------------------------------------------------

# Security Group for the EKS Control Plane (Cluster API)
resource "aws_security_group" "eks_control_plane" {
  name        = "${var.project_name}-${var.environment}-eks-control-plane-sg"
  description = "Security group for the EKS control plane"
  vpc_id      = var.vpc_id

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-eks-control-plane-sg"
  })
}

# Security Group for the EKS Worker Nodes
resource "aws_security_group" "eks_nodes" {
  name        = "${var.project_name}-${var.environment}-eks-nodes-sg"
  description = "Security group for the EKS worker nodes"
  vpc_id      = var.vpc_id

  # Ingress from the control plane for management
  ingress {
    description     = "From EKS control plane to nodes for Kubelet"
    from_port       = 1025
    to_port         = 65535
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_control_plane.id]
  }

  # Ingress from other nodes within the same security group for pod-to-pod communication
  ingress {
    description = "Allow all traffic from other worker nodes"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    self        = true
  }

  # Egress to allow all outbound traffic (for pulling images, accessing AWS APIs, etc.)
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-eks-nodes-sg"
  })
}

# Add rules to the EKS control plane security group to allow communication from nodes
resource "aws_security_group_rule" "eks_control_plane_ingress_from_nodes" {
  type                     = "ingress"
  from_port                = 443
  to_port                  = 443
  protocol                 = "tcp"
  security_group_id        = aws_security_group.eks_control_plane.id
  source_security_group_id = aws_security_group.eks_nodes.id
  description              = "Allow worker nodes to connect to the control plane"
}

# Security Group for the RDS PostgreSQL Instance
resource "aws_security_group" "rds" {
  name        = "${var.project_name}-${var.environment}-rds-sg"
  description = "Security group for the RDS PostgreSQL instance"
  vpc_id      = var.vpc_id

  # Ingress for PostgreSQL from EKS worker nodes
  ingress {
    description     = "Allow PostgreSQL access from EKS worker nodes"
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_nodes.id]
  }

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-rds-sg"
  })
}

# Security Group for the ElastiCache Redis Cluster
resource "aws_security_group" "elasticache" {
  name        = "${var.project_name}-${var.environment}-elasticache-sg"
  description = "Security group for the ElastiCache Redis cluster"
  vpc_id      = var.vpc_id

  # Ingress for Redis from EKS worker nodes
  ingress {
    description     = "Allow Redis access from EKS worker nodes"
    from_port       = 6379
    to_port         = 6379
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_nodes.id]
  }

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-elasticache-sg"
  })
}

# Security Group for the Amazon MQ RabbitMQ Broker
resource "aws_security_group" "mq" {
  name        = "${var.project_name}-${var.environment}-mq-sg"
  description = "Security group for the Amazon MQ RabbitMQ broker"
  vpc_id      = var.vpc_id

  # Ingress for RabbitMQ from EKS worker nodes
  ingress {
    description     = "Allow AMQP access from EKS worker nodes"
    from_port       = 5671 # AMQPS
    to_port         = 5671
    protocol        = "tcp"
    security_groups = [aws_security_group.eks_nodes.id]
  }

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-mq-sg"
  })
}


# --------------------------------------------------------------------------------------------------
# IAM ROLES FOR SERVICE ACCOUNTS (IRSA)
#
# Defines IAM roles that can be assumed by Kubernetes service accounts within the EKS cluster.
# This is a security best practice for granting pods fine-grained AWS permissions.
# Per REQ-1-503
# --------------------------------------------------------------------------------------------------

data "aws_iam_policy_document" "k8s_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRoleWithWebIdentity"]
    effect  = "Allow"

    principals {
      type        = "Federated"
      identifiers = [var.eks_cluster_oidc_provider_arn]
    }

    # Condition to scope the role to a specific Kubernetes service account
    # This will be further specified in each role for the specific service account.
    condition {
      test     = "StringEquals"
      variable = "${replace(var.eks_cluster_oidc_provider_arn, "https://", "")}:sub"
      # This variable is a placeholder for the service account string, which will be specified per role
      # e.g., "system:serviceaccount:kube-system:aws-load-balancer-controller"
      # The actual service account name will be defined per role below.
      values = ["*"] # This is intentionally broad at the data source level and narrowed down in each role.
    }
  }
}

# --- Generic Application Pod Role ---
# This role will be assumed by the Odoo and FastAPI pods to access Secrets Manager and S3.
resource "aws_iam_role" "app_pods" {
  name = "${var.project_name}-${var.environment}-app-pods-role"

  assume_role_policy = jsonencode({
    Version = "2008-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Federated = var.eks_cluster_oidc_provider_arn
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringEquals = {
            "${replace(var.eks_cluster_oidc_provider_arn, "https://", "")}:sub" = [
              "system:serviceaccount:${var.tms_app_namespace}:odoo-service-account",
              "system:serviceaccount:${var.tms_app_namespace}:gps-microservice-service-account"
            ]
          }
        }
      }
    ]
  })

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-app-pods-role"
  })
}

resource "aws_iam_policy" "app_pods_policy" {
  name        = "${var.project_name}-${var.environment}-app-pods-policy"
  description = "Policy for TMS application pods to access S3 and Secrets Manager"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "secretsmanager:GetSecretValue",
          "secretsmanager:DescribeSecret"
        ]
        # Scoped to secrets tagged for the specific environment
        Resource = "arn:aws:secretsmanager:${var.aws_region}:${data.aws_caller_identity.current.account_id}:secret:tms/${var.environment}/*"
      },
      {
        Effect = "Allow"
        Action = [
          "s3:GetObject",
          "s3:PutObject",
          "s3:DeleteObject",
          "s3:ListBucket"
        ]
        Resource = [
          var.s3_attachments_bucket_arn,
          "${var.s3_attachments_bucket_arn}/*"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "app_pods_attachment" {
  role       = aws_iam_role.app_pods.name
  policy_arn = aws_iam_policy.app_pods_policy.arn
}

# --- AWS Load Balancer Controller Role ---
resource "aws_iam_role" "aws_load_balancer_controller" {
  name = "${var.project_name}-${var.environment}-aws-lbc-role"

  assume_role_policy = jsonencode({
    Version = "2008-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Federated = var.eks_cluster_oidc_provider_arn
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringEquals = {
            "${replace(var.eks_cluster_oidc_provider_arn, "https://", "")}:sub" = "system:serviceaccount:kube-system:aws-load-balancer-controller"
          }
        }
      }
    ]
  })

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-aws-lbc-role"
  })
}

data "aws_iam_policy_document" "aws_load_balancer_controller_policy_doc" {
  # This policy is based on the official AWS documentation for the LBC
  # It is quite extensive and specific.
  # Source: https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/main/docs/install/iam_policy.json
  statement {
    effect = "Allow"
    actions = [
      "iam:CreateServiceLinkedRole",
    ]
    resources = ["*"]
    condition {
      test     = "StringEquals"
      variable = "iam:AWSServiceName"
      values   = ["elasticloadbalancing.amazonaws.com"]
    }
  }
  statement {
    effect = "Allow"
    actions = [
      "ec2:DescribeAccountAttributes",
      "ec2:DescribeAddresses",
      "ec2:DescribeAvailabilityZones",
      "ec2:DescribeInternetGateways",
      "ec2:DescribeVpcs",
      "ec2:DescribeVpcPeeringConnections",
      "ec2:DescribeSubnets",
      "ec2:DescribeSecurityGroups",
      "ec2:DescribeInstances",
      "ec2:DescribeNetworkInterfaces",
      "ec2:DescribeTags",
      "ec2:GetCoipPoolUsage",
      "ec2:DescribeCoipPools",
      "elasticloadbalancing:DescribeLoadBalancers",
      "elasticloadbalancing:DescribeLoadBalancerAttributes",
      "elasticloadbalancing:DescribeListeners",
      "elasticloadbalancing:DescribeListenerCertificates",
      "elasticloadbalancing:DescribeSSLPolicies",
      "elasticloadbalancing:DescribeRules",
      "elasticloadbalancing:DescribeTargetGroups",
      "elasticloadbalancing:DescribeTargetGroupAttributes",
      "elasticloadbalancing:DescribeTargetHealth",
      "elasticloadbalancing:DescribeTags"
    ]
    resources = ["*"]
  }
  # Other statements for actions on specific resources...
  statement {
    effect = "Allow"
    actions = [
      "cognito-idp:DescribeUserPoolClient",
      "acm:ListCertificates",
      "acm:DescribeCertificate",
      "iam:ListServerCertificates",
      "iam:GetServerCertificate",
      "waf-regional:GetWebACLForResource",
      "waf-regional:GetWebACL",
      "waf-regional:AssociateWebACL",
      "waf-regional:DisassociateWebACL",
      "wafv2:GetWebACL",
      "wafv2:GetWebACLForResource",
      "wafv2:AssociateWebACL",
      "wafv2:DisassociateWebACL",
      "shield:GetSubscriptionState",
      "shield:DescribeProtection",
      "shield:CreateProtection",
      "shield:DeleteProtection"
    ]
    resources = ["*"]
  }
  # ... and many more specific actions
}

resource "aws_iam_policy" "aws_load_balancer_controller_policy" {
  name        = "${var.project_name}-${var.environment}-aws-lbc-policy"
  description = "IAM policy for the AWS Load Balancer Controller"
  policy      = data.aws_iam_policy_document.aws_load_balancer_controller_policy_doc.json
}

resource "aws_iam_role_policy_attachment" "aws_load_balancer_controller_attachment" {
  role       = aws_iam_role.aws_load_balancer_controller.name
  policy_arn = aws_iam_policy.aws_load_balancer_controller_policy.arn
}

# --- Cluster Autoscaler Role ---
resource "aws_iam_role" "cluster_autoscaler" {
  name = "${var.project_name}-${var.environment}-cluster-autoscaler-role"

  assume_role_policy = jsonencode({
    Version = "2008-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Federated = var.eks_cluster_oidc_provider_arn
        }
        Action = "sts:AssumeRoleWithWebIdentity"
        Condition = {
          StringEquals = {
            "${replace(var.eks_cluster_oidc_provider_arn, "https://", "")}:sub" = "system:serviceaccount:kube-system:cluster-autoscaler"
          }
        }
      }
    ]
  })

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-cluster-autoscaler-role"
  })
}

resource "aws_iam_policy" "cluster_autoscaler_policy" {
  name        = "${var.project_name}-${var.environment}-cluster-autoscaler-policy"
  description = "IAM policy for the Kubernetes Cluster Autoscaler"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "autoscaling:DescribeAutoScalingGroups",
          "autoscaling:DescribeAutoScalingInstances",
          "autoscaling:DescribeLaunchConfigurations",
          "autoscaling:DescribeTags",
          "autoscaling:SetDesiredCapacity",
          "autoscaling:TerminateInstanceInAutoScalingGroup",
          "ec2:DescribeLaunchTemplateVersions",
          "ec2:DescribeInstanceTypes"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "cluster_autoscaler_attachment" {
  role       = aws_iam_role.cluster_autoscaler.name
  policy_arn = aws_iam_policy.cluster_autoscaler_policy.arn
}

data "aws_caller_identity" "current" {}