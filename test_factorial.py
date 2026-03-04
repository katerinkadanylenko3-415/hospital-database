import unittest
from my_log_1 import *


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
