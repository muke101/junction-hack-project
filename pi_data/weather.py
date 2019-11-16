import dbconnect as db



class weather:
    def __init__(self):
        self.engine, self.bf15 = db.dbConnect()
        self.conn = self.engine.connect()

    def pullData(self, input_time): 

        HW = sa.Table(
            'Helsinki_Weather',
            metadata,
            autoload=True,
            autoload_with=engine
        ) 

        sel = sa.select([HW.c.Air_temperature, HW.c.Relative_humidity, HW.c.Pressure, HW.c.Dewpoint, HW.c.timestamp]
        ).where(HW.c.timestamp==input_time)

        dbPull=self.conn.execute(sel).fetchall()
        return(dbPull)
