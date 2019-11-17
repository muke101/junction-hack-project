from db import db
from models.base import Base

class Job(Base):
    __tablename__ = 'stara_full'

    id = db.Column(db.String, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    tila = db.Column('tila', db.String)
    työnkuvaus = db.Column('työnkuvaus', db.String)
    alkurajapvm = db.Column('alkurajapvm', db.String)
    loppuraja = db.Column('loppuraja', db.String)
    address_f = db.Column('address_f', db.String)
