import boto3
import json
import pandas as pd
from urllib.parse import urlparse
import re

s3      = boto3.client('s3')
bucket  = "aws-us-east-1-test-bucket"
key     = "hitdata/data.tsv"

def referrer_data(referrer):
        """
        This function get an URL and returns domain name, query and search term from Search engine.
        Search term is derived based on regex and currently supports google, yahoo and bing

        :param referrer: Input Url
        :return: domain_name, query and search_term
        """
        r = urlparse(referrer)
        search_term = None
        domain_name = '.'.join(r.netloc.split('.')[1:])
        query = r.query
        regex = f"( ?q=|p=|pid=|k=)([^&#]+)"
        s = re.search(regex, query, re.IGNORECASE)
        if s:
            search_term = s[2]
        return domain_name, query, search_term.lower()
    
def lambda_handler(event, context):
    
    #Retrieves objects from S3
    response  = s3.get_object(Bucket=bucket, Key=key)
    
    # Read Input data from S3
    inputData = pd.read_csv(response['Body'], sep='\t')

    #Create Dataframe with required columns from the data
    requiredColumns = inputData[["hit_time_gmt", "date_time", "ip","referrer", "product_list", "event_list"]]
    productList     = requiredColumns[["product_list"]]

    #Split the Product List column based on the delimiter
    requiredColumns[["Category", "Product_Name", "Number_of_Items", "Total_Revenue", "Custom_Event"]] = productList["product_list"].str.split(";", n=5, expand = True)
    
    #Create new column to store the referrer address
    requiredColumns["vistit_referral"] = requiredColumns.groupby(["ip"])["referrer"].transform('first')
    
    #Filter records for the completed orders
    filteredData                  = requiredColumns[requiredColumns["event_list"]==1.0]
    filteredData["Total_Revenue"] = filteredData["Total_Revenue"].astype(int)
    
    #Get Domain, Query & Search Keyword from the referrer link
    filteredData['Search Engine Domain'], filteredData['search_query'], filteredData['Search Keyword'] = zip(*filteredData['vistit_referral'].map(referrer_data))

    domainRevenue     = filteredData.groupby(["Search Engine Domain"])["Total_Revenue"].sum()
    keywordRevenue    = filteredData.groupby(["Search Engine Domain", "Search Keyword"])["Total_Revenue"].sum()
    print(keywordRevenue)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
