from sqlalchemy.orm import Session

from app.models.region import Region

def get_region(db: Session, region_id):
    return db.query(Region).filter(Region.id == region_id).first()

def get_regions(db: Session):
    return db.query(Region).offset(0).limit(100).all()