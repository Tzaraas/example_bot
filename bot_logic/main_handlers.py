import sqlite3
from telebot import types
from peewee import IntegrityError

from database.db_conf import User, get_script
from config_data.config import DEFAULT_LANG
from .states import States


def initialization_main_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_message(message):
        user_id = message.from_user.id
        user_name = message.from_user.first_name

        try:
            User.create(
                user_id=user_id,
                user_name=user_name,
                user_lang=DEFAULT_LANG
            )
            bot.reply_to(message, "Добро пожаловать!")
        except IntegrityError:
            bot.reply_to(message, f"Рад видеть вас снова, {user_name}!")

        main_menu(message)


    def main_menu(message):
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=True)
        item1 = types.KeyboardButton("Планировщик задач")
        item2 = types.KeyboardButton("Перевод текста")
        markup1.add(item1, item2)
        bot.send_message(message.chat.id, "Чем могу помочь?", reply_markup=markup1)
        bot.set_state(message.from_user.id, States.main)
        

    @bot.message_handler(state=States.main, content_types=['text'])
    def button(message):
        match message.text:
            case "Планировщик задач":
                menu_tasks(message)

            case "Перевод текста":
                menu_dictionary(message)

            case _:
                bot.reply_to(message, "Используйте кнопки виртуальной клавиатуры внизу для управления.")


    def menu_tasks(message):
        markup2 = types.InlineKeyboardMarkup(row_width=2)
        item1 = types.InlineKeyboardButton("Задачи на сегодня", callback_data="today")
        item2 = types.InlineKeyboardButton("Последние 10 задач", callback_data="tasks")
        item3 = types.InlineKeyboardButton("Новая задача", callback_data="newtask")
        markup2.add(item1, item2, item3)
        bot.send_message(message.chat.id, "Выберите действие планировщика:", reply_markup=markup2)


    def menu_dictionary(message):
        user_lang = get_script(message.from_user.id)
          
        markup3 = types.InlineKeyboardMarkup(row_width=1)
        item1 = types.InlineKeyboardButton("Поиск слова или фразы", callback_data="lookup")
        item2 = types.InlineKeyboardButton("Сменить направление перевода", callback_data="set_lang")
        markup3.add(item1, item2)
        bot.send_message(message.chat.id, 
                            f"Это бот Яндекс.Словаря. Он умеет переводить слова. Направление перевода - [{user_lang}]. Выберите действие:",
                            reply_markup=markup3)
