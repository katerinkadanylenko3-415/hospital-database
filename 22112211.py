class Animal:
    def __init__(self, name):
        self.name = name
        self.__id = 0
        self._protected_prop = 1

    def speak(self):
        print("some sound")

    def get_info(self):
        return f"Name {self.name}"

    # @property
    # def protected_prop(self):
    #     return self._protected_prop


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def speak(self):
        print("meow meow")

    def get_info(self):
        return f"Name {self.name} \nage {self.age}"

class Dog(Animal):
    def speak(self):
        print("gaf gaf")

    def guard_house(self):
        print(f"{self.name} starts to guard house")


class Cow(Animal):
    def speak(self):
        print("mo mo")

    def eat_grass(self):
        print(f"{self.name} starts to eat grass")

cat1 = Cat("Murzic", 10)
cat1.speak()
print(cat1.name)
# cat1.protected_prop = 2
print(cat1._protected_prop)
print(cat1.get_info())

dog1 = Dog("Sharix")
dog1.speak()
print(dog1.get_info())

cow1 = Cow("Muza")
cow1.speak()
print(cow1.get_info())


# class Cat:
#     def __init__(self, name, age, colour):
#         self.__name = name
#         self.__age = age
#         self.__colour = colour
#
#     def get_info(self):
#         return (f"Name = {self.__name}, Age = {self.__age}, Colour = {self.__colour}")
#
#
# class Dog:
#     def __init__(self, name, age, colour):
#         self.__name = name
#         self.__age = age
#         self.__colour = colour
#
#     def get_info(self):
#         return (f"Name = {self.__name}, Age = {self.__age}, Colour = {self.__colour}")
#
#
# class Cow:
#     def __init__(self, name, age, colour):
#         self.__name = name
#         self.__age = age
#         self.__colour = colour
#
#     def get_info(self):
#         return (f"Name = {self.__name}, Age = {self.__age}, Colour = {self.__colour}")



