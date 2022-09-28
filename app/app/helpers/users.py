
from app.db import mongo

def get_user_by_key(value, key='username'):
    user = mongo.users.find_one({key: value})
    return user

def create_user(user_data):
    mongo.users.insert_one(user_data.__dict__)

