class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def perimeter(self):
        return 2 * (self.width + self.height)
    def area(self):
        return self.width * self.height

rect = Rectangle(3,4)
print("Area:", rect.area(), "perimeter:", rect.perimeter())