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

    # def check_input(self, convert_to, convert_from):
    #     '''
    #     Edge case check for convert_to input
    #     '''
    #     if len(convert_to) == 3:
    #         convert_to = True
    #     else: 
    #         convert_to = f"Not a valid code: {convert_to}. Please type in proper exchange symbol for 'converting to'"

    #     if len(convert_from) == 3:
    #         convert_from = True
    #     else: 
    #         convert_from = f"Not a valid code: {convert_from}. Please type in proper exchange symbol for 'converting from'"

    #     return convert_to, convert_from

    # def check_valid_amount(self, money_amount):
    #     '''
    #     Edge case check for money_amount input
    #     '''
    #     check_alpha = money_amount.isalpha()
    #     if check_alpha:
    #         money_amount = True
    #     if int(money_amount) > 0:
    #         money_amount =  True
    #     else:
    #         money_amount =  f"Not a valid amount: {money_amount}. Please type in a proper amount"
        
    #     return money_amount


    """
    Had to use try and catch to avoid "Internal Server Error"
    """
    def check_valid_input(self, convert_to, convert_from, money_amount):
        """
        Returns True if input is valid. 
        """
        # Turning dictionary of codes to list so that I can append 'USD'
        codes_list = list(self.codes_list)
        codes_list.append('USD')
        
        convert_to_check = f"Not a valid code: {convert_to}. Please type in proper exchange symbol for 'converting to'"
        convert_from_check = f"Not a valid code: {convert_from}. Please type in proper exchange symbol for 'converting from'"
        money_amount_check = True
        # money_amount_check = f"Not a valid amount: {money_amount}. Please type in a proper amount"

        # Calling self.currency.get_rates('USD') in two functions does not work.
        # code_list = self.currency.get_rates('USD').keys()

        if convert_to in codes_list:
            convert_to_check = True

        if convert_from in codes_list:
            convert_from_check = True
            
        # if int(money_amount) > 0:
        #     money_amount_check =  True


        return convert_to_check, convert_from_check, money_amount_check

    def calculate(self, convert_to, convert_from, money_amount):
        '''
        calculating exchange rate after it passes edge cases for inputs.
        '''
        
        # codes_list = self.currency.get_rates('USD')
        codes_list = list(self.codes_list)
        codes_list.append('USD')

        convert_to = convert_to.upper()
        convert_from = convert_from.upper()
        # money_amount = Decimal(money_amount)
        # convert requires amount parameter is of type Decimal.
        conversion = self.currency.convert(convert_to, convert_from, Decimal(money_amount))
        convert_to_symbol = self.codes.get_symbol(convert_to)
        convert_from_symbol = self.codes.get_symbol(convert_from)
        convert_to_name = self.codes.get_currency_name(convert_to)
        convert_from_name = self.codes.get_currency_name(convert_from)
        converted_amount = f'{convert_to_symbol} {round(conversion, 2)}'

        return convert_to_name, convert_from_name, converted_amount, convert_from_symbol, codes_list
