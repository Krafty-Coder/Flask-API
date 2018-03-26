from flask import Flask

app = Flask(__name__)
users = []


class User:
    """Creating, deleting and manipulation of user-data"""

    def __init__(self):
        self.user_info = {}
        self.users = users

    def register_user(self, username, email, password, password_confirmation):
        """
        Stores username, email and  password  in a dictionary for mapping.
        """
        pass