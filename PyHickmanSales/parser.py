from typing import TypeVar, Union, Optional, List

import requests
from lxml import html

from PyHickmanSales.vehicle import Vehicle
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


def get_listings(*, category: Parameter[Category] = None, vehicle_type: Parameter[VehicleType] = None, make: Parameter[str] = None, model: Parameter[str] = None, year: Parameter[int] = None, **kwargs) -> List[Vehicle]:
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
    tree = html.fromstring(listings.content)

    cars = tree.xpath('//*[@id="card-view/card/d50da2b4-6e35-431c-8c4d-efd07b27015f"]/div[3]')[0].findall("section")

    vehicles = []

    for car in cars:
        data_dict = {a.split(":")[0]: a.split(":")[1] for a in car.get("data-params").split(";") if a != ""}
        url = car.find("div", {"class": "content"}).find("div", {"class": "title"}).find("h4").find("a").get("href")
        vehicle = Vehicle(data_dict["make"], data_dict["model"], data_dict["trim"], data_dict["vin"], data_dict["year"], data_dict["featuredPrice"], data_dict["salePrice"], data_dict["exteriorColor"], data_dict["stockNumber"], url)
        vehicles.append(vehicle)

    return vehicles