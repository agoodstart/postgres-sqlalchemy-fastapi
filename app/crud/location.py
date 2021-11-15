from sqlalchemy.orm import Session, aliased

from app.models.location import Location

def get_locations(db: Session):
    return db.query(Location).offset(0).limit(100).all()