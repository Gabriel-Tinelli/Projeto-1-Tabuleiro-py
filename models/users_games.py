from app.app import db
from sqlalchemy import Enum

class Users_Games(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False, primary_key=True) #FK
    game_id = db.Column(db.Integer, db.ForeignKey('games.game_id'), nullable=False, primary_key=True) #FK
    score = db.Column(db.SmallInteger)
    favorite_status = db.Column(db.Boolean, nullable=False, default=False)
    owned_status = db.Column(db.Boolean, nullable=False, default=False)
    played_status = db.Column(db.Boolean, nullable=False, default=False)
    want_status = db.Column(db.Boolean, nullable=False, default=False)