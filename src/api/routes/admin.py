from datetime import timedelta
from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm.session import Session

from api.auth.admins import validate_admin

from api import deps
from api.crud import admin
from api.schemas.admin import Admin, AdminCreate

from api.auth.jwthandle import (
    create_access_token,
    get_current_admin,
    ACCESS_TOKEN_EXPIRES,
)

admin_router = APIRouter(
    prefix="/api/v1/auth",
    tags=["admin"]
)

@admin_router.post('/signup', status_code=201, response_model=Admin)
def create_admin_signup(
    *,
    db: Session = Depends(deps.get_db),
    admin_in: AdminCreate,
):
    return admin.create_admin(db=db, admin_in=admin_in)

@admin_router.post('/login')
def login(
    db: Session = Depends(deps.get_db),
    admin_form: OAuth2PasswordRequestForm = Depends()
):
    admin = validate_admin(admin_form)

    if not admin:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRES)
    access_token = create_access_token(
        data={"sub": admin.admin_email}, expires_delta=access_token_expires
    )
    token = jsonable_encoder(access_token)
    content = {"message": "Log in succesfull"}
    response = JSONResponse(content=content)
    response.set_cookie(
        "Authorization",
        value=f"Bearer {token}",
        httponly=True,
        max_age=1800,
        expires=1800,
        samesite="Lax",
        secure=False
    )

    return response

@admin_router.get('/me', response_model=Admin, dependencies=[Depends(get_current_admin)])
def read_admins_me(current_admin: Admin = Depends(get_current_admin)):
    return current_admin