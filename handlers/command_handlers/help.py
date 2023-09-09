from telebot.types import Message

from loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = '''Кнопки управления внизу. Если их там нет, нажми значок [Х] справа от поля ввода.\nА если скучно, отправь боту любое слово (или не слово).'''
    bot.reply_to(message, text)
