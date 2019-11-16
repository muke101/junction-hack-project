import weather.weather as wt
import traffic.traffic as tr
import popdensity.popdensity as pd

class calCoeff:
    def __init__(self):
        coeffs = []
        self.notifs = {'raining': False, 'icy': False}

    def calWeather(self, k=0.05):
        data = wt.pullData()
        averageTemp = 15
        subCoeff = abs(averageTemp-data['Air_temperature'])*k+data['Relative_humidity']/data['Pressure']
        if abs(data['Dew_Point']-data['Air_temperature']) < 1:
            self.notifs['raining'] = True
        return subCoeff

    def calTraffic(self):
        return tr.countTraffic

    def calPopDensity(self):
        std = 4898
        mean = 85
        threshhold = 6000
         


