from abc import *
class Person(ABC):
    #constructor 
    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    def __str__(self):
        return "Person's name is: "+self.getName()+ " and Address is: "+self.getAddress()

    @abstractmethod
    def studentship(self):
        pass


class Student(Person):
    #constructor
    def __init__(self, name, address, studentID):
        super().__init__(name, address)
        self.__studentID = studentID

    def studentship(self):
        if self.__studentID == 0:
            print("The person is Not a Student")

        else:
            print("The person is a Student")

    def __str__(self):
        return super().__str__()

stud1 = Student("Peter Miller", "Frenchay Campus", 0)
stud2 = Student("Max Miller", "Glenside Campus", 1234)
stud1.studentship()
stud2.studentship()
print(stud1)
print(stud2)

p = Person("Abstract Person", "Heaven")    

