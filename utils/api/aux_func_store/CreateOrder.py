from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.api import store_api
from utils.loader import bot


''' Отвечает за логику работы API магазина (функционал - создать заказ) '''

def step1(call: CallbackQuery):
    bot.send_message(call.message.chat.id, "Введите имя получателя:")
    bot.register_next_step_handler(call.message, step2)

def step2(message: Message):
    with bot.retrieve_data(message.from_user.id) as memory:
        memory['user_name'] = message.text
    bot.send_message(message.chat.id, "Введите адрес:")
    bot.register_next_step_handler(message, step3) 

def step3(message: Message):
    with bot.retrieve_data(message.from_user.id) as memory:
        memory['user_address'] = message.text
        answer = store_api.CreateOrder(memory['user_name'], memory['user_address'])
    
    if answer:
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуйте снова, следите за корректностю ввода.")

    front_lv_2.kb_3(message)
    