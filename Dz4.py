# #1
# sentence = input("Enter your sentence: ")
# count = len(sentence)
# print(count)

# #2
# text = input("Enter a sentence: ")
# for i in text:
#     print(i, end='\n')

# #3
# count = 0
# text = input("Enter a sentence: ")
# for i in text:
#     if i.isupper():
#         count += 1
#
# print(count)

#4
# count = 0
# text = input("Enter a sentence: ")
# for i in text:
#     if i in ".!?":
#         count += 1
#
# print(count)
# print(str1.endswith("python"))
# print(str1.startswith("python"))

#5

# text = input("Enter a sentence: ")
# clean_text = ""
# for a in text:
#     if a.isalnum():
#         clean_text += a.lower()
# for a in range(len(clean_text)//2):
#     if clean_text[a] == clean_text[-(a+1)]:
#         print("Це паліндром")
#     else:
#         print("Це не паліндром")

text1 = input("Enter a sentence: ")
text2 = text1.lower()
text = text2.replace(" ", "")
if text == text[::-1]:
    print("Це паліндром")
else:
    print("Це не паліндром")


#6
#print(str1.rfind('python')) #  шукає з кінця рядка
#print(str1.find('test', 10))
# # методи перевірки рядків
# print(str1.endswith("python"))
# print(str1.startswith("python"))














