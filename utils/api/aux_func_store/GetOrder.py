from telebot.types import Message, CallbackQuery

from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.api import store_api
from utils.loader import bot


''' Отвечает за логику работы API магазина (функционал - получить состояние заказа) '''

def step1(call: CallbackQuery):
    bot.send_message(call.message.chat.id, "Введите id заказа:")
    bot.clear_step_handler_by_chat_id(call.message.chat.id)
    bot.register_next_step_handler(call.message, step2)

def step2(message: Message):
    with bot.retrieve_data(message.from_user.id) as memory:
        memory['order_id'] = message.text
        answer = store_api.GetOrder(memory['order_id'])
    
    if answer:
        total = 0

# Вывод данных № 1:
        answer_1 = f"Заказ {answer['order']['id']}. Дата создания: {answer['order']['created']}.\n"\
                   f"Получатель: {answer['order']['customer']}, адрес: {answer['order']['address']}.\n\n"\
                   f"Список товаров:\n"
        bot.send_message(message.chat.id, answer_1)

# Вывод данных № 2:
        for elem in answer['items']:
            answer_2 = f"id {elem['id']}, наименование: {elem['name']}, цена: {elem['price']}."
            bot.send_message(message.chat.id, answer_2)
            total += elem['price']

# Вывод данных № 3:
        answer_3 = f"Всего товаров: {len(answer['items'])}. Суммарная стоимость: {total}."
        bot.send_message(message.chat.id, answer_3)
        
# Откладываю данные, чтобы потом сохранить в базу данных:
        with bot.retrieve_data(message.from_user.id) as memory:
            memory['order_local'] = answer['order']['id']
            memory['order_date'] = answer['order']['created']
            memory['order_total'] = total
            memory['order_customer'] = answer['order']['customer']
            memory['products'] = answer['items']

    else:
        bot.send_message(message.chat.id, "Что-то пошло не так. Попробуйте снова, следите за корректностю ввода.")

    front_lv_2.kb_3(message)
    