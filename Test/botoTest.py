import prettyprinter
from prettyprinter import pprint
import boto3
from botocore.exceptions import ClientError
from config_data import deviceInfo
import logging
logging.getLogger('boto3').setLevel(logging.CRITICAL)
logging.getLogger('botocore').setLevel(logging.CRITICAL)

dynamo_url = deviceInfo.getDynamoUrl()

def get_data(sensor, id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url)

    table = dynamodb.Table('Data')

    try:
        response = table.get_item(Key={'id': id, 'sensor': sensor})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def delete_item(sensor, id, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url)

    table = dynamodb.Table('Data')

    try:
        response = table.delete_item(
            Key={
                'id': id,
                'sensor': sensor
            }
        )
    except ClientError as e:
        if e.response['Error']['Code'] == "ConditionalCheckFailedException":
            print(e.response['Error']['Message'])
        else:
            raise
    else:
        return response


def update_data(sensor, id, parameter, value, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url)

    table = dynamodb.Table('Data')

    response = table.update_item(
        Key={
            'id': id,
            'sensor': sensor
        },
        UpdateExpression="set info." + parameter + "=:c",
        ExpressionAttributeValues={
            ':c': str(value)
        },
        ReturnValues="UPDATED_NEW"
    )

def put_data(sensor, id, preference, value, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url)

    table = dynamodb.Table('Data')
    response = table.put_item(
        Item={
            'id': id,
            'sensor': sensor,
            'info': {
                preference: str(value),
            }
        }
    )
    return response