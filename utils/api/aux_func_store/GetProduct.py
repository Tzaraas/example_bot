from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.api import store_api
from utils.loader import bot


''' Отвечает за логику работы API магазина (функционал - подробности о продукте) '''

def step1(call: CallbackQuery):
    bot.send_message(call.message.chat.id, "Введите id товара:")
    bot.register_next_step_handler(call.message, step2)

def step2(message: Message):
    with bot.retrieve_data(message.from_user.id) as memory:
        memory['product_id'] = message.text
        answer = store_api.GetProduct(memory['product_id'])
    
    if answer:
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуйте снова, следите за корректностю ввода.")

    front_lv_2.kb_3(message)
