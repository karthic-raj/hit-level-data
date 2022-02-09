import boto3
import json

s3      = boto3.client('s3')
bucket  = "aws-us-east-1-test-bucket"
key     = "hitdata/data.tsv"
    
def lambda_handler(event, context):
    
    #Read Data from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    emailcontent = response['Body'].read().decode('utf-8')
    print(emailcontent)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
