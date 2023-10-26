from sqlalchemy import Enum
from app import db

# Modelos

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(64), nullable=False)
    person_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(320), nullable=False, unique=True)
    blocked = db.Column(db.Boolean, nullable=False, default=False)
    deleted = db.Column(db.Boolean, nullable=False, default=False)

class Games(db.Model):
    game_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False) #FK
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    release_year = db.Column(db.SmallInteger)
    difficulty = db.Column(db.SmallInteger, nullable=True)
    lenght = db.Column(db.SmallInteger, nullable=True)
    required_players = db.Column(db.Integer,  nullable=True)
    thumbnail_url = db.Column(db.String(400), nullable=True)
    designer = db.Column(db.String(100), nullable=True)
    deleted = db.Column(db.Boolean, nullable=False, default=False)

class Games_Pictures(db.Model):
    picture_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(400), nullable=False)

class Tags(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    type = db.Column(Enum('Mechanism', 'Theme', 'Other'), nullable=False)

class Users_Games(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False, primary_key=True) #FK
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False, primary_key=True) #FK
    score = db.Column(db.SmallInteger)
    favorite_status = db.Column(db.Boolean, nullable=False, default=False)
    owned_status = db.Column(db.Boolean, nullable=False, default=False)
    played_status = db.Column(db.Boolean, nullable=False, default=False)
    want_status = db.Column(db.Boolean, nullable=False, default=False)

class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

class Games_Tags(db.Model):
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False, primary_key=True) #FK
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'), nullable=False, primary_key=True) #FK
