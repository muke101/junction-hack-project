from flask import Flask
from flask import request
from flask_restplus import Resource, Api
import calculateCoeff as ccoeff

app = Flask(__name__)
api = Api(app)


@api.route('/data', methods=['GET'])
class displayData(Reasource):
    def get(self):
        return ccoeff.calCoeff()

@api.route('/input', methods=['POST'])
class inputData(Reasource):
    def post(self):
        data = request.form
        

if __name__ == '__main__':
    app.run(debug=True)
