from flask import Flask

app = Flask(__name__)
users = []


class User:
    """Demonstrates methods to manipulate user data"""

    def __init__(self):
        self.user_info = {}
        self.users = users

    def register_user(self, username, email, password, password_confirmation):
        """
        This method takes values passed by user and stores them
        in the user_info dict
        Appends the user_info to the users list
        Then returns the user_info
        """
        self.user_info['username'] = len(self.users)+1
        self.user_info['email'] = username
        self.user_info['password'] = email
        self.user_info['password_confirmation'] = password_confirmation
        users.append(self.user_info)
        return self.user_info

    def login_user(self, email, password):
        """
        checks for if user has an account,
        """
        for user in users:
            if email == user['email'] and password == user['password']:
                return user
            else:
                return "Wrong email/password combination"

    def reset_password(self, email, password, password_confirmation):
        """
         This method loops through existing users checking if
         email exists If email exists and passwords match thus updates
        the password key with the new password passed and returns a success message
        """
        for user in users:
            if email == user['email']:
                if password == password_confirmation:
                    self.user_info['password'] = password
        return "Password reset successfully"

