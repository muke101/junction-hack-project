
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


data_folder = Path("./")

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

data_folder = Path("./trafficData")
for x in os.listdir(data_folder)[1:]:
    file_to_open = data_folder / x
    with open(file_to_open, 'r') as f:
        data = json.load(f)

    df = pd.DataFrame(data)
    df.to_sql('business_finland_massive', conn, if_exists='append')

#metadata.create_all(engine)

#with open(file_to_open, 'r') as f:
#    data = f.read(600)
#print(data)