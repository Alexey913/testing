import unittest
from fizz_buzz import fizz_buzz
from first_last_6 import first_last_6
from discount import discount
from lucky_sum import lucky_sum


class TestFizzBuzz(unittest.TestCase):
    def test_fizz_buzz_15(self):
        self.assertEqual(fizz_buzz(45), 'FizzBuzz')

    def test_fizz_buzz_5(self):
        self.assertEqual(fizz_buzz(25), 'Buzz')

    def test_fizz_buzz_3(self):
        self.assertEqual(fizz_buzz(9), 'Fizz')

    def test_fizz_buzz_other(self):
        self.assertEqual(fizz_buzz(7), '7')


class TestFirstLast(unittest.TestCase):
    def test_first_last_6_first(self):
        self.assertTrue(first_last_6(numbers=[6, 5, 10, 8, 5]))

    def test_first_last_6_last(self):
        self.assertTrue(first_last_6(numbers=[8, 5, 10, 8, 6]))

    def test_first_last_6_both(self):
        self.assertTrue(first_last_6(numbers=[6, 5, 10, 8, 6]))

    def test_first_last_6_without(self):
        self.assertFalse(first_last_6(numbers=[0, 5, 10, 8, 2]))


class TestDiscount(unittest.TestCase):
    def test_discount_raise_sum_buy(self):
        self.assertRaisesRegex(ValueError, 'Сумма должна быть больше 0', discount, sum_buy=-10, percent_sale=5)

    def test_discount_raise_sum_percent_less(self):
        self.assertRaisesRegex(ValueError, 'Процент должен быть в диапазоне от 0 до 100', discount, sum_buy=100, percent_sale=-5)

    def test_discount_raise_sum_percent_more(self):
        self.assertRaisesRegex(ValueError, 'Процент должен быть в диапазоне от 0 до 10', discount, sum_buy=100, percent_sale=110)

    def test_discount_sucsess(self):
        self.assertEqual(discount(100, 15), 85)    


class TestLuckySum(unittest.TestCase):
    def test_lucky_sum_error(self):
        self.assertRaisesRegex(ValueError, 'Все числа равны 13', lucky_sum, a=13, b=13, c=13)

    def test_lucky_sum_one_number(self):
        self.assertEqual(lucky_sum(1, 2, 13), 3)    
        self.assertEqual(lucky_sum(1, 13, 4), 5)
        self.assertEqual(lucky_sum(13, 3, 7), 10)
    
    def test_lucky_sum_two_number(self):
        self.assertEqual(lucky_sum(1, 13, 13), 1)    
        self.assertEqual(lucky_sum(13, 13, 4), 4)
        self.assertEqual(lucky_sum(13, 3, 13), 3)

    def test_lucky_sum_two_number(self):
        self.assertEqual(lucky_sum(1, 2, 3), 6)


if __name__ == '__main__':
    unittest.main()
