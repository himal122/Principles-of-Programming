from nav_sys import NavSys

# Create a stock item with 10 units, price 99.99, stock code NS101, and brand TomTom
item = NavSys("NS101", 10, 99.99, "TomTom")

print("Creating a stock with 10 units Navigation system, price 99.99, item \ncode NS101, and brand TomTom")

# Printing item stock information
print("Printing item stock information: ")
print(item)

# Increase 10 more units
print("\nIncreasing 10 more units")

item.increase_stock(10)
print("Printing item stock information:")
print(item)

# Sell 2 units
print("\nSold 2 units")

item.sell_stock(2)
print("Printing item stock information:")
print(item)

# Set a new price of 100.99 per unit
print("\nSet new price 100.99 per unit")

item.set_price(100.99)
print("Printing item stock information:")
print(item)

# Increase 0 more units (this should trigger an error)
print("\nIncreasing 0 more units")
try:
    item.increase_stock(0)
except ValueError as e:
    print(f"The error was: {e}")
