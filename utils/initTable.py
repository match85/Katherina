#Python3

import boto3

def create_data_table(dynamodb=None):
        if not dynamodb:
                dynamodb = boto3.resource('dynamodb', endpoint_url="http://192.168.1.100:8000")

        table = dynamodb.create_table(
                TableName='Data',
                KeySchema=[
                        {
                                'AttributeName': 'id',
                                'KeyType': 'HASH'
                        },
                        {
                                'AttributeName': 'sensor',
                                'KeyType': 'RANGE'
                        }
                ],
                AttributeDefinitions=[
                        {
                                'AttributeName': 'sensor',
                                'AttributeType': 'S'
                        },
                        {
                                'AttributeName': 'id',
                                'AttributeType': 'N'
                        },
                ],
                ProvisionedThroughput={
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                }
        )
        return table

if __name__ == '__main__':
        data_table = create_data_table()
        print("Table status:", data_table.table_status)

