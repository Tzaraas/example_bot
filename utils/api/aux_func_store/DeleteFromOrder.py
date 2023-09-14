from telebot.types import Message, CallbackQuery

from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.api import store_api
from utils.loader import bot


''' Отвечает за логику работы API магазина (функционал - удалить из заказа) '''

def step1(call: CallbackQuery):
    bot.send_message(call.message.chat.id, "Введите id заказа:")
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
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
    