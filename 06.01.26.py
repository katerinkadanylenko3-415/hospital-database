# from abc import ABC, abstractmethod
#
#
# class Transport(ABC):
#     @abstractmethod
#     def move(self):
#         pass
#
#     def info(self):
#         print("Це транспортний засіб")
#
# class Car(Transport):
#     def move(self):
#         print("Автомобіль їде по дорозі")
#
#
# class Bicycle(Transport):
#     def move(self):
#         print("Велосипед рухається педалями")
#
#
# class Train(Transport):
#     def move(self):
#         print("Поїзд рухається по рейках")
#
# transports = [Car(), Bicycle(), Train()]
# for t in transports:
#     t.info()
#     t.move()

#2
# from abc import ABC, abstractmethod
#
# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     def get_info(self):
#         print("It`s an animal")
#
#
# class Dog(Animal):
#     def make_sound(self):
#         print("It`s a dog")
#
# class Cat(Animal):
#     def make_sound(self):
#         print("It`s a cat")
#
# class Bird(Animal):
#     def make_sound(self):
#         print("It`s a bird")
#
# animals = [Dog(), Cat(), Bird()]
# for a in animals:
#     a.get_info()
#     a.make_sound()

# from abc import ABC, abstractmethod
#
# class Transport(ABC):
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed
#
#     @abstractmethod
#     def move(self):
#         pass
#
#     def info(self):
#         print(f"This is {self.name}, speed: {self.speed}")
#
#     def __str__(self):
#         return f"{self.name} drives {self.speed} km/h"
#
#
# class Car(Transport):
#     def move(self):
#         print(f"{self.name} is a car")
#
#
# class Bicycle(Transport):
#     def move(self):
#         print(f"{self.name} is a bicycle")
#
#
# class Train(Transport):
#     def move(self):
#         print(f"{self.name} is a train")
#
#
# # Демонстрація роботи
# transports = [Car("BMW", 120), Bicycle("Phill", 30), Train("Ukrain", 240)]
#
# for a in transports:
#     a.info()
#     a.move()
#     print(a)
#     print("---")


#2
from abc import ABC, abstractmethod
class ValidationMeta(type):
    def __new__(cls, name, bases, attrs):

        print(f"\nСтворюється клас: {name}")


        if "description" not in attrs:
            print("description не знайдено - додаємо автоматично")
            attrs["description"] = "Default description"

        if not isinstance(attrs["description"], str):
            raise ValueError("description має бути рядком (str)")


        for attr_name in attrs:
            attr_value = attrs[attr_name]

            if callable(attr_value):
                if attr_name.startswith("__"):
                    continue

                if not attr_name.startswith("do_"):
                    raise ValueError(
                        f"Метод '{attr_name}' повинен починатися з 'do_'"
                    )

        print(f"Клас {name} успішно створений")
        return super().__new__(cls, name, bases, attrs)

class ValidatedClass(ABC, metaclass=ValidationMeta):

    @abstractmethod
    def do_action(self):
        pass

class GoodClass(ValidatedClass):

    description = "Correct class"

    def do_action(self):
        print("Doing action")

    def do_task(self):
        print("Doing task")

try:
    class BadClass(ValidatedClass):

        def action(self):
            print("Wrong method")
except ValueError as error:
    print("\nПОМИЛКА:", error)

obj = GoodClass()
print("\nDescription:", obj.description)
obj.do_action()


