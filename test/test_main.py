import unittest

from app import main


class TestMain(unittest.TestCase):

    def test_hello(self):
        result = main.hello()
        self.assertEqual("Hello world", result)

    def test_holidays_japan(self):
        result = main.holidays()
        self.assertIn("Japan", result)

    def test_holidays_india(self):
        result = main.holidays()
        self.assertIn("India", result)
