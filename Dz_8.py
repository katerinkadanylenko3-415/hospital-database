#1
# 1.Використовуючи функцію map, створіть новий список, у якому кожен елемент буде зводитись у квадрат. Вихідний список: [1, 2, 3, 4, 5].

# nums = [1, 2, 3, 4, 5]
# numbers = list(map(lambda num: num * num, nums))
# print(numbers)

#2
#2.Використовуючи функцію map, перетворіть список рядків на список їх довжин. Вихідний список: ["apple", "banana", "cherry"].
# fruits = ["apple", "banana", "cherry"]
# lengths = map(len, fruits)
# lengths_list = list(lengths)
# listed = list(map(lambda word: len(word), fruits))
#
# print(listed)


#3
#3.Використовуючи функцію filter, відфільтруйте список чисел, залишивши лише парні числа. Вихідний список: [1, 2, 3, 4, 5].

# nums = [1, 2, 3, 4, 5]
# filt = list(filter(lambda num: num % 2 == 0, nums))
# print(filt)

#4
# 4.Використовуючи функцію filter, відфільтруйте список рядків, залишивши лише рядки, що починаються з літери "a". Вихідний список: ["apple", "banana", "cherry"].
# fruits = ["apple", "banana", "cherry"]
# fruit = list(filter(lambda fruit: fruit.startswith("a"), fruits))
# print(fruit)

#5
# 5.Використовуючи функції map і filter, створіть новий список, у якому залишаться лише числа, що поділяються на 3. Вихідний список: [1, 2, 3, 4, 5].
# nums = [1, 2, 3, 4, 5]
# num1 = list(filter(lambda num: num % 3 == 0, nums))
# print(num1)

#6
# 6.Використовуючи функцію zip, об'єднайте два списки чисел до списку пар чисел. Вихідні списки: [1, 2, 3] та [4, 5, 6]

# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# num3 = list(zip(num1, num2))
# print(num3)

#7
# 7.Використовуючи функцію map, перетворіть два списки чисел на список їх творів. Вихідні списки: [1, 2, 3] та [4, 5, 6].
# num1 = [1, 2, 3]
# num2 = [4, 5, 6]
# num3 = lambda num1, num2: num1 * num2
# listt = list(map(num3, num1, num2))
# print(listt)

#8
# 8.Використовуючи функцію filter, відфільтруйте список пар чисел, залишивши лише пари, в яких перше число більше за друге.
#  Вихідний список: [(1,2), (3, 1), (4, 4), (5, 3)].
# nums = [(1,2), (3, 1), (4, 4), (5, 3)]
# num_list1 = lambda pair: pair[0] > pair[1]
# num_list2 = filter(num_list1, nums)
# num = list(num_list2)
# print(num)


# 9
# nums = [-1, 3, 6, -3, 0, -4, 7, 9, 10, 2]
# numbers = list(filter(lambda x: x > 0, nums))
# print(numbers)

#10
# num1 = int(input("Enter a number1 : "))
# num2 = int(input("Enter a number2 : "))
# lower = min(num1, num2)
# upper = max(num1, num2)
# num3 = range(num1, num2+1)
#
# numbers = list(filter(lambda x: x % 2 == 0, num3))
# print(numbers)

#11

# numbers = [1, 0, 1.3, 4.6, 7, 3, 2, 9,1, 10]
# num = list(filter(lambda x: isinstance(x, int), numbers))
# print(num)

#12

# logins = ['Cat', 'paRRots', 'CuCuMbEr2', 'FrUUUit123', '12ABCD21']
# additions = list(map(lambda x: x + '$', logins))
# print(additions)

#13

# num1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# num2 = ['Apple', 'Banana', 'Cherri', 'Dolphin', 'Egg', 'Friday', 'God', 'House', 'Mouse', 'Kangaroo']
# num3 = ['!', '@', '#', '$', '%', '&', '*', '+', '~', '^']
# additions = list(zip(num1, num2, num3))
# print(additions)

#14
num1= [1,2,3,4,5,6]
print(f"Початковий список цифр: {num1}")
num2 = ['A','B','C','D','E','F']
num1 = num2
print(f"Новий список: {num1}")


# def move_num_str(num1):
#     list1 = list(map(str, num1))
#     return list1
#
# result = move_num_str(num1)
# print(result)
#
# move_num_str(num1)

























