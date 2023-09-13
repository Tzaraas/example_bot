from telebot.types import Message, CallbackQuery
from telebot.apihelper import ApiTelegramException
from typing import Union

from utils.loader import bot


def fork(enter: Union[Message, CallbackQuery], keyboard, text, lv):
    ''' Вилка, определяет логику работы клавиатуры, в т.ч. удаления ее старой версии. '''

    bot.set_state(enter.from_user.id, lv)
    
    if isinstance(enter, CallbackQuery):
        with bot.retrieve_data(enter.from_user.id) as memory:
            memory['old'] = enter.message.id
        bot.edit_message_text(text, enter.message.chat.id, enter.message.id, reply_markup=keyboard)
    else:
        with bot.retrieve_data(enter.from_user.id) as memory:
            if memory:
                try:
                    bot.delete_message(enter.chat.id, memory['old'])
                except ApiTelegramException:
                    pass    
            memory['old'] = bot.send_message(enter.chat.id, text).message_id
            bot.edit_message_text(text, enter.chat.id, memory['old'], reply_markup=keyboard)


def spoon(call: CallbackQuery):
    ''' Ложка, убивает старую клавиатуру, когда вилка не хочет. Функционально является костылем. '''

    with bot.retrieve_data(call.from_user.id) as memory:
        try:
            bot.delete_message(call.message.chat.id, memory['old'])
        except ApiTelegramException:
            pass