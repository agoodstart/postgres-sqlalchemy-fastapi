from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import functions
from . import schemas, models

def get_locations(db: Session):
    return db.query(models.Location).offset(0).limit(100).all()