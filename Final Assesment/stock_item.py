from datetime import datetime

class StockItem:
    """
    Represents Car Accessories Stock Mangement System

    Attributes:
        stock_category (str): Class variable of the stock item.
        __stock_code (str): Unique code for the stock item.
        __quantity (int): Current quantity of the item.
        __price (float): Price of the item.
        __vat_rate (float): VAT rate for the item.
        __max_quantity (int): Maximum quantity for the stock item.
        __last_updated (datetime): Last updateed time for the stock item.
    """

    stock_category = "Car accessories"

    def __init__(self, stock_code, quantity, price, vat_rate=17.5, max_quantity=100):
        """
        Initialize a new StockItem instance.

        Args:
            stock_code (str): Unique code for the stock item.
            quantity (int): Initial quantity of the item.
            price (float): Price of the item.
            vat_rate (float): VAT rate for the item (default 17.5%).
            max_quantity (int): Maximum allowed quantity for the item (default 100).
        """

        # Validation checks for non-negative price and quantity
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        if max_quantity < 1:
            raise ValueError("Maximum quantity must be at least 1.")
        

        # private instance variables
        self.__stock_code = stock_code
        self.__quantity = quantity
        self.__price = price
        self.__vat_rate = vat_rate
        self.__max_quantity = max_quantity
        self.__last_updated = datetime.now() # gives the current time


    def get_last_updated(self):
        # getter to get the last updated time
        return self.__last_updated.strftime('%Y-%m-%d %H:%M:%S')

    def get_stock_code(self):
        # Getter to get the stock code of the item.
        return self.__stock_code

    def get_quantity(self):
        # Getter for the current quantity of the item in stock.
        return self.__quantity

    def get_price(self):
        # Getter for the price of the item.
        return self.__price

    def set_price(self, price):
        # Setter for a new price for the item.
        self.__price = price
        self.__last_updated = datetime.now()

    def get_stock_name(self):
        # Get the name of the stock item.
        return "Unknown Stock Name"

    def get_stock_description(self):
        # Get the description of the stock item.
        return "Unknown Stock Description"

    def increase_stock(self, amount):
        # Increase the stock quantity by the provided amount.
        if amount < 1:
            raise ValueError("Increased item must be greater than or equal to one")
        if (self.__quantity + amount) > self.__max_quantity:
            raise ValueError(f"Stock cannot exceed more than {self.__max_quantity} units.")
        
        self.__quantity += amount
        self.__last_updated = datetime.now()


    def sell_stock(self, amount):
        # Decrease the stock quantity by the provided amount.
        if amount < 1:
            raise ValueError("Cannot sell less than one item.")
        if amount > self.__quantity:
            raise ValueError("Not enough stock to sell.")
        
        self.__quantity -= amount
        self.__last_updated = datetime.now()
        
        return True
        

    def get_vat(self):
        # Get the VAT rate.
        return self.__vat_rate
    
    
    def set_vat_rate(self, vat_rate):
        # update the VAT rate after the object is created.
        if vat_rate < 0:
            raise ValueError("VAT rate cannot be negative.")
        self.__vat_rate = vat_rate
        self.__last_updated = datetime.now()

    def get_price_with_vat(self):
        # Get the price including VAT.
        return self.__price * (1 + self.get_vat() / 100)
    
    def get_total_value(self, include_vat=False):
        price = self.get_price_with_vat() if include_vat else self.get_price()
        return price * self.__quantity
    
    def check_stock_level(self):
        # warnings related to the stock level
        if self.__quantity < 5:
            return "Low stock: Consider restocking."
        elif self.__quantity > 90:
            return "High stock: Might get overstocked."
        return "Stock levels are normal."
    

    def __str__(self):
        # Get a string representation of the stock item.
        return (
            f"Stock Category: {self.stock_category}\n"
            f"Stock Type: {self.get_stock_name()}\n"
            f"Description: {self.get_stock_description()}\n"
            f"StockCode: {self.get_stock_code()}\n"
            f"PriceWithoutVAT: {self.get_price():.2f}\n"
            f"PriceWithVAT: {self.get_price_with_vat():.2f}\n"
            f"Total unit in stock: {self.get_quantity()}\n"
            f"Total Value Without VAT: {self.get_total_value():.2f}\n"
            f"Total Value With VAT: {self.get_total_value(include_vat=True):.2f}\n"
            f"Stock Warning: {self.check_stock_level()}\n"
            f"Last Updated: {self.get_last_updated()}"
        )