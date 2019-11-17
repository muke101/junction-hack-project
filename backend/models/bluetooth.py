from db import db
from models.base import Base

class Bluetooth(Base):
    __tablename__ = 'business_finland_aggregate_loc'

    serial = db.Column(db.String, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    time = db.Column(db.String, primary_key=True)
    n_devices_found = db.Column(db.Integer)
