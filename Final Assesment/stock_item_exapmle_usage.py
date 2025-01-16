from stock_item import StockItem

# Create a stock item with 10 units, price 99.99, and stock code W101
item = StockItem("W101", 10, 99.99)

print("Creating a stock with 10 units Unknown item, price 99.99, \nand stock code W101")

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
