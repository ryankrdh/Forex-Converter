from forex_python.converter import CurrencyRates, CurrencyCodes

class CurrencyCalculator():
    '''
    This class calculates the currency rate.
    '''
    def __init__(self):
        '''
        Uses forex-python to get currency rates, codes, and symbols.
        '''
        self.c = CurrencyRates()
        self.c = CurrencyCodes()