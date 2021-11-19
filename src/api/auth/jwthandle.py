import os
from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, Request
from fastapi import security
from fastapi.openapi.models import OAuthFlows
from fastapi.security import OAuth2
from fastapi.security.utils import get_authorization_scheme_param
from jose import JWTError, jwt
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session

from api import deps

from api.schemas.token import TokenData
from api.schemas.admin import AdminCreate as AdminCreateSchema
from api.models.admin import Admin as AdminModel

from api.crud.admin import search_admin

SECRET_KEY = "verysecret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRES = 30

class OAuth2PasswordBearerCookie(OAuth2):
    def __init__(
        self,
        token_url: str,
        scheme_name: str = None,
        scopes: dict = None,
        auto_error: bool = True
    ):
        if not scopes:
            scopes = {}
        
        flows = OAuthFlows(password={"tokenUrl": token_url, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        authorization: str = request.cookies.get("Authorization")
        
        scheme, param = get_authorization_scheme_param(authorization)

        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=401,
                    detail="Not authorized",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        
        return param

security = OAuth2PasswordBearerCookie(token_url="/api/v1/auth/login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

async def get_current_admin(
    db: Session = Depends(deps.get_db),
    token: str = Depends(security)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        admin_email: str = payload.get("sub")
        if admin_email is None:
            raise credentials_exception
        token_data = TokenData(admin_email=admin_email)
    except JWTError:
        raise credentials_exception
    
    try:
        user = search_admin(db, token_data.admin_email)
    except NoResultFound:
        raise credentials_exception

    return user