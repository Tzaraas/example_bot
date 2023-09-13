from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.api import store_api
from loader import bot


def step1(call: CallbackQuery):
    bot.set_state(call.from_user.id, Level.listen)
    bot.send_message(call.message.chat.id, "Введите id заказа:")
    bot.register_next_step_handler(call.message, step2)

def step2(message: Message):
    with bot.retrieve_data(message.from_user.id) as memory:
        memory['order_id'] = message.text
    bot.send_message(message.chat.id, "Введите id товара:")
    bot.register_next_step_handler(message, step3) 

def step3(message: Message):
    with bot.retrieve_data(message.from_user.id) as memory:
        memory['product_id'] = message.text
        answer = store_api.DeleteFromOrder(memory['order_id'], memory['product_id'])
    
    if answer:
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуйте снова, следите за корректностю ввода.")

    front_lv_2.kb_3(message)
    