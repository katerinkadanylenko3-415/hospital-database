# 1
# num1 = int(input("Enter a number1 : "))
# num2 = int(input("Enter a number2 : "))
# for num in range(num1, num2):
#     if num % 7 == 0:
#         print(num)

#2
# count = 0
# num1 = int(input("Enter a number1 : "))
# num2 = int(input("Enter a number2 : "))
# for num_1 in range(num1, num2+1):
#     print(num_1)
# print("----------")
# for num_2 in range(num2, num1-1, -1):
#     print(num_2)
# print("----------")
# for num_3 in range(num1, num2+1):
#     if num_3 % 7 == 0:
#         print(num_3)
# print("----------")
# for num_4 in range(num1, num2+1):
#     if num_4 % 5 == 0:
#         count += 1
#
# print(count)

#3
# num1 = int(input("Enter a number1 : "))
# num2 = int(input("Enter a number2 : "))
# for num_1 in range(num1, num2 + 1):
#     if num_1 % 3 == 0:
#         print("Fizz")
#     if num_1 % 5 == 0:
#         print("Buzz")
#     if num_1 % 3 == 0 and num_1 % 5 == 0:
#         print("FizzBuzz")
#     elif num_1 % 3 != 0 and num_1 % 5 != 0:
#         print(num_1)

# #4
# num1 = int(input("Enter a number1 : "))
# num2 = int(input("Enter a number2 : "))
# interval = int(input("Enter an interval : "))
# order = input("Choose the order in which numbers are displayed : 1) forward or 2) reverse ? Write -  ")
# if order == "1":
#     for i in range(num1, num2+1, interval):
#         print(i)
# elif order == "2":
#     for j in range(num2, num1-1, -interval):
#         print(j)


#5
# num1 = int(input("Enter a number1 : "))
# num2 = int(input("Enter a number2 : "))
# product = 1
# for num_1 in range(num1, num2 + 1):
#     if num_1 % 4 == 0 and num_1 % 6 != 0:
#         product *= num_1
#
# print(product)


# # 6
# number_a = int(input("Enter a number: "))
# power_n = int(input("Enter the power of a number: "))
# product = 1
# for a in range(power_n):
#     product *= number_a
#
# print(product)