from datetime import date
from typing import List, Optional, Sequence
from datetime import datetime

from pydantic import BaseModel

class AdminCreate(BaseModel):
    admin_email: str
    admin_password: str

class Admin(BaseModel):
    admin_email: str
    created_on: datetime
    last_login: datetime

