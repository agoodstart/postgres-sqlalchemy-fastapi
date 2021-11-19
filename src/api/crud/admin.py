from fastapi import HTTPException
from passlib.context import CryptContext
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, aliased

from api.deps import get_db

from api.models.admin import Admin as AdminModel
from api.schemas.admin import Admin as AdminSchema, AdminCreate as AdminSchemaCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def search_admin(db: Session, email: str):
    return db.query(AdminModel).filter(AdminModel.admin_email == email).first()

def create_admin(db: Session, *, admin_in: AdminSchemaCreate) -> AdminSchema:
    admin_in.admin_password = pwd_context.encrypt(admin_in.admin_password)

    try:
        admin_obj = AdminModel(
            **admin_in.dict()
        )
        db.add(admin_obj)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=401, detail="That email already exists.")

    return admin_obj

# def create_admin(entry: AdminCreate, db: Session):
#     entry = AdminModel(
#     )
#     db.add(entry)
#     db.commit()
#     db.refresh(entry)
#     return entry