# def add(*args, **kwargs):
#     logging.info("Add func start ")
#     result = 0
#     for elem in list(args) + list(kwargs.values()):
#         if isinstance(elem, (int, float, bool)):
#             result += elem
#         else:
#             try:
#                 result += float(elem)
#                 continue
#             except (ValueError, TypeError) as ex:
#                 logging.error(ex)
#     return result
#
# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename="logs.log",
#     filemode="w",
#     format="We have next logging message: %(asctime)s : %(levelname)s - %(message)s"
# )
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
#
# try:
#     logging.warning("cant devide by zero")
#     print(10/0)
# except Exception as ex:
#     logging.exception(ex)
#     logging.error(ex)
#
# add(2, "2asd")

def is_palindrome(text):
    text = text.lower()
    reversed_text = ""

    for char in text:
        reversed_text = char + reversed_text

    return text == reversed_text


import unittest

class TestIsPalindrome(unittest.TestCase):

    def test_palindrome(self):
        self.assertTrue(is_palindrome("Alla"))
        self.assertTrue(is_palindrome("Anna"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("fruit"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

if __name__ == "__main__":
    unittest.main()




