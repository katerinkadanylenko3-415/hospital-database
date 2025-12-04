# # 1
# numbers = input("Enter 5 numbers with spaces: ")
# numbers = numbers.split()
# numbers = [int(elements) for elements in numbers]
#
# print(numbers)
# print("Перше число - " , numbers[0])
# print("Останнє число - " , numbers[4])

# #2

# numbers = [3, 7, 2, 9, 4]
# print("Максимальне число = " , max(numbers))
# print("Мініальне число = " , min(numbers))
# print("Сума = " , sum(numbers))

#3
#Користувач вводить слова через пробіл.
#Створити список слів та вивести кожне на новому рядку.
# words = input("enter words with spaces: ")
# words = words.split()
# print(words)
# for word in words:
#     print(word)

#4
# Є список:
# fruits = ["apple", "banana", "orange"]
# Додати новий фрукт, введений користувачем.
# Вивести оновлений список.

# fruits = ["apple", "banana", "orange"]
# print(fruits)
# addition = input("Enter one more fruit: ")
# fruits.append(addition)
# print(fruits)

#5
# Є список:
# nums = [2, 4, 6, 8, 10]
# Замінити другий елемент списку на число 100
# Вивести новий список.
#
# nums = [2, 4, 6, 8, 10]
# print(nums)
# nums[1] = 100
# print(nums)

#6
# Користувач вводить числа.
# Сформувати список і вивести тільки парні числа.
# list_num = []
# nums = input("Enter numbers with spaces: ").split()
# for i in nums:
#     if int(i) % 2 == 0:
#         list_num.append(int(i))
#
# print(list_num)

#7
# Створити список з 10 будь-яких чисел.
# Вивести список у зворотному порядку (не змінюючи сам список).

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums)
# print(nums[:: -1])

#8
# Є список символів:
# letters = ['a', 'b', 'c', 'd']
# Видалити останній елемент і вивести список.

# letters = ['a', 'b', 'c', 'd']
# print(letters)
# letters.pop(3)
# print(letters)

#9
# Є список:
# nums = [1, 1, 2, 3, 3, 3, 4]
# Порахувати, скільки разів зустрічається число 3.

# nums = [1, 1, 2, 3, 3, 3, 4]
# print(nums)
# three = nums.count(3)
# print(three)


#10
# Користувач вводить 7 чисел, додати їх у список
# і вивести середнє арифметичне елементів.

# list_num = []
# i = input("Enter 7 numbers: ").split()
# for num in i:
#     (list_num.append(int(num)))
# print(list_num)
# print(f"avg: {sum(list_num)/len(list_num)}")

# 11
# У списку цілих, заповненому випадковими числами, визначити мінімальний, додатний елемент і максимальний,
# від'ємний елемент, порахувати кількість від'ємних елементів, порахувати кількість додатних елементів, порахувати кількість нулів. Результати вивести на екран

# numbers = [-1, 1, 0, 2, -2, 7, 8, -10, 0, 5, 0]
# print(numbers)
# positive_numbers = [num for num in numbers if num > 0]
# if positive_numbers:
#     min_positive = min(positive_numbers)
#     print("Мінімальний додатний елемент:", min_positive)
# else:
#     print("Додатніх елементів немає")
#
# negative_numbers = [num for num in numbers if num < 0]
# if negative_numbers:
#     max_negative = max(negative_numbers)
#     print("Максимальний від'ємний елемент:", max_negative)
# else:
#     print("Від'ємних елементів немає")
#
# neg_num = 0
# pos_num = 0
# for num in numbers:
#     if num < 0:
#         neg_num += 1
#     if num > 0:
#         pos_num += 1
#
# print("Кількість від'ємних чисел = " , neg_num)
# print("Кількість додатніх чисел = " , pos_num)
#
# Zeros = numbers.count(numbers == 0)
# print("Кількість нулів = " , Zeros)











