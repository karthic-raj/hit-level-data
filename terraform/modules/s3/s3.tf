resource "aws_s3_bucket" "s3Bucket" {
  bucket = var.bucketName
  acl    = "private"
}

resource "aws_s3_bucket_public_access_block" "s3BlockAccess" {
  bucket 			  		= aws_s3_bucket.s3Bucket.id
  block_public_acls   		= true
  block_public_policy 		= true
  ignore_public_acls 		= true
  restrict_public_buckets 	= true
}

resource "aws_s3_bucket_object" "object" {
  bucket = aws_s3_bucket.s3Bucket.id
  key    = "hitdata/data.tsv"
  source = "./src/data.tsv"
  etag = filemd5("./src/data.tsv")
}