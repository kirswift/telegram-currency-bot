import requests

class Converter:
    def __init__(self):
        self._url = 'https://api.exchangeratesapi.io/latest'
        self._codes = ['RUB', 'USD', 'EUR', 'CAD', 'HKD', 'ISK',
        'DKK', 'HUF', 'CZK', 'AUD', 'SEK', 'IDR', 'JPY', 'NOK', 'GBP']

    def get_exchange_rate(self, base, currency):
        if base.upper() not in self._codes or currency.upper() not in self._codes:
            raise ValueError('Неподдерживаемый код валюты')

        params = {'base': base.upper(), 'symbols': currency.upper()}
        return requests.get(self._url, params).json()['rates'][currency.upper()]

    def convert(self, amount, convert_from, convert_to):
        try:
            rate = self.get_exchange_rate(convert_from, convert_to)
        except ValueError:
            raise
        return amount * rate

    def get_allowed_codes(self):
        return self._codes