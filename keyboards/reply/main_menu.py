from telebot.types import ReplyKeyboardMarkup, KeyboardButton


def menu_button() -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
        button_1 = KeyboardButton("База данных Python")
        button_2 = KeyboardButton("База данных SQL")
        keyboard.add(button_1, button_2)
        return keyboard