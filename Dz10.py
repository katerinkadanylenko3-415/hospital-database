#1
#Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку
# num1 = {'1', '2', '3', '4'}
# num2 = {'5', '1', '2', '4'}
# num3 = {'6', '2', '9', '1'}

# tuple1 = (1, 2, 3, 10, 11)
# tuple2 = (2, 3, 4, 5, 10)
# tuple3 = (3, 5, 6, 7, 11)
#
# set1 = set(tuple1)
# set2 = set(tuple2)
# set3 = set(tuple3)
#
# unique1 = set1 - set2 - set3
# unique2 = set2 - set3 - set1
# unique3 = set3 - set1 - set2
#
# print(f"Кортеж 1: {tuple1}")
# print(f"Кортеж 2: {tuple2}")
# print(f"Кортеж 3: {tuple3}")
#
# print(f"Унікальні для 1-го: {unique1}")
# print(f"Унікальні для 2-го: {unique2}")
# print(f"Унікальні для 3-го: {unique3}")


# num1 = ('10', '1', '2', '3', '4', '6')
# num2 = ('10', '5', '1', '2', '6')
# num3 = ('10', '7', '8', '6', '1', '9', '2')
#
# num_1 = {'0', '1', '2', '3', '4', '6'}
# num_2 = {'0', '5', '1', '2', '6'}
# num_3 = {'0', '7', '8', '6', '1', '9', '2'}
#
#
# def finde_posession(n1, n2, n3):
#     element = min(len(n1), len(n2), len(n3))
#
#     matching_elements = []
#
#     for i in range(element):
#         if n1[i] == n2[i] == n3[i]:
#             matching_elements.append(n1[i])
#
#     return matching_elements
#
# print("Числа(о)", finde_posession(num1, num2, num3), "знаходя(и)ться в кожному з них на тій самій позиції.")
# print("Числа(о)",  num_1 & num_2 & num_3,  " є в кожному з кортежів.")


#3
# tuple = (5, 12, 123, 8, 456, 9999, 10, 7, 20000, 1500)
#
# counting = {}
#
# for number in tuple:
#     num_digits = len(str(number))
#     if num_digits in counting:
#         counting[num_digits] += 1
#     else:
#         counting[num_digits] = 1
#
# print("Статистика:")
#
# for i in sorted(counting.keys()):
#     statistic = counting[i]
#     if i == 1:
#         number = "Одна цифра"
#     elif i >= 2 and i <= 4:
#         number = f"{i} цифри"
#     else:
#         number = f"{i} цифр"
#
#     print(f"{number} — {statistic} елемент и/ів")

#4
# name1 = input("Enter name: ").__str__()
# age1 = int(input("Enter age: "))
# name2 = input("Enter name: ").__str__()
# age2 = int(input("Enter age: "))
# name3 = input("Enter name: ").__str__()
# age3 = int(input("Enter age: "))
# name4 = input("Enter name: ").__str__()
# age4 = int(input("Enter age: "))
#
#
# tuple1 = (name1, age1)
# tuple2 = (name2, age2)
# tuple3 = (name3, age3)
# tuple4 = (name4, age4)
#
# people_from_input = [tuple1, tuple2, tuple3, tuple4]
#
# adult_names = []
#
# for name, age in people_from_input:
#     if age > 18:
#         adult_names.append(name)
#
# print(adult_names)

#5
# item1 = input("Enter item name").__str__()
# num1 = int(input("Enter item number"))
# item2 = input("Enter item name").__str__()
# num2 = int(input("Enter item number"))
# item3 = input("Enter item name").__str__()
# num3 = int(input("Enter item number"))
# item4 = input("Enter item name").__str__()
# num4 = int(input("Enter item number"))
#
# tuple1 = (item1, num1)
# tuple2 = (item2, num2)
# tuple3 = (item3, num3)
# tuple4 = (item4, num4)
#
# supermarket = (tuple1, tuple2, tuple3, tuple4)
#
# total_count = 0
#
# for a, b in supermarket:
#     total_count += b
#
# print(f"список: {supermarket}")
# print("-" * 30)
# print(f"Загальна кількість товарів: {total_count}")


#6
# tuple1 = ('Майстер і Маргарита', 'Михайло Булаков', 1967)
# tuple2 = ('Злочин і покарання', 'Федор Достоєвський', 1866)
# tuple3 = ('Війна і мир', 'Лев Толстой', 1869)
# tuple4 = ('Майстер і Маргарита', 'Михайло Булаков', 1967)
# tuple5 = ('1984', 'Джордж Оруелл', 1949)
# tuple6 = ('1984', 'Джордж Оруелл', 1949)

# books = [
#     ('Майстер і Маргарита', 'Михайло Булгаков', 1967),
#     ('Злочин і покарання', 'Федір Достоєвський', 1866),
#     ('Війна і мир', 'Лев Толстой', 1869),
#     ('1984', 'Джордж Орвелл', 1949),
#     ('Собаче серце', 'Михайло Булгаков', 1925),
#     ('Брати Карамазови', 'Федір Достоєвський', 1880)]
#
# def get_unique_authors(books_data):
#     unique_authors_set = set()
#     for book in books_data:
#         author = book[1]
#         unique_authors_set.add(author)
#
#     return list(unique_authors_set)
#
# unique_authors_list = get_unique_authors(books)
# print("Список авторів:\n")
#
# for author in unique_authors_list:
#   print(author)












