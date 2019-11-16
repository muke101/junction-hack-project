import weather as wt
import traffic as tr
import popdensity as pd

class calCoeff:
    def __init__(self):
        coeffs = []

    def calWeather(self):
        subCoeff = 0
        humidity, pressure, temperature, chanceOfRain = wt.pullData()
        if humidity > 90:
            subCoeff+=1
        if pressure > 1025:
            subCoeff+=1
        if temperature > 25 or temperatue < -10:
            subCoeff+=1 
        return subCoeff

    def calTraffic(self):
        normalized = 
        return tr.countTraffic
        
            
        
