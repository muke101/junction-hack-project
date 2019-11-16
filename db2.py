import sqlalchemy as sa 
from sqlalchemy import func 
from pathlib import Path

from sqlalchemy import create_engine

data_folder = Path("C:/Users/iita/Documents/")

file_to_open = data_folder / "conn.txt"

with open(file_to_open) as f:
    database_connection_string = f.read()
engine = create_engine(database_connection_string)
conn = engine.connect()

# MetaData
metadata = sa.MetaData(engine)

bf15 = sa.Table(
    'business_finland_fifteenseconds',
    metadata,
    autoload=True,
    autoload_with=engine
)

sel = sa.select(
    [bf15.c.serial, 
    bf15.c.time, 
    func.count(bf15.c.hash).label('n_devices_found')]
).where(bf15.c.serial=='00000000f1124bca').group_by(bf15.c.serial,bf15.c.time)

b = conn.execute(sel).fetchall()

print(b)

