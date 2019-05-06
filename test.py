import unittest

from sigma import sigma

class Test(unittest.TestCase):
    def test_case1(self):
        """ Check if the sigma() works as expected """
        self.assertEqual(sigma(3), 6)
    def test_case2(self):
        """ Check if the sigma() works as expected """
        self.assertEqual(sigma(37), 703)
    def test_case3(self):
        """ Check if the sigma() works as expected """
        self.assertNotEqual(sigma(100), 5040)