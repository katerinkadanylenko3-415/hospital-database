#1
class Film:
    all_films = []

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        Film.all_films.append(self)

    @classmethod
    def Avg_rating(cls):
        total = 0
        for film in cls.all_films:
            total += film.rating
        return total / len(cls.all_films)

    @classmethod
    def Show_rating(cls):
        for film in cls.all_films:
            print(f"Фільм: {film.name}, рейтинг: {film.rating}")

    @classmethod
    def Show_name(cls):
        for film in cls.all_films:
            print(film.name)



film1 = Film("Avatar", 8)
film2 = Film("Titanic", 9)
film3 = Film("Gladiator", 8)

print("Назви фільмів:")
Film.Show_name()

print("\nРейтинги фільмів:")
Film.Show_rating()

print("\nСередній рейтинг:")
print(Film.Avg_rating())

#2
'''
1 Створіть базовий клас Instrument, який представлятиме загальні властивості та методи для всіх музичних інструментів.
Визначте метод play, який має бути реалізований у підкласах.
2 Створіть підкласи StringInstrument, WindInstrument і PercussionInstrument, які представляють струнні, духові та ударні інструменти відповідно.
Кожен із цих класів повинен успадковувати від Instrument та надавати свою реалізацію методу play.
3 Створіть додаткові підкласи для конкретних музичних інструментів, таких як Guitar, Flute та Drum.
Ці класи повинні успадковувати від відповідних підкласів (StringInstrument, WindInstrument, або PercussionInstrument) та
можуть додатково визначати свої унікальні методи та властивості, наприклад, метод tune для налаштування гітари.
4 Створіть екземпляри різних музичних інструментів та викличте метод play для кожного з них, щоб побачити,
як кожний інструмент звучить.
5 Реалізуйте множинне спадкування, щоб створити новий клас HybridInstrument, який успадковує від кількох класів,
які представляють різні види музичних інструментів. У цьому класі визначте свій метод play, що комбінує звуки від усіх успадкованих класів.
6 Створіть екземпляр HybridInstrument і викличте його метод play, щоб побачити, як множинне успадкування дозволяє комбінувати властивості та методи з кількох батьківських класів.
'''

# class Instrument:
#     def play(self):
#         print("Інструмент звучить")
#
# class StringInstrument(Instrument):
#     def play(self):
#         print("Звучить струнний інструмент")
#
#
# class WindInstrument(Instrument):
#     def play(self):
#         print("Звучить духовий інструмент")
#
#
# class PercussionInstrument(Instrument):
#     def play(self):
#         print("Звучить ударний інструмент")
#
# class Guitar(StringInstrument):
#     def play(self):
#         print("Гітара грає мелодію")
#
#     def tune(self):
#         print("Гітара налаштовується")
#
# class Flute(WindInstrument):
#     def play(self):
#         print("Флейта видає ніжний звук")
#
# class Drum(PercussionInstrument):
#     def play(self):
#         print("Барабан гучно бʼє")
#
# guitar = Guitar()
# flute = Flute()
# drum = Drum()
#
# guitar.play()
# flute.play()
# drum.play()
#
# guitar.tune()
#
# class HybridInstrument(StringInstrument, PercussionInstrument):
#     def play(self):
#         print("Гібридний інструмент поєднує:")
#         StringInstrument.play(self)
#         PercussionInstrument.play(self)
#
# hybrid = HybridInstrument()
# hybrid.play()

#1
import pickle
import gzip

numbers = list(map(int, input("Введіть числа через пробіл: ").split()))

with gzip.open("numbers.dat", "wb") as f:
    pickle.dump(numbers, f)

with gzip.open("numbers.dat", "rb") as f:
    new_numbers = pickle.load(f)

print("Список після завантаження з файлу:", new_numbers)

#2
def save_data(data, filename="numbers.dat"):
    with gzip.open(filename, "wb") as f:
        pickle.dump(data, f)
    print("Дані збережено!")

def load_data(filename="numbers.dat"):
    try:
        with gzip.open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return []

data = []

while True:
    print("\nМеню:")
    print("1. Завантаження даних")
    print("2. Збереження даних")
    print("3. Додавання даних")
    print("4. Видалення даних")
    print("5. Показати список")
    print("0. Вихід")
    choice = input("Ваш вибір: ")

    if choice == "1":
        data = load_data()
        print("Дані завантажено:", data)
    elif choice == "2":
        save_data(data)
    elif choice == "3":
        numbers = list(map(int, input("Введіть числа через пробіл: ").split()))
        data.extend(numbers)
    elif choice == "4":
        numbers = list(map(int, input("Введіть числа для видалення через пробіл: ").split()))
        data = [x for x in data if x not in numbers]
    elif choice == "5":
        print("Поточний список:", data)
    elif choice == "0":
        break
    else:
        print("Невірний вибір!")

#3
users = {}

def save_users(users, filename="users.dat"):
    with gzip.open(filename, "wb") as f:
        pickle.dump(users, f)
    print("Користувачі збережені!")

def load_users(filename="users.dat"):
    try:
        with gzip.open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Файл не знайдено!")
        return {}

while True:
    print("\nМеню користувачів:")
    print("1. Додати користувача")
    print("2. Видалити користувача")
    print("3. Пошук користувача")
    print("4. Редагувати пароль")
    print("5. Показати всіх користувачів")
    print("6. Завантажити з файлу")
    print("7. Зберегти у файл")
    print("0. Вихід")
    choice = input("Ваш вибір: ")

    if choice == "1":
        login = input("Логін: ")
        password = input("Пароль: ")
        users[login] = password
    elif choice == "2":
        login = input("Логін для видалення: ")
        users.pop(login, None)
    elif choice == "3":
        login = input("Логін для пошуку: ")
        if login in users:
            print(f"Пароль: {users[login]}")
        else:
            print("Користувача не знайдено")
    elif choice == "4":
        login = input("Логін для редагування: ")
        if login in users:
            new_pass = input("Новий пароль: ")
            users[login] = new_pass
        else:
            print("Користувача не знайдено")
    elif choice == "5":
        print("Словник користувачів:", users)
    elif choice == "6":
        users = load_users()
        print("Користувачі завантажені:", users)
    elif choice == "7":
        save_users(users)
    elif choice == "0":
        break
    else:
        print("Невірний вибір!")
