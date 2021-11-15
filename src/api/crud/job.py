from sqlalchemy.orm import Session, aliased

from api.models.job import Job

def get_jobs(db: Session):
    return db.query(Job).offset(0).limit(100).all()