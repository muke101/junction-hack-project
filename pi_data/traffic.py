import dbconnect as db
import sqlalchemy as sa

class traffic:
    def __init__(self, beaconSerial):
        self.engine, self.bf15 = db.dbConnect(name='business_finland_fifteenseconds')
        self.conn = self.engine.connect()
        self.traffic_density = None

    def countTraffic(self, interval, serial):
        sel = sa.select(
            [self.bf15.c.serial,
            self.bf15.c.time,
            sa.func.count(self.bf15.c.hash).label('n_devices_found')]
            ).where(self.bf15.c.serial==serial).group_by(self.bf15.c.serial,self.bf15.c.time)
        dbPull = self.conn.execute(sel).fetchall()

        self.traffic_density = {traffic_density:sum(dbPull)} 

        return self.traffic_density 

    def updateDB(self):
        if self.traffic_density == None:
            self.traffic_density = self.countTraffic()
        db.dbPush(self.traffic_density, 'traffic_density', self.conn)
