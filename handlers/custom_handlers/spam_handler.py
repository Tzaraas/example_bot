from telebot.types import Message

from states.base_states import Level
from utils.loader import bot


@bot.message_handler()
def reply(message: Message):
    ''' В случае перезапуска бота напоминает о необходимости нажать старт '''
    bot.send_message(message.chat.id, "Пожалуйста, начинайте работу с команды /start")


@bot.message_handler(content_types=['voice', 'photo', 'document', 'audio', 'sticker', 'video'])
def reply(message: Message):
    ''' Отлавливает самые популярные форматы, кроме текста. '''
    bot.send_message(message.chat.id, "Пожалуйста, введите текст.")
