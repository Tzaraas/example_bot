from telebot import types
from database.ORM_conf import User
from peewee import IntegrityError
from .states import States


def initialization_main_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name

        try:
            User.create(
                user_id=user_id,
                user_name=user_name
            )
            bot.reply_to(message, "Добро пожаловать!")
        except IntegrityError:
            bot.reply_to(message, f"Рад вас снова видеть, {user_name}!")

        main_menu(message)


    def main_menu(message):
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("Планировщик задач")
        item2 = types.KeyboardButton("Перевод текста")
        markup1.add(item1, item2)
        bot.send_message(message.chat.id, "Чем могу помочь?", reply_markup=markup1)
        bot.set_state(message.from_user.id, States.main)
        

    @bot.message_handler(state=States.main, content_types=['text'])
    def button(message):
        match message.text:
            case "Планировщик задач":
                markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
                item1 = types.MenuButtonCommands("Создать задачу")
                item2 = types.MenuButtonCommands("Последние 10 задач")
                item3 = types.MenuButtonCommands("Задачи на сегодня")
                markup2.add(item1, item2, item3)
                bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup2)

            case "Перевод текста":
                pass

            case "Создать задачу":
                bot.send_message(message.chat.id, "/newtask")

            case "Последние 10 задач":
                bot.send_message(message.chat.id, "/tasks")

            case "Задачи на сегодня":
                bot.send_message(message.chat.id, "/today")

            case _:
                bot.reply_to(message, "На такую комманду я не запрограммирован...")
                # bot.send_message(message.chat.id, "На такую комманду я не запрограммирован...")