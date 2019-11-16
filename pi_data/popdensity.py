import dbconnect as db

class popdensity:
    def __init__(self):
        self.engine, self.bf15 = db.dbConnect(name='zipcopes_population_area')
    
    def  
