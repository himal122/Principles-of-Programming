class Car:
    def __init__(self, model, speed=0.0):
        self.__model = model
        self.__speed = speed

    def set_model(self, model):
        if 1 <= len(model) <= 50:
            self.__model = model
        else:
            print("Model name must be between 1 to 50 characters.")

    def get_model(self):
        return self.__model

    def set_speed(self, speed):
        if 0 <= speed <= 300:
            self.__speed = speed
        else:
            print("Speed must be between 0 to 300 km/h.")

    def get_speed(self):
        return self.__speed

    def accelerate(self, amount):
        new_speed = self.__speed + amount
        self.set_speed(new_speed)

    def brake(self, amount):
        new_speed = max(0, self.__speed - amount)
        self.set_speed(new_speed)

    def display(self):
        print(f"Car Model: {self.__model}, Current Speed: {self.__speed} km/h")

# User input for car model
is_valid_model = False
while not is_valid_model:
    car_model = input("Enter car model: ")
    if 1 <= len(car_model) <= 50:
        is_valid_model = True
    else:
        print("Model name must be between 1 to 50 characters.")

# User input for initial speed
is_valid_speed = False
while not is_valid_speed:
    try:
        initial_speed = float(input("Enter initial speed (0-300 km/h): "))
        if 0 <= initial_speed <= 300:
            is_valid_speed = True
        else:
            print("Speed must be between 0 to 300 km/h.")
    except ValueError:
        print("Please enter a valid number for speed.")

# Create car object
my_car = Car(car_model, initial_speed)


print("\nInitial car information:")
my_car.display()


my_car.accelerate(30)
print("\nAfter acceleration:")
my_car.display()


my_car.brake(10)
print("\nAfter braking:")
my_car.display()


my_car.set_speed(400)
my_car.set_model("SUBARUTOYOTAMERCEDESROLLSROYCEOPELPORCHEDODGEVOLKSWAGEN")

