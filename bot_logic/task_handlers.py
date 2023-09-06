from datetime import datetime, date
from typing import List

from database.db_conf import User, Task
from .states import States
from config_data.config import DATE_FORMAT


def initialization_task_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data in ["newtask", "tasks", "today"])
    def callback_tasks(call):
        match call.data:
            case "newtask":
                handle_new_task(call)
            case "tasks":
                handle_tasks(call)
            case "today":
                handle_today(call)


    def handle_new_task(call):
        user_id = call.from_user.id

        bot.send_message(user_id, "Введите название задачи")
        bot.set_state(call.from_user.id, States.new_task_title)
        with bot.retrieve_data(call.from_user.id) as data:
            data["new_task"] = {"user_id": user_id}


    def handle_tasks(call):
        user_id = call.from_user.id
        user = User.get_or_none(User.user_id == user_id)

        tasks: List[Task] = user.tasks.order_by(-Task.due_date, -Task.task_id).limit(10)

        result = []
        result.extend(map(str, reversed(tasks)))

        if not result:
            bot.send_message(call.from_user.id, "У вас ещё нет задач")
            return

        result.append("\nВведите номер задачи, чтобы изменить её статус.")
        bot.send_message(call.from_user.id, "\n".join(result))
        bot.set_state(call.from_user.id, States.tasks_make_done)


    def handle_today(call):
        user_id = call.from_user.id
        user = User.get_or_none(User.user_id == user_id)

        tasks: List[Task] = user.tasks.where(Task.due_date == date.today())

        result = []
        result.extend(map(str, tasks))

        if not result:
            bot.send_message(call.from_user.id, "У вас еще нет задач")
            return

        result.append("\nВведите номер задачи, чтобы изменить ее статус.")
        bot.send_message(call.from_user.id, "\n".join(result))
        bot.set_state(call.from_user.id, States.tasks_make_done)


    @bot.message_handler(state=States.new_task_title)
    def process_task_title(message):
        with bot.retrieve_data(message.from_user.id) as data:
            data["new_task"]["title"] = message.text
        bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
        bot.set_state(message.from_user.id, States.new_task_due_date)


    @bot.message_handler(state=States.new_task_due_date)
    def process_task_due_date(message):
        due_date_string = message.text.replace(',', '.')
        try:
            due_date = datetime.strptime(due_date_string, DATE_FORMAT)
        except ValueError:
            bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
            return

        with bot.retrieve_data(message.from_user.id) as data:
            data["new_task"]["due_date"] = due_date

        new_task = Task(**data["new_task"])
        new_task.save()
        bot.send_message(message.from_user.id, f"Задача добавлена:\n{new_task}.\nИспользуйте кнопки внизу для управления.")
        bot.set_state(message.from_user.id, States.main)


    @bot.message_handler(state=States.tasks_make_done)
    def process_task_done(message):
        try:
            task_id = int(message.text)
            task = Task.get_or_none(Task.task_id == task_id)
            if task is None:
                bot.send_message(message.from_user.id, "Задачи с таким ID не существует.\nПовторите попытку ввода.")
                return

            if task.user_id != message.from_user.id:
                bot.send_message(
                    message.from_user.id, "Вы не являетесь владельцем данной задачи.\nПовторите попытку ввода."
                )
                return

            task.is_done = not task.is_done
            task.save()
            bot.send_message(message.from_user.id, task)
            bot.set_state(message.from_user.id, States.main)
            bot.send_message(message.from_user.id, "Что-то еще?")

        except ValueError:
            bot.set_state(message.from_user.id, States.main)
            bot.send_message(message.from_user.id, "Номер не распознан. Вернули вас в главное меню.\nКнопки управления в вашем распоряжении.")
        