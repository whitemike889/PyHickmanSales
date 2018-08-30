from typing import Optional


class Vehicle:
    """
    Represents a vehicle listed for sale.
    """

    make: str
    model: str
    trim: str
    vin: str
    year: int
    msrp: Optional[int]
    price: Optional[int]
    colour: str
    stock_number: str
    url: str

    @staticmethod
    def _process_price(price: str) -> Optional[int]:
        """
        Processes the price string from the data-params object into a more usable form
        :param price: The price string
        :return: The int value of the price if it is able to be processed, otherwise None
        """
        price = "".join(i for i in price if i not in "$,")
        try:
            return int(price)
        except ValueError:
            return None

    def __init__(self, make: str, model: str, trim: str, vin: str, year: str, msrp: str, price: str, colour: str, stock_number: str, url: str):
        self.make = make
        self.model = model
        self.trim = trim
        self.vin = vin
        self.year = int(year)
        self.msrp = self._process_price(msrp)
        self.price = self._process_price(price)
        self.colour = colour
        self.stock_number = stock_number
        self.url = url
