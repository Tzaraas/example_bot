from telebot.types import Message, CallbackQuery

from states.my_states import Status
from keyboards.inline import db_python
from database.models import DB_Coll, DB_Method
from loader import bot


@bot.callback_query_handler(func=lambda call: True, state=Status.db_python)
def db_python_call(call: CallbackQuery):
    match call.data:
        case "prompt":
            bot.edit_message_text("Выбери интересующую тему:", call.from_user.id, call.message.id, reply_markup=db_python.menu_prompt())
        case "coll":
            bot.edit_message_text("Выбери интересующую коллекцию:", call.from_user.id, call.message.id, reply_markup=db_python.menu_coll())
        case "collections_types":
            bot.send_photo(call.from_user.id, open(r'utils\picture\collections_types.jpg', 'rb'))
        case "str" | "list" | "dict":
            get_query(call)
        case "back":
            bot.edit_message_text("Выберите интересующий раздел:", call.from_user.id, call.message.id, reply_markup=db_python.menu_button())


def get_query(call: CallbackQuery):
    bot.send_message(call.from_user.id, "Введите ключевое слово или оставьте поле пустым и нажмите Enter:")
    with bot.retrieve_data(call.from_user.id) as memory:
        memory['collection'] = call.data
    bot.set_state(call.from_user.id, Status.listen)


@bot.message_handler(state=Status.listen)
def listen_query(message: Message):
    with bot.retrieve_data(message.from_user.id) as memory:
        bot.register_next_step_handler(message, get_data(message, memory['collection'], message.text))
        match memory['collection']:
            case "str":
                bot.send_message(message.from_user.id, "https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html")
            case "list":
                bot.send_message(message.from_user.id, "https://pythonworld.ru/tipy-dannyx-v-python/spiski-list-funkcii-i-metody-spiskov.html")
            case "dict":
                bot.send_message(message.from_user.id, "https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html")
    bot.set_state(message.from_user.id, Status.db_python)
    bot.send_message(message.from_user.id, "Выберите интересующий раздел:", reply_markup=db_python.menu_button())


def get_data(message: Message, collection: str, query: str):
    for method in DB_Method.select(DB_Method.met_name, DB_Method.met_desc).join(DB_Coll).where(DB_Coll.coll_name == collection):
        if query in method.met_desc.lower():
            bot.send_message(message.from_user.id, method, parse_mode="html")


@bot.message_handler(state=Status.db_python)
def db_python_text(message: Message):
    bot.set_state(message.from_user.id, Status.main)
    bot.reply_to(message, "Прости, я прослушал. Повтори, пожалуйста.")
