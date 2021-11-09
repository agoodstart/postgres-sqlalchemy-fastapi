from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def read_all(db: Session = Depends(get_db)):
    result = crud.get_all(db)

    return result

@app.get('/regions/', response_model=List[schemas.Region])
def read_regions(db: Session = Depends(get_db)):
    regions = crud.get_regions(db)
    return regions

@app.get('/countries/', response_model=List[schemas.Country])
def read_countries(db: Session = Depends(get_db)):
    countries = crud.get_countries(db)
    return countries

@app.get('/locations/', response_model=List[schemas.Location])
def read_locations(db: Session = Depends(get_db)):
    locations = crud.get_locations(db)
    return locations

@app.get('/departments/', response_model=List[schemas.Department])
def read_departments(db: Session = Depends(get_db)):
    departments = crud.get_departments(db)
    return departments

@app.get('/jobs/', response_model=List[schemas.Job])
def read_jobs(db: Session = Depends(get_db)):
    jobs = crud.get_jobs(db)
    return jobs

@app.get('/employees/', response_model=List[schemas.Employee])
def read_employees(db: Session = Depends(get_db)):
    employees = crud.get_employees(db)
    return employees

@app.get('/managers/', response_model=List[schemas.Manager])
def read_employees(db: Session = Depends(get_db)):
    managers = crud.get_managers(db)
    return managers

@app.get('/employees/president/', response_model=schemas.Employee)
def read_president(db: Session = Depends(get_db)):
    president = crud.get_the_president(db)
    return president