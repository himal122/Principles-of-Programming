class Rectangle:
    def __init__(self, width=1.0, height=1.0):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * (self.width + self.height)

# Test
rect1 = Rectangle(4, 40)
rect2 = Rectangle(3.5, 35.9)

print(f"Rectangle 1 - Width: {rect1.width}, Height: {rect1.height}, Area: {rect1.getArea()}, Perimeter: {rect1.getPerimeter()}")
print(f"Rectangle 2 - Width: {rect2.width}, Height: {rect2.height}, Area: {rect2.getArea()}, Perimeter: {rect2.getPerimeter()}")
