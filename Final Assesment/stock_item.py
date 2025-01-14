class StockItem:
    stock_category = "Car accessories"

    def __init__(self,stock_code,  quantity, price):
        self.__stock_code = stock_code
        self.__quantity = quantity
        self.__price = price

    def get_stock_code(self):
        return self.__stock_code

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def set_price(self, price):
        pass

    def get_stock_name(self):
        pass

    def get_stock_description(self):
        pass

    def increase_stock(self, amount):
        pass

    def sell_stock(self, amount):
        pass

    def get_vat():
        pass

    def get_price_with_vat(self):
        pass

    def __str__(self):
        pass