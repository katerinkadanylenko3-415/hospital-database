# списки
from faulthandler import cancel_dump_traceback_later

num1 = 10
num2 = 20
num3 = 30

# list

numbers = [10, 20, 30]  # буде з дужками
print(numbers)
print(type(numbers)) # class - list

courses = list(('Math' , 'Design' , 'Blogging')) # колекція для вже існуючих колекцій
print(courses)
#
elements = [123, 123,  "Cat" , True , 3.14]
print(elements)

list1 = [i for i in range(1 , 10)] # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1)

print(elements[0])
print(elements[1])
print(len(elements))
# print(len(elements[len(elements)-1])

print(list1[:len(list1)//2]) # pershi
print(list1[len(list1)//2])
print(list1[len(list1)//2:]) # ostanni

print(list1[:: -1])

# change elements in list
marks = [10 , 2, 9, 11, 8]
print(marks)
marks[1] = 10
print(marks)
# [10, 2, 9, 11, 8]
# [10, 10, 9, 11, 8]

# python methods for list
marks = []

prices = [100, 234, 567, 34, 7]
print(f"count of elem: {len(prices)}") #  кількість
print(prices)
print(f"Sum of prices: {sum(prices)}") # сума
print(f"max price: {max(prices)}") # макс ціна
print(f"min price: {min(prices)}")
print(f"avg price: {sum(prices)/len(prices)}")
print(f"sorted prices: {sorted(prices)}") # у порядку зростання виставить

category1 = ["drama" , "comedy"]
category2 = ["actioin" , "killer"]
print(category1 + category2)
print(category1 * 2)

# methods of list

# додавання
categories = category1 + category2
print(categories)
categories.append("fantasy") # додає у кінець щось
print("add fantasy")
print(categories)
categories.insert(0, "horror") # додає у чітко визначенен місце, зміщенняБ місце познач індексом
print(categories)
categories.extend(category1) # додав у колекцію інший список, просто у кінець
print(categories)

# віднімання
categories.pop(1) # ostanniy element,now we dont have drama, index ne perevy diapazon
categories.remove("drama") # delet znachennya, yak ne zna index
# categories.clear()  delite everything
print(categories)
if 'horror' in categories: # захист елементів від видалення
    print(categories.index('horror'))

print(categories.count("fantasy"))
categories.sort(reverse=True)  # по алф з кінця
print(categories)

new_cats = categories  #копіювання
# categories.pop()
print(new_cats)

studScores = [['St', 5, 11, 12, 8, 9, 10],
             ['Jane', 2],
             ['Bill', 2]]
print(studScores)
for cat in categories:
    print(cat)

for stud in studScores:
    for data in stud:
        print(data, end=" | ")
    print()


# sun = int(input("Enter your elements of list: "))
# cus = [sun]
# for cus in sun:
#     print(f"Sum of elements: {sum(sun)}")


    #print(f"Avg element: {avg(sun)}")


# # num = [1, 2, 3]
# num = list(int(input("Enter a number: "))
# print(f"Sum of elements: {sum(num)}")
# print(f"Avg of elements: {sum(num)/len(num)} ")

# numbers = []
# sum = 0
# num = -1
#
# while num != 0:
#
#     num = int(input("Enter a number: "))
#     sum += num
#
# print(f"sum: {sum(numbers)")
# print(f"avg: {sum(numbers)/len(numbers) -1}")
