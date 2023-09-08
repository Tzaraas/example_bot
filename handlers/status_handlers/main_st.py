from telebot.types import Message

from states.my_states import Status
from keyboards.inline import db_python
from loader import bot


@bot.message_handler(state=Status.main, content_types=['text'])
def main_text(message: Message):
    match message.text:
        case "База данных Python":
            bot.set_state(message.from_user.id, Status.db_python)
            bot.send_message(message.chat.id, "Выберите интересующий раздел:", reply_markup=db_python.menu_button())

        case "База данных SQL":
            bot.send_message(message.chat.id, "Раздел находится в разработке")  # TODO

        case _:
            bot.reply_to(message, "Это что-то на китайском? Держи гифку!")  # TODO подключить АПИ с выводом картинок с поиском по введенному слову


@bot.message_handler(state=Status.main, content_types=['voice', 'photo', 'document', 'audio', 'sticker', 'video'])
def main_spam(message: Message):
    bot.reply_to(message, "Однажды я смогу тебе ответить, но не сегодня.\nДавай текстом? А лучше кнопками, они там, внизу.")
