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
        self.code_list = self.currency.get_rates('USD').keys()

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

    def check_valid_input(self, convert_to, convert_from, money_amount):
        """
        Returns True if input is valid. 
        """
        convert_to_check = f"Not a valid code: {convert_to}. Please type in proper exchange symbol for 'converting to'"
        convert_from_check = f"Not a valid code: {convert_from}. Please type in proper exchange symbol for 'converting from'"
        money_amount_check = f"Not a valid amount: {money_amount}. Please type in a proper amount"

        # self.currency.get_rates().keys()
        if len(convert_to) == 3:
            convert_to_check = True

        if len(convert_from) == 3:
            convert_from_check = True
            
        if int(money_amount) > 0:
            money_amount_check =  True


        return convert_to_check, convert_from_check, money_amount_check

    def calculate(self, convert_to, convert_from, money_amount):
        '''
        calculating exchange rate after it passes edge cases for inputs.
        '''
        
        # try: 
        #     Decimal(money_amount)

        # except:
        #     print('stopped an error!!')
        convert_to = convert_to.upper()
        convert_from = convert_from.upper()
        # money_amount = Decimal(money_amount)
        # convert requires amount parameter is of type Decimal.
        conversion = self.currency.convert(convert_to, convert_from,Decimal(money_amount))
        convert_to_symbol = self.codes.get_symbol(convert_to)
        convert_from_symbol = self.codes.get_symbol(convert_from)
        convert_to_name = self.codes.get_currency_name(convert_to)
        convert_from_name = self.codes.get_currency_name(convert_from)
        converted_amount = f'{convert_to_symbol} {round(conversion, 2)}'

        return convert_to_name, convert_from_name, converted_amount, convert_from_symbol
