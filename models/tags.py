from sqlalchemy import Enum
from app import db

class Tags(db.Model):
    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    type = db.Column(Enum('Mechanism', 'Theme', 'Other'), nullable=False)