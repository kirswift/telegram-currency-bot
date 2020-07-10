import requests

class Bot:
    def __init__(self, token):
        self._url = f'https://api.telegram.org/bot{token}/'

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        requests.post(self._url + 'sendMessage', params)


bot = Bot('1233613509:AAGYxH3vYQ7WYFz1NlzVFX3DI9GFCwVk0fs')
bot.send_message(120751938, 'test')