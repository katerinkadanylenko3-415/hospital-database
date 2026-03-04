class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        print("Math")

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def area(self):
        print(3.14 * (self.radius ** 2))

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height

    def area(self):
        print(self.width * self.height)

class Triangle(Shape):
    def __init__(self, a, b):
        super().__init__("triangle")
        self.a = a
        self.b = b

    def area(self):
        print(0.5 * self.a * self.b)


#2

class Mathtools:

    @staticmethod
    def add(a, b):
        return a + b

print(Mathtools.add(1, 2))



# class User:
#     def __init__(self, name, age):
#         self.name = name
#         if not User.is_valid_age(age):
#             raise ValueError("Age must be positive")
#         self.age = age
#
#     @staticmethod
#     def is_valid_age(age):
#         return age > 0
#
# user1 = User("John", 20)
# print(User.is_valid_age(10))

#3
class Validator:
    @staticmethod
    def is_email(text):
        return "@" in text and "." in text





