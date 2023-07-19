from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import relationship, validates
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin

from datetime import datetime

from config import db, bcrypt

# Join table for many-to-many relationship between Potion and Ingredient
PotionIngredient = db.Table('potion_ingredient',
    db.Column('potion_id', db.Integer, db.ForeignKey('potions.id'), primary_key=True),
    db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'), primary_key=True)
    )

class User(db.Model, SerializerMixin, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    score = db.Column(db.Integer)
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    house = db.relationship('House', backref='users')
    _password_hash = db.Column(db.String)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('username')
    def validate_username(self, key, username):
        if len(username) > 25 or len(username) < 1:
            raise ValueError("Username must be between 1 and 25 characters")
        return username
    
    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode('utf-8'))
    
    @property
    def is_active(self):
        return True

    def get_id(self):
        return int(self.id)

    @classmethod
    def get_by_id(cls, user_id):
        # Retrieve a user by their ID
        return cls.query.get(int(user_id))

    @classmethod
    def get_by_username(cls, username):
        # Retrieve a user by their username
        return cls.query.filter_by(username=username).first()

    def __repr__(self):
        return f"<User id={self.id}, username={self.username}>"

class Ingredient(db.Model, SerializerMixin):
    __tablename__ = 'ingredients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(50))
    thumbnail = db.Column(db.String) # Add a column to store the thumbnail image URL
    potions = db.relationship('Potion', secondary=PotionIngredient, back_populates='potions')

class Potion(db.Model, SerializerMixin):
    __tablename__ = 'potions'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    correct_ingredients = db.Column(db.ARRAY(db.Integer))
    thumbnail = db.Column(db.String) # Add a column to store the thumbnail image URL
    ingredients = db.relationship('Ingredient', secondary=PotionIngredient, back_populates='potions')

class House(db.Model, SerializerMixin):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    overall_score = db.Column(db.Integer, default=0) # Add a column to store the overall score of each house

    users = db.relationship('User', back_populates='house')

    @property
    
    def calculate_overall_score(self):
        # Calculate the overall score based on the individual scores of the users in the house
        overall_score = sum(user.score for user in self.users)
        self.overall_score = overall_score
        return overall_score


# class Score(db.Model, SerializerMixin):
#     __tablename__ = 'scores'

#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = db.relationship('User', backref='scores')
#     house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
#     score = db.Column(db.Integer)

#     created_at = db.Column(db.DateTime, server_default=db.func.now())
#     updated_at = db.Column(db.DateTime, onupdate=db.func.now())

