# Pydantic models (schemas) that will be used when reading data, when returning it from the API.
# For example, before creating an item, we don't know what will be the ID assigned to it, but when reading it (when returning it from the API) we will already know its ID.

from typing import List, Optional, Union, Dict

from pydantic import BaseModel

class LocationBase(BaseModel):
    city: str
    state_province: str
    country_id: str

# class LocationCreate(BaseModel):


# class Location(LocationBase):

class CountryBase(BaseModel):
    country_id: str
    country_name: str
    region_id: int

class CountryCreate(BaseModel):
    pass

class Country(CountryBase):
    class Config:
        orm_mode = True

class RegionBase(BaseModel):
    region_id: int
    region_name: str
    countries: List[Country] = None

class RegionCreate(BaseModel):
    pass

class Region(RegionBase):
    class Config:
        orm_mode = True