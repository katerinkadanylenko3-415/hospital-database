# dictionary
'''
nums = [1, 2, 3]
print(nums[0])

student_info = ["Bob", 19, 11]
print(f"Name: {student_info[0]}")

str_info_dict = {"name": "Bob",
                 "age": 19,
                 "avg_mark": 11}

print(type(str_info_dict))

bookDict = {
    'author': 'Vlad',
    'title': 'Python Programming',
    'price': 230,
    'pages': 550
}
print(bookDict)

mydict1 = dict([("a", 111), ("b", 222), ("c", 333)])
print(mydict1)

keyList = ["a", "b"]
valueList = [111, 222]
mydict2 = dict(zip(keyList, valueList))
print(mydict2)

mydict3 = dict(firstname="Bill", lastname="Geits")
print(mydict3)

emptyDict = {}
emptyDict['newkey'] = 111
emptyDict['newkey'] = 222 # update
print(emptyDict)

print(len(bookDict))

print(bookDict)
# newkey = input("Enter new properties of book: ")
# if newkey not in bookDict:
#     bookDict[newkey] = input("Enter new value: ") # add new key with value
#
# print(bookDict['language'])


for key in bookDict:
    print(f"{key} : {bookDict[key]}")



print(bookDict.items())
for key, value in bookDict.items():
    print(f"{key} : {value}")

# print(bookDict.get('title',"start"))
# # print(bookDict.get['newkey'])

bookDict.update([('reading age', 20), ('cnline', False)])
print(bookDict)

# del bookDict
# print(bookDict.clear()) # робимо його пустим
print(bookDict.values())
print(bookDict.keys())
print(bookDict.pop('title')) # del item by key, anoth way = error
print(bookDict.popitem())
print(bookDict)

'''

users = [
    {'name': 'user1', 'age': 21, 'login1': 'admin1'},
    {'name': 'user2', 'age': 22, 'login2': 'admin2'},
    {'name': 'user2', 'age': 23, 'login3': 'admin3'},
    {'name': 'user3', 'age': 24, 'login4': 'admin4'},
    {'name': 'user3', 'age': 25, 'login5': 'admin5'},

]
# keyName = input("Enter info type: ")
# keyValue = input("Enter info value: ")
# keyValue = keyValue if keyName != 'age' else int(keyValue)
# ifElementFount = False
#
# for user in users:
#     if user.get(keyName) == keyValue:
#         print("Element is found ")
#         for key, value in user.items():
#             print(f"{key} : {value}")
#
#         ifElementFount = True
#         break
#
# if not ifElementFount:
#     print("Element is not found ")




def find_user_by_key(users, keyName, keyValue):
