from bson import objectid

from .users import get_user_by_key

def create_task(username, task):
    user = get_user_by_key(username)
    
    user_tasks = user["tasks"]
    user_tasks.append({
        "task_id": objectid.ObjectId(),
        "description": task,
        "done": False
    })

    mongo.users.update_one({"username": username}, { "$set":{"tasks": user_tasks}})

def get_tasks(username):
    user = get_user_by_key(username)
    return user["tasks"]

def delete_a_task(username, task_id):
    user_tasks = get_tasks(username)

    for ind, task in enumerate(user_tasks):
        if task["task_id"] == objectid.ObjectId(task_id):
            del user_tasks[ind]
            break

    mongo.users.update_one({"username": username}, { "$set":{"tasks": user_tasks}})
