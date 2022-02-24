from locale import currency
from unittest import TestCase
from currency import CurrencyCalculator

currency_rate = CurrencyCalculator()

class CurrencyTestCase(TestCase):
    """
    Unit tests for currency.py
    """

    def check_valid_input(self):
        self.assertTrue(currency_rate.check_valid_input('USD', 'EUR', 100))