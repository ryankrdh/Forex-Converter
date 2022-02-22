from forex_python.converter import CurrencyRates, CurrencyCodes

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

    def check_convert_to(self, convert_to):
        '''
        Edge case check for convert_to input
        '''
        if len(convert_to) == 3:
            return True
        else: 
            return False
    
    def check_convert_from(self, convert_from):
        '''
        Edge case check for convert_from input
        '''
        if len(convert_from) == 3:
            return True
        else:
            return False

    def check_valid_amount(self, money_amount):
        '''
        Edge case check for money_amount input
        '''
        if (type(money_amount) == int) and money_amount > 0:
            return True
        else:
            return False

    def calculate(self, convert_to, convert_from, money_amount):
        '''
        calculating exchange rate after it passes edge cases for inputs.
        '''
        
        convert_to = convert_to.upper()
        convert_from = convert_from.upper()

        conversion = self.currency.convert(convert_to, convert_from, money_amount)
        symbol = self.codes.get_symbol(convert_to)
        convert_to_name = self.codes.get_currency_name(convert_to)
        convert_from_name = self.codes.get_currency_name(convert_from)
        converted_amount = f'{symbol}{conversion}'

        return convert_to_name, convert_from_name, converted_amount

        