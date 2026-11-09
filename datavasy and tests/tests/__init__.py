import unittest
from unittest import TestCase
from app import calc
class TestCalcMethods(TestCase):
    def test_calc(self):
        self.assertEqual(calc(1,2), 'F00')

if __name__ == '__main__':
    tests = TestCalcMethods()
    tests.test_calc()