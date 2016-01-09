class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y
    def perimeter(self):
        return 2*self.x + 2*self.y
    def scale_size(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale 

class Square(Rectangle):
    def __init__(self, x):
        self.x, self.y = x

class DoubleSquare(Square):
    def __init__(self, y):
        self.x = 2 * y
        self.y = y
    def perimeter(self):
        return 2*self.x + 3*self.y