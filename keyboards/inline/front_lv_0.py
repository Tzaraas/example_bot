from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from typing import Union

from utils import out_kb


def kb_base(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button_1 = InlineKeyboardButton("Простой пример - информация о выбранной стране", callback_data="l0_kb_b1")
    button_2 = InlineKeyboardButton("Стандартный уровень - запрос текущей погоды", callback_data="l0_kb_b2")
    button_3 = InlineKeyboardButton("Полноценный API - web магазин", callback_data="l0_kb_b3")
    keyboard.add(button_1, button_2, button_3)

    text = "Взаимодействовать с API силами TelegramBotAPI очень легко.\nРассмотроим несколько примеров:"
    out_kb.fork(enter, keyboard, text)
