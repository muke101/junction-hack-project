import pandas as pd
from pathlib import Path
import sqlalchemy as sa
from sqlalchemy import func
from sqlalchemy import create_engine
from geopy import Nominatim
data_folder = Path(".")

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

def getAddress(value):
    print(value)
    try:
        location = geolocator.geocode(value)
        if(location):
            return [location.latitude, location.longitude]
        return [0, 0]
    except:
        return [0, 0]

location = df.apply(lambda x: pd.Series(getAddress(x['address_f'].strip()+', Helsinki, Finland'), index=['latitude', 'longitude']), axis=1)

df = df.merge(location, 'inner', left_index=True, right_index=True)
print(df.head())

df.to_sql('stara_locations_av', conn)

#
#for index, row in data['Lyhyt teksti']:
#    print(geolocator.geocode(row).latitude,geolocator.geocode(row).longitude)
#location = geolocator.geocode(" Roihuvuorentie 2")
#print(location.latitude, location.longitude)

