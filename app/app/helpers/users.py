from app.db import resource, client, create_table_dynamodb

try:
    response = client.describe_table(TableName='Users')
except client.exceptions.ResourceNotFoundException:
    create_table_dynamodb('Users', 'username', 'S')

users_table = resource.Table('Users')

def get_user_by_key(username):
    response = users_table.get_item(
        Key = {
            'username': username
        },
    )
    return response

def get_user_data(username, data_to_get: list):
    response = users_table.get_item(
        Key = {
            'username': username
        },
        AttributesToGet = data_to_get
    )

    if "Item" in response:
        return response["Item"]
    
    return {}

def create_user(user_data):
    response = users_table.put_item(Item=user_data.__dict__)
    return response
    

