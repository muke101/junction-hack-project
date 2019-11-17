import pandas as pd 
from pathlib import Path
import sqlalchemy as sa 
from sqlalchemy import func 
from sqlalchemy import create_engine
from geopy import Nominatim
data_folder = Path("C:/Users/iita/Documents/junction-hack-project")

file_to_open2 = data_folder / "conn.txt"
with open(file_to_open2) as f:
    database_connection_string = f.read()
engine = create_engine(database_connection_string)
conn = engine.connect()
metadata = sa.MetaData(engine)
stara = sa.Table(
    'stara_jobs_filtered',
    metadata,
    autoload=True,
    autoload_with=engine
)

sel = sa.select([stara.c.index.label('index'), stara.c.address_f.label('address_f')])
data1 = conn.execute(sel)
data = data1.fetchall()
df = pd.DataFrame(data)
df.columns = ['index', 'address_f']
geolocator = Nominatim(user_agent="stara.py")
print(df.head())

df['latitude'] = df.apply(lambda x: geolocator.geocode(x, timeout=15), axis=1)


#
#for index, row in data['Lyhyt teksti']:
#    print(geolocator.geocode(row).latitude,geolocator.geocode(row).longitude)
#location = geolocator.geocode(" Roihuvuorentie 2")
#print(location.latitude, location.longitude)

