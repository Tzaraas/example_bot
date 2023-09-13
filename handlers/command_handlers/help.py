from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = '''Бот показывает несколько примеров работы с API на практике. Для управления используйте интерактивные кнопки.'''
    bot.reply_to(message, text)
