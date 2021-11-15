from typing import List

from .base import BaseConfig
from .location import Location

class Country(BaseConfig):
    country_id: str
    country_name: str
    region_id: int
    locations: List[Location] = None