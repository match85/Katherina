from prettyprinter import pprint
import boto3
from botocore.exceptions import ClientError
from decimal import Decimal

def put_movie(title, year, plot, rating, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

    table = dynamodb.Table('Movies')
    response = table.put_item(
       Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

    table = dynamodb.Table('Movies')

    try:
        response = table.get_item(Key={'year': year, 'title': title})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']

def update_movie(title, year, rating, plot, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

    table = dynamodb.Table('Movies')

    response = table.update_item(
        Key={
            'year': year,
            'title': title
        },
        UpdateExpression="set info.rating=:r, info.plot=:p",
        ExpressionAttributeValues={
            ':r': Decimal(rating),
            ':p': plot,
        },
        ReturnValues="UPDATED_NEW"
    )

if __name__ == '__main__':
    movie_resp = put_movie("The Big New Movie", 2016,
                           "Nothing happens at all.", 1)
    print("Put movie succeeded:")
    pprint(movie_resp)
    movie = get_movie("The Big New Movie",2016)
    if movie:
        print("Get movie succeeded:")
        pprint(movie)

    update_response = update_movie("The Big New Movie", 2016, 5.5, "Everything happens all at once.")
    print("Update movie succeeded")
    pprint(update_response)
    movie = get_movie("The Big New Movie",2016)
    if movie:
        print("Get movie succeeded:")
        pprint(movie)

