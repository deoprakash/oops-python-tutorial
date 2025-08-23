''' Calculate Area and perimeter of circle.'''

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def perimeter(self):
        return (2 * 3.14 * self.radius)

    @property
    def area(self):
        return (3.14 * self.radius * self.radius)
    
c1 = Circle(5)
print("Area: ", c1.area)
print("Perimeter: ", c1.perimeter)