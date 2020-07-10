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
                    self.send_message(120751938, 'pong')
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


bot = Bot('1233613509:AAGYxH3vYQ7WYFz1NlzVFX3DI9GFCwVk0fs')
bot.start()