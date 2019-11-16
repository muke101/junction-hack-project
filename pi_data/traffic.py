#function to pull data that gets called periodically
#counts total number of detections over peroid
#directly proportional to sub-coeff
#could possibly calculate density as well using ranges given rather than direct numbers
#at certain threshholds can send alerts like 'possible event happening here'
from sqlalchemy import create_engine
import os

host = os.environ['POSTGRES_HOST']
db = os.environ['POSTGRES_DB']
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
port = 5432
dbConnectionString = 'postgressql://+'user+':'+password+'@'+host+'/'+db+'/'port

engine = create_engine(dbConnectionString)

#SQL query goes here

totalNumber = 20


