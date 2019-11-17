class calCoeff:
    def calc(self, data):
        if data is not None:
            return {'weather':self.calWeather(data),'traffic':self.calTraffic(data),'population density':self.calPopDensity(data)}

    def calWeather(self, data):
        k = 0.05
        averageTemp = 15
        temp = data['Air_temperature']
        humidity = data['Relative_humidity']
        pressure = data['pressure']
        tempDifference = abs(averageTemp-temp)
        subCoeff = 0

        weather = {'temperature':temp,'humidity':humidity,'pressure':pressure, 'rainChance':False}

        if tempDifference > 20:
           subCoeff+=1
        if tempDifference < 5:
            subCoeff-=1
        if humidity/pressure > 1:
            subCoeff+=1

        if abs(data['Dew_point'] - temp) < 1:
            weather['rainChance'] = True

        if subCoeff == -1:
            weather['weatherDist'] = 'Good'
        if subCoeff == 0:
            weather['weatherDist'] = 'Normal'
        if subCoeff > 0:
            weather['weatherDist'] = 'Bad'
    
        return weather

    def calTraffic(self):
        return tr.countTraffic

    def calPopDensity(self,data):
        upperThreshhold=6000
        lowerThreshhold=2000
        popdense = {}
        popdense['population density'] = data['population density']
        density = popdense['population density']

        if int(density) > upperThreshhold:
            distruption = 'Bad'
        if int(density) < lowerThreshhold:
            distruption = 'Good'
        else:
            distruption = 'Normal'

        popdense['popDist'] = distruption

        return popdense

