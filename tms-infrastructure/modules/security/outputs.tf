output "eks_control_plane_sg_id" {
  description = "The ID of the security group for the EKS control plane."
  value       = aws_security_group.eks_control_plane.id
}

output "eks_nodes_sg_id" {
  description = "The ID of the security group for the EKS worker nodes."
  value       = aws_security_group.eks_nodes.id
}

output "rds_sg_id" {
  description = "The ID of the security group for the RDS instance."
  value       = aws_security_group.rds.id
}

output "elasticache_sg_id" {
  description = "The ID of the security group for the ElastiCache Redis cluster."
  value       = aws_security_group.elasticache.id
}

output "mq_sg_id" {
  description = "The ID of the security group for the Amazon MQ RabbitMQ broker."
  value       = aws_security_group.mq.id
}

output "app_pods_role_arn" {
  description = "The ARN of the IAM role for the main application pods (Odoo, FastAPI)."
  value       = aws_iam_role.app_pods.arn
}

output "aws_load_balancer_controller_role_arn" {
  description = "The ARN of the IAM role for the AWS Load Balancer Controller."
  value       = aws_iam_role.aws_load_balancer_controller.arn
}

output "cluster_autoscaler_role_arn" {
  description = "The ARN of the IAM role for the Kubernetes Cluster Autoscaler."
  value       = aws_iam_role.cluster_autoscaler.arn
}