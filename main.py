from telegram import Bot
from converter import Converter

converter = Converter()
bot = Bot('1233613509:AAGYxH3vYQ7WYFz1NlzVFX3DI9GFCwVk0fs')

def help_handler(chat_id, args):
    bot.send_message(chat_id, '*Вы ввели команду /help*')

bot.add_command('/help', help_handler)

print(converter.get_exchange_rate('EUR', 'RUB'))

print(converter.convert(10, 'EUR', 'RUB'))

# bot.start()