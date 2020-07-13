from telegram import Bot
from converter import Converter

converter = Converter()
bot = Bot('1233613509:AAGYxH3vYQ7WYFz1NlzVFX3DI9GFCwVk0fs')

def help_handler(chat_id, args):
    bot.send_message(chat_id, '*Вы ввели команду /help*')

bot.add_command('/help', help_handler)

def convert_handler(chat_id, args):
    if len(args) < 3:
        bot.send_message(chat_id, 'Неверное количество аргументов')
        return
    try:
        amount = float(args[0])
        convert_from = args[1]
        convert_to = args[2]
        result = converter.convert(amount, convert_from, convert_to)
        bot.send_message(chat_id, f'*{amount}* {convert_from.upper()} = *{result}* {convert_to.upper()}')
    except ValueError as err:
        bot.send_message(chat_id, f'Ошибка: *{err}*')

bot.add_command('/convert', convert_handler)

bot.start()