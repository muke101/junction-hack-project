import weather.weather as wt
import traffic.traffic as tr
import popdensity.popdensity as pd

class calCoeff:
    def __init__(self):
        coeffs = []

    def calWeather(self, k=0.05):
        data = wt.pullData()
        averageTemp = 15
        subCoeff = abs(averageTemp-data['Air_temperature'])*k+data['Relative_humidity']/data['Pressure']
        isRaining = True if abs(data['Dew_Point']-data['Air_temperature']) < 1 else False 
        return subCoeff, isRaining

    def calTraffic(self):
        return tr.countTraffic
        
            
        
