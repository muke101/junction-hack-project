from flask import Flask
from flask_restplus import Resource, Api
from swagger import initSwagger

app = Flask(__name__)
api = Api(app)
initSwagger(app)


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return {'hello':'world'}

if __name__ == '__main__':
    app.run(debug=True)
