class Car:
    def __init__(self, number_of_doors, price, color, brand):
        self.number_of_doors = number_of_doors
        self.price = price
        self.color = color
        self.brand = brand

    def startCar(self):
        print("Car has started")

    def stopCar(self):
        print("Car has stopped")

    def setNumberOfDoors(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def getNumberOfDoors(self):
        return self.number_of_doors

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setBrand(self, brand):
        self.brand = brand

    def getBrand(self):
        return self.brand

# Test
car1 = Car(5, 20000, "White", "ToyCar")

print(f"Car - Number of Doors: {car1.getNumberOfDoors()}, Price: {car1.getPrice()}, Color: {car1.getColor()}, Brand: {car1.getBrand()}")
car1.startCar()
car1.stopCar()

# Changing car attributes
car1.setPrice(25000)
car1.setColor("Red")
car1.setBrand("SuperCar")

print(f"Updated Car - Number of Doors: {car1.getNumberOfDoors()}, Price: {car1.getPrice()}, Color: {car1.getColor()}, Brand: {car1.getBrand()}")
