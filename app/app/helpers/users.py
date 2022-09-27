from app.db import mongo

def get_user_by_key(value, key='username'):
    user = mongo.users.find_one({key: value})
    return user

