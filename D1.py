# Створіть клас Passport (паспорт), який міститиме паспортну інформацію про громадянина заданої країни.
#
# За допомогою механізму успадкування реалізуйте клас ForeignPassport (закор­дон­ний паспорт), похідний від Passport.
#
# Нагадаємо, що закордонний паспорт містить, крім паспортних даних, дані про візи і номер закордонного паспорта.
#
# Кожен із класів має містити необхідні методи.

class Passport:
    def __init__(self, name, surname, age, sex, country, birth_place, id_number):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex
        self.country = country
        self.birth_place = birth_place
        self.id_number = id_number

    def get_info(self):
        return (
            f"Name: {self.name}\n"
            f"Surname: {self.surname}\n"
            f"Age: {self.age}\n"
            f"Sex: {self.sex}\n"
            f"Country: {self.country}\n"
            f"Birth place: {self.birth_place}\n"
            f"ID number: {self.id_number}"
        )


class ForeignPassport(Passport):
    def __init__(self, name, surname, age, sex, country, birth_place, id_number, foreign_id_number, visas):
        super().__init__(name, surname, age, sex, country, birth_place, id_number)
        self.foreign_id_number = foreign_id_number
        self.visas = visas

    def get_info(self):
        base_info = super().get_info()
        return (
            base_info + "\n"
            f"Foreign passport number: {self.foreign_id_number}\n"
            f"Visas: {self.visas}"
        )


alastor_passport = Passport("Alastor", "Franklin", 29, "Male", "USA", "New York", 2121212)
print(alastor_passport.get_info())
alastor_foreign_passport = ForeignPassport("Alastor", "Franklin", 29, "Male", "USA", "New York",2121212, 987654321, ["Poland", "Germany"])
print("\n--- Passport ---\n")
print(alastor_passport.get_info())
print("\n--- Foreign Passport ---\n")
print(alastor_foreign_passport.get_info())


# Завдання 2
# Створіть клас Device, який містить інформацію про пристрій.
#
# За допомогою механізму успадкування реалізуйте клас CoffeeMachine (містить інформацію про кавомашину),
# клас Blender (містить інформацію про блендер), клас MeatGrinder (містить інформацію про м'ясорубку).
#
# Кожен із класів має містити необхідні для роботи методи.

# class Device:
#     def __init__(self, name, colour, size, material, manufacturer, model):
#         self.name = name
#         self.colour = colour
#         self.size = size
#         self.material = material
#         self.manufacturer = manufacturer
#         self.model = model
#
#
#     def get_info(self):
#         return (
#             f"Name: {self.name}\n"
#             f"Colour: {self.colour}\n"
#             f"Size: {self.size}\n"
#             f"Material: {self.material}\n"
#             f"Manufacturer: {self.manufacturer}\n"
#             f"Model: {self.model}\n"
#         )
#
# class CoffeeMachine(Device):
#     def __init__(self, device_purpose):
#         super().__init__(
#             name="Coffee Machine",
#             colour="Black",
#             size="Big",
#             material="Metal",
#             manufacturer="Fox",
#             model="E1"
#         )
#         self.device_purpose = device_purpose
#
#     def get_info(self):
#         return super().get_info() + f"\nPurpose: {self.device_purpose}"
#
#
# class Blender(Device):
#     def __init__(self, device_purpose):
#         super().__init__(
#             name="Blender",
#             colour="White",
#             size="Small",
#             material="Metal and plastic",
#             manufacturer="Sommerferien",
#             model="A2"
#         )
#         self.device_purpose = device_purpose
#
#     def get_info(self):
#         return super().get_info() + f"\nPurpose: {self.device_purpose}"
#
#
# class MeatGrinder(Device):
#     def __init__(self, device_purpose):
#         super().__init__(
#             name="Meat Grinder",
#             colour="Orange",
#             size="Middle",
#             material="Metal",
#             manufacturer="Pig",
#             model="B3"
#         )
#         self.device_purpose = device_purpose
#
#     def get_info(self):
#         return super().get_info() + f"\nPurpose: {self.device_purpose}"
#
#
# coffee = CoffeeMachine("Making coffee")
# blender = Blender("Mixing products")
# meat_grinder = MeatGrinder("Grinding meat")
#
# print(coffee.get_info())
# print("\n---\n")
# print(blender.get_info())
# print("\n---\n")
# print(meat_grinder.get_info())

class Money:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor
        if self.minor >= 100:
            self.major = self.major + self.minor // 100
            self.minor = self.minor % 100

    def set_amount(self, major, minor):
        self.major = major
        self.minor = minor

        if self.minor >= 100:
            self.major = self.major + self.minor // 100
            self.minor = self.minor % 100

    def show(self):
        print(self.major, "грн", self.minor, "коп")


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price   # об'єкт Money

    def reduce_price(self, major, minor):
        self.price.major = self.price.major - major
        self.price.minor = self.price.minor - minor

        if self.price.minor < 0:
            self.price.major = self.price.major - 1
            self.price.minor = self.price.minor + 100

    def show(self):
        print("Product:", self.name)
        self.price.show()

price = Money(10, 50)
product = Product("Chocolate", price)
product.show()
product.reduce_price(2, 75)
product.show()


class TemperatureConverter:
    count = 0   # лічильник підрахунків

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.count = TemperatureConverter.count + 1
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.count = TemperatureConverter.count + 1
        return (fahrenheit - 32) * 5 / 9

    @staticmethod
    def get_count():
        return TemperatureConverter.count

t1 = TemperatureConverter.celsius_to_fahrenheit(0)
print("0°C =", t1, "°F")
t2 = TemperatureConverter.fahrenheit_to_celsius(32)
print("32°F =", t2, "°C")
t3 = TemperatureConverter.celsius_to_fahrenheit(100)
print("100°C =", t3, "°F")
print("Кількість підрахунків:", TemperatureConverter.get_count())




























