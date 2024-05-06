import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x=0, y=0, radius=0):
        self.center = Point(x, y)
        self.radius = radius

    def subtract(self, other):
        if isinstance(other, Circle):
            dx = self.center.x - other.center.x
            dy = self.center.y - other.center.y
            distance = math.sqrt(dx**2 + dy**2)
            new_radius = abs(self.radius - other.radius)
            if new_radius == 0:
                return Point(self.center.x, self.center.y)
            else:
                return Circle(self.center.x, self.center.y, new_radius)
        else:
            raise ValueError("Cannot subtract a non-circle object")


circle1 = Circle(0, 0, 5)
circle2 = Circle(3, 4, 3)
circle3 = Circle(0, 0, 5)

result = circle1.subtract(circle2)
print("Result 1:", result.radius)

result = circle1.subtract(circle3)
print("Result 2:", result.x, result.y)
