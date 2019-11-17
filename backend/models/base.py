from db import db

class Base(db.Model):
    __abstract__ = True

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def as_geojson(self):
        dictFormat = self.as_dict()
        return {
            "type": "Feature",
            "properties": dictFormat,
            "geometry": {
                "type": "Point",
                "coordinates": [ dictFormat["longitude"], dictFormat["latitude"], 0.0 ]
            }
       }
