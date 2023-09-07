from telebot.handler_backends import State, StatesGroup


class Status(StatesGroup):
    main = State()
