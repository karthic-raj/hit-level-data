provider "aws" {
  region = "us-east-1"
  default_tags {
	tags = {
	  Environment = "Test"
	}
  }
}


module "s3" {
  source  	 = "./modules/s3"
  bucketName = "aws-us-east-1-test-bucket"
}