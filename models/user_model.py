"""
Module containing functions to support the user model
"""
import datetime

from models.objects.user import User


class UserModel:
    """
    Class contains special methods to maintain the user model
    """
    user_id = 0

    user = []

    def register(self, *args):
        self.user_id += 1
        user_name = args[0]
        email = args[1]
        role = args[2]
        password = args[3]
        new_user = User(user_name, email, role, password)
        new_user.last_seen = datetime.datetime.now()
        self.user.append(new_user)

        del new_user.password

        return new_user

    def find_user_by_id(self, user_id):

        for obj in self.user:
            if user_id == obj['user_id']:
                return obj
            return None
