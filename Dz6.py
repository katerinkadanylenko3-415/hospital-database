#1
# Напишіть функцію, яка приймає два числа як параметр
# і відображає усі парні числа між ними.
from _pyrepl.commands import end
from turtledemo.penrose import start

from Class_R5 import numbers


# def two_num(num1, num2):
#     for i in range(num1, num2+1):
#         if i % 2 == 0:
#             print(i)
#
# two_num(1, 10)

#2
# Напишіть функцію, яка повертає мінімальне з п’яти чисел (можна використати *args)
# Числа передаються як параметри.

# def min_num(num1, num2, num3, num4, num5):
#     return min(num1, num2, num3, num4, num5)
#
# product = min(1, 2, 3, 4, 5)
# print(product)

#3
# Напишіть функцію, яка повертає добуток чисел у зазначеному діапазоні. Межі діапазону передаються як параметри.
# # Якщо межі діапазону переплутані (наприклад, 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцями.
# #
# def multi_num(num1, num2):
#     started = min(num1, num2)
#     ended = max(num1, num2)
#
#     product = 1
#
#     for number in range(started, ended + 1):
#         if number == 0:
#             return 0
#         product *= number
#
#     print(product)
#
# multi_num(1, 11)


#4
# Завдання 4
# Напишіть функцію, яка підраховує кількість цифр у числі.
# Число передається як параметр. Поверніть з функції отриману
# кількість цифр. Наприклад, якщо передали 3456, кількість
# цифр буде 4.

#
# def numbers_symbols(number):
#     text_number = str(number)
#     count = len(text_number)
#     print(count)
#
# numbers_symbols(123456789)

#5

# Завдання 5
# Напишіть функцію, яка перевіряє число на паліндром.
# Число передається як параметр. Якщо число є паліндромом,
# поверніть з функції true, якщо ні — false.
# «Паліндром» — це число, в якому перша частина цифр
# дорівнює другій перевернутій частини цифр. Наприклад,
# 123321 — паліндром (перша частина 123, друга 321, яка після
# перевороту стає 123), 546645 — паліндром, а 421987 — не
# паліндром.

# number=int(input("enter a number: "))
# temp=number
# reverse=0
# while temp != 0:
#     reverse = reverse*10 + temp%10
#     temp=temp//10
#
# if number==reverse:
#     print("True")
# else:
#     print("False")

#6
# Завдання 6
# Напишіть функцію для підрахунку добутку елементів
# списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції.

# def math_num(num1, num2):
#
#     product = 1
#
#     for number in range(num1, num2 + 1):
#
#         product *= number
#
#     print(product)
#     return product
#
# math_num(2, 9)


#7
# Завдання 7
# Напишіть функцію для знаходження мінімуму в списку
# цілих. Список передається як параметр. Отриманий результат
# повертається із функції.

# def search_min_num(num1, num2):
#     min_num = min(num1, num2)
#     print(min_num)
#     return min_num
#
# search_min_num(1, 10)


#8
# Завдання 8
# Напишіть функцію, яка визначає кількість простих чисел
# у списку цілих. Список передається як параметр. Отриманий
# результат повертається із функції.


# def simple_numbers(num1, num2):
#     product = 1
#     for number in range(num1, num2 + 1):
#         if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
#             return True

# def simple_numbers(num1, num2):
#     prime_count = 0
#     for number in range(num1, num2 + 1):
#         if number % 2 != 0 and number % 3 != 0 and number % 5 != 0 and number % 7 != 0 or number == 1 or number == 2 or number == 3 or number == 5 or number == 7:
#             prime_count += 1
#
#     print(prime_count)
#     return prime_count
#
# simple_numbers(1, 11)

#9
# Завдання 9
# Напишіть функцію, яка видаляє зі списку цілих певне
# задане число. З функції потрібно повернути кількість віддалених елементі

# def delete_num_list():
#     nums = input("Enter numbers with spaces: ").split()
#     lit_num = nums
#     for num in nums:
#         num1 = input("chose the number to delete: ")
#         lit_num.remove(num1)
#         print(lit_num)
#         break
#
# delete_num_list()