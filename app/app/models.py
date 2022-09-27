from flask_login import UserMixin

from app.helpers.users import get_user_by_key

class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserModel(UserMixin):
    def __init__(self, user_data: UserData):
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(username):
        user_doc = get_user_by_key(username)
        user_data = UserData(
            username = user_doc["username"],
            password = user_doc["password"]
        )

        return UserModel(user_data)