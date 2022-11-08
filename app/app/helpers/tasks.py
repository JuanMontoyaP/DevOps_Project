from bson import objectid

from .users import get_user_data, users_table

def create_task(username, task):
    user_data = get_user_data(username, ['tasks'])
    
    user_tasks = user_data["tasks"]
    user_tasks.append({
        "task_id": str(objectid.ObjectId()),
        "description": task,
        "done": False
    })

    users_table.update_item(
        Key = {
            'username': username
        },
        AttributeUpdates = {
            'tasks': {
                'Value': user_tasks,
                'Action': 'PUT'
            }
        },
        ReturnValues = "UPDATED_NEW"
    )

def get_tasks(username):
    user_tasks = get_user_data(username, ['tasks'])
    if user_tasks:
        return user_tasks["tasks"]
    else:
        return []

def delete_a_task(username, task_id):
    user_tasks = get_tasks(username)

    for ind, task in enumerate(user_tasks):
        if task["task_id"] == task_id:
            del user_tasks[ind]
            break

    users_table.update_item(
        Key = {
            'username': username
        },
        AttributeUpdates = {
            'tasks': {
                'Value': user_tasks,
                'Action': 'PUT'
            }
        },
        ReturnValues = "UPDATED_NEW"
    )
    