import unittest
from unittest.mock import Mock

from rand_number_list import rand_number_list
from max_elem import find_max


class TestRandList(unittest.TestCase):
    def test_rand_number_list(self):
        lst = rand_number_list(10)
        self.assertIsInstance(lst, list)
        self.assertEqual(len(lst), 10)


class TestRnd(unittest.TestCase):
    def test_rnd(self):
        lst = rand_number_list(10)
        self.assertEqual(find_max(lst), sorted(lst)[-1])
        

if __name__ == '__main__':
    unittest.main()
