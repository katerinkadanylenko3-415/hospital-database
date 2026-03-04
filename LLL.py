# import random
#
#
# class Pearson:
#     hobby = "cooking"
#
#     def __init__(self, name, age):
#         #public
#         self.name = name
#         #protected
#         self._age = age
#         #privat
#         self.__personID = random.randint(1, 100)
#
#     def __showID(self):
#         print(self.__personID)
#
#     def getInfo(self):
#         return f"Pearson's name - {self.name}, age = {self._age}, pearson ID = {self.__personID}"
#
#     @classmethod
#     def setDefaltHobby(cls, newhobby):
#         cls.hobby = newhobby
#
#     pr1 = Pearson("Bob", 30)
#     print(pr1.getInfo())
#     print(pr1.hobby)
#
#     Pearson.setDefaltHobby('driving')
#
#     pr2 = Pearson("Alice", 40)
#     print(pr2.getInfo())
#     print(pr2.hobby)
#     print(pr1.hobby)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showBookInfo(self):
        print("Title: ", self.title)
        print("Author: ", self.author)
        print("Pages: ", self.pages)

class File:
    def __init__(self, file_size, SRC):
        self.file_size = file_size
        self.SRC = SRC

    def showFileProps(self):
        print("File size: ", self.file_size)
        print("File SRC: ", self.SRC)

class EBook(Book, File):
    def __init__(self, title, author, pages, SRC):
        Book.__init__(self, title, author, pages)
        File.__init__(self, file_size=123, SRC=SRC)




ebook1 = EBook("python", "gvido", 400, "C////")
ebook1.showBookInfo()
ebook1.showFileProps()
print(EBook.mro())

class Flyer:
    def fly(self):
        print("Duck is flying")


class Swimmer:
    def swim(self):
        print("Duck is swimming")


class Duck(Flyer, Swimmer):
    def move(self):
        self.fly()
        self.swim()


duck = Duck()
duck.move()


class Engine:
    def __init__(self, power):
        self.power = power


class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


class HybridCar(Engine, Battery):
    def __init__(self, power, capacity):
        Engine.__init__(self, power)
        Battery.__init__(self, capacity)

    def specs(self):
        print("Engine power:", self.power)
        print("Battery capacity:", self.capacity)


hybridcar = HybridCar(150, 60)
hybridcar.specs()



class BaseUser:
    def get_permissions(self):
        return ["text1"]


class AdminUser(BaseUser):
    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append("text2")
        permissions.append("text3")
        return permissions


class ModeratorUser(BaseUser):
    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append("text4")
        return permissions


class SuperUser(AdminUser, ModeratorUser):
    def get_permissions(self):
        permissions = super().get_permissions()
        permissions.append("text5")
        return permissions



user = SuperUser()
print(user.get_permissions())







