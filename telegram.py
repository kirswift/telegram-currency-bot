import requests
import time

class Bot:
    def __init__(self, token):
        self._url = f'https://api.telegram.org/bot{token}/'
        self._commands = {}

    def start(self):
        offset = 0
        while True:
            updates = self.get_updates(offset)
            if len(updates) > 0:
                for update in updates:
                    if self.is_command(update): 
                        self.handle_command(self.get_chat_id(update), update['message']['text'])
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

    def is_command(self, update):
        if 'entities' not in update['message']: return False
        return update['message']['entities'][0]['type'] == 'bot_command'

    def add_command(self, name, handler):
        self._commands[name] = handler

    def handle_command(self, chat_id, text):
        args = text.split(' ')
        name = args.pop(0)
        if name in self._commands:
            self._commands[name](chat_id, args)
            self.send_message(chat_id, f'handle {name}')
        else:
            self.send_message(chat_id, 'no such command')