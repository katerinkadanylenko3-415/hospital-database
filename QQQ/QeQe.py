# import threading
# import time
#
# numbers = []
#
# user_input = input("Введіть числа по одному через 'Entr' (або 'stop' для завершення): ")
#
# while user_input != "stop":
#     numbers.append(int(user_input))
#     user_input = input("Введіть наступне число або 'stop': ")
#
# def find_max():
#     print("Максимум:", max(numbers))
#     time.sleep(1)
#
# def find_min():
#     print("Мінімум:", min(numbers))
#     time.sleep(1)
#
# thread1 = threading.Thread(target=find_max)
# thread2 = threading.Thread(target=find_min)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("Головна програма завершена !")

#2

# import threading
# file_path = input("Введіть шлях до файлу з числами: ")
#
#
# with open(file_path, "r") as file:
#     content = file.read()
#     numbers = []
#
#     for value in content.split():
#         numbers.append(int(value))
#
# def even_number():
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#
#     with open("even.txt", "w") as file:
#         for num in even_numbers:
#             file.write(str(num) + " ")
#
#     print("Кількість парних чисел:", len(even_numbers))
#
#
# def odd_number():
#     odd_numbers = []
#     for num in numbers:
#         if num % 2 != 0:
#             odd_numbers.append(num)
#
#     with open("odd.txt", "w") as file:
#         for num in odd_numbers:
#             file.write(str(num) + " ")
#
#     print("Кількість непарних чисел:", len(odd_numbers))
#
# thread1 = threading.Thread(target=even_number)
# thread2 = threading.Thread(target=odd_number)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("Головна програма завершена !")


#3
# import threading
#
# def search_word(file_path, word):
#     found = False
#
#     with open(file_path, "r", encoding="utf-8") as file:
#         for line in file:
#             if word in line:
#                 found = True
#                 break
#
#     if found:
#         print(f"Слово '{word}' знайдено у файлі !")
#     else:
#         print(f"Слово '{word}' НЕ знайдено !")
#
# file_path = input("Введіть шлях до файлу: ")
# word = input("Введіть слово для пошуку: ")
#
# thread = threading.Thread(target=search_word, args=(file_path, word))
#
# thread.start()
# thread.join()
#
# print("Пошук завершено !")

#4
import threading
import random
import time

numbers = []

def fill_list():
    for _ in range(10):
        num = random.randint(1, 100)
        numbers.append(num)
        time.sleep(0.3)
    print("Список заповнений:", numbers)

def calculate_sum():
    total = sum(numbers)
    time.sleep(0.8)
    print("Сума елементів списку:", total)

def calculate_average():
    avg = sum(numbers) / len(numbers)
    time.sleep(1.3)
    print("Середнє арифметичне:", avg)

thread_fill = threading.Thread(target=fill_list)
thread_fill.start()
thread_fill.join()

thread_sum = threading.Thread(target=calculate_sum)
thread_avg = threading.Thread(target=calculate_average)

thread_sum.start()
thread_avg.start()

thread_sum.join()
thread_avg.join()

print("Програма завершена !")
