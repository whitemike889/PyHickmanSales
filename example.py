from PyHickmanSales import get_listings, Category

# Prints the stock number and VIN of all Cruze demo units for sale
cars = get_listings(make="Chevrolet", model="Cruze", category=Category.DEMO)

for car in cars:
    print(f"{car.stock_number}: {car.vin}")

# Gets the average price for a new Cadillac
cars = get_listings(make="Cadillac", category=Category.NEW)

total = 0
for car in cars:
    total += car.price

average = float(total)/len(cars)
print(f"\nAverage Cadillac price: ${average}")

# Gets the average price of a new or demo vehicle that is blue (uses a custom filter that isn't built in to the function, hence the strange capitalization)
cars = get_listings(bodyColor="Blue", category=[Category.NEW, Category.DEMO])

total = 0
for car in cars:
    total += car.price

average = float(total)/len(cars)
print(f"Average price for a blue vehicle: ${average}")

# Gets the total value of all the listed vehicles
cars = get_listings()
total = sum([car.msrp for car in cars])
print(f"Total value of all vehicles: ${total}")
