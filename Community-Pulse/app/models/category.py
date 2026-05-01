from sqlalchemy import Column, Integer, String
from app import db

class Category(db.Model):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

