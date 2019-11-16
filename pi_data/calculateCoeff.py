import weather as wt
import traffic as tr
import popdensity as pd
import dbconnect as db

class calCoeff:
    def __init__(self):
        self.conn = db.dbConnect().connect()

