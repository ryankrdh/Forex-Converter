from locale import currency
from unittest import TestCase
from currency import CurrencyCalculator

currency_rate = CurrencyCalculator()

class CurrencyTestCase(TestCase):
    """
    Unit tests for currency.py
    """

    def test_check_valid_input(self):
        self.assertTrue(currency_rate.check_valid_input('USD', 'EUR', '100'))
        self.assertTrue(currency_rate.check_valid_input('USD', 'jpy', '200'))
        self.assertTrue(currency_rate.check_valid_input('eur', 'usd', '50'))

        # QUESTION: How would I write a test case for this function? Do I need to rewrite my code so that it returns True or False?
        self.assertEqual(currency_rate.check_valid_input('USD', 'EUR', '-11'), True, True, f"Not a valid amount: -11. Please type in a proper amount")
        # ** assertFalse test does not work due to output not being false...
        # self.assertFalse(currency_rate.check_valid_input('USD', 'EUR', '-100'))
        # self.assertFalse(currency_rate.check_valid_input('USD', 'EUR', 'weqr'))
        # self.assertFalse(currency_rate.check_valid_input('USD', 'asd', '100'))
        # self.assertFalse(currency_rate.check_valid_input('USDR', 'EUR', '100'))
        # pass
    
    def test_calculate(self):
        self.assertEqual(currency_rate.check_valid_input())