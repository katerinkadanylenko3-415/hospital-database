class City:
    def __init__(self, city="", region="", country="", population=0, postal_code="", phone_code=""):
        self.city = city
        self.region = region
        self.country = country
        self.population = population
        self.postal_code = postal_code
        self.phone_code = phone_code

    def display_info(self):

        print("Інформація про місто...")
        print(f"Назва міста:{self.city}")
        print(f"Регіон:{self.region}")
        print(f"Країна:{self.country}")
        print(f"Кількість жителів:{self.population:,} осіб")
        print(f"Поштовий індекс:{self.postal_code}")
        print(f"Телефонний код:{self.phone_code}")
        print("---------------------------")

    def input_info(self):
        print("Введення даних про місто...")
        self.city = input("Введіть назву міста: ")
        self.region = input("Введіть назву регіону/області: ")
        self.country = input("Введіть назву країни: ")
        self.population = int(input("Введіть кількість жителів міста:"))
        self.postal_code = input("Введіть поштовий індекс: ")
        self.phone_code = input("Введіть телефонний код міста: ")
        print("--------------------------------")

    def is_million_city(self, population):
        self.population = population
        if population > 1000000:
            print("Місто є містом-мільйонником ")
        elif population < 1000:
            print("Місто не є містом-мільйонником")

print()
