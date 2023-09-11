from telebot.types import Message, CallbackQuery
from typing import Union

from loader import bot


def fork(enter: Union[Message, CallbackQuery], keyboard, text, lv):
    bot.set_state(enter.from_user.id, lv)
    
    if isinstance(enter, CallbackQuery):
        with bot.retrieve_data(enter.from_user.id) as memory:
            memory['old'] = enter.message.id
        bot.edit_message_text(text, enter.message.chat.id, enter.message.id, reply_markup=keyboard)
    else:
        with bot.retrieve_data(enter.from_user.id) as memory:
            if memory:
                bot.delete_message(enter.chat.id, memory['old'])
        bot.send_message(enter.chat.id, text, reply_markup=keyboard)