provider "aws" {
  region = "us-east-1"
  default_tags {
	tags = {
	  Environment = "Test"
	}
  }
}

data "archive_file" "zipFile" {
  type        = "zip"
  output_path = "hit_data.zip"
  source_file = "./src/hit_data.py"
}

module "s3" {
  source  	 = "./modules/s3"
  bucketName = "aws-us-east-1-test-bucket"
}

module "lambda" {
  source  	 = "./modules/lambda"
  lambdaName = "hit_data"
  lambdaRole = "arn:aws:iam::228823017630:role/aws-lambda-role"
}