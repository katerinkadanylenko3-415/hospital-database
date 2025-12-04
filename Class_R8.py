
# lambda - позначка аномнімн функц

# lambda arg1 arg2 : вираз
#
# def add10(x):
#     return x + 10
#
# nums = [1,2,3,4,5]
# # for num in nums:
# #     print(add10(num))
#
# for num in nums:
#     print((lambda x: x + 10)(num))
#
# students = [['Bob' , 70],
#             ['Jane' , 30],
#             ['Kate' , 100]]
#
# print(students)
# sorted_students = sorted(students, key=lambda x: x[1])
# print(sorted_students)
#
# Dollar = 42
# discount = 0.15
# priceDol = lambda x: x/Dollar *(1 - discount)
#
# price = 4200
# print(f"price: {priceDol(price)} .")
# print(f"price: {priceDol(3500)} .")
#
# userName = lambda firstName, lastName: f"Full name: {firstName.title()} {lastName.title()}"
#
# print(userName("John", "Smith"))
#
# num = int(input("Enter a number: "))
# kvadratic = lambda x: x ** 2
# result = kvadratic(num)
# print(result)
#
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# find_max = lambda a, b: max(a, b)
# print(find_max(num1, num2))


# x = int(input("Enter a number: "))
# find_num = lambda x: x % 2 == 0
# print(True)
# if lambda x: x % 2 != 0:
#     print(False)

student_birth_year = [2000, 2007, 2002, 1999]
print(student_birth_year)
studAges = list(map(lambda x: 2025 - x, student_birth_year))
print(studAges)

# for year in student_birth_year:
#     studAges.append(2025 - year)
#
# print(studAges)

# number = int(input("Enter a number: "))
# print(abs(number))
#
#
# def make_log(username, maker):
#     return maker(username)
#
#
# def name_upper(name):
#     return 'user' + name.upper()
#
# def name_lower(name):
#     return 'user' + name.lower()
#
# print(make_log("admin", name_upper))

# map()  filter()  zip()

user_logs = ['admin', 'STUDENT', 'sTar', 'CaTyCitCat']
print(user_logs)

user_LogsLow = list(map(str.lower, user_logs))
print(user_LogsLow)

values = ['1.3', '12', '1.3', '14', '3', '100']
print(values)

numbers = list(map(float, values))
print(numbers)

digits = list(map(lambda num: int(num[0]), values))
print(digits)


nums1 = [10, 20, 30, 40, 50]
nums2 = [1, 2, 3, 4, 5]
result = list(map(lambda a, b: a**b, nums1, nums2))
print(result)

prices = [100, 53, 67, 49, 45]
expensive = list(filter(lambda x: x > 50, prices))
print(prices)
print(expensive)

userPass = ['1111', 'cat', '1234']

for log, passw in zip(user_logs, userPass):
    print(f"login: {log}, password: {passw}")

print(list(zip(user_logs, userPass)))





