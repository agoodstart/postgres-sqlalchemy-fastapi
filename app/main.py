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

@app.get('/regions/', response_model=List[schemas.Region])
def read_regions(db: Session = Depends(get_db)):
    regions = crud.get_regions(db)
    return regions

@app.get('/countries/', response_model=List[schemas.Country])
def read_countries(db: Session = Depends(get_db)):
    countries = crud.get_countries(db)
    return countries