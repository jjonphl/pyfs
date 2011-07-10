import pymssql
from sqlalchemy import create_engine

class Connection(object):
    def __init__(self, server, username, password):
        self.engine = create_engine('mssql+pymssql://%s:%s@%s' % (username, password, server))
        self.metadata = MetaData(self.engine)
