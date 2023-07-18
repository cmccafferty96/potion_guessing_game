#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify
from flask_restful import Resource
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

# Local imports
from config import app, db, api
from models import User 

# Views go here!

app = Flask(__name__)
app.secret_key = 'your_secret_key'
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route('/register', methods=['POST'])
def register():
    # Extract user registration data from request
    username = request.json['username']
    password = request.json['password']

    # Check if the username is already taken
    if User.query.filter_by(username=username).first():
        return jsonify(message='Username already exists'), 409
    
    # Create a new user object and hash the password
    user = User(username=username)
    user.password_hash = password

    # Save the user to the database
    db.session.add(user)
    db.session.commit()

    return jsonify(message='User registered successfully')

@app.route('/login', methods=['POST'])
def login():
    # Extract user login data from request
    username = request.json['username']
    password = request.json['password']

    # Retrieve the user from the database
    user = User.query.filter_by(username=username).first()

    if user and user.authenticate(password):
        # Log in the user and store their ID in the session
        login_user(user)
        return jsonify(message='Login successful')
    
    return jsonify(message='Invalid username or password'), 401

if __name__ == '__main__':
    app.run(port=5555, debug=True)
