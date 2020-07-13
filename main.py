from telegram import Bot
from converter import Converter
import textwrap
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

converter = Converter()
bot = Bot(config['telegram']['token'])

def help_handler(chat_id, args):
    bot.send_message(chat_id, textwrap.dedent(f'''  
    */rate [код]* - получить текущий курс валюты по отношению к рублю
    */convert [сумма] [код #1] [код #2]* - конвертировать валюту #1 в валюту #2\n
    Доступные коды валют: *{', '.join(converter.get_allowed_codes())}*
    '''))

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

def rate_handler(chat_id, args):
    try:
        if len(args) < 1:
            bot.send_message(chat_id, 'Неверное количество аргументов')
            return
        base = args[0]
        rate = converter.get_exchange_rate(base, 'RUB')
        bot.send_message(chat_id, f'Курс {base.upper()}: *{rate}*')
    except ValueError as err:
        bot.send_message(chat_id, f'Ошибка: *{err}*')

bot.add_command('/rate', rate_handler)

bot.start()