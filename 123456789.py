import random


class Student:
    spec = "Computer scientist"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show_info(self):
        return f"nam: {self.name}, age: {self.age}"

    def showMsg(self,text):
        return f"Student {self.name} says {text}"



st1 = Student('Bob',22)
st2 = Student('Joe',23)
print(st1.show_info())

# st2 = Student()
# st2.name = "Erik"
print(st2.show_info())
print(st1.showMsg("Hello"))

print(type(st1))

#1
class Car:
    def __init__(self):
            self._color = "red"

    def color(self):
        return self._color

ferrary = Car()
print(ferrary.color())

class Pearson:
    def __init__(self, name, age, salary):
        #public properties
        self.name = name
        self.age = age
        self.salary = salary
        #privt prop
        self.__pearsonID = random.randint(1,100)

    def __getID(self):
        return f"{self.__pearsonID}" #privat

    @property
    def name(self):
        return self.name.title()

    @name.setter
    def name(self, value):
        self.name = value.title()

    @property
    def __pearsonID(self):
        return self.__pearsonID



    def getInfo(self):
        return f"name: {self.name}, age: {self.age}, salary: {self.salary}, id: {self.__getID()}"

    @pearsonID.setter
    def pearsonID(self, value):
        self.__personID = value



pearson1 = Pearson("John",22,20000)
print(pearson1.name)
# print(pearson1.__pearsonID)
# print(pearson1.salary)
pearson1.name = "Johnnnne"
print(pearson1.getInfo())
pearson1.name = "test new name"