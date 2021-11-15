from sqlalchemy.sql.schema import MetaData
from .session import database

Mdata = MetaData(bind=database.engine)
Mdata.reflect(views=True)