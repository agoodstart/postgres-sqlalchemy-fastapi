from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.schema import MetaData

SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost/EmployeeDB'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Each instance of the SessionLocal class will be a database session, this instance will be the actual database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Mdata = MetaData(bind=engine)
Mdata.reflect(views=True)

Base = declarative_base()