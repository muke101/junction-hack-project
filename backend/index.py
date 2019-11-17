from flask import Flask, request, jsonify
from db import db, dbConnectionString
from flask_restplus import Resource, Api

from models.comment import Comment
from models.weather import Weather
from models.bluetooth import Bluetooth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = dbConnectionString
app.config['PROPAGATE_EXCEPTIONS'] = True
db.init_app(app)

api = Api(app)

#db.create_all()

def toDictList(query):
    return list(map(lambda x: x.as_dict(), query))

def toGeoJson(query):
    return {
        "type": "FeatureCollection",
        "crs": { "type": "name", "properties": { "name": "urn:ogc:def:crs:OGC:1.3:CRS84" } },
        "features": list(map(lambda x: x.as_geojson(), query))
    }

    list(map(lambda x: x.as_dict(), query))

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return toDictList(Comment.query.all())

@api.route('/weather')
class WeatherController(Resource):
    def get(self):
        return toDictList(Weather.query.all())

@api.route('/bluetooth')
class BluetoothController(Resource):
    def get(self):
        return toGeoJson(Bluetooth.query.all())

@api.route('/reports')
class CommentController(Resource):
    def post(self):
        extracted = {key: request.json[key] for key in (
            'longitude', 'latitude', 'comment', #'user', 'priority'
        )}
        comment = Comment(**extracted)

        # Do something with priority & user uuid fields?
        # Fuck migrations, want sleep.

        db.session.add(comment)
        db.session.commit()

        return jsonify(comment.as_dict())

    def get(self):
        return toDictList(Comment.query.all())


if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
