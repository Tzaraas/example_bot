from telebot.types import Message
from peewee import IntegrityError

from loader import bot
from states.my_states import Status
from database.models import User
from keyboards.reply import main_menu


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
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

    bot.set_state(message.from_user.id, Status.main)
    bot.send_message(message.chat.id, "Чем займемся?", reply_markup=main_menu.menu_button())
