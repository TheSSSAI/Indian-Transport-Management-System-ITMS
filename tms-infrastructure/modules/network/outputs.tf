output "vpc_id" {
  description = "The ID of the created VPC."
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "A list of IDs for the public subnets."
  value       = [for s in aws_subnet.public : s.id]
}

output "private_subnet_ids" {
  description = "A list of IDs for the private subnets."
  value       = [for s in aws_subnet.private : s.id]
}

output "vpc_cidr_block" {
  description = "The CIDR block of the VPC."
  value       = aws_vpc.main.cidr_block
}