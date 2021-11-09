from sqlalchemy.orm import Session

from . import schemas, models

def get_region(db: Session, region_id):
    return db.query(models.Region).filter(models.Region.id == region_id).first()

def get_regions(db: Session):
    return db.query(models.Region).offset(0).limit(100).all()

def get_countries(db: Session):
    return db.query(models.Country).offset(0).limit(100).all()
