from stock_item import StockItem

class NavSys(StockItem):
    def __init__(self, stock_code, quantity, price, brand):
        super().__init__(stock_code, quantity, price)
        self.__brand = brand

    def get_stock_name(self):
        pass

    def get_stock_description(self):
        pass

    def get_brand(self):
        return self.__brand

    def __str__(self):
        return super().__str__() + f"\nBrand: {self.__brand}"