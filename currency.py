from http.client import INTERNAL_SERVER_ERROR
from forex_python.converter import CurrencyRates, CurrencyCodes
from decimal import *

class CurrencyCalculator():
    '''
    This class calculates the currency rate.
    '''
    def __init__(self):
        '''
        Uses forex-python to get currency rates, symbols, and codes
        '''
        self.currency = CurrencyRates()
        self.codes = CurrencyCodes()
        # this will get all the currency codes that you can exchange to with USD.
        self.codes_list = self.currency.get_rates('USD').keys()

    def check_valid_input(self, convert_to, convert_from, money_amount):
        """
        Returns True if input is valid. 
        """
        # Turning dictionary of codes to list so that I can append 'USD'
        codes_list = list(self.codes_list)
        codes_list.append('USD')
        # money_amount = int(money_amount)
        convert_to_check = f"Not a valid code: {convert_to}. Please type in proper exchange symbol for 'converting to'"
        convert_from_check = f"Not a valid code: {convert_from}. Please type in proper exchange symbol for 'converting from'"
        # money_amount_check = True
        money_amount_check = f"Not a valid amount: {money_amount}. Please type in a proper amount"

        # QUESTION:
        # Calling self.currency.get_rates('USD') in two functions does not work.
        # code_list = self.currency.get_rates('USD').keys()

        if convert_to.upper() in codes_list:
            convert_to_check = True

        if convert_from.upper() in codes_list:
            convert_from_check = True

        if not money_amount.isalpha():
            if (int(money_amount) > 0):
                money_amount_check =  True

        return convert_to_check, convert_from_check, money_amount_check, codes_list

    def calculate(self, convert_to, convert_from, money_amount):
        '''
        calculating exchange rate after it passes edge cases for inputs.
        '''

        convert_to = convert_to.upper()
        convert_from = convert_from.upper()
        # convert requires amount parameter is of type Decimal.
        conversion = self.currency.convert(convert_to, convert_from, Decimal(money_amount))
        convert_to_symbol = self.codes.get_symbol(convert_to)
        convert_from_symbol = self.codes.get_symbol(convert_from)
        convert_to_name = self.codes.get_currency_name(convert_to)
        convert_from_name = self.codes.get_currency_name(convert_from)
        converted_amount = f'{convert_to_symbol} {round(conversion, 2)}'

        return convert_to_name, convert_from_name, converted_amount, convert_from_symbol
