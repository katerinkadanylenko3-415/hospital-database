# from pickletools import string1
#
# myStr = "Hello"
# print(type(myStr))
# print(myStr)
#
# myStr2 = 'hello'
# print(myStr2)
#
# myStr3 = '''
# some
# text
# '''
#
# userSas = "python пайтон"
# userSasEncode = userSas.encode('utf-8')
#
# userSasDec = userSasEncode.decode('utf-8')
#
# print(userSas, "==", userSasEncode)
#
# print(id(myStr))
# myStr = "new text"
# print(id(myStr))
#
#
myStr = "python"
print(myStr)
print(myStr[0])
print(myStr[1])
print(myStr[len(myStr)-1])
print(len(myStr))
#
# # myStr[0] = "s" # do not in this way, TypeError: 'str' object does not support item assignment
#
# str1 = "hello "
# str2 = "admin"
# print(str1 + str2)

# методи змні регістру ряду - мал і вел буква
# str1 = "python cool"
# print(str1)
# print(str1.upper())
# print(str1.lower())
# print(str1.title()) # every word with the first letter is big
# print(str1.capitalize()) # only the first word with big letter
# print(str1.swapcase()) # lower = upper, upper = lower
#
# # методи пошуку підядок в рядку 9шматочок у рядку)
# print(str1.count("y"))
# print(str1.count("python", 10)) # весь код # з 10-го символу
#
# print(str1.find('python', 10)) #коли уперше зустріч слово
# print(str1.find('test', 10))
#
# print(str1.rfind('python')) #  шукає з кінця рядка
#
# print(str1.index('t')) # виклик виключення, вказ фолз
# print(str1.rindex('t')) #
#
# # методи перевірки рядків
# print(str1.endswith("python"))
# print(str1.startswith("python"))


testStr = 'ftf'
print(testStr.isdigit())
print(testStr.isalpha())
print(testStr.islower())
print(testStr.isupper())
print(testStr.isalnum())
print(testStr.isspace())
#
# # методи форматування рядків
#
# print(testStr.center(40)) # пробілів від слова спочатку
# print(testStr.center(40, "*"))
# testSpace = " space "
# print(testSpace.lstrip()) # про зайві пробіли/ на початку немає
# print(testSpace.rstrip()) # про зайві пробіли/ на кінці немає
# print(testSpace.strip()) # і там і там видаляє пробіли

# # зрізи ,фрагмент дістати з рядка
# myStr2 = "Hello World"
# print(myStr2)
# print(myStr2[0:6])
# print(myStr2[:6]) # = print(myStr2[0:6])
# print(myStr2[:-1])
# print(myStr2[-1:])
#
# print(myStr2[0:10:2]) # останнє - інтервал пропущених букв
# print(myStr2[:len(myStr2)//2])  #половина символів виводить


# print(f"str1: {str1}, str2: {str2}" ) # оbєдн текст зі смінними

# print(testStr.isdigit())
# print(testStr.isalpha())

# User = input("Enter a number : ")
# number = "User"
# digits = 0
# letters = 0
#
# for s in number:
#     if s.isdigit():
#         digits += 1
#     elif s.isalpha():
#         letters = 1
#
# print(f"digits : {digits}")
# print(f"letters : {letters}")




