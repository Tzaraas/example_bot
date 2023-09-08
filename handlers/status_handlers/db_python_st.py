from telebot.types import Message, CallbackQuery

from states.my_states import Status
from database.db_conf import DB_Coll, DB_Method
from keyboards.inline import db_python
from loader import bot


@bot.callback_query_handler(func=lambda call: True, state=Status.db_python)
def db_python_call(call: CallbackQuery):
    match call.data:
        case "prompt":
            bot.edit_message_text("Выбери интересующую тему:", call.from_user.id, call.message.id, reply_markup=db_python.menu_prompt())
        case "coll":
            bot.edit_message_text("Выбери интересующую коллекцию:", call.from_user.id, call.message.id, reply_markup=db_python.menu_coll())  # TODO DB_Coll, DB_Method
        case "collections_types":
            bot.send_photo(call.from_user.id, open(r'database\picture\collections_types.jpg', 'rb'))
        case "int":
            bot.send_message(call.from_user.id, "Сперва надо заполнить базу данных.")
        case "str":
            bot.send_message(call.from_user.id, "Сперва надо заполнить базу данных.")
        case "list":
            bot.send_message(call.from_user.id, "Сперва надо заполнить базу данных.")
        case "dict":
            bot.send_message(call.from_user.id, "Сперва надо заполнить базу данных.")
        case "back":
            bot.edit_message_text("Выберите интересующий раздел:", call.from_user.id, call.message.id, reply_markup=db_python.menu_button())


@bot.message_handler(state=Status.db_python)
def db_python_text(message: Message):
    bot.set_state(message.from_user.id, Status.main)
    bot.reply_to(message, "К чему бы это? Вернусь ка лучше в главное меню. Теперь жги)")