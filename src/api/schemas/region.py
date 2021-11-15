from typing import List

from .base import BaseConfig
from .country import Country

class Region(BaseConfig):
    region_id: int
    region_name: str
    countries: List[Country] = None