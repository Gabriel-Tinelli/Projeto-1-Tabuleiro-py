from app.app import db
from sqlalchemy import Enum

class Games_Pictures(db.Model):
    picture_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    url = db.Column(db.String(400), nullable=False)