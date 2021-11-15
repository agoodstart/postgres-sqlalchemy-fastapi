from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import functions
from . import schemas, models

def get_jobs(db: Session):
    return db.query(models.Job).offset(0).limit(100).all()