from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot.types import CallbackQuery

from loader import bot


def menu_button() -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup()
        button_1 = InlineKeyboardButton("Выбрать коллекцию", callback_data="coll")
        button_2 = InlineKeyboardButton("Подсказки", callback_data="prompt")
        keyboard.add(button_1, button_2)
        return keyboard


def menu_prompt() -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(row_width=1)
        button_1 = InlineKeyboardButton("Типы коллекций", callback_data="collections_types")
        button_0 = InlineKeyboardButton("Назад", callback_data="back")
        keyboard.add(button_1, button_0)
        return keyboard


def menu_coll() -> InlineKeyboardMarkup:
        keyboard = InlineKeyboardMarkup(row_width=1)
        button_1 = InlineKeyboardButton("Цифры", callback_data="int")
        button_2 = InlineKeyboardButton("Строки", callback_data="str")
        button_3 = InlineKeyboardButton("Списки", callback_data="list")
        button_4 = InlineKeyboardButton("Словари", callback_data="dict")
        button_0 = InlineKeyboardButton("Назад", callback_data="back")
        keyboard.add(button_1, button_2, button_3, button_4, button_0)
        return keyboard