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

def get_all(db: Session):
    emp = aliased(models.Employee)
    man = aliased(models.Employee)
    jobs = aliased(models.Job)
    departments = aliased(models.Department)
    locations = aliased(models.Location)
    countries = aliased(models.Country)
    regions = aliased(models.Region)

    q = db.query(
        emp.first_name.label('first_name'),
        emp.last_name.label('last_name'),
        emp.salary.label('salary'),
        jobs.job_title.label('job_title'),
        functions.concat(man.first_name, ' ', man.last_name).label("manager_full_name"),
        departments.department_name.label('department_name'),
        functions.concat(locations.city, ', ', countries.country_name, ', ', regions.region_name).label('current_location')).\
            join(man, emp.manager_id == man.employee_id, isouter=True).\
            join(jobs, jobs.job_id == emp.job_id).\
            join(departments, departments.department_id == emp.department_id).\
            join(locations, locations.location_id == departments.location_id).\
            join(countries, countries.country_id == locations.country_id).\
            join(regions, regions.region_id == countries.region_id).\
            order_by(emp.salary.desc()).\
            all()
    return q