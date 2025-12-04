# #1
# capitals = {"Україна": "Київ", "Польща": "Варшава", "Німеччина": "Берлін"}
# country = list(capitals.keys())
# city = list(capitals.values())
# print(country)
# print(city)
# capitals["Франція"] = "Париж"
# print(capitals)
# country = list(capitals.keys())
# city = list(capitals.values())
# print(country)
# print(city)


# #2
# prices = {"яблуко": 15, "банан": 20, "груша": 18}
# item = input("Enter item`s name: ").lower()
# if item in prices:
#     price = prices[item]
#     print(f"Ціна за {item} становить: {price} грн.")
# else:
#     print(f"Такого товару '{item}' немає в магазині.")

#3

#3
# employees = {
#     "Іванов І.І.": {
#         "Телефон": "050-123-45-67",
#         "Email": "ivanov@firm.com",
#         "Посада": "Менеджер",
#         "Кабінет": "201",
#         "Skype": "ivanov_skype"
#     },
#     "Матвєєнко І.Р.": {
#         "Телефон": "097-666-94-84",
#         "Email": "matveenko@firm.com",
#         "Посада": "Директор",
#         "Кабінет": "301",
#         "Skype": "matveenko_skype"
#     }
# }
#
#
# def add_employee():
#     print("\n--- Додавання працівника ---")
#     pib = input("Введіть ПІБ працівника : ").strip()
#
#     if pib in employees:
#         print(f"Помилка: Працівник з ПІБ '{pib}' вже існує.")
#         return
#
#     phone = input("Введіть телефон: ")
#     email = input("Введіть корпоративний email: ")
#     position = input("Введіть назву посади: ")
#     office = input("Введіть номер кабінету: ")
#     skype = input("Введіть Skype: ")
#
#     employees[pib] = {
#         "Телефон": phone,
#         "Email": email,
#         "Посада": position,
#         "Кабінет": office,
#         "Skype": skype
#     }
#     print(f"Працівника '{pib}' успішно додано.")
#
#
# def find_employee():
#     print("Пошук працівника...")
#     pib = input("Введіть ПІБ працівника для пошуку: ").strip()
#
#     if pib in employees:
#         print(f"Інформація про працівника: {pib}")
#         for key, value in employees[pib].items():
#             print(f"{key}: {value}")
#     else:
#         print(f"Працівника з ПІБ '{pib}' не знайдено.")
#
#
# def delete_employee():
#     print("Видалення працівника...")
#     pib = input("Введіть ПІБ працівника для видалення: ").strip()
#
#     if pib in employees:
#         del employees[pib]
#         print(f"Працівника '{pib}' видалено.")
#     else:
#         print(f"Працівника з ПІБ '{pib}' не знайдено.")
#
#
# def update_employee():
#     print("Зміна даних працівника...")
#     pib = input("Введіть ПІБ працівника для зміни даних: ").strip()
#
#     if pib not in employees:
#         print(f"Працівника з ПІБ '{pib}' не знайдено.")
#         return
#
#     print(f"Зміна даних для '{pib}'...")
#     for key, value in employees[pib].items():
#         print(f"{key} (поточне: {value})")
#
#     field = input("Яке поле змінити? (Телефон, Email, Посада, Кабінет, Skype): ").capitalize()
#
#     if field in employees[pib]:
#         new_value = input(f"Введіть нове значення для {field}: ")
#         employees[pib][field] = new_value
#         print(f"Дані працівника '{pib}' успішно оновлено. Нове значення {field}: {new_value}")
#     else:
#         print(f"Поля '{field}' не існує.")
#
# def menu():
#     """Головне меню програми."""
#     while True:
#         print("\n===============================")
#         print("  МЕНЮ ПРОГРАМИ «ФІРМА»")
#         print("===============================")
#         print("1. Додати працівника")
#         print("2. Знайти працівника")
#         print("3. Змінити дані працівника")
#         print("4. Видалити працівника")
#         print("5. Показати всіх працівників")
#         print("6. Вихід")
#         print("-------------------------------")
#
#         choice = input("Оберіть дію (1-6): ")
#
#         if choice == '1':
#             add_employee()
#         elif choice == '2':
#             find_employee()
#         elif choice == '3':
#             update_employee()
#         elif choice == '4':
#             delete_employee()
#         elif choice == '5':
#             print("Дякуємо за використання програми! До побачення.")
#             break
#         else:
#             print("Невірний вибір. Будь ласка, введіть число від 1 до 5.")
#
#
#
# print(menu())

#4

# dict1 = {
#     'вишня': 10,
#     'черешня': 20,
#     'полуниця': 30,
# }
#
# dict2 = {
#     'виноград': 11,
#     'банан': 22,
#     'полуниця': 33,
# }
#
# def add_dictionaries(dict1: dict, dict2: dict):
#     dict_result = dict1.copy()
#     for key, value in dict1.items():
#         if key in dict_result:
#             dict_result[key] += value
#         else:
#             dict_result[key] = value
#
#
#     return dict_result
#
# result = add_dictionaries(dict1, dict2)
# print(result)


# dict1 = {
#     'вишня': 10,
#     'черешня': 20,
#     'полуниця': 30,
# }
#
# dict2 = {
#     'виноград': 11,
#     'банан': 22,
#     'полуниця': 33,
# }
#
#
# def add_dictionaries(dict1: dict, dict2: dict) -> dict:
#     dict_result = dict1.copy()
#     for key, value in dict2.items():
#         if key in dict_result:
#             dict_result[key] += value
#         else:
#             dict_result[key] = value
#
#     return dict_result
#
# result = add_dictionaries(dict1, dict2)
# print(result)






