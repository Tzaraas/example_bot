from telebot.types import KeyboardButton, ReplyKeyboardMarkup


def menu_button() -> ReplyKeyboardMarkup:
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
        button_1 = KeyboardButton("Поднять себе настроение")
        button_2 = KeyboardButton("Заняться делом")
        keyboard.add(button_1, button_2)
        return keyboard