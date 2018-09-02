from typing import TypeVar, Union, Optional, List

import requests
from lxml import html

from PyHickmanSales.vehicle import Vehicle
from .enums import Category, VehicleType

BASE_URL = "http://www.hickmanchev.ca/VehicleSearchResults"

T = TypeVar("T")
Parameter = Union[List[T], T]


def _process_parameter(param: Parameter[T]) -> Optional[Union[str, T]]:
    """
    Processes the parameters into a format that will work for requests and the website
    :param param: The parameter to process
    :return: The processed parameter
    """
    if not param:
        return None
    if isinstance(param, list):
        return ",".join(param).replace(" ", "%20")
    else:
        return param


def get_listings(*, category: Parameter[Category] = None, vehicle_type: Parameter[VehicleType] = None, make: Parameter[str] = None, model: Parameter[str] = None, year: Parameter[int] = None, **kwargs) -> List[Vehicle]:
    """
    Gets all sales listings that match the given filters.
    :param category: The category of sale
    :param vehicle_type: The type of vehicle
    :param make: The make of vehicle
    :param model: The model of vehicle
    :param year: The year of vehicle
    :param kwargs: Any custom filters
    :return: A list of vehicles that match
    """
    # Prepare all the parameters and make the request
    params = {
        "search": _process_parameter(category),
        "bodyType": _process_parameter(vehicle_type),
        "make": _process_parameter(make),
        "model": _process_parameter(model),
        "year": _process_parameter(year),
        "limit": 10000
    }
    params.update(kwargs)
    listings = requests.get(BASE_URL, params=params, headers={"User-Agent": "PyHickmanSales V1.1.0 (https://github.com/nint8835/PyHickmanSales)"})

    # Create a tree from the page and find the table containing the vehicles
    tree = html.fromstring(listings.content)
    cars = tree.xpath('//*[@id="card-view/card/d50da2b4-6e35-431c-8c4d-efd07b27015f"]/div[3]')[0].findall("section")

    vehicles = []

    for car in cars:
        # Convert the monstrous "data-params" value into a dictionary so we can get info out
        data_dict = {a.split(":")[0]: a.split(":")[1] for a in car.get("data-params").split(";") if a != ""}
        # Find the url to the vehicle's page
        url = car.find("div", {"class": "content"}).find("div", {"class": "title"}).find("h4").find("a").get("href")
        # Create a vehicle object and add it to the list
        vehicle = Vehicle(data_dict["make"], data_dict["model"], data_dict["trim"], data_dict["vin"], data_dict["year"], data_dict["featuredPrice"], data_dict["salePrice"], data_dict["exteriorColor"], data_dict["stockNumber"], url)
        vehicles.append(vehicle)

    return vehicles
