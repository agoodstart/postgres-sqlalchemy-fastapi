from sqlalchemy.orm import Session

from api.db.metadata import Mdata
from api.models.employee import Employee, Manager

def get_employees(db: Session):
    return db.query(Employee).offset(0).limit(100).all()

def get_managers(db: Session):
    return db.query(Manager).filter(Manager.employees != None).all()

def get_the_president(db: Session):
    return db.query(Employee).filter(Employee.job_id == 4).first()

def get_view(db: Session):
    views = Mdata.tables['joined_view']
    return db.query(views).all()