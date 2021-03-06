resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = "./src/Pandas_Package.zip"
  layer_name = "panda_pacakages"

  compatible_runtimes = ["python3.7"]
}


resource "aws_lambda_function" "test_lambda" {
  function_name 	= var.lambdaName
  filename      	= "hit_data.zip"
  role          	= var.lambdaRole
  handler       	= "hit_data.lambda_handler"
  runtime 			= "python3.7"
  source_code_hash 	= filebase64sha512("hit_data.zip")
  layers			= [aws_lambda_layer_version.lambda_layer.arn]
}