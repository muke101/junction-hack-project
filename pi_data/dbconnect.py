import sqlalchemy as sa
import os
import pandas

def dbConnect(
            host=os.environ['POSTGRES_HOST'],
            db=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            port="5432", name=None
            ):
    
    dbConnectionString = 'postgressql://'+user+':'+password+'@'+host+'/'+db+'/'+port
    
    engine = sa.create_engine(dbConnectionString)

    if name == None:
        return engine

    metadata = sa.MetaData(engine)
    bf15 = sa.Table(
        name,
        metadata,
        autoload=True
        autoload_with=engine
        )
    
    return engine, bf15

def dbPush(data, name, conn):
    df = pd.DataFrame(data)
    df.to_sql(name, conn)

