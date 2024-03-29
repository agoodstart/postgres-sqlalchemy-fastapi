from sqlalchemy.orm import Session

from api.models.department import Department

def get_departments(db: Session):
    return db.query(Department).offset(0).limit(100).all()