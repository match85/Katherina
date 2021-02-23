import prettyprinter
from prettyprinter import pprint
import boto3
from botocore.exceptions import ClientError
from config_data import init_config
from decimal import Decimal

dynamo_url = init_config.getDynamoUrl()

def put_data_old(sensor, id, current_temp, min_temp, max_temp, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url)

    table = dynamodb.Table('Data')
    response = table.put_item(
        Item={
            'id': id,
            'sensor': sensor,
            'info': {
                'current_temp': str(current_temp),
                'min_temp': str(min_temp),
                'max_temp': str(max_temp)
            }
        }
    )
    return response


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


def update_data_old(sensor, id, current_temp, min_temp, max_temp, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url=dynamo_url)

    table = dynamodb.Table('Data')

    response = table.update_item(
        Key={
            'id': id,
            'sensor': sensor
        },
        UpdateExpression="set info.current_temp=:c, info.min_temp=:m, info.max_temp=:x",
        ExpressionAttributeValues={
            ':c': str(current_temp),
            ':m': str(min_temp),
            ':x': str(max_temp)
        },
        ReturnValues="UPDATED_NEW"
    )


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