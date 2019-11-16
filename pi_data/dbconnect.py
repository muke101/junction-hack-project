from sqlalchemy import create_engine
import os

def dbConnect(
            host=os.environ['POSTGRES_HOST'],
            db=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            port="5432"
            ):
    
    dbConnectionString = 'postgressql://'+user+':'+password+'@'+host+'/'+db+'/'+port
    
    engine = create_engine(dbConnectionString)
    
    return engine

