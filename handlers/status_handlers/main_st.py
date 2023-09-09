from telebot.types import Message

from states.my_states import Status
from keyboards.inline import db_python
from database.models import Words
from utils import gif_api
from loader import bot


@bot.message_handler(state=Status.main, content_types=['text'])
def main_text(message: Message):
    match message.text:
        case "База данных Python":
            bot.set_state(message.from_user.id, Status.db_python)
            bot.send_message(message.chat.id, "Выберите интересующий раздел:", reply_markup=db_python.menu_button())

        case "База данных SQL":
            bot.send_message(message.chat.id, "Раздел находится в разработке")  # TODO как только, так сразу.

        case _:
            send_gif(message)


@bot.message_handler(state=Status.main, content_types=['voice', 'photo', 'document', 'audio', 'sticker', 'video'])
def main_spam(message: Message):
    bot.reply_to(message, "Однажды я смогу тебе ответить, но не сегодня.\nДавай текстом? А лучше кнопками, они там, внизу.")


def send_gif(message: Message):
    if Words.get_or_none(Words.word_name == message.text):
        word = Words.get(Words.word_name == message.text)
        word.word_count += 1
        word.save()
    else:
        Words.create(
            word_name=message.text,
            word_count = 0
        )
        word = Words.get(Words.word_name == message.text)

    gif = gif_api.api_request('search', message.text, word.word_count)
    if isinstance(gif, str):
        bot.reply_to(message, "Хочешь развлечься? Держи гифку в тему!")
        bot.send_animation(message.from_user.id, gif)
    else:
        gif = gif_api.api_request('random', '', '')
        if isinstance(gif, str):
            bot.reply_to(message, "Это что-то на китайском? Держи случайную гифку!")
            bot.send_animation(message.from_user.id, gif)
        else:
            bot.send_message(message.chat.id, "https://www.youtube.com/watch?v=dQw4w9WgXcQ&t=1s")
    bot.send_message(message.chat.id, "Еще посмеемся или нажмешь кнопку внизу?")

