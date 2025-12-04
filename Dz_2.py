# file_name1 = "main1.txt"
# try:
#     file1 = open(file_name1, 'w', encoding='utf-8')
#     file1.write("some text \nCherry \nGood")
# finally:
#     if 'file1' in locals() and not file1.closed:
#         file1.close()
#
# file_name2 = "main2.txt"
# try:
#     file2 = open(file_name2, 'w', encoding='utf-8')
#     file2.write("some text \nCherry \nBad")
# finally:
#     if 'file2' in locals() and not file2.closed:
#         file2.close()
#
# print(f"Створено файл 1: {file_name1}")
# print(f"Створено файл 2: {file_name2}")
#
# with open(file_name1, 'r', encoding='utf-8') as f:
#     print(f"{file_name1} вміст: {f.read()}")
# with open(file_name2, 'r', encoding='utf-8') as f:
#     print(f"{file_name2} вміст: {f.read()}")
#
#
#
# def compare_files_simple(file1_name, file2_name):
#     try:
#         with open(file1_name, 'r', encoding='utf-8') as file1, \
#                 open(file2_name, 'r', encoding='utf-8') as file2:
#
#             line_num = 0
#
#             for line_a, line_b in zip(file1, file2):
#                 line_num += 1
#
#                 if line_a != line_b:
#                     print(f"\n--- ЗНАЙДЕНО РОЗБІЖНІСТЬ (Рядок {line_num}) ---")
#                     print(f"Файл 1 (рядок): '{line_a.strip()}'")
#                     print(f"Файл 2 (рядок): '{line_b.strip()}'")
#                     return
#
#             print("\nУсі проаналізовані рядки співпадають.")
#
#     except FileNotFoundError:
#         print("\nПомилка: Один або обидва файли не знайдено.")
#     except Exception as e:
#         print(f"\nВиникла несподівана помилка: {e}")
#
#
# compare_files_simple("main1.txt", "main2.txt")

#2

# 2
SOURCE_FILE = "source.txt"
OUTPUT_FILE = "statystyka.txt"

test_content = "Валентність - це здатність елементу приєднувати до себе 1 і більше елементів. \nІснує 118 елементів, 90 з яких знаходяться в природі."

with open(SOURCE_FILE, 'w', encoding='utf-8') as f:
    f.write(test_content)

print(f"Створено вихідний файл '{SOURCE_FILE}' для аналізу.")
print("---")


# def simple_file_stats(source_path, output_path):
#     VOWELS = "аеиіоуяюєї"
#     CONSONANTS = "бвгґджзклмнпрстфхцчшщ"
#
#     vowel_count = 0
#     consonant_count = 0
#     digit_count = 0
#
#     try:
#         with open(source_path, 'r', encoding='utf-8') as f:
#             content = f.read()
#
#     except FileNotFoundError:
#         print(f"Помилка: Файл '{source_path}' не знайдено!")
#         return
#
#     char_count = len(content)
#
#     line_count = content.count('\n') + 1
#
#
#     for char in content.lower():
#
#         if char in VOWELS:
#             vowel_count += 1
#
#         elif char in CONSONANTS:
#             consonant_count += 1
#
#         elif char.isdigit():
#             digit_count += 1
#
#
#     results = [
#         f"Статистика файлу: {source_path}",
#         f"--------------------------------",
#         f"Кількість символів: {char_count}",
#         f"Кількість рядків: {line_count}",
#         f"Кількість голосних літер: {vowel_count}",
#         f"Кількість приголосних літер: {consonant_count}",
#         f"Кількість цифр: {digit_count}"
#     ]
#
#     try:
#         with open(output_path, 'w', encoding='utf-8') as f_out:
#             f_out.write('\n'.join(results))
#         print(f"\nСтатистика записана у файл: '{output_path}'")
#
#     except Exception as e:
#         print(f"Помилка при записі у файл: {e}")
#
#
# simple_file_stats(SOURCE_FILE, OUTPUT_FILE)

#4
# def find_longest_line_simple(filename):
#     try:
#
#         with open(filename, 'r', encoding='utf-8') as f:
#             all_lines = f.read().splitlines()
#
#         if not all_lines:
#             print(f"Файл '{filename}' порожній.")
#             return 0
#
#         lengths = []
#         for line in all_lines:
#             lengths.append(len(line))
#
#         max_length = max(lengths)
#
#         print(f"Довжина найдовшого рядка: **{max_length}** символів.")
#         return max_length
#
#     except FileNotFoundError:
#         print(f"Помилка: Файл '{filename}' не знайдено.")
#         return -1
#     except Exception as e:
#         print(f"Сталася помилка: {e}")
#         return -1
#
#
# file_to_check = "my_text_file_simple.txt"
#
# try:
#     with open(file_to_check, 'w', encoding='utf-8') as f:
#         f.write("Короткий.\n")
#         f.write("Це наш найдовший рядок для тестування.....\n")
#         f.write("Середнійййй.")
# except:
#     pass
#
# find_longest_line_simple(file_to_check)


#5
SOURCE_FILE = "document.txt"

test_content = """
Кожен атом будь-якого елементу складається з електронів, протонів та нейтронів.
Атом Гідрогену має найменшу кількість електронів - 1.
Особливість електронів - негативний заряд.
За допомогою електронів металам і деяким речовинам притаманна властивість "електропровідність".
Масою електронів в розрахунках можна знехтувати за рахунок їхньої неймовірно малої маси.
"""

with open(SOURCE_FILE, 'w', encoding='utf-8') as f:
    f.write(test_content)

print(f"Створено файл '{SOURCE_FILE}' для тестування.")

def simple_word_count(source_path):
    try:
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

    except FileNotFoundError:
        print(f"Помилка: Файл '{source_path}' не знайдено.")
        return


    search_word = input("\nВведіть слово (або частину слова) для підрахунку: ").strip()

    if not search_word:
        print("Ви нічого не ввели.")
        return


    content_lower = content.lower()
    search_word_lower = search_word.lower()


    count = content_lower.count(search_word_lower)

    print(f"\n--- РЕЗУЛЬТАТ ---")
    print(f"Шукане слово/фрагмент: '{search_word}'")
    print(f"Кількість входжень у файлі: {count}")
    print("-------------------")


simple_word_count(SOURCE_FILE)








