import requests
import time

class Bot:
    def __init__(self, token):
        self._url = f'https://api.telegram.org/bot{token}/'

    def start(self):
        offset = 0
        while True:
            updates = self.get_updates(offset)
            if len(updates) > 0:
                for update in updates:
                    self.send_message(self.get_chat_id(update), 'pong')
                offset = self.get_last_update_id(updates) + 1
            time.sleep(1)

    def get_updates(self, offset):
        params = {'timeout': 60, 'offset': offset}
        return requests.get(self._url + 'getUpdates', params).json()['result']

    def get_last_update_id(self, updates):
        return updates[len(updates) - 1]['update_id']

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        requests.post(self._url + 'sendMessage', params)

    def get_chat_id(self, update):
        return update['message']['chat']['id']