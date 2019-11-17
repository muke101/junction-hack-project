from flask import Flask
from flask import request
from flask_restplus import Resource, Api
import calculateCoeff as ccoeff

app = Flask(__name__)
api = Api(app)

@api.route('/', methods=['GET','POST'])
class displayData(Resource):
    def __init__(self,data):
        self.data = data
        self.weatherDict = None
        self.trafficDict = None
        self.densityDict = None
        self.allDicts = [self.weatherDict, self.trafficDict, self.densityDict]
        if request.method == "GET":
            self.get()
        if request.method == "POST":
            self.post()

    def get(self):
        if self.data is not None:
            return self.dataDict
        else:
            return 'please post data'

    def post(self):
        self.data = request.form
        for target in data['target']:
            if target == 'weather':
                self.weatherDict = ccoeff.calWeather(self.data)
            if target == 'traffic':
                self.trafficDict = ccoeff.calTraffic(self.data)
            if target == 'density':
                self.densityDict = ccoeff.calPopDensity(self.data)
        activeDicts = [d for d in self.allDicts if d is not None]
        self.dataDict = reduce(self.merge_dicts, activeDicts) #important!!: dictionaries must all have unique keys

    def merge_dicts(self,*dict_args):
        result = {}
        for dictionary in dict_args:
            result.update(dictionary)
        return result


            
        

if __name__ == '__main__':
    app.run()
