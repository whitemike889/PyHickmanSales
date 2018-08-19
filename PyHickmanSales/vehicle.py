class Vehicle:
    """
    Represents a vehicle listed for sale.
    """

    make: str
    model: str
    trim: str
    vin: str
    year: int
    msrp: int
    price: int
    colour: str
    stock_number: str
    url: str

    def __init__(self, make: str, model: str, trim: str, vin: str, year: str, msrp: str, price: str, colour: str, stock_number: str, url: str):
        self.make = make
        self.model = model
        self.trim = trim
        self.vin = vin
        self.year = int(year)
        self.msrp = int("".join(i for i in msrp if i not in "$,"))
        self.price = int("".join(i for i in price if i not in "$,"))
        self.colour = colour
        self.stock_number = stock_number
        self.url = url