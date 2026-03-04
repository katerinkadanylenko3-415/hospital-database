num1 = 1
num2 = 2
print(num1 + num2)

# str1 = "1"
# str2 = "2"
#
# print(str1 + str2)
# print(len("python"))
# print(len([1, 2, 3]))
#
# class File:
#     def __init__(self, tittle, director):
#         self.tittle = tittle
#         self.director = director
#
#     def show(self):
#         print(f"File tittle: {self.tittle}")
#         print(f"File director: {self.director}")
#
#
# class Book:
#
#     def __new__(cls, *args, **kwargs):
#         print(f"I am __new__ magic method")
#         return super(Book, cls).__new__(cls)
#
#
#     def __init__(self, title, author, pages):
#         print("I am __init__ magic method")
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     def show(self):
#         print(f"Book Title: {self.title}")
#         print(f"Book Author: {self.author}")
#
#     def __str__(self):
#         return f"Title: {self.title}, Author: {self.author}"
#
#     def __eq__(self, otherOBJ):
#         if self.author == otherOBJ.author and self.title == otherOBJ.title and self.pages == otherOBJ.pages:
#             return True
#         else:
#             return False
#
#     def __gt__(self, other):
#         if isinstance(other, Book):
#             return self.pages > other.pages
#
#     def __lt__(self, other):
#         if isinstance(other, Book):
#             return self.pages < other.pages
#
#     def __ge__(self, other):
#         if isinstance(other, Book):
#             return self.pages >= other.pages
#
#     def __le__(self, other):
#         if isinstance(other, Book):
#             return self.pages <= other.pages







#
# file1 = File('Avatar', 'Cameron')
# book1 = Book('Python', 'Gvido', 200)
# book2 = Book('Harry Potter', "Rolling", 300)
# book3 = Book('Harry Potter', "Rolling", 300)
#
# for item in (file1, book1):
#     item.show()
#
# # print(book1 + book2)
#
# book1 = Book("Python", "Gvido", 200)
# print(book1)
# print(book1.__str__())
#
# print(book1 == book3)

class Point:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} : {self.y}"

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(
                self.x * other,
                self.y * other
            )
        elif isinstance(other, Point):
            return Point(
                self.x * other.x,
                self.y * other.y
            )

    def __iadd__(self, other):
        if isinstance(other, int):
            self.x += other
            self.y += other
            return self
        elif isinstance(other, Point):
            self.x += other.x
            self.y += other.y
            return self

    def __float__(self):
        return Point(float(self.x), float(self.y))


print(Point(2, 2) *2)
print(Point(2, 2) * Point(3,4))

num = 1
num +=1
p1 = Point(1,1)
p1 += 2
print(p1)

print(p1.__float__())

print(p1.__dict__)

class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return super().__str__() + f" : {self.z}"


p3 = Point3D(1, 1, 1)
print(p3)
print(p3.__slots__)
# print(p3.__dict__)