# def debug_info_universal(func):
#     def wrapper(*args):
#         print("Start function")
#         result = func(*args)
#         print("End function")
#         return result
#     return wrapper
#
# @debug_info_universal
# def add_numbers(a, b):
#     print(f"Adding {a} and {b}")
#     return a + b
#
# print(f"Result: {add_numbers(10, 5)}")

#2
# def upper_text(func):
#     def wrapper(*args):
#         result = func(*args)
#
#         if isinstance(result, str):
#             return result.upper()
#         else:
#             return result
#
#     return wrapper
#
#
# @upper_text
# def get_greeting(name, language):
#     return f"hello, {name}! your language is {language}."
#
#
# @upper_text
# def get_simple_word():
#     return "python"
#
# print(get_greeting("python", "python"))
# print(get_simple_word())

#4
# def repeat_three_times(func):
#     def wrapper():
#         print("--- Починаємо повторення ---")
#
#         for i in range(3):
#             print(f"Запуск функції (Раз {i + 1})")
#
#             func()
#
#         print("--- Повторення завершено ---")
#
#     return wrapper
#
# @repeat_three_times
# def print_simple_message():
#     print("Я виконуюсь!")
#
#
# print("--- Запуск функції ---")
# print_simple_message()

