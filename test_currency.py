from locale import currency
from unittest import TestCase
from currency import CurrencyCalculator
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *
from app import app

currency_rate = CurrencyCalculator()

class CurrencyTestCase(TestCase):
    """
    Unit tests for currency.py
    """
    
# TESTING routes

    def test_forex_form(self):
        with app.test_client() as client:
            # import pdb
            # pdb.set_trace()
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<form action="/currency" class="user_input">', html)

    def test_currency_route(self):
        with app.test_client() as client:
            res = client.post('/currency', query_string={'convert_to':'EUR', 'convert_from':'USD', 'money_amount': '100'})
            html = res.get_data(as_text=True)
            # import pdb
            # pdb.set_trace()
            self.assertEqual(res.status_code, 200)
            self.assertIn('$ 100 United States dollar European Euro € 108.92', html)

# TESTING check_valid_input function

    def test_check_correct_inputs(self):
        self.assertTrue(currency_rate.check_valid_input('USD', 'EUR', '100'))
        self.assertTrue(currency_rate.check_valid_input('USD', 'jpy', '200'))
        self.assertTrue(currency_rate.check_valid_input('eur', 'usd', '50'))

    def test_check_incorrect_convert_to_one(self):
        convert_to, convert_from, amount = currency_rate.check_valid_input('USDer', 'EUR', '100')
        self.assertFalse(convert_to)
        self.assertTrue(convert_from)
        self.assertTrue(amount)

    def test_check_incorrect_convert_to_two(self):
        convert_to, convert_from, amount = currency_rate.check_valid_input('1234', 'EUR', '100')
        self.assertFalse(convert_to)
        self.assertTrue(convert_from)
        self.assertTrue(amount)
        
    def test_check_incorrect_convert_from_one(self):
        convert_to, convert_from, amount = currency_rate.check_valid_input('USD', 'sdewr', '100')
        self.assertTrue(convert_to)
        self.assertFalse(convert_from)
        self.assertTrue(amount)

    def test_check_incorrect_convert_from_two(self):
        convert_to, convert_from, amount = currency_rate.check_valid_input('USD', '2344', '100')
        self.assertTrue(convert_to)
        self.assertFalse(convert_from)
        self.assertTrue(amount)

    def test_check_incorrect_amount_one(self):
        convert_to, convert_from, amount = currency_rate.check_valid_input('USD', 'EUR', 'werd')
        self.assertTrue(convert_to)
        self.assertTrue(convert_from)
        self.assertFalse(amount)

    def test_check_incorrect_amount_one(self):
        convert_to, convert_from, amount = currency_rate.check_valid_input('USD', 'EUR', '-100')
        self.assertTrue(convert_to)
        self.assertTrue(convert_from)
        self.assertFalse(amount)

    def test_check_incorrect_convert_to(self):
        convert_to, convert_from, amount = currency_rate.check_valid_input('USDer', 'EUR', '100')
        self.assertFalse(convert_to)
        self.assertTrue(convert_from)
        self.assertTrue(amount)


