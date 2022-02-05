resource "aws_lambda_function" "test_lambda" {
  function_name 	= var.lambdaName
  filename      	= "hit_data.zip"
  role          	= var.lambdaRole
  handler       	= "hit_data.lambda_handler"
  runtime 			= "python3.8"
  source_code_hash 	= filebase64sha512("hit_data.zip")
}