from typing import TypeVar, Union, Optional, List

import requests

from .enums import Category, VehicleType

BASE_URL = "http://www.hickmanchev.ca/VehicleSearchResults"

T = TypeVar("T")
Parameter = Union[List[T], T]


def process_parameter(param: Parameter[T]) -> Optional[Union[str, T]]:
    if not param:
        return None
    if isinstance(param, list):
        return ",".join(param).replace(" ", "%20")
    else:
        return param


def get_listings(*, category: Parameter[Category] = None, vehicle_type: Parameter[VehicleType] = None, make: Parameter[str] = None, model: Parameter[str] = None, year: Parameter[int] = None, **kwargs):
    params = {
        "search": process_parameter(category),
        "bodyType": process_parameter(vehicle_type),
        "make": process_parameter(make),
        "model": process_parameter(model),
        "year": process_parameter(year),
        "limit": 10000
    }
    params.update(kwargs)

    listings = requests.get(BASE_URL, params=params)
    return listings.content
