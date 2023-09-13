from telebot.handler_backends import State, StatesGroup


class Level(StatesGroup):
    lv_0 = State()
    lv_1 = State()
    lv_2 = State()

    listen = State()
