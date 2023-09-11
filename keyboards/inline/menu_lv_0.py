from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from typing import Union

from states.base_states import Level
from utils import out_kb


def kb_base(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Простой пример - информация о выбранной стране", callback_data="b1")
    button_2 = InlineKeyboardButton("Стандартный уровень - запрос текущей погоды", callback_data="b2")
    button_3 = InlineKeyboardButton("Полноценный API - web магазин", callback_data="b3")
    button_0 = InlineKeyboardButton("Завершить работу", callback_data="exit")
    keyboard.add(button_1, button_2, button_3, button_0)

    text = "Взаимодействовать с API силами TelegramBotAPI очень легко.\nРассмотроим несколько примеров:"
    out_kb.fork(enter, keyboard, text, Level.lv_0)
