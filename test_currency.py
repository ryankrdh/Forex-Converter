from unittest import TestCase
from currency import CurrencyCalculator

currency_rate = CurrencyCalculator()

class CurrencyCalculatorUnittest(TestCase):
    """
    Unit tests for currency.py
    """

    def check_valid_input(self):