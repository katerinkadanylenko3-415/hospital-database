# #1
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# choice = input("What do you want to find out? + or * ? Your choice: ")
# if choice == "+":
#     print(num1 + num2 + num3)
# elif choice == "*":
#     print(num1 * num2 * num3)
# else:
#     print("error, try again")

#2
# num1 = int(input("Your task is to write three numbers. Enter number 1 : "))
# num2 = int(input("Enter number 2 : "))
# num3 = int(input("Enter number 3 : "))
# task = input("What do you want to find out ? max/min/avg number ? Write your choice: ")
# if task == "max":
#     print("The maximum value is", max(num1, num2, num3))
# elif task == "min":
#     print("The minimum value is", min(num1, num2, num3))
# elif task == "avg":
#     print("The average value is", (num1 + num2 + num3) / 3)
# else:
#     print("error, try again")

#3
# mark = input("Enter your mark which is representing a rating on a scale of 1 to 5 - ")
# if mark == "1":
#     print("Дуже погано")
# elif mark == "2":
#     print("Погано")
# elif mark == "3":
#     print("Задовільно")
# elif mark == "4":
#     print("Добре")
# elif mark == "5":
#     print("Відмінно")
# else:
#     print("error")

#4
metr = float(input("Enter your number of meters: "))
task = input("Choose an action: \n1 Convert to one of the units of your choice: miles, inches or yards"
             "\n2 Convert to all three units at once - miles, inches and yards"
             "\n3 Convert to kilometers and centimeters:"
             "\nYour choice is ")
if task == "1":
    num1 = input("Enter one of the units of your choice: miles, inches or yards: ")
    if num1 == "miles":
        print(metr/1609 , "miles.")
    elif num1 == "inches":
        print(metr*39 , "inches.")
    elif num1 == "yards":
        print(metr*1.09 , "yards.")
    else:
        print("error")

if task == "2":
    print(metr/1609 , "miles ,", metr*39 , "inches ,", metr*1.09 , "yards.")

if task == "3":
    print(metr/1000 , "kilometers ,", metr*100 , "centimeters.")


#5
# number1 = int(input("Enter a number1: "))
# number2 = int(input("Enter a number2: "))
# task = input("Choose an action: "
#              "\n1 addition"
#              "\n2 subtraction"
#              "\n3 multiplication"
#              "\n4 division"
#              "\n5 finding the remainder"
#              "\n6 raising to a power"
#              "\nYour choice is : ")
# if task == "1":
#     print(number1 + number2)
# elif task == "2":
#     print(number1 - number2)
# elif task =="3":
#     print(number1 * number2)
# elif task =="4":
#     print(number1 / number2)
# elif task == "5":
#     print(number1 % number2)
# elif task == "6":
#     print(number1 ** number2)
# else:
#     print("error, try again")

#6
# number = input("Enter a three-digit number: ")
# if number[0] == number[1] == number[2]:
#     print("Всі цифри однакові")
# else:
#     print("Цифри різні")

