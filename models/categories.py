from app.app import db
from sqlalchemy import Enum

class Categories(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)