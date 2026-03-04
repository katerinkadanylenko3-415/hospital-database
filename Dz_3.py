# def debug_info_universal(func):
#     def wrapper(*args):
#         print("Start function")
#         result = func(*args)
#         print("End function")
#         return result
#     return wrapper
#
# @debug_info_universal
# def add_numbers(a, b):
#     print(f"Adding {a} and {b}")
#     return a + b
#
# print(f"Result: {add_numbers(10, 5)}")

#2
# def upper_text(func):
#     def wrapper(*args):
#         result = func(*args)
#
#         if isinstance(result, str):
#             return result.upper()
#         else:
#             return result
#
#     return wrapper
#
#
# @upper_text
# def get_greeting(name, language):
#     return f"hello, {name}! your language is {language}."
#
#
# @upper_text
# def get_simple_word():
#     return "python"
#
# print(get_greeting("python", "python"))
# print(get_simple_word())

#4
# def repeat_three_times(func):
#     def wrapper():
#         print("--- Починаємо повторення ---")
#
#         for i in range(3):
#             print(f"Запуск функції (Раз {i + 1})")
#
#             func()
#
#         print("--- Повторення завершено ---")
#
#     return wrapper
#
# @repeat_three_times
# def print_simple_message():
#     print("Я виконуюсь!")
#
#
# print("--- Запуск функції ---")
# print_simple_message()

class Person:
    def __init__(self, full_name, birth_year, phone, city, country, address):
        self.full_name = full_name
        self.birth_year = birth_year
        self.phone = phone
        self.city = city
        self.country = country
        self.address = address

    def input_data(self):
        self.full_name = input("Enter full name: ")
        self.birth_year = int(input("Enter birth year: "))
        self.phone = input("Enter phone number: ")
        self.city = input("Enter city: ")
        self.country = input("Enter country: ")
        self.address = input("Enter address: ")

    def show_data(self):
        print("Full name:", self.full_name)
        print("Birth year:", self.birth_year)
        print("Phone:", self.phone)
        print("City:", self.city)
        print("Country:", self.country)
        print("Address:", self.address)

    def is_major(self):
        current_year = 2025
        age = current_year - self.birth_year
        return age >= 18

person = Person(
    "Alastor Franklin",
    2006,
    "+380991234567",
    "Kyiv",
    "Ukraine",
    "Shevchenko Street 10"
)

person.show_data()

print("Is adult:", person.is_major())




class City:
    def __init__(self, name, region, country, population, zipcode, phone_code):
        self.name = name
        self.region = region
        self.country = country
        self.population = population
        self.zipcode = zipcode
        self.phone_code = phone_code

    def input_data(self):
        self.name = input("Enter city name: ")
        self.region = input("Enter region: ")
        self.country = input("Enter country: ")
        self.population = int(input("Enter population: "))
        self.zipcode = input("Enter zipcode: ")
        self.phone_code = input("Enter phone code: ")

    def show_data(self):
        print("City:", self.name)
        print("Region:", self.region)
        print("Country:", self.country)
        print("Population:", self.population)
        print("Zipcode:", self.zipcode)
        print("Phone code:", self.phone_code)

    def is_valid_zipcode(self):
        if len(self.zipcode) == 5 and self.zipcode.isdigit():
            return True
        else:
            return False

city = City(
    "Kyiv",
    "Kyiv region",
    "Ukraine",
    2967000,
    "01001",
    "+38044"
)

city.show_data()

print("Zipcode is valid:", city.is_valid_zipcode())

#3

class Country:
    def __init__(self, name, continent, population, phone_code, capital, cities):
        self.name = name
        self.continent = continent
        self.population = population
        self.phone_code = phone_code
        self.capital = capital
        self.cities = cities

    def show_data(self):
        print("Country:", self.name)
        print("Continent:", self.continent)
        print("Population:", self.population)
        print("Phone code:", self.phone_code)
        print("Capital:", self.capital)
        print("Cities:", end=" ")
        for i in range(len(self.cities)):
            print(self.cities[i], end="")
            if i < len(self.cities) - 1:
                print(", ", end="")
        print()

    def has_city(self, city_name):
        for city in self.cities:
            if city_name == city:
                return True
        return False

ukraine = Country(
    "Ukraine",
    "Europe",
    43000000,
    "+380",
    "Kyiv",
    ["Kyiv", "Lviv", "Odesa", "Kharkiv"]
)

ukraine.show_data()

print("Does Ukraine have Lviv?", ukraine.has_city("Lviv"))
print("Does Ukraine have Paris?", ukraine.has_city("Paris"))

#4
class Car:
    def __init__(self, model, year, manufacturer, engine_volume, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Enter car model: ")
        self.year = int(input("Enter year of manufacture: "))
        self.manufacturer = input("Enter manufacturer: ")
        self.engine_volume = float(input("Enter engine volume (liters): "))
        self.color = input("Enter car color: ")
        self.price = float(input("Enter price: "))

    def show_data(self):
        print("Car model:", self.model)
        print("Year:", self.year)
        print("Manufacturer:", self.manufacturer)
        print("Engine volume:", self.engine_volume, "L")
        print("Color:", self.color)
        print("Price:", self.price)

my_car = Car("Toyota Corolla", 2020, "Toyota", 1.6, "White", 20000)
my_car.show_data()

