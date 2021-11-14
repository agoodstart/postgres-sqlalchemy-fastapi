from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils.functions import database
from .postgresdb import Database

database = Database()
database.create_db_connection("EmployeeDB")

# Each instance of the SessionLocal class will be a database session, this instance will be the actual database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database.engine)