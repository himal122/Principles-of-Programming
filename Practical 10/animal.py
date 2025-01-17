from abc import *
class Animal(ABC):
    #constructor 
    def __init__(self, numberOfLegs):
        self.__numberOfLegs = numberOfLegs
        
    def setNumberOfLegs(self, numberOfLegs):
        self.__numberOfLegs = numberOfLegs

    def getNumberOfLegs(self):
        return self.__numberOfLegs

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def walk(self):
        pass

class Pet(ABC):
    def __init__(self, name):
        self.__name = name
    
    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def play(self):
        pass

class Spider(Animal):
    #constructor
    def __init__(self, numberOfLegs=8):
        super().__init__(numberOfLegs)

    def eat(self):
        print("spider eats fly")

    def walk(self):
        print("spider walks with "+str(self.getNumberOfLegs())+" legs")

    
class Cat(Animal, Pet):
    #constructor
    def __init__(self, numberOfLegs, name):
        Animal.__init__(self,numberOfLegs)
        Pet.__init__(self,name)

    def eat(self):
        print(str(self.getName())+" eats mice")

    def walk(self):
        print(str(self.getName())+" walks with "+str(self.getNumberOfLegs())+" legs")

    def play(self):
        print(str(self.getName())+" plays with tail")


class Fish (Animal, Pet):
    #constructor
    def __init__(self, numberOfLegs, name):
        Animal.__init__(self,numberOfLegs)
        Pet.__init__(self,name)

    def eat(self):
        print(str(self.getName())+" eats plants")

    def walk(self):
        print(str(self.getName())+" can't walk")

    def play(self):
        print(str(self.getName())+" plays pokemon")

s = Spider()
c = Cat(4, "Max")
f = Fish(0, "Nemo")

s.eat()
s.walk()
#c.eat()
#c.walk()
#c.play()
#f.eat()
#f.walk()
#f.play()

for x in (c,f):
    x.eat()
    x.walk()
    x.play()

