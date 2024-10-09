import unittest
from index import Fibonacci, formatted_name


class TestFibonacci(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fib = Fibonacci()

    def test_fibonacci_first_element(self):
        self.assertEqual(self.fib(0), 0)

    def test_fibonacci_second_element(self):
        self.assertEqual(self.fib(1), 1)

    def test_fibonacci_third_element(self):
        self.assertEqual(self.fib(2), 1)

    def test_fibonacci_tenth_element(self):
        self.assertEqual(self.fib(10), 55)

    def test_fibonacci_hundredth_element(self):
        self.assertEqual(self.fib(100), 354_224_848_179_261_915_075)

    def test_fibonacci_negative_position(self):
        self.assertRaisesRegex(ValueError, r"Positive integer number expected, got \".*\"", self.fib, -1)


class TestFormattedName(unittest.TestCase):
    def test_formatted_name_with_middle_name(self):
        self.assertEqual(formatted_name("serhii", "rojnuy", "vasylovich"), "Serhii Vasylovich Rojnuy")

    def test_formatted_name_without_middle_name(self):
        self.assertEqual(formatted_name("serhii", "rojnuy"), "Serhii Rojnuy")

    def test_formatted_name_with_middle_name_upper_case(self):
        self.assertEqual(formatted_name("SERHII", "ROJNUY", "VASYLOVICH"), "Serhii Vasylovich Rojnuy")

    def test_formatted_name_without_middle_name_upper_case(self):
        self.assertEqual(formatted_name("SERHII", "ROJNUY"), "Serhii Rojnuy")

    def test_formatted_name_empty_first_name(self):
        self.assertEqual(formatted_name("", "rojnuy"), " Rojnuy")

    def test_formatted_name_empty_last_name(self):
        self.assertEqual(formatted_name("serhii", ""), "Serhii ")

    def test_formatted_name_empty_full_name(self):
        self.assertEqual(formatted_name("", ""), " ")
