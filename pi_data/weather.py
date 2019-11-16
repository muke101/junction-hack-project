import dbconnect as db

class weather:
    def __init__(self):
        self.engine, self.bf15 = db.dbConnect()
        self.conn = self.engine.connect()

    def pullData(self): 
        
        dbPull = 

        return {'temperature':dbPull['Air temperature'], 'humidity':dbPull['Relative humidity'], 'pressure':dbPull['Pressure'], 'dew point':dbPull['Dew-point']}
