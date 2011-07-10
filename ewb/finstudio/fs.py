import pymssql
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

username, password, server, database = 'fibdbo', 'fibdbo', '172.28.10.60', 'fsdb_phoenix'

engine = create_engine('mssql+pymssql://%s:%s@%s/%s' % (username, password, server, database))
metadata = MetaData(engine)

def get_metadata():
    return metadata

from mappings.static import *

Session = sessionmaker(bind=engine, autoflush=True)
def get_entities(session=None):
    if not session:
        session = Session()
    return session.execute('SELECT * FROM t_entity')

