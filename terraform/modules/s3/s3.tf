resource "aws_s3_bucket" "s3Bucket" {
  bucket = var.bucketName
  acl    = "private"

  tags = {
    Name        = var.bucketName
    Environment = "Dev"
  }
}

resource "aws_s3_bucket_public_access_block" "s3BlockAccess" {
  bucket 			  		= aws_s3_bucket.s3Bucket.id
  block_public_acls   		= true
  block_public_policy 		= true
  ignore_public_acls 		= true
  restrict_public_buckets 	= true
}