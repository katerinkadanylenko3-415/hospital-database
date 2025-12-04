#1
# def SumCalculation(num_a, num_b):
#     if num_a > num_b:
#         return 0
#     else:
#         print(num_a, end="+")
#         return num_a + SumCalculation(num_a + 1, num_b)
#
# num_a = int(input("Enter number1 = "))
# num_b = int(input("Enter number2 = "))
# if num_a > num_b:
#     num_a, num_b = num_b, num_a
# total_sum = SumCalculation(num_a, num_b)
#
# print(" =" , total_sum)

#2
#Напишіть рекурсивну функцію, яка виводить в рядок
# N зірочок, число N задає користувач. Покажіть приклад роботи функції.

# def starscount(num):
#     if num == 0:
#         return 0
#     else:
#         return num * "*"
#
#
# num = int(input("Enter a number: "))
# print(starscount(num))

#3
# Створити список із трьох різних функцій square, cube, negate.
# Попросити користувача вибрати 1–3 і застосувати відповідну функцію до числа.

# def Square(num):
#     return num ** 2
#
# def Cube(num):
#     return num ** 3
#
# def Negate(num):
#     return -num
#
# def MathChoice(choice):
#     if choice == 1:
#         return num ** 2
#     elif choice == 2:
#         return num ** 3
#     else:
#         if choice == 3:
#             return -num
#
# num = int(input("Enter a number: "))
# choice = int(input("Enter your choice_number: "))
# print(MathChoice(choice))

#5
# Завдання 5 *
# Напишіть рекурсивну функцію знаходження найбільшого загального дільника двох цілих чисел.

# def The_biggest_num_dil(a,b):
#     a = abs(a)
#     b = abs(b)
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     elif a > b:
#         remainder1 = a % b
#         return The_biggest_num_dil(b, remainder1)
#     else:
#         if b > a:
#             remainder2 = b % a
#             return The_biggest_num_dil(a, remainder2)
#
# a = int(input("enter a number: "))
# b = int(input("enter another number: "))
#
# result = The_biggest_num_dil(a,b)
#
# print(result)
























