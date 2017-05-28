# AWS S3 bucket for static hosting
resource "aws_s3_bucket" "${var.bucket_name}" {
  bucket = "${var.bucket_name}"
  acl = "public-read"

  tags {
    Environment = "${var.tag_environment}"
    Name = "${var.tag_name}"
  }

  cors_rule {
    allowed_headers = ["*"]
    allowed_methods = ["PUT","POST"]
    allowed_origins = ["*"]
    expose_headers = ["ETag"]
    max_age_seconds = 3000
  }
}
