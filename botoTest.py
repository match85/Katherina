from prettyprinter import pprint
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal


def put_data(sensor, id, current_temp, min_temp, max_temp, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

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
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

    table = dynamodb.Table('Data')

    try:
        response = table.get_item(Key={'id': id, 'sensor': sensor})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']


def update_data(sensor, id, current_temp, min_temp, max_temp, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

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
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

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


if __name__ == '__main__':
    sensor_resp = put_data("Temperature", 1, 22, 21, 23)
    print("Put data succeeded:")
    pprint(sensor_resp)

    sensor = get_data("Temperature", 1)
    if sensor:
        print("Get data succeeded:")
        pprint(sensor)

    update_response = update_data("Temperature", 1, 21.5, 21, 23)
    print("Update data succeeded")
    pprint(update_response)

    sensor = get_data("Temperature", 1)
    if sensor:
        print("Get data succeeded:")
        pprint(sensor)
    print("Attempting to delete an item...")

"""
    delete_response = delete_item("Temperature", 1)
    if delete_response:
        print("Delete data succeeded:")
        pprint(delete_response)
"""
"""
    movie = get_movie("The Big New Movie",2016)
    if movie:
        print("Get movie succeeded:")
        pprint(movie)
"""
