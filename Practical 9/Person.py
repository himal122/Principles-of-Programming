class Person:
    #constructor
    def __init__(self, firstName='Mr', lastName='X', address='Bristol'):
        self.__firstName = firstName #private variable
        self.__lastName = lastName   #private variable
        self.__address = address     #private variable

    def setFirstName(self, firstName):
        self.__firstName = firstName

    def setLastName(self, lastName):
        self.__lastName = lastName

    def setAddress(self,address):
        self.__address = address

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getAddress(self):
        return self.__address

    def __str__(self):
        return "Person's name is " + self.getFirstName() +" "+ self.getLastName() +"\nAddress is "+ self.getAddress()


#creating Lecturer subclass
class Lecturer(Person):
    #defining constructor
    def __init__(self, firstName, lastName, address, lecturerID):
        self.__lecturerID = lecturerID #private variable
        #calling base class constructor
        super().__init__(firstName, lastName, address)

    #settter
    def setLecturerID(self,lecturerID):
        self.__lecturerID = lecturerID

    #getter
    def getLecturerID(self):
        return self.__lecturerID
    
    #overridding __str__
    def __str__(self):
        #using base class super
        return super().__str__()+"\nLecturer's ID is "+str(self.getLecturerID())



#creating Student class
class Student (Person):
    #can be implemented like Lecturer
    #use bases class __str__ 
    pass


#creating GraduateStudent class
class GraduateStdent (Student):
    #can be implemented like other sub classes
    #use bases class __str__  [in this case it is Student]
    pass



#creating a Person object with default values
print("Creating a Person object with default values")
p =  Person()
#printing the information using __str__ method
print("Printing the information using __str__ method")
print(p)
#setting name and address
print("Now setting the names and address")
p.setFirstName("Abdur")
p.setLastName("Rakib")
p.setAddress("UWE Frenchay Campus 4QXX")
#printing the information using __str__ method
print("Printing the information using __str__ method")
print(p)
#Creating another object by passing the values explicitly 
print("Creating another Person object by passing the values explicitly")
p1 = Person("Jun", "Hong", "UWE Frenchay Campus 3QXX")
#printing the information using __str__ method
print("Printing the information using __str__ method")
print(p1)


#Creating a Lecturer object by passing the values explicitly
l = Lecturer("Kun", "Wei", "UWE FC 4QXX", 1234)

#printing the information using __str__ method
print("Printing the information using __str__ method")
print(l)

