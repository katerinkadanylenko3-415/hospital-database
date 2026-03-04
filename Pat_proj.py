#1
'''
class Car:
    def __init__(self):
        self.brand = None
        self.body_type = None
        self.color = None
        self.engine = None
        self.doors = None
        self.options = []

    def __str__(self):
        return (
            f"Марка: {self.brand}\n"
            f"Тип кузова: {self.body_type}\n"
            f"Колір: {self.color}\n"
            f"Двигун: {self.engine}\n"
            f"Кількість дверей: {self.doors}\n"
            f"Опції: {', '.join(self.options) if self.options else 'немає'}"
        )

class CarBuilder:
    def __init__(self):
        self.car = Car()

    def set_brand(self, brand):
        self.car.brand = brand
        return self

    def set_body_type(self, body_type):
        self.car.body_type = body_type
        return self

    def set_color(self, color):
        self.car.color = color
        return self

    def set_engine(self, engine):
        self.car.engine = engine
        return self

    def set_doors(self, doors):
        self.car.doors = doors
        return self

    def add_option(self, option):
        self.car.options.append(option)
        return self

    def get_car(self):
        return self.car

class Director:
    def build_electric_car(self, builder):
        return (
            builder
            .set_brand("Tesla")
            .set_body_type("седан")
            .set_color("білий")
            .set_engine("електричний")
            .set_doors(4)
            .add_option("автопілот")
            .add_option("панорамний дах")
            .get_car()
        )

    def build_suv(self, builder):
        return (
            builder
            .set_brand("BMW")
            .set_body_type("позашляховик")
            .set_color("чорний")
            .set_engine("дизельний")
            .set_doors(5)
            .add_option("повний привід")
            .add_option("шкіряний салон")
            .get_car()
        )

director = Director()

builder1 = CarBuilder()
car1 = director.build_electric_car(builder1)
print("Автомобіль 1")
print(car1)

builder2 = CarBuilder()
car2 = director.build_suv(builder2)
print("Автомобіль 2")
print(car2)
'''
#2

class Pasta:
    def __init__(self):
        self.type = None
        self.sauce = None
        self.filling = None
        self.supplements = None

    def __str__(self):
        return (
            f"Тип пасти: {self.type}\n"
            f"Соус: {self.sauce}\n"
            f"Начинка: {self.filling}\n"
            f"Добавки: {self.supplements}\n"
        )

class PastaBuilder:
    def __init__(self):
        self.pasta = Pasta()

    def set_type(self, type):
        self.pasta.type = type
        return self

    def set_sauce(self, sauce):
        self.pasta.sauce = sauce
        return self

    def set_filling(self, filling):
        self.pasta.filling = filling
        return self

    def set_supplements(self, supplements):
        self.pasta.supplements = supplements
        return self

    def get_pasta(self):
        return self.pasta

class Director:
    def Spaghetti(self, builder):
        return (
            builder
            .set_type("Спагеті")
            .set_sauce("Томатний")
            .set_filling("М’ясо")
            .set_supplements("Пармезан")
            .get_pasta()
        )

    def Ravioli(self, builder):
        return (
            builder
            .set_type("Равіолі")
            .set_sauce("Вершковий")
            .set_filling("Сир")
            .set_supplements("Зелень")
            .get_pasta()
        )

    def Lasagna(self, builder):
        return (
            builder
            .set_type("Лазанья")
            .set_sauce("Болоньєзе")
            .set_filling("Фарш")
            .set_supplements("Моцарела")
            .get_pasta()
        )

    def Fettuccine(self, builder):
        return (
            builder
            .set_type("Фетучіні")
            .set_sauce("Альфредо")
            .set_filling("Курка")
            .set_supplements("Пармезан")
            .get_pasta()
        )

    def Penne(self, builder):
        return (
            builder
            .set_type("Пенне")
            .set_sauce("Арраббʼята")
            .set_filling("Без начинки")
            .set_supplements("Чилі")
            .get_pasta()
        )

builder = PastaBuilder()
director = Director()

pasta1 = director.Spaghetti(builder)
print(pasta1)

builder = PastaBuilder()
pasta2 = director.Ravioli(builder)
print(pasta2)

builder = PastaBuilder()
pasta3 = director.Lasagna(builder)
print(pasta3)

pasta4 = director.Fettuccine(builder)
print(pasta4)

builder = PastaBuilder()
pasta5 = director.Penne(builder)
print(pasta5)
