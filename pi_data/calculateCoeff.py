import weather.weather as wt
import traffic.traffic as tr
import popdensity.popdensity as pd

class calCoeff:
    def __init__(self):
        return {'weather':self.calWeather(),'traffic':self.calTraffic(),'population density':self.calPopDensity()}

    def calWeather(self, k=0.05):
        data = wt.pullData()
        averageTemp = 15
        temp = data['Air_temperature']
        humidity = data['Relative_humidity']
        pressure = data['pressure']
        tempDifference = abs(averageTemp-temp)
        subCoeff = 0

        weather = {'temperature':temp,'humidity':humidity,'pressure',pressure, 'rainChance':False}

        if tempDifference > 20:
           subCoeff+=1
        if tempDifference < 5:
            subCoeff-=1
        if humidity/pressure > 1:
            subCoeff+=1

        if abs(data['Dew_point'] - temp) < 1:
            weather['rainChance'] = True

        if subCoeff == -1:
            weather['distruption'] = 'Good'
        if subCoeff == 0:
            weather['distruption'] = 'Normal'
        if subCoeff > 0:
            weather['distruption'] = 'Bad'
    
        return weather

    def calTraffic(self):
        return tr.countTraffic

    def calPopDensity(self,upperThreshhold=6000,lowerThreshhold=2000):
        data = pd.pullData()

        
        popdense['population density'] = data

        if data > upperThreshhold:
            distruption = 'Bad'
        if data < lowerThreshhold:
            distruption = 'Good'
        else:
            distruption = 'Normal'

        popdense['distruption'] = distruption

        return popdense
