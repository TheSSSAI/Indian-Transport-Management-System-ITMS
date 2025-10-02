# variables.tf in modules/eks
# Defines the input contract for the EKS module.

variable "project_name" {
  description = "The name of the project."
  type        = string
}

variable "environment" {
  description = "The environment name (e.g., dev, staging, prod)."
  type        = string
}

variable "tags" {
  description = "A map of tags to assign to all resources."
  type        = map(string)
  default     = {}
}

variable "cluster_name" {
  description = "The name of the EKS cluster."
  type        = string
}

variable "cluster_version" {
  description = "The Kubernetes version for the EKS cluster."
  type        = string
  default     = "1.28"
}

variable "private_subnet_ids" {
  description = "A list of private subnet IDs where the EKS cluster and nodes will be deployed."
  type        = list(string)
  validation {
    condition     = length(var.private_subnet_ids) >= 2
    error_message = "At least two private subnets are required for high availability."
  }
}

variable "cluster_security_group_id" {
  description = "The security group ID for the EKS cluster control plane."
  type        = string
}

variable "node_security_group_id" {
  description = "The security group ID for the EKS worker nodes."
  type        = string
}

variable "cluster_service_ipv4_cidr" {
  description = "The CIDR block for the Kubernetes services."
  type        = string
  default     = "172.20.0.0/16"
}

variable "node_instance_type" {
  description = "The EC2 instance type for the worker nodes."
  type        = string
  default     = "t3.medium"
}

variable "node_group_desired_size" {
  description = "The desired number of worker nodes."
  type        = number
  default     = 2
}

variable "node_group_min_size" {
  description = "The minimum number of worker nodes for the autoscaling group."
  type        = number
  default     = 2
}

variable "node_group_max_size" {
  description = "The maximum number of worker nodes for the autoscaling group."
  type        = number
  default     = 4
}

variable "ec2_ssh_key_name" {
  description = "The name of the EC2 key pair to allow SSH access to nodes (optional)."
  type        = string
  default     = null
}

variable "ebs_csi_driver_role_arn" {
  description = "The ARN of the IAM role for the EBS CSI driver service account (IRSA)."
  type        = string
}