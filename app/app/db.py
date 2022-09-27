from pymongo import MongoClient

client = MongoClient('localhost', 27017)
mongo = client.todo_app
tasks = mongo.tasks

# tasks.insert_one({"task" :1})

# mongo.users.insert_one({"username": "Juan", "password": "123"})

# print(mongo.users.find_one({'username': 'Juan'}))

def get_task():
    return tasks.find()