#1
# try:
#     name = input("What is your name? - ")
#     age = int(input("How old are you? - "))
#     if 0 > age or age > 130:
#         raise ValueError("Вік повинен бути в діапазоні від 0 до 130 років.")
#     print(f"Привіт, {name}! Твій вік — {age}")
#
# except ValueError as e:
#     print(f"Помилка введення - {e}")
#
# except Exception as e:
#     print(f"Помилка {e}")
#
# finally:
#     print("Code has been finished.")


#2
# def Person_info(name1, age1):
#     return name1, age1
#
# try:
#     name2 = input("What is your name? - ")
#     age2 = int(input("What is your age? - "))
#     if not (0 <= age2 <= 130):
#         raise ValueError("Вік повинен бути в діапазоні від 0 до 130 років.")
#     print(f"Привіт, {name2}! Твій вік — {age2}")
#
# except ValueError as e:
#     print(f"Помилка введення - {e}")
#
# except Exception as e:
#     print(f"Помилка {e}")
#
# finally:
#     print("Code has been finished.")
#
# Person_info("Anna", 12)


# def Personal_info(name: str, age: int) -> str:
#     if age < 0 or age > 130:
#         raise ValueError("Введено некоректний вік. Вік повинен бути в діапазоні від 0 до 130.")
#     return f"Привіт, {name}! Твій вік — {age}"
#
# print("\n--- Обробка ЗОВНІ функції ---")
# name = input("Enter your name: ")
# age = input("Enter your age: ")
#
#
# try:
#     age = int(age)
#     if not (0 <= age <= 130):
#         raise ValueError("Вік повинен бути в діапазоні від 0 до 130 років.")
#     print(f"Привіт, {name}! Твій вік — {age}")
#
# except ValueError as e:
#     print(f"Помилка введення - {e}")
#     print("Помилка: Ви ввели буквене значення або невірний формат числа!")
#
# except Exception as e:
#     print(f"Помилка {e}")
#
# finally:
#     print("Code has been finished.")
#
# Personal_info("Anna", 12)

# def Personal_info(name: str, age: int) -> str:
#     try:
#         if age < 0 or age > 130:
#             raise ValueError
#         print(f"Привіт, {name}! Твій вік — {age}")
#
#     except ValueError:
#         return "Помилка: Введено некоректний вік. Вік повинен бути в діапазоні від 0 до 130."
#
#     except Exception as e:
#         return f"Помилка: Виникла несподівана помилка: {e}"
#
#     finally:
#         print("Code has finished.")
#
# Personal_info("Anna", 12)

#3
# def Sum_Numbers():
#     numbers = []
#     print("Введіть додатні числа. Щоб продовжити вводити числа натисніть Enter. Щоб завершити введіть 'done'.")
#     while True:
#             user_input = input("Ведіть число: ").strip()
#
#             if user_input == 'done':
#                 if numbers:
#                     sum_num = sum(numbers)
#                     print(sum_num)
#                 else:
#                     print("\nВведення завершено. Список чисел порожній.")
#                 break
#
#             try:
#                 if user_input < 0:
#                     raise ValueError(f"Помилка! Виявлено від'ємне число: {user_input}. Програма припиняє роботу.")
#
#                     # Додавання коректного числа до списку
#                 numbers.append(user_input)
#
#                 except ValueError as e:
#                 print(f"\n--- ПОМИЛКА ---")
#                 print(e)
#                 print("-----------------")
#                 return  # Зупиняємо виконання функції після помилки
#
#             except Exception as e:
#                 print(f"Виникла несподівана помилка: {e}")
#                 return
#
# Sum_Numbers()


#
# def Sum_Numbers():
#     numbers = []
#     print("Введіть додатні числа. Щоб продовжити вводити числа натисніть Enter (це не вихід!). Щоб завершити, введіть 'done'.")
#
#     while True:
#         user_input = input("Введіть число: ").strip()
#         if user_input.lower() == 'done':
#             if numbers:
#                 sum_num = sum(numbers)
#                 print(f"\n--- РЕЗУЛЬТАТ ---")
#                 print(f"Сума введених чисел: {sum_num}")
#             else:
#                 print("\nВведення завершено. Список чисел порожній.")
#             break
#
#
#         try:
#             number = float(user_input)
#
#             if number < 0:
#                 raise ValueError(f"Помилка! Виявлено від'ємне число: {number}. Програма припиняє роботу.")
#
#             numbers.append(number)
#
#         except ValueError as e:
#             print(f"\n--- ПОМИЛКА ---")
#             print(e)
#             print("-----------------")
#             return
#
#         except Exception as e:
#             print(f"Виникла несподівана помилка: {e}")
#             return
#
#
#
# Sum_Numbers()

#4

# def sum_positive(numbers_list: list) -> float:
#     for number in numbers_list:
#         if number < 0:
#             raise ValueError(f"Помилка! Виявлено від'ємне число у списку: {number}.")
#
#     return sum(numbers_list)
#
#
# def collect_user_data_and_process():
#     user_numbers = []
#     print("Введіть додатні числа. Введіть 'done' або натисніть Enter, щоб завершити.")
#     while True:
#         user_input_str = input("Введіть число: ").strip()
#
#         if user_input_str.lower() == 'done' or not user_input_str:
#             break
#
#         try:
#             number = float(user_input_str)
#             user_numbers.append(number)
#
#         except ValueError:
#             print(f"Помилка: Введено некоректний формат '{user_input_str}'. Спробуйте ще.")
#             continue
#
#     print("\n--- Аналіз зібраного списку ---")
#     print(f"Зібраний список: {user_numbers}")
#
#     if not user_numbers:
#         print("Список порожній. Аналіз не потрібен.")
#         return
#
#     try:
#         result = sum_positive(user_numbers)
#
#         print(f"\n--- УСПІХ ---")
#         print(f"Всі числа додатні. Сума елементів: {result}")
#         print("-------------")
#
#     except ValueError as e:
#         print(f"\n--- ПОМИЛКА ---")
#         print(e)
#         print("Програма зупинена через наявність від'ємного числа.")
#         print("---------------")
#
#
# collect_user_data_and_process()


