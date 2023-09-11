from telebot.types import Message

from states.base_states import Level
from loader import bot


@bot.message_handler()
def reply(message: Message):
    bot.send_message(message.chat.id, "Пожалуйста, начинайте работу с команды /start")


@bot.message_handler(content_types=['voice', 'photo', 'document', 'audio', 'sticker', 'video'])
def reply(message: Message):
    bot.send_message(message.chat.id, "Пожалуйста, введите текст.")
