from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = '''Это тестовое сообщение помошника.'''
    bot.reply_to(message, text)
