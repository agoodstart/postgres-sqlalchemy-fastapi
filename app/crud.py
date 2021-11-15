from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import functions
from . import schemas, models
from .database import Mdata

def get_region(db: Session, region_id):
    return db.query(models.Region).filter(models.Region.id == region_id).first()

def get_regions(db: Session):
    return db.query(models.Region).offset(0).limit(100).all()

def get_countries(db: Session):
    return db.query(models.Country).offset(0).limit(100).all()

def get_locations(db: Session):
    return db.query(models.Location).offset(0).limit(100).all()

def get_departments(db: Session):
    return db.query(models.Department).offset(0).limit(100).all()

def get_jobs(db: Session):
    return db.query(models.Job).offset(0).limit(100).all()

def get_employees(db: Session):
    return db.query(models.Employee).offset(0).limit(100).all()

def get_managers(db: Session):
    return db.query(models.Manager).filter(models.Manager.employees != None).all()

def get_the_president(db: Session):
    return db.query(models.Employee).filter(models.Employee.job_id == 4).first()

def get_view(db: Session):
    views = Mdata.tables['joined_view']
    return db.query(views).all()