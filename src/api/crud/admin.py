from sqlalchemy.orm import Session, aliased

from api.models.admin import Admin as AdminModel
from api.schemas.admin import Admin as AdminSchema, AdminCreate as AdminSchemaCreate

def search_admin(db: Session, email: str):
    return db.query(AdminModel).filter(AdminModel.admin_email == email).first()

# def create_admin(db: Session, *, admin_in: AdminSchemaCreate) -> AdminSchema:

