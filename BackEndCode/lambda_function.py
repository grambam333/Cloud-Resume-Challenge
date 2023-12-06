import json
import boto3

def lambda_handler(event, context):

    # connect to DynamoDB resource
    client = boto3.resource('dynamodb')
    
    # create a DynamoDB client to visitor count table
    table = client.Table('visitor_count')
    
    #increment visitor count by index.html
    # references
    response = table.update_item(
        Key={
            'path': 'index.html'
        },
        AttributeUpdates={
            'visitor_count':{
                'Value': 1,
                'Action': 'ADD'
            }
        }
    )
  
    # get visitor count from visitor_count table for inndex.html
    response = table.get_item(
        Key={
             'path': 'index.html'
        }
    )
    
    visitor_count = response['Item']['visitor_count']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': visitor_count
    }
