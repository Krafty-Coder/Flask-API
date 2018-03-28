from flask import jsonify, request, session
import re
from app import app
from app.user_model import User
from app.book_model import Book


@app.route('/api/home/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to Hello-Books'})


@app.route('/api/auth/register/', methods=['POST'])
def register_user():
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
        return jsonify({"message": "Username can't be blank"}), 401
    elif not email:
        return jsonify({"message": "Email can't be blank"}), 401
    elif not password:
        return jsonify({"message": "Password can't be blank"}), 401
    elif password != password_confirmation:
        return jsonify({"message": "Password does not match"}), 401
    elif not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z.]+$)", email):
        return jsonify({"message": "Input a valid email address"}), 401
    elif len(password) < 8:
        return jsonify({"message": "Password too short, please keep a strong password"}), 401
    elif [user for user in user.users if user['email'] == email]:
        return jsonify({"message": "User already exists"}), 401

    user.register_user(username, email, password, password_confirmation)
    return jsonify({"message": "Registration successful"}), 201


@app.route('/api/auth/login', methods=['POST'])
def login():
    """
    Checks if user exits in users
    then checks for matching password and username from users list
    hence logs in a user and creates a session
    """
    user_obj = User()
    email = request.json['email']
    password = request.json['password']
    user = [i for i in user_obj.users if email == i['email'] and password == i['password']]
    if not user:
        return jsonify({"message": "Invalid email/password combination"}), 401

    user_obj.login_user(email, password)
    session['email'] = email
    return jsonify({"message": "Login successful"}), 200


@app.route('/api/auth/logout', methods=['POST'])
def logout():
    """
    This method checks if a session exists
    then logs user out by clearing the session
    """
    user_session = session.get('email')
    if not user_session:
        return jsonify({"message": "You are not logged in"}), 400
    session.pop('email')
    return jsonify({"message": "Log out success"}), 200

@app.route('/api/books')
def add_book():
    """
    Checks for the required fields then gets to input them
    :return: "book added successfully" || "Add book Failed"
    """
    book = Book()
    title = request.json['Title']
    author = request.json['Author']
    id = request.json['ID']
    publisher = request.json['Publisher']
    number_of_books = request.json['number_of_books']

    if not title:
        return jsonify({"message": "Title can't be blank, please fix"}),
    elif not author:
        return jsonify({"message": "Author can't be blank, People with names write books"}),
    elif not publisher:
        return jsonify({"message": "Publisher can't be blank"}),
    elif not number_of_books and number_of_books < 5:
        return jsonify({"message": "Number of books must be more than five in the library"}),
    elif [book for book in book.library if book['ID'] == id]:
        return jsonify({"message": "Book already exists"}),

    book.add_book(title, author, id, publisher, number_of_books)
    return jsonify({"message": "Add book successful"}), 201
