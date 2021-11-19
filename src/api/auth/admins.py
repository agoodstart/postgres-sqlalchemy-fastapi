from fastapi import HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import Session

from api import deps

from api.models.admin import Admin as AdminModel
from api.schemas.admin import Admin as AdminSchema
from api.crud.admin import search_admin

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_admin(db: Session, admin_email: str):
    return search_admin(db=db, email=admin_email)

# def validate_admin(
#     *,
#     admin_email: str,
#     admin_password: str
# ):
#     try:
#         entry = get_admin(admin_email)
#     except NoResultFound:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect email"
#         )
    
#     if not verify_password(admin_password, entry.admin_password):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect password"
#         )

#     return entry

def validate_admin(db: Session, form_data: OAuth2PasswordRequestForm = Depends()):
    try:
        entry = get_admin(db, form_data.username)
    except NoResultFound:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email"
        )
    
    if not verify_password(form_data.password, entry.admin_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password"
        )

    return entry