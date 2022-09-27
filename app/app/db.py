from pymongo import MongoClient

client = MongoClient('mongodb', 27017)
mongo = client.todo_app