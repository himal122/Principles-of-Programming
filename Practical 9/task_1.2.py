class Shape:
    
 #constructor for Shape class
 def __init__(self):
    print("Shape constructor is called")
    
 def displayShape(self):
    print("Shape is displaying")
    
class Rectangle(Shape):
 #constructor for Rectangle class
 def __init__(self):
     print("Rectangle constructor is called")
     
 def displayRectangle(self):
    print("Rectangle is displaying")
    
rec = Rectangle()
rec.displayShape()
rec.displayRectangle()
