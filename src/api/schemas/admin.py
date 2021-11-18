from datetime import date
from typing import List, Optional, Sequence
from datetime import datetime

from pydantic import BaseModel, EmailStr

class AdminCreate(BaseModel):
    admin_email: EmailStr
    admin_password: str

class Admin(BaseModel):
    admin_email: EmailStr
    created_on: datetime
    last_login: datetime

