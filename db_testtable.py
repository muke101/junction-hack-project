
import os
import pandas as pd
import requests
from datetime import datetime
#import s3fs
#from params.eurostat_params import define_query_specifications
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from pathlib import Path
from urllib.parse import quote_plus
#import airflow
#from airflow.models import DAG
#from airflow.operators.python_operator import PythonOperator
import json
# connection sqlalchemy
data_folder = Path("C:/Users/iita/Documents/")


file_to_open = Path("C:/Users/iita/Documents/junction-hack-project/traffic") / "gotValues.json"
with open(file_to_open, 'rb') as f:
    print(f.read(1000))
    f.seek(-1000, 2)
    print()
    print(f.read(1000))

import os
os.exit(1)



file_to_open = data_folder / "conn.txt"

with open(file_to_open) as f:
    database_connection_string = f.read()

engine = create_engine(database_connection_string)
conn = engine.connect()

# MetaData
metadata = sa.MetaData(engine)

#test_table = sa.Table(
#    'test_table',
#    metadata,
#    sa.Column('column1', sa.Integer)
#)



data_folder = Path("C:/Users/iita/Documents/junction-hack-project/traffic")

file_to_open = data_folder / "gotValues.json"

with open(file_to_open, 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df.to_sql('business_finland_massive', conn)
#metadata.create_all(engine)

#with open(file_to_open, 'r') as f:
#    data = f.read(600)
#print(data)