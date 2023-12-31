from telebot.types import Message

from database.models import Words
from states.base_states import Level
from utils.api import gif_api
from utils.loader import bot


@bot.message_handler(content_types=['text'], state=Level.read)
def send_gif(message: Message):
    ''' Отвечает за отлов ненужного текста на всех уровнях '''

    if Words.get_or_none(Words.word_name == message.text, Words.word_user_id == message.from_user.id):
        word = Words.update(word_count = Words.word_count + 1).where(Words.word_name == message.text, Words.word_user_id == message.from_user.id)
        word.execute()
    else:
        Words.create(word_user_id=message.from_user.id,
                     word_name=message.text,
                     word_count = 0)
        
    word = Words.get(Words.word_name == message.text, Words.word_user_id == message.from_user.id)
    gif = gif_api.gif_api_request('search', message.text, word.word_count)

    if isinstance(gif, str):
        bot.send_animation(message.from_user.id, gif)
    else:
        bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=1s")

    bot.reply_to(message, "Пожалуйста, используйте кнопки.")


@bot.message_handler(content_types=['voice', 'photo', 'document', 'audio', 'sticker', 'video'])
def reply(message: Message):
    ''' Отлавливает самые популярные форматы, кроме текста. '''
    bot.send_message(message.chat.id, "Пожалуйста, введите текст.")


@bot.message_handler()
def reply(message: Message):
    ''' В случае перезапуска бота напоминает о необходимости нажать старт '''
    bot.send_message(message.chat.id, "Пожалуйста, начинайте работу с команды /start")
