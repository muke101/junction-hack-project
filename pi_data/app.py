from flask import Flask
from flask_restplus import Resource, Api
from swagger import initSwagger
import calculateCoeff as ccoeff

app = Flask(__name__)
api = Api(app)
initSwagger(app)


@api.route('/')
class displayData(Reasource):
    def get(self):
        return ccoeff.calCoeff()

if __name__ == '__main__':
    app.run(debug=True)
