import unittest
from index import Fibonacci, formatted_name


class TestFibonacci(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fib = Fibonacci()

    def test_fibonacci_first_element(self):
        self.assertEqual(self.fib(0), 0)

    def test_fibonacci_tenth_element(self):
        self.assertEqual(self.fib(10), 55)

    def test_fibonacci_negative_position(self):
        self.assertRaisesRegex(ValueError, r"Positive integer number expected, got \".*\"", self.fib, -1)


class TestFormattedName(unittest.TestCase):
    def test_formatted_name_with_middle_name(self):
        self.assertEqual(formatted_name("serhii", "rojnuy", "vasylovich"), "Serhii Vasylovich Rojnuy")

    def test_formatted_name_without_middle_name(self):
        self.assertEqual(formatted_name("serhii", "rojnuy"), "Serhii Rojnuy")
