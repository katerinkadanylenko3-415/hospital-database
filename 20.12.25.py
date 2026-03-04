# Завдання 1
# Створіть клас Airplane (Літак). За допомогою перевантаження операторів, реалі­зуйте:
#
# перевірку на рівність типів літаків (операція = =);
# збільшення та зменшення пасажирів у салоні літака (операції +, -, +=, -=);
# порівняння двох літаків за максимально можливою кількістю пасажирів на борту (операції >, <, <=, >=).
import math
'''
class Plane:
    def __init__(self, planeType, pasangers, max_pasangers ):
        self.planeType = planeType
        self.pasangers = pasangers
        self.max_pasangers = max_pasangers

    def __eq__(self, other):
        return self.planeType == other.planeType

    def __iadd__(self, other):
        self.pasangers += other.pasangers
        return self

    def __isub__(self, other):
        self.pasangers -= other.pasangers
        return self

    def __lt__(self, other):
        return self.max_pasangers < other.max_pasangers

    def __gt__(self, other):
        return self.max_pasangers > other.max_pasangers

    def __le__(self, other):
        return self.max_pasangers <= other.max_pasangers

    def __ge__(self, other):
        return self.max_pasangers >= other.max_pasangers

plane1 = Plane(2, 5, 45)
plane2 = Plane(7, 5, 34)

print(plane1 == plane2)
print(plane1 < plane2)
print(plane1 > plane2)
print(plane1 <= plane2)
print(plane1 >= plane2)
'''

# Завдання 2
# Створіть клас Flat (Квартира). Реалізуйте перевантажені оператори:
#
# перевірку на рівність площ квартир (операція ==);
# перевірку на нерівність площ квартир (операція !=);
# порівняння двох квартир за ціною (операції >, <, <=, >=).
'''
class Flat:
    def __init__(self, S, price):
        self.S = S
        self.price = price

    def __eq__(self, other):
        return self.S == other.S

    def __ne__(self, other):
        return self.S != other.S

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price

flat1 = Flat(504, 500000)
flat2 = Flat(404, 300000)

print(flat1 == flat2)
print(flat1 != flat2)
print(flat1 < flat2)
print(flat1 > flat2)
print(flat1 <= flat2)
print(flat1 >= flat2)
'''

#3
# Завдання 3
# Створіть базовий клас Shape для рисування плоских фігур. Визначте методи:
#
# Show() — виведення на екран інформації про фігуру;
# Save() — збереження фігури у файл;
# Load() — зчитування фігури з файлу.
#
# Визначте похідні класи:
#
# Square — квадрат із заданими з координатами лівого верхнього кута та дов­жи­ною сторони.
# Rectangle — прямокутник із заданими координатами верхнього лівого кута та розмірами.
# Circle — коло із заданими координатами центру та радіусом.
# Ellipse — еліпс із заданими координатами верхнього кута описаного навколо нього прямокутника зі сторонами, паралельними осям координат, та розмірами цього прямокутника.
# Створіть список фігур, збережіть фігури у файл, завантажте в інший список та відобразіть інформацію про кожну фігуру

class Shape:
    def Show(self):
        print("Це плоска фігура!")

    def Save(self, file):
        pass

    def Load(self, data):
        pass


class Square(Shape):
    def __init__(self, x, y, length):
        self.x = x
        self.y = y
        self.length = length

    def Show(self):
        print(f"Квадрат: верхній лівий кут ({self.x}, {self.y}), сторона = {self.length}")

    def Save(self, file):
        file.write(f"Square {self.x} {self.y} {self.length}\n")

    def Load(self, data):
        self.x, self.y, self.length = map(int, data)


class Rectangle(Shape):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def Show(self):
        print(f"Прямокутник: верхній лівий кут ({self.x}, {self.y}), "
              f"довжина = {self.length}, ширина = {self.width}")

    def Save(self, file):
        file.write(f"Rectangle {self.x} {self.y} {self.length} {self.width}\n")

    def Load(self, data):
        self.x, self.y, self.length, self.width = map(int, data)


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def Show(self):
        print(f"Коло: центр ({self.x}, {self.y}), радіус = {self.radius}")

    def Save(self, file):
        file.write(f"Circle {self.x} {self.y} {self.radius}\n")

    def Load(self, data):
        self.x, self.y, self.radius = map(int, data)


class Ellipse(Shape):
    def __init__(self, x, y, length, width):
        self.x = x
        self.y = y
        self.length = length
        self.width = width

    def Show(self):
        print(f"Еліпс: верхній лівий кут ({self.x}, {self.y}), "
              f"Прямокутник - довжина = {self.length}, ширина = {self.width}")

    def Save(self, file):
        file.write(f"Ellipse {self.x} {self.y} {self.length} {self.width}\n")

    def Load(self, data):
        self.x, self.y, self.length, self.width = map(int, data)


shapes = [
    Square(10, 10, 5),
    Rectangle(0, 0, 10, 5),
    Circle(5, 5, 3),
    Ellipse(2, 2, 8, 4)
]

with open("shapes.txt", "w") as file:
    for shape in shapes:
        shape.Save(file)

loaded_shapes = []

with open("shapes.txt", "r") as file:
    for line in file:
        parts = line.split()
        figure_type = parts[0]
        data = parts[1:]

        if figure_type == "Square":
            shape = Square(0, 0, 0)
        elif figure_type == "Rectangle":
            shape = Rectangle(0, 0, 0, 0)
        elif figure_type == "Circle":
            shape = Circle(0, 0, 0)
        elif figure_type == "Ellipse":
            shape = Ellipse(0, 0, 0, 0)
        else:
            continue

        shape.Load(data)
        loaded_shapes.append(shape)

for shape in loaded_shapes:
    shape.Show()

import os

def show_tree(path, indent=""):
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            print(indent + f"[{item}]")
            show_tree(item_path, indent + "    ")
        else:
            print(indent + item)

show_tree("MyFolder")









