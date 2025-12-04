def sayHello():
    name = "qwerty"
    print(f"Hello, {name}")

sayHello()

print(type(sayHello))

greeting = sayHello
greeting() # аля псевдонім для функції sayHello

customers = ["AdminJane", "AdminBob","StudentNick", "StudentJane", "Kate"]

def sayHelloForClient(customer):
    if customer.find('Admin') != -1:
        print(f"Hello admin - {customer}")
    elif customer.find('Student') != -1:
        print(f"Hello student - {customer}")
    else:
        print(f"Hello - {customer}")


def greting(customerList, greetFunc):
    if isinstance(customerList, list):
        for c in customerList:
            greetFunc(c.lower())


greting(customers, sayHelloForClient)


def calculateSum(a, b):
    return a + b

def calculateMinus(a, b):
    return a - b

def calculateDil(a, b):
    if b != 0:
        return a / b

def userChoice(c):
    if c == '1':
        return calculateSum
    elif c == '2':
        return calculateMinus
    elif c == '3':
        return calculateDil

myCalculation = userChoice('1')
print(myCalculation(2,2))


# рекурсія - функція, що викликає сама себе, в тілі функціївиклик сама функція
# num = 1
# while True:
#     if num == 10:
#         break
#     num += 1

def fuctorialCalculation(num):
    if num == 0:
        return 1
    else:
        print(num, end="*")
        return num * fuctorialCalculation(num-1)

print("-------------------")
print(fuctorialCalculation(5))


def isStrPalindrom(mystr):
    if len(mystr) == 0:
        return True
    else:
        if mystr[0] == mystr[-1]:
            print(mystr[1:-1])
            return isStrPalindrom(mystr[1:-1])
        else:
            return False

str1 = 'madam'
print(isStrPalindrom(str1))

def findMin(numberList):
    if len(numberList) > 1:
        return min(findMin(numberList[:-1]), numberList[-1])
    else:
        return numberList[0]

nums = [1, 2, 3, 4, 5]
print("min = " , findMin(nums))


# sum_digits(1234) → 10

# def sum_digits(number):
#     if number == 0:
#         return 0
#     else:
#         print(number)
#         return (number % 10) + sum_digits(number // 10)
#
# print(sum_digits(1234))

# def list_num(mylist):
#     if len(mylist) == 0:
#         return 0
#     else:
#         n = mylist[0]
#
# print(list_num([1, 2, 3, 4, 5]))

# def greetingHello():
#     print("Hello")
#
# say_hello = greetingHello

def square(num):
    return num ** 2

def cube(num):
    return num ** 3

def negate(num):
    return -num

def math_choice(number):
    if number == '1':
        return 2 ** 2
    elif number == '2':
        return 2 ** 3
    elif number == '3':
        return -2

print(math_choice(1))
print(math_choice(2))
print(math_choice(3))












