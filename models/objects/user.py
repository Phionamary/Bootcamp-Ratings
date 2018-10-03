"""
Module to handle user model
"""


class User:
    """
    Class to handle user data
    """
    def __init__(self, *args):
        self.user_id = None
        self.user_name = args[0]
        self.email = args[1]
        self.role = args[2]
        self.password = args[3]
        self.last_seen = None
