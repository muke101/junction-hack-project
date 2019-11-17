from db import db
from models.base import Base

class Job(Base):
    __tablename__ = 'stara_locations_av'

    index = db.Column(db.String, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    status = db.Column('Tila', db.String)
    shorDescription = db.Column('Lyhyt teksti', db.String)
    description = db.Column('Työnkuvaus', db.String)
    lastIn = db.Column('Viim. tulokirjaus', db.String)
    lastIncome = db.Column('Viim. tulokirjaus', db.String)
    startDate = db.Column('Alkurajapvm', db.String)
    endDate = db.Column('Loppuraja', db.String)
    address = db.Column('address_f', db.String)
