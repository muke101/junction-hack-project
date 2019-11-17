from db import db
from models.base import Base

class Weather(Base):
    __tablename__ = 'helsinki_weather'

    id = db.Column(db.Integer, primary_key=True)
    pressure = db.Column(db.Float)
    dewpoint = db.Column(db.Float)
