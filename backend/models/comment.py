from db import db
from models.base import Base

class Comment(Base):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(160))
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    #user = db.Column(db.String(32))
    #priority = db.Column(db.Integer)

