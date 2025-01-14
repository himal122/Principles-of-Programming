class Kitten: 
    breed = 'Abyssinian'   # class variable shared by all instances 
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
 
print(kitt.breed)      # shared by all kittens 
print(kitt2.breed)     # shared by all kittens 
print(Kitten.breed)    #breed is accessed using the Class 
# print(Kitten.age)      # instance variable cannot be accessed via Class

#changing the breed value 
Kitten.breed = 'American Bobtail' 

print(kitt.breed)      
# shared by all kittens 
print(kitt2.breed)     
# shared by all kittens