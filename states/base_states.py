from telebot.handler_backends import State, StatesGroup


class Level(StatesGroup):
    read = State()

    listen_city = State()
    listen_country = State()
