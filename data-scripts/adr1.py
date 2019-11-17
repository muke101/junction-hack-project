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
        result = geolocator.geocode(value)
        if(result):
            return result
        return {"latitude": 0, "longitude": 0}
    except:
        return {"latitude": 0, "longitude": 0}

df['latitude'] = df.apply(lambda x: getAddress(x['address_f'].strip()+', Helsinki, Finland'), axis=1)['latitude']
df['longitude'] = df.apply(lambda x: getAddress(x['address_f'].strip()+', Helsinki, Finland'), axis=1)['longitude']

print(df.head())

#
#for index, row in data['Lyhyt teksti']:
#    print(geolocator.geocode(row).latitude,geolocator.geocode(row).longitude)
#location = geolocator.geocode(" Roihuvuorentie 2")
#print(location.latitude, location.longitude)

