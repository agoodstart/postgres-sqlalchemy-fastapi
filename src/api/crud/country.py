from sqlalchemy.orm import Session, aliased

from api.models.country import Country

def get_countries(db: Session):
    return db.query(Country).offset(0).limit(100).all()