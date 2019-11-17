from flask import Flask
from flask import request
from flask_restplus import Resource, Api
from flask import jsonify
from functools import reduce
import calculateCoeff as ccoeff

app = Flask(__name__)
api = Api(app)

@api.route('/summary', methods=['POST'])
class displayData(Resource):
    def __init__(self, data):
        self.post()

    def post(self):
        self.activeDicts = []
        self.data = request.get_json()
        for target in self.data['target'].split(','):
            if target == 'weather':
                self.weatherDict = ccoeff.calCoeff().calWeather(self.data)
                self.activeDicts.append(self.weatherDict)
            if target == 'traffic':
                self.trafficDict = ccoeff.calCoeff().calTraffic(self.data)
                self.activeDicts.append(self.trafficDict)
            if target == 'density':
                self.densityDict = ccoeff.calCoeff().calPopDensity(self.data)
                self.activeDicts.append(self.densityDict)
        return jsonify(reduce(self.merge_dicts, self.activeDicts)) #important!!: dictionaries must all have unique keys

    def merge_dicts(self,*dict_args):
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result


            
        

if __name__ == '__main__':
    app.run(host="0.0.0.0")
