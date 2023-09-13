from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from typing import Union

from states.base_states import Level
from utils import out_kb


def kb_1(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Запустить API", callback_data="l1_k1_b1")
    button_2 = InlineKeyboardButton("Замечания о работе c API", callback_data="l1_k1_b2")
    button_3 = InlineKeyboardButton("DataBase: Часто запрашиваемые страны", callback_data="l1_k1_b3")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="l1_back_main")
    keyboard.add(button_1, button_2, button_3, button_0)

    text = "Базовая информация о стране.\nИспользуем сервис https://api.openweathermap.org/"
    out_kb.fork(enter, keyboard, text, Level.lv_1)


def kb_2(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Запустить API", callback_data="l1_k2_b1")
    button_2 = InlineKeyboardButton("Замечания о работе c API", callback_data="l1_k2_b2")
    button_3 = InlineKeyboardButton("DataBase: Часто запрашиваемые города", callback_data="l1_k2_b3")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="l1_back_main")
    keyboard.add(button_1, button_2, button_3, button_0)

    text = "Погода за окном.\nИспользуем сервис https://restcountries.com/"
    out_kb.fork(enter, keyboard, text, Level.lv_1)


def kb_3(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Запустить API", callback_data="l1_k3_b1")
    button_2 = InlineKeyboardButton("Замечания о работе c API", callback_data="l1_k3_b2")
    button_3 = InlineKeyboardButton("DataBase: последние 5 заказов", callback_data="l1_k3_b3")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="l1_back_main")
    keyboard.add(button_1, button_2, button_3, button_0)
    
    text = "Полноценный web магазин.\nИспользуется https://rapidapi.com/iddogino1/api/my-store2"
    out_kb.fork(enter, keyboard, text, Level.lv_1)
