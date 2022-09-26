from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.todo_app
tasks = db.tasks

def get_task():
    return tasks.find()