from datetime import date
from typing import List, Optional, Sequence
from datetime import datetime

from .base import BaseConfig

class AdminCreate(BaseConfig):
    admin_email: str
    admin_password: str

class Admin(BaseConfig):
    admin_email: str
    created_on: datetime
    last_login: Optional[datetime] = None

