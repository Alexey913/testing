import unittest
from hw_app import even_odd_number, number_in_interval

# Напишите тесты, покрывающие на 100% метод evenOddNumber, который проверяет, является ли переданное число четным или нечетным

class TestEvenOddNumber(unittest.TestCase):
    def test_even_odd_number_even(self):
        self.assertTrue(even_odd_number(8), "Число 8 явялется четным")

    def test_even_odd_number_not_even(self):
        self.assertFalse(even_odd_number(15), "Число 15 является нечетным")

    def test_even_odd_number_float(self):
        self.assertFalse(even_odd_number(10.2), "Число 10.2 не является четным")

    def test_even_odd_number_not_number(self):
        self.assertRaises(TypeError, even_odd_number, 'e')

# Разработайте и протестируйте метод numberInInterval, который проверяет, попадает ли переданное число в интервал (25;100)

class TestNumberInInterval(unittest.TestCase):
    def test_number_in_interval_in(self):
        self.assertTrue(number_in_interval(50), "Число 50 находится в диапазоне (25, 100)")

    def test_number_in_interval_less(self):
        self.assertFalse(number_in_interval(10), "Число 10 находится вне диапазона (25, 100)")

    def test_number_in_interval_more(self):
        self.assertFalse(number_in_interval(150), "Число 150 находится вне диапазона (25, 100)")
    
    def test_number_in_interval_down_limit(self):
        self.assertFalse(number_in_interval(25), "Число 25 находится вне диапазона (25, 100)")
    
    def test_number_in_interval_up_limit(self):
        self.assertFalse(number_in_interval(100), "Число 100 находится вне диапазона (25, 100)")

    def test_number_in_interval_float(self):
        self.assertFalse(number_in_interval(10.2), "Число 10.2 вне диапазона (25, 100)")

    def test_even_odd_number_not_number(self):
        self.assertRaises(TypeError, number_in_interval, 'e')

if __name__ == '__main__':
    unittest.main()
