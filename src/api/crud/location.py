from sqlalchemy.orm import Session, aliased

from api.models.location import Location

def get_locations(db: Session):
    return db.query(Location).offset(0).limit(100).all()