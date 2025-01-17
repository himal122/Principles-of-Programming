class Shape:
    
 def displayShape(self):
    print("Shape is displaying")
    
class Rectangle(Shape):
    
 def displayRectangle(self):
    print("Rectangle is displaying")
    
rec = Rectangle()
rec.displayShape()
rec.displayRectangle()