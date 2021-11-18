from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session

from api import deps
from api.crud import admin
from api.schemas.admin import Admin, AdminCreate

admin_router = APIRouter(
    prefix="/api/v1/auth",
    tags=["admin"]
)

# @admin_router.post('/signup', status_code=201, response_model=Admin)
# def create_admin_signup(
#     *,
#     db: Session = Depends(deps.get_db),
#     admin_in: AdminCreate,
# ) -> Admin:
#     new_admin = admin.search_admin(admin_in.admin_email)
#     if new_admin:
#         raise HTTPException(
#             status_code=400,
#             detail="Email already exists"
#         )
#     # new_admin
#     return {"msg": "Can create account"}

@admin_router.post('/signup', status_code=201, response_model=Admin)
def create_admin_signup(
    *,
    db: Session = Depends(deps.get_db),
    admin_in: AdminCreate,
):
    return admin.create_admin(db=db, admin_in=admin_in)