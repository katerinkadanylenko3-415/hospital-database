import unittest
from factorial import factorial

class TestFactorial(unittest.TestCase):

    def setUp(self):
        self.value = 5

    def tearDown(self):
        self.value = None

    def test_factorial_positive(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(3), 6)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    def test_factorial_not_integer(self):
        with self.assertRaises(ValueError):
            factorial(2.5)
        with self.assertRaises(ValueError):
            factorial("5")


if __name__ == "__main__":
    unittest.main()
