from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = '''Это тестовое сообщение помощника.'''  # TODO придумать корректное описание работы бота
    bot.reply_to(message, text)
