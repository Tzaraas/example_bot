from telebot.handler_backends import State, StatesGroup


class Status(StatesGroup):
    main = State()
    db_python = State()
    db_sql = State()
    listen = State()
