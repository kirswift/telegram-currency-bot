import requests

class Converter:
    def __init__(self):
        self._url = 'https://api.exchangeratesapi.io/latest'
        self._codes = ['RUB', 'USD', 'EUR']

    def get_exchange_rate(self, base, currency):
        params = {'base': base, 'symbols': currency}
        return requests.get(self._url, params).json()['rates'][currency]