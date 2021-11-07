from config import config
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists

class Database(object):
    def __init__(self):
        self.params = config()

    def create_db_connection(self, db_name):
        user, host, dbapi = self.params['user'], self.params['host'], self.params['dbapi']
        pw = self.params['password']
        url = 'postgresql+{}://{}:{}@{}/{}'
        url = url.format(dbapi, user, pw, host, db_name)
        self.engine = create_engine(url)

        if not database_exists(self.engine.url):
            print('Database not found')
