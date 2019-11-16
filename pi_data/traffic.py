import dbconnect as db
import sqlalchemy as sa
import os

class traffic:
    def __init__(self, beaconSerial):
        self.engine, self.bf15 = db.dbConnect(name='business_finland_fifteenseconds')
        self.conn = self.engine.connect()

    def countTraffic(self, serial):
        sel = sa.select(
            [self.bf15.c.serial,
            self.bf15.c.time,
            sa.func.count(self.bf15.c.hash).label('n_devices_found')]
            ).where(self.bf15.c.serial==serial).group_by(self.bf15.c.serial,self.bf15.c.time)
        dbPull = self.conn.execute(sel).fetchall()

        return {traffic_density:len(dbPull)} 

