resource "aws_timestreamwrite_database" "main" {
  database_name = var.database_name
  kms_key_id    = var.kms_key_id

  tags = var.tags
}

resource "aws_timestreamwrite_table" "main" {
  database_name = aws_timestreamwrite_database.main.database_name
  table_name    = var.table_name

  retention_properties {
    memory_store_retention_period_in_hours = var.memory_retention_hours
    magnetic_store_retention_period_in_days = var.magnetic_retention_days
  }
  
  magnetic_store_write_properties {
    enable_magnetic_store_writes = true
  }

  tags = var.tags
}