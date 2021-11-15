from sqlalchemy.orm import Session, aliased
from sqlalchemy.sql import functions
from . import schemas, models

def get_region(db: Session, region_id):
    return db.query(models.Region).filter(models.Region.id == region_id).first()

def get_regions(db: Session):
    return db.query(models.Region).offset(0).limit(100).all()