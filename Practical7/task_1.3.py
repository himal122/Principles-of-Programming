class Kitten: 

# constructor 
    def __init__(self): 
    #initilialising instance/member variable age 

        self.age=1 

    #an instance/member method 
    def display_age(self): 
        print(self.age) 

# creating object of the class. This invokes constructor 
kitt = Kitten() 

# calling the instance/member method using the object kitt 
kitt.display_age() 