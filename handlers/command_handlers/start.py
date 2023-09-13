from telebot.types import Message
from peewee import IntegrityError

from database.models import User
from keyboards.inline import front_lv_0
from utils.loader import bot


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    ''' Приветствует пользователя, является единственной точкой входа в программу '''

    user_id = message.from_user.id
    user_name = message.from_user.first_name

    try:
        User.create(
            user_id=user_id,
            user_name=user_name
        )
        bot.reply_to(message, "Добро пожаловать!")
    except IntegrityError:
        bot.reply_to(message, f"Рад видеть вас снова, {user_name}!")

    front_lv_0.kb_base(message)
