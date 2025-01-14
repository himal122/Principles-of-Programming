class Kitten: 
    # constructor 
    # def __init__(self): 
    # initilialising instance/member variable age 
    #   self.age=1 
 
    # parameterised constructor 
 
    def __init__(self, value): 
        # initilialising instance/member variable age 
        self.age = value 
 
   #an instance/member method 
    def set_age(self,value): 
        self.age=value 
 
    # an instance/member method 
    def display_age(self): 
        print(self.age) 
 
# creating object of the class. This invokes parameterised constructor 
kitt = Kitten(3) 
 
kitt2 = Kitten(4) 
 
#This invokes default constructor 
#kitt3 = Kitten() 
 
# calling the instance/member method using the object kitt 
kitt.display_age() 
 
kitt2.display_age() 
 
kitt.display_age() 
 
kitt.set_age(5) 

kitt.display_age()

# What’s the difference between initialising the member variables using a parameterised (or 
# default) constructor and by calling set_age method? (Just write the answers as comments in the 
# code)

# ==> Initializing member variables using a constructor sets the initial state of the object when it's created.
# Using the set_age method allows changing the object's state after creation.
