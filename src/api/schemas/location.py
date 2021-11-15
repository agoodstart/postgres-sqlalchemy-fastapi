from typing import List, Optional

from .base import BaseConfig
from .department import Department

class Location(BaseConfig):
    location_id: int
    street_address: str
    postal_code: Optional[str] = None
    city: str
    state_province: Optional[str] = None
    country_id: str
    departments: List[Department] = None