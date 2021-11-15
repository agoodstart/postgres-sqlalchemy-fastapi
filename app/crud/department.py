from sqlalchemy.orm import Session
from . import models

def get_departments(db: Session):
    return db.query(models.Department).offset(0).limit(100).all()