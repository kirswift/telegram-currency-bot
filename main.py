from telegram import Bot

bot = Bot('1233613509:AAGYxH3vYQ7WYFz1NlzVFX3DI9GFCwVk0fs')

def help_handler(chat_id, args):
    bot.send_message(chat_id, '*Вы ввели команду /help*')

bot.add_command('/help', help_handler)

bot.start()