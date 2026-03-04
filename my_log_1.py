''''
import logging

logging.basicConfig(
    level=logging.WARNING,
    filename="logs.log",
    filemode="w",
    format="We have some error: %(asctime)s : %(levelname)s : %(message)s"
)

class Calculator:

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            logging.error("Division by zero")
            raise

    def max(self, a, b):
        return max(a, b)

    def min(self, a, b):
        return min(a, b)

    def percent(self, number, percent):
        return number * percent / 100

    def power(self, a, b):
        return a ** b


import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()
        self.a = 10
        self.b = 5

    def tearDown(self):
        self.calc = None

    def test_add(self):
        self.assertEqual(self.calc.add(self.a, self.b), 15)

    def test_sub(self):
        self.assertEqual(self.calc.sub(self.a, self.b), 5)

    def test_mul(self):
        self.assertEqual(self.calc.mul(self.a, self.b), 50)

    def test_div(self):
        self.assertEqual(self.calc.div(self.a, self.b), 2)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.div(self.a, 0)

    def test_max(self):
        self.assertEqual(self.calc.max(self.a, self.b), 10)

    def test_min(self):
        self.assertEqual(self.calc.min(self.a, self.b), 5)

    def test_percent(self):
        self.assertEqual(self.calc.percent(50, 20), 10)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)


if __name__ == "__main__":
    unittest.main()
'''

#2
'''
Додатково - Завдання 2: Тестування функції для обчислення факторіалу
Створіть функцію factorial(n), яка приймає позитивне ціле число n як аргумент і повертає його факторіал.
Факторіал числа n – це добуток всіх позитивних цілих чисел від 1 до n.
Напишіть юніт-тести для функції factorial, використовуючи модуль unittest. Ваші тести повинні включати такі випадки:
Позитивний тест: Перевірте, чи функція правильно обчислює факторіал для заданого числа (наприклад, 5! = 120).
Тест на нуль: Перевірте, чи факторіал числа 0 дорівнює 1.
Тест на негативне число: Перевірте, що функція генерує виключення ValueError, якщо аргумент є негативним.
Тест на неціле число: Перевірте, що функція генерує виключення ValueError, якщо аргумент не є цілим числом.
Створіть файл test_factorial.py, в якому визначте клас для тестування функцій factorial.
Запустіть тести, використовуючи модуль unittest.
'''

def factorial(n):
    if n >= 0:
        return n * factorial(n - 1)
    elif n < 0:
        return ValueError
    elif n == float:
        return ValueError
    else:
        return f"Your number {n} is negative. You cannot use it for factorials."

import unittest
class Test_factorial(unittest.TestCase):

    def setUp(self):
        self.n = 10

    def tearDown(self):
        self.n = None

    def test_factorial_correct(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 0)

    def test_factorial_negative(self):
        self.assertEqual(factorial(-1), "Your number is negative. It cannot be used for calculating.")

    def test_factorial_float(self):
        self.assertEqual(factorial(3.14), "Your number is float. It cannot be used for calculating.")
        