import boto3

client = boto3.client(
    'dynamodb',
    region_name='us-west-1'
)

resource = boto3.resource(
    'dynamodb',
    region_name='us-west-1'
)

def create_table_dynamodb(table_name, primary_key, primary_key_type):
        
    client.create_table(
        AttributeDefinitions = [ # Name and type of the attributes 
            {
                'AttributeName': primary_key, # Name of the attribute
                'AttributeType': primary_key_type   # N -> Number (S -> String, B-> Binary)
            }
        ],
        TableName = table_name, # Name of the table 
        KeySchema = [       # Partition key/sort key attribute 
            {
                'AttributeName': primary_key,
                'KeyType'      : 'HASH' 
                # 'HASH' -> partition key, 'RANGE' -> sort key
            }
        ],
        BillingMode = 'PAY_PER_REQUEST',
        Tags = [ # OPTIONAL 
            {
                'Key' : 'test-resource',
                'Value': 'todo-app'
            }
        ]
    )
