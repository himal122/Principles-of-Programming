
from stock_item import StockItem

class NavSys(StockItem):
    """
    represents a navigation system, inherits from StockItem.

    Attributes:
        __brand (str): Brand name of the navsys.
    """
    def __init__(self, stock_code, quantity, price, brand, vat_rate=17.5, max_quantity=100):
        """
        Initialize a new NavSys instance.

        Args:
            stock_code (str): Unique code for the stock item.
            quantity (int): Initial quantity of the item.
            price (float): Price of the item.
            brand (str): Brand name of the navsys.
            vat_rate (float): VAT rate for the item (default 17.5%).
            max_quantity (int): Maximum allowed quantity for the item (default 100).
        """

        super().__init__(stock_code, quantity, price, vat_rate, max_quantity)
        self.__brand = brand

    def get_stock_name(self):
        # get the name of NavSys. Returns: string name
        return "Navigation System"

    def get_stock_description(self):
        # get the description of NavSYs. Returns: string description
        return "GeoVision Sat Nav"

    def get_brand(self):
        # get the brand of the NavSys. Returns: brand name
        return self.__brand


    def __str__(self):
        """
        string representation of the NavSys.

        Returns:
            str: string describing the NavSys including its brand and stockItem.
        """
        return super().__str__() + f"\nBrand: {self.get_brand()}"
