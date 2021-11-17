from sqlalchemy.orm import Session
from sqlalchemy.sql import functions

from api.db.metadata import Mdata
from api.models.employee import Employee, Manager
from api.schemas.employee import EmployeeCreate

def get_employees(db: Session):
    return db.query(Employee).offset(0).limit(100).all()

def get_employees_from_small_list(db: Session):
    els = Mdata.tables['employee_list_small']
    return db.query(els).all()

def get_employees_from_full_list(db: Session):
    efl = Mdata.tables['employee_full_list']
    return db.query(efl).all()

def filter_from_small_list(select: str, search, db: Session):
    els = Mdata.tables['employee_list_small']
    list = []

    for query in db.query(els).filter(els.c[select].ilike(f"%{search}%")):
        list.append(query)
    return list

def get_managers(db: Session):
    return db.query(Manager).filter(Manager.employees != None).all()

def get_the_president(db: Session):
    return db.query(Employee).filter(Employee.job_id == 4).first()

def get_employee_row(employee_id: int, db: Session):
    efl = Mdata.tables['employee_full_list']
    return db.query(efl).filter(efl.c.employee_id == employee_id).first()

def get_view(db: Session):
    views = Mdata.tables['joined_view']
    return db.query(views).all()

def get_random_employee_from_view(db: Session):
    views = Mdata.tables['joined_view']
    return db.query(views).order_by(functions.random()).first()

def create_new_employee_entry(entry: EmployeeCreate, db: Session):
    entry = Employee(
        first_name=entry.first_name,
        last_name=entry.last_name,
        email=entry.email,
        phone_number=entry.phone_number or None,
        hire_date=entry.hire_date,
        job_id=entry.job_id,
        salary=entry.salary,
        manager_id=entry.manager_id or None,
        department_id=entry.department_id
    )
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry