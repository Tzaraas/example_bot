from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from typing import Union

from states.base_states import Level
from utils import out_kb


def kb_1(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Пример работы API", callback_data="b1")
    button_2 = InlineKeyboardButton("Замечания о работе c API", callback_data="b2")
    button_3 = InlineKeyboardButton("Статистика использования API", callback_data="b3")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="back")
    keyboard.add(button_1, button_2, button_3, button_0)

    text = "Базовая информация о стране.\nИспользуем сервис restcountries.com"
    out_kb.fork(enter, keyboard, text, Level.lv_1)


def kb_2(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Пример работы API", callback_data="b4")
    button_2 = InlineKeyboardButton("Замечания о работе c API", callback_data="b5")
    button_3 = InlineKeyboardButton("Статистика использования API", callback_data="b6")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="back")
    keyboard.add(button_1, button_2, button_3, button_0)

    text = "Погода за окном.\nИспользуем сервис openweathermap.org"
    out_kb.fork(enter, keyboard, text, Level.lv_1)


def kb_3(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Пример работы API", callback_data="b7")
    button_2 = InlineKeyboardButton("Замечания о работе c API", callback_data="b8")
    button_3 = InlineKeyboardButton("Статистика использования API", callback_data="b9")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="back")
    keyboard.add(button_1, button_2, button_3, button_0)
    
    text = "Полноценный web магазин.\nИспользуется https://rapidapi.com/iddogino1/api/my-store2"
    out_kb.fork(enter, keyboard, text, Level.lv_1)
