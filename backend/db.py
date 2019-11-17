import os
from flask_sqlalchemy import SQLAlchemy

dbHost=os.environ['POSTGRES_HOST']
dbDb=os.environ['POSTGRES_DB']
dbUser=os.environ['POSTGRES_USER']
dbPassword=os.environ['POSTGRES_PASSWORD']
dbPort="5432"
dbConnectionString = 'postgresql://'+dbUser+':'+dbPassword+'@'+dbHost+':'+dbPort+'/'+dbDb

db = SQLAlchemy()
