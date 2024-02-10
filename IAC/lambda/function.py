# import libraries - boto3 is the library used to interact with AWS resources
import json
import boto3
dynamodb = boto3.resource('dynamodb')
# call the cloud resume challenge table and get the item with id 0
table = dynamodb.Table('cloudresumechallenge')
def lambda_handler(event, context):
    response = table.get_item(Key={
        'id':'0'
    })
    views = response['Item']['views']
    # increment the views count when someone visits and display current views
    views = views + 1
    print(views)
    # update the dynamodb with the new value of 
    response = table.put_item(Item={
        'id':'0',
        'views':views
    })
    
    return views
