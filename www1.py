import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __lt__(self, other):
        return 2 * math.pi * self.radius < 2 * math.pi * other.radius

    def __gt__(self, other):
        return 2 * math.pi * self.radius > 2 * math.pi * other.radius

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self


c1 = Circle(5)
c2 = Circle(7)

print(c1 == c2)
print(c1 < c2)
print(c1 > c2)

c1 += 2
print(c1.radius)

c1 -= 3
print(c1.radius)

