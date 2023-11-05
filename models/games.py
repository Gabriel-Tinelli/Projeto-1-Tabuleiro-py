from app import db
from sqlalchemy import Enum

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