resource "aws_s3_bucket" "main" {
  bucket = var.bucket_name

  tags = var.tags
}

resource "aws_s3_bucket_versioning" "main" {
  bucket = aws_s3_bucket.main.id
  versioning_configuration {
    status = var.enable_versioning ? "Enabled" : "Suspended"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "main" {
  bucket = aws_s3_bucket.main.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "main" {
  bucket = aws_s3_bucket.main.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_logging" "main" {
  count  = var.log_bucket_name != "" ? 1 : 0
  bucket = aws_s3_bucket.main.id

  target_bucket = var.log_bucket_name
  target_prefix = "log/${var.bucket_name}/"
}

resource "aws_s3_bucket_lifecycle_configuration" "main" {
  count  = var.enable_lifecycle_policy ? 1 : 0
  bucket = aws_s3_bucket.main.id

  rule {
    id     = "log"
    status = "Enabled"

    filter {
      prefix = "log/"
    }

    transition {
      days          = 30
      storage_class = "STANDARD_IA"
    }

    transition {
      days          = 60
      storage_class = "GLACIER"
    }

    expiration {
      days = 90
    }
  }

  rule {
    id     = "incomplete_multipart_uploads"
    status = "Enabled"
    
    abort_incomplete_multipart_upload {
      days_after_initiation = 7
    }
  }
}