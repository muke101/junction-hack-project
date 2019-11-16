import requests as req
#import dbconnect as db
import pandas

data = req.get("https://micromec.org:32001").json()['CF:FC:1D:65:2E:98']

#def pullData(MAC, url="https://micromec.org", port="32001"):
#    humidity = data['humidity']
#    pressure = data['pressure']
#    temperature = data['temperature']
#    
#    #pull in slipping danger api here
#
#    if humidity > 80 and pressure < 1022:
#        chanceOfRain = True
#    else:
#        chanceOfRain = False
#    
#
def updateDB():
    engine = db.dbConnect()
    
print(data)
