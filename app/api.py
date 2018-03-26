from flask import Flask, jsonify, request, session
import re
from app.user_model import User


app = Flask(__name__)


@app.route('/api/home/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Hello-Books'})


@app.route('/api/auth/register/', methods=['POST'])
def register():
    """
    Gets data from user in JSON Format
    and uses them to register user with the register_user method
    """
    user = User()
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    password_confirmation = request.json['password_confirmation']

    if not username or len(username.strip()) == 0:
        return jsonify({"message": "Username can't be blank"}),401
    elif not email:
        return jsonify({"message": "Email can't be blank"}),401
    elif not password:
        return jsonify({"message": "Password can't be blank"}), 401
    elif password != password_confirmation:
        return jsonify({"message": "Password does not match"}), 401
    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+$)", email):
        return jsonify({"message": "Input a valid email address"}), 401
    elif len(password) < 5:
        return jsonify({"message": "Password too short, please keep a strong password"}), 401
    elif [i for i in user.users if i['email'] == email]:
        return jsonify({"message": "User already exists"}), 401

    user.register_user(username, email, password, password_confirmation)
    return jsonify({"message": "Registration successful"}), 201