#5
# def Max_num_in_list(user_numbers):
#     print(f"Max_number = {max(user_numbers)}")
#
# def Min_num_in_list(user_numbers):
#     print(f"Min_number = {min(user_numbers)}")
#
# def Show_list(user_numbers):
#     print(f"user_list: {user_numbers}")
#
# def Show_element(user_numbers, element):
#     element = int(input("Enter index = "))
#     elem = user_numbers[element]
#     print(f"element: {elem}")
#
# def Delete_element(user_numbers, element):
#     element = int(input("Enter index = "))
#     del user_numbers[element]
#     print(f"List without your element '{element}' = {user_numbers}")
#
#
#
# def List_num_operation():
#     user_numbers = []
#     print("Введіть додатні числа. Введіть 'done' або натисніть Enter, щоб завершити.")
#     while True:
#         user_input_str = input("Введіть число: ").strip()
#         if user_input_str.lower() == 'done' or not user_input_str:
#             break
#
#         try:
#             number = float(user_input_str)
#
#             user_numbers.append(number)
#
#         except ValueError:
#             print(f"Помилка: Введено некоректний формат '{user_input_str}'. Спробуйте ще.")
#             continue
#
#     def menu():
#         choice = int(input("What to do? Choose: "
#               "\nShow my list = 1"
#               "\nShow my max_element = 2"
#               "\nShow my min_number = 3"
#               "\nShow my element in list by index = 4"
#               "\nDelete my element in list by index = 5"
#               "\nYour choice is ... = "))
#
#         if choice == 1:
#             print(f"user_list: {user_numbers}")
#
#         elif choice == 2:
#             print(f"Max_number = {max(user_numbers)}")
#
#         elif choice == 3:
#             print(f"Min_number = {min(user_numbers)}")
#
#         elif choice == 4:
#             element = int(input("Enter index = "))
#             elem = user_numbers[element]
#             print(f"element: {elem}")
#
#         elif choice == 5:
#             element = int(input("Enter index = "))
#             del user_numbers[element]
#             print(f"List without your element '{element}' = {user_numbers}")
#
#         else:
#             print("That's not a valid choice.")
#
# def List_num_operation():
#     user_numbers = []
#
#     print("--- ЗАПОВНЕННЯ СПИСКУ ---")
#     print("Введіть числа. Введіть 'done' або натисніть Enter, щоб завершити.")
#     while True:
#         user_input_str = input("Введіть число: ").strip()
#
#         if user_input_str.lower() == 'done' or not user_input_str:
#             break
#
#         try:
#             number = float(user_input_str)
#             user_numbers.append(number)
#
#         except ValueError:
#             print(f"Помилка: Введено некоректний формат '{user_input_str}'. Спробуйте ще.")
#             continue
#
#     if not user_numbers:
#         print("\nСписок порожній. Програма завершує роботу.")
#         return
#
#     print("\n--- МЕНЮ ОПЕРАЦІЙ ---")
#
#     while True:
#         print(f"Поточний список: {user_numbers}")
#         print("1. Відобразити список")
#         print("2. Отримати максимальне значення")
#         print("3. Отримати мінімальне значення")
#         print("4. Відобразити елемент за індексом")
#         print("5. Видалити елемент за індексом")
#         print("0. Вийти з програми")
#         print("------------")
#
#         try:
#             choice = input("Ваш вибір (0-5): ").strip()
#             choice = int(choice)
#         except ValueError:
#             print("Некоректний вибір. Введіть число від 0 до 5.")
#             continue
#
#         if choice == 0:
#             print("Програма завершена. До побачення!")
#             break
#
#         elif choice == 1:
#             print(f"\nВідображення списку: {user_numbers}")
#
#         elif choice == 2:
#             print(f"\nМаксимальне значення: {max(user_numbers)}")
#
#         elif choice == 3:
#             print(f"\nМінімальне значення: {min(user_numbers)}")
#
#         elif choice == 4:
#             try:
#                 index = int(input(f"Введіть індекс (від 0 до {len(user_numbers) - 1}): "))
#                 elem = user_numbers[index]
#                 print(f"Елемент за індексом {index}: {elem}")
#             except ValueError:
#                 print("Помилка: Індекс має бути цілим числом.")
#             except IndexError:
#                 print(f"Помилка: Індекс {index} виходить за межі списку (0 до {len(user_numbers) - 1}).")
#
#         elif choice == 5:
#             try:
#                 index = int(input(f"Введіть індекс для видалення (від 0 до {len(user_numbers) - 1}): "))
#
#                 deleted_element = user_numbers[index]
#
#                 del user_numbers[index]
#
#                 print(f"Елемент '{deleted_element}' за індексом {index} успішно видалено.")
#                 print(f"Новий список: {user_numbers}")
#
#                 if not user_numbers:
#                     print("Список став порожнім. Програма завершує роботу.")
#                     break
#
#             except ValueError:
#                 print("Помилка: Індекс має бути цілим числом.")
#             except IndexError:
#                 print(f"Помилка: Індекс {index} виходить за межі списку (0 до {len(user_numbers) - 1}).")
#
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")
#
#
# List_num_operation()


