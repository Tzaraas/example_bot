from database.ORM_conf import User, Task
from telebot.handler_backends import State, StatesGroup
from .states import States
from config_data.config import DATE_FORMAT
from typing import List
from datetime import datetime, date


def initialization_task_handlers(bot):
    @bot.message_handler(state="*", commands=["newtask"])
    def handle_new_task(message):
        user_id = message.from_user.id
        if User.get_or_none(User.user_id == user_id) is None:
            bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
            return

        bot.send_message(user_id, "Введите название задачи")
        bot.set_state(message.from_user.id, States.new_task_title)
        with bot.retrieve_data(message.from_user.id) as data:
            data["new_task"] = {"user_id": user_id}


    @bot.message_handler(state="*", commands=["tasks"])
    def handle_tasks(message):
        user_id = message.from_user.id
        user = User.get_or_none(User.user_id == user_id)
        if user is None:
            bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
            return

        tasks: List[Task] = user.tasks.order_by(-Task.due_date, -Task.task_id).limit(10)

        result = []
        result.extend(map(str, reversed(tasks)))

        if not result:
            bot.send_message(message.from_user.id, "У вас ещё нет задач")
            return

        result.append("\nВведите номер задачи, чтобы изменить её статус.")
        bot.send_message(message.from_user.id, "\n".join(result))
        bot.set_state(message.from_user.id, States.tasks_make_done)


    @bot.message_handler(state="*", commands=["today"])
    def handle_today(message):
        user_id = message.from_user.id
        user = User.get_or_none(User.user_id == user_id)
        if user is None:
            bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
            return

        tasks: List[Task] = user.tasks.where(Task.due_date == date.today())

        result = []
        result.extend(map(str, tasks))

        if not result:
            bot.send_message(message.from_user.id, "У вас еще нет задач")
            return

        result.append("\nВведите номер задачи, чтобы изменить ее статус.")
        bot.send_message(message.from_user.id, "\n".join(result))
        bot.set_state(message.from_user.id, States.tasks_make_done)


    @bot.message_handler(state=States.new_task_title)
    def process_task_title(message):
        with bot.retrieve_data(message.from_user.id) as data:
            data["new_task"]["title"] = message.text
        bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
        bot.set_state(message.from_user.id, States.new_task_due_date)


    @bot.message_handler(state=States.new_task_due_date)
    def process_task_due_date(message):
        due_date_string = message.text
        try:
            due_date = datetime.strptime(due_date_string, DATE_FORMAT)
        except ValueError:
            bot.send_message(message.from_user.id, "Введите дату (ДД.ММ.ГГГГ):")
            return

        with bot.retrieve_data(message.from_user.id) as data:
            data["new_task"]["due_date"] = due_date

        new_task = Task(**data["new_task"])
        new_task.save()
        bot.send_message(message.from_user.id, f"Задача добавлена:\n{new_task}")
        bot.delete_state(message.from_user.id)


    @bot.message_handler(state=States.tasks_make_done)
    def process_task_done(message):
        task_id = int(message.text)
        task = Task.get_or_none(Task.task_id == task_id)
        if task is None:
            bot.send_message(message.from_user.id, "Задачи с таким ID не существует.")
            return

        if task.user_id != message.from_user.id:
            bot.send_message(
                message.from_user.id, "Вы не являетесь владельцем данной задачи."
            )
            return

        task.is_done = not task.is_done
        task.save()
        bot.send_message(message.from_user.id, task)