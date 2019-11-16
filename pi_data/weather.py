import requests as req
import dbconnect as db

class weather:
    def __init__(self, MAC, url="https://micromec.org", port="32001"):
        self.conn = db.dbConnect().connect()
        self.data = req.get(url+':'+port).json()[MAC]

    def pullData(self): 
        humidity = self.data['humidity']
        pressure = self.data['pressure']
        temperature = self.data['temperature']
        
        #pull in slipping danger api here
        #maybe include dew point calc
    
        if humidity > 80 and pressure < 1022:
            chanceOfRain = True
        else:
            chanceOfRain = False

        return [humidity, pressure, temperature, chanceOfRain] 
