#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
# from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from flask_migrate import Migrate

# Local imports
from config import app, db, api 
from models import User, House, Potion, Ingredient, PotionIngredients

# Initialize the API
# api = Api(app)

# Views go here!
# migrate = Migrate(app, db)

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.secret_key = 'your_secret_key'
# login_manager = LoginManager(app)
# login_manager.login_view = 'login'

@app.route('/register', methods=['POST'])

def register():
    # Extract user registration data from request
    username = request.json['username']
    password = request.json['password']

    # Check if the username is already taken
    if User.query.filter_by(username=username).first():
        return jsonify(message='Username already exists'), 409
    
    # Create a new user object and hash the password
    user = User(username=username, password=password)

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


class Users(Resource):
    def get(self):
        users = User.query.all()
        user_list = [user.to_dict() for user in users]
        return user_list, 200
    
    def post(self):
        # try:
        new_user = User(
            username=request.json['username'],
            password=request.json['password']
        )

        db.session.add(new_user)
        db.session.commit()

        new_user_dict = new_user.to_dict()

        # print(new_user_dict)

        return new_user_dict, 201
        # except:
        #     return jsonify({'error': '400: Validation error'}), 400
        
api.add_resource(Users, '/users')

class UserByUsername(Resource):
    def get(self, username):
        user = User.query.filter_by(username=username).first()

        if user:
            return user.serialize(), 200
        else:
            return {'error': '404: User not found'}, 404
        
    def patch(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            for attr in request.json:
                setattr(user, attr, request.json[attr])
            
            db.session.commit()
            return user.to_dict(), 202
        
        return {'error': 'User not found'}, 404
    
    
    def delete(self, id):
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit()

            response = make_response({}, 204)

            return response
        
        return {'error': 'User not found'}, 404
    
api.add_resource(UserByUsername, '/users/<int:id>')

class Potions(Resource):
    def get(self):
        potions = Potion.query.all()
        potion_list = [potion.to_dict() for potion in potions]
        return potion_list, 200
    
api.add_resource(Potions, '/potions')

class Ingredients(Resource):
    def get(self):
        ingredients = Ingredient.query.all()
        ingredient_list = [ingredient.to_dict() for ingredient in ingredients]
        return ingredient_list, 200
    
api.add_resource(Ingredients, '/ingredients')
    
class Houses(Resource):
    def get(self):
        houses = House.query.all()
        house_list = [house.to_dict() for house in houses]
        return house_list, 200
    
api.add_resource(Houses, '/houses')
    
# class PotionIngredientsList(Resource):
#     def get(self):
#         potion_ingredients = PotionIngredients.query.all()
#         potion_ingredient_list = [pi.serialize]

if __name__ == '__main__':
    app.run(port=5555, debug=True)
