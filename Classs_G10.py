# типи колекцій
# tuple  set   frozenset

# tuple  - list

# userTypes = ('admin', 'student', 'teacher')
# print(userTypes)
# # userTypes[0] = 'admin2'
# # print(userTypes)
#
# NUMBER_PI = 3.14 # all big letters = never change this const
# print(NUMBER_PI)
#
# myEmptyTuple = ()
# print(type(myEmptyTuple))
#
# myTuple1 = (100,)
# print(type(myTuple1))
#
# tuple2 = tuple([1, 2, 3])
# print(tuple2)
#
# itemTuple = ('item1', 'item2', 100, 300, (1,2,3), [2,3,4])
# print(itemTuple)
# print(itemTuple[0])
# print(itemTuple[-1])

# del itemTuple # - you delete tuple
# print(itemTuple)
#
# print(itemTuple.index('item2')) # where it is in list
# print(itemTuple.count('item2')) # how many times it meet us in list
# for i in range(len(itemTuple)):
#     print(itemTuple[i])  # поелемнтний вивід з списку
#
#
# for elem in itemTuple:
#     print(elem) # the same vuvid
#
# tuple1 = ([1])
# tuple2 = ([2])
#
# tuple3 = tuple1 + tuple2
# print(tuple3)
#
# def askPersInf():
#     fName = input("enter your name: ")
#     lName = input("enter your name: ")
#     Birth = input("enter your year birthday: ")
#     return fName, lName, Birth

# persInf = askPersInf()
# print(persInf)
#
# def askHobby():
#     hobbyInd = 1
#     hobbylist = []
#     while True:
#         hobbyName = input("enter your hobby's name: ")
#         if hobbyName == "":
#             print("No info")
#             break
#         else:
#             hobbylist.append(hobbyName)
#             hobbyInd += 1
#     if len(hobbylist) > 0:
#         print(f"you have {hobbyInd -1} hobbies.")
#     else:
#         print("you have no hobby.")
#     return hobbylist


# def askAdditionalInfo(quertyStr):
#     infoInd = 1
#     infolist = []
#     while True:
#         infoName = input("enter your hobby's name: ")
#         if infoName == "":
#             print("No info")
#             break
#         else:
#             infolist.append(infoName)
#             infoInd += 1
#     if len(infolist) > 0:
#         if quertyStr == 'hobby':
#             print(f"you have {infoInd -1} code-languages.")
#         elif quertyStr == 'info':
#             print(f"you have {infoInd -1} code-languages.")
#     else:
#         print("you have no hobby.")
#     return infolist
#
#
# userInfo = []
# userInfo.append(askPersInf())
# userInfo.append(askAdditionalInfo('hobby'))
#
# print(userInfo)


# set  множини
# у множині не може бути дублікатів + немає індексації + не мож вклд списки
# зберігає незмін типи данних, списки тільки через дужки
# може співпрацюв з текстами
mySet1 = {1, 2, 3, 3}
mySet2 = {'Bob', 'Diana', 'Sally'}
mySet3 = {1, 3, 'text', 1.3, True}
print(mySet1)
print(type(mySet2))
print(type(mySet3))

nums = [12, 12, 23, 45, 6, 45]
print(set(nums))

myList1 = ['121', (1, 2, 3, 4)]
print(set(myList1))

marks1 = {1, 2, 3, 4}
marks2 = {4, 3, 2, 1}
print(marks1 == marks2)
for elem in mySet2:
    print(elem)


word = "some letters"
for letter in set(word):
    print(letter)

mySet = {1, 12, 45, 3}
print(mySet)

mySet.add(4)
mySet.update({9, 0, 6})

if 9 in mySet:
    mySet.remove(9)

mySet.remove(6) # виведе помилку якщо ввести неінуючий елемнт
mySet.discard(5) # якщо ввести неіснуючий ел, він проігнрорує і не виведе помилку
mySet.pop()
print(mySet)


old_users = {'user1', 'user2', 'user3'}
new_users = {'user3', 'user4', 'user5'}
print("intersection of sets ")
print(old_users & new_users)  # перетин, може 1 значення
print(old_users.intersection(new_users))
print("Union of sets")
print(old_users | new_users) # об'єднання
print(old_users.union(new_users))
print("diferrence")
print(old_users - new_users)
print(old_users.difference(new_users))


# frozenset - незмінна множина
frozenset1 = frozenset(old_users)
print(frozenset1)


# fruits = ['apple', 'orange', 'apple', 'peach']
# fruit = input("Enter fruit: ")
# print(fruits.count(fruit))


# print(itemTuple.count('item2'))


# fruits = ['apple', 'banana', 'bananamango', 'mango', 'srawberrybanana']















