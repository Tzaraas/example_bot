from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = '''тут что-то будет'''  # TODO придумать описание
    bot.reply_to(message, text)
