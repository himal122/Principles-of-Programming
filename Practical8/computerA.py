class ComputerA:
    # parameterised constructor

    def __init__(self, name, price):
        # initilialising instance/member variable age
        self.name = name  #private variable
        self.price = price  #private variable


    #setters 

    def setName(self, name):
      self.name = name

    def setPrice(self, price):
      self.price = price


    #getters 

    def getName(self):
      return self.name

    def getPrice(self):
      return self.price

    # an instance/member method
    def display(self):
        print("Computer's name is: " +str(self.getName())+ " and it's price is: "+str(self.getPrice()))


# User provides a valid computer name

isValidName = False

while not isValidName:
    computername = str(input("Enter computer's name: "))
    
    if 2 <= len(computername) <= 10:
            isValidName = True
    else:
            print("You must enter a valid name between 2 and 10 chars length")


# User provides a valid computer price

isValidPrice = False

while not isValidPrice:
    computerprice = float(input("Enter computer's price: "))

    if 99.99 <= computerprice <= 999.99:
            isValidPrice = True
    else:
            print("You must enter a valid price between 99.99 and 999.99")


#creating the comp object based on user's input
comp = ComputerA(computername,computerprice)

#displaying computer's information
comp.display()

#setting a different computer name using the setName method
comp.setName("Dell")

#setting a different computer name by accessing the name variable which is public
#comp.name = 'Dell'

#setting new price using the setPrice method
comp.setPrice(890.90)

#setting new price by accessing the price variable which is public
#comp.price = 890.90

#displaying computer's (new) information
comp.display()