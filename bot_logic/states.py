from telebot.handler_backends import State, StatesGroup


class States(StatesGroup):
    main = State()

    new_task_title = State()
    new_task_due_date = State()
    tasks_make_done = State()

