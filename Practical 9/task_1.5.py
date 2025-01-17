class Shape:
    
 #constructor for Shape class
 def __init__(self, colour='Black'):
    self.__colour = colour
    # self._colour = colour
    print("Shape constructor is called")
 
 def displayShape(self):
    print("Shape is displaying")
    
 def getColour(self):
    return self.colour

class Rectangle(Shape):
    
 def __init__(self):
    super().__init__()
    print("Rectangle constructor is called")
    
 def displayRectangle(self):
    print("Rectangle is displaying")
    
 def getRectangleColour(self):
    return self.getColour

rec = Rectangle()
print(rec.getRectangleColour())