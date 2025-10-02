# outputs.tf in modules/eks
# Defines the output contract of the EKS module, exposing critical identifiers.

output "cluster_name" {
  description = "The name of the EKS cluster."
  value       = aws_eks_cluster.main.name
}

output "cluster_endpoint" {
  description = "The API server endpoint for the EKS cluster."
  value       = aws_eks_cluster.main.endpoint
}

output "cluster_ca_certificate" {
  description = "The Base64 encoded CA certificate for the cluster."
  value       = aws_eks_cluster.main.certificate_authority[0].data
}

output "cluster_oidc_issuer_url" {
  description = "The OIDC issuer URL for the cluster, required for IRSA."
  value       = aws_eks_cluster.main.identity[0].oidc[0].issuer
}

output "node_group_role_arn" {
  description = "The ARN of the IAM role for the EKS node group."
  value       = aws_iam_role.nodes.arn
}

output "oidc_provider_arn" {
  description = "The ARN of the OIDC provider."
  value       = aws_iam_openid_connect_provider.eks.arn
}