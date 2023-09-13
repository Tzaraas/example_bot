from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
from typing import Union

from states.base_states import Level
from utils import out_kb


def kb_1(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton("Нет ключа", callback_data="l2_k1_b1")
    button_2 = InlineKeyboardButton("Мало переменных", callback_data="l2_k1_b2")
    button_3 = InlineKeyboardButton("Настройка вывода", callback_data="l2_k1_b3")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="l2_back_l1_k1")
    keyboard.add(button_1, button_2, button_0, button_3)

    text = "Замечания о работе c restcountries.com:"
    out_kb.fork(enter, keyboard, text, Level.lv_2)


def kb_2(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton("Разные запросы", callback_data="l2_k2_b1")
    button_2 = InlineKeyboardButton("Адаптация данных", callback_data="l2_k2_b2")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="l2_back_l1_k2")
    keyboard.add(button_1, button_2, button_0)

    text = "Замечания о работе c openweathermap.org:"
    out_kb.fork(enter, keyboard, text, Level.lv_2)


def kb_3(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton("Создание позиции (sudo)", callback_data="l2_k3_b1")
    button_2 = InlineKeyboardButton("Удаление позиции (sudo)", callback_data="l2_k3_b2")
    button_3 = InlineKeyboardButton("Cписок товаров", callback_data="l2_k3_b3")
    button_4 = InlineKeyboardButton("Выбрать товар", callback_data="l2_k3_b4")
    button_5 = InlineKeyboardButton("Создать заказ", callback_data="l2_k3_b5")
    button_6 = InlineKeyboardButton("Проверить корзину", callback_data="l2_k3_b6")
    button_7 = InlineKeyboardButton("Добавить в заказ", callback_data="l2_k3_b7")
    button_8 = InlineKeyboardButton("Удалить из заказа", callback_data="l2_k3_b8")
    button_9 = InlineKeyboardButton("Оформить заказ", callback_data="l2_k3_b9")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="l2_back_l1_k3")
    keyboard.add(button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_0, button_9)

    text = "Основной порядок действий:\n  1) Создать товар.\n  2) Выгрузить список.\n  3) Выбрать товары.\n  4) Добавить в корзину.\n  5) Оформить заказ.\n\n"\
           'п.1 можно пропустить, если использовать категорию "ноутбуки". Загрузил туда пару моделей.'
    out_kb.fork(enter, keyboard, text, Level.lv_2)


def kb_4(enter: Union[Message, CallbackQuery]):
    keyboard = InlineKeyboardMarkup(row_width=2)
    button_1 = InlineKeyboardButton("Несколько типов запросов", callback_data="l2_k4_b1")
    button_2 = InlineKeyboardButton("Описание кода на сайте", callback_data="l2_k4_b2")
    button_3 = InlineKeyboardButton("GetOrder", callback_data="l2_k4_b3")
    button_4 = InlineKeyboardButton("Хранение результатов", callback_data="l2_k4_b4")
    button_0 = InlineKeyboardButton("<< Вернуться назад", callback_data="l2_back_l1_k3")
    keyboard.add(button_1, button_2, button_3, button_4, button_0)

    text = "Замечания о работе c web магазином:"
    out_kb.fork(enter, keyboard, text, Level.lv_2)
