# main.tf in modules/rds
# Provisions a high-availability RDS for PostgreSQL 16 instance.
# Aligns with REQ-1-014 and REQ-1-502.

# Create a DB subnet group for the RDS instance
resource "aws_db_subnet_group" "main" {
  name       = "${var.project_name}-${var.environment}-rds-subnet-group"
  subnet_ids = var.db_subnet_ids

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-rds-subnet-group"
  })
}

# Retrieve the master password from AWS Secrets Manager
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = var.master_password_secret_arn
}

# Provision the RDS for PostgreSQL 16 instance
resource "aws_db_instance" "main" {
  identifier           = "${var.project_name}-${var.environment}-rds"
  allocated_storage    = var.allocated_storage
  storage_type         = var.storage_type
  iops                 = var.storage_type == "io1" ? var.iops : null
  engine               = "postgres"
  engine_version       = "16"
  instance_class       = var.instance_class
  username             = var.master_username
  password             = data.aws_secretsmanager_secret_version.db_password.secret_string
  db_subnet_group_name = aws_db_subnet_group.main.name
  vpc_security_group_ids = [var.vpc_security_group_id]

  # High Availability and Recovery settings (REQ-1-502)
  multi_az               = var.multi_az
  backup_retention_period = var.backup_retention_period # Enables Point-In-Time-Recovery (PITR)
  delete_automated_backups = var.delete_automated_backups
  final_snapshot_identifier = var.environment == "prod" ? "${var.project_name}-${var.environment}-rds-final-snapshot" : null
  skip_final_snapshot    = var.environment != "prod"

  # Security and Maintenance
  storage_encrypted   = true
  publicly_accessible = false
  apply_immediately   = var.apply_immediately
  
  # Logging
  enabled_cloudwatch_logs_exports = ["postgresql", "upgrade"]

  tags = merge(var.tags, {
    Name = "${var.project_name}-${var.environment}-rds"
  })

  lifecycle {
    ignore_changes = [password]
  }
}