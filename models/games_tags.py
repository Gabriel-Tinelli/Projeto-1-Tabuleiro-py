from app import db
from sqlalchemy import Enum

class Games_Tags(db.Model):
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False, primary_key=True) #FK
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.tag_id'), nullable=False, primary_key=True) #FK