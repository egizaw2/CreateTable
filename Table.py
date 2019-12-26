# CreateTable

import boto3
dynamodb = boto3.rescource('dynamodb')
table = dynamodb.create_table(
    TableName='Courses',
    KeySchema=[
        {
            'AttributeName': 'HashKey',
            'KeyType': 'HASH'
            },
            {
                'AttributeName': 'RangeKey',
                'KeyType': 'RANGE'
            }
            
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'HashKey',
                'AttributeType': 'N'
            },
            { 
                'AttributeName': 'RangeKey',
                'AttributeType': 'S'
              },
            
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
)
print("Table status:", table.table_status)
