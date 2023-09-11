from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from typing import Union

from states.base_states import Level
from utils import out_kb


def kb_2(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=3)
    button_1 = InlineKeyboardButton("Нет ключа", callback_data="b1")
    button_2 = InlineKeyboardButton("Мало переменных", callback_data="b2")
    button_3 = InlineKeyboardButton("Настройка вывода", callback_data="b3")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="back_1")
    keyboard.add(button_1, button_2, button_3, button_0)

    text = "Замечания о работе c restcountries.com:"
    out_kb.fork(enter, keyboard, text, Level.lv_2)


def kb_5(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton("Разные запросы", callback_data="b4")
    button_2 = InlineKeyboardButton("Адаптация данных", callback_data="b5")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="back_2")
    keyboard.add(button_1, button_2, button_0)

    text = "Замечания о работе c openweathermap.org:"
    out_kb.fork(enter, keyboard, text, Level.lv_2)


def kb_8(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton("Множество типов запросов", callback_data="b6")
    button_2 = InlineKeyboardButton("Хранение результатов", callback_data="b7")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="back_2")
    keyboard.add(button_1, button_2, button_0)

    text = "Замечания о работе c openweathermap.org:"
    out_kb.fork(enter, keyboard, text, Level.lv_2)