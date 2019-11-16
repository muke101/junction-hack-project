import pandas as pd 
from pathlib import Path
import sqlalchemy as sa 
from sqlalchemy import func 
from sqlalchemy import create_engine

data_folder = Path("C:/Users/iita/Documents/junction-hack-project")

file_to_open = data_folder / "paavo_9_koko.csv"

data = pd.read_csv(file_to_open, sep=';')

file_to_open2 = data_folder / "conn.txt"
with open(file_to_open2) as f:
    database_connection_string = f.read()
engine = create_engine(database_connection_string)
conn = engine.connect()

data.to_sql('zipcodes_population_area', conn)

print(data.head())