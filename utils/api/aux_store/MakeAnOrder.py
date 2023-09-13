from telebot.types import Message, CallbackQuery
from peewee import IntegrityError

from database.models import Orders, Products
from utils.loader import bot


''' Отвечает за логику работы базы данных магазина (функционал - сохранить заказ в базу данных) '''

def CompleteOrder(call: CallbackQuery):
    with bot.retrieve_data(call.from_user.id) as memory:
        try:
            Orders.create(order_local = memory['order_local'],
                          order_date = memory['order_date'][:10],
                          order_total = memory['order_total'],
                          order_customer = memory['order_customer'],
                          order_user_id = call.from_user.id)
            for elem in memory['products']:
                Products.create(product_name = elem['name'],
                                product_price = elem['price'],
                                product_order = memory['order_local'])
            
            bot.send_message(call.message.chat.id, "Заказ успешно создан.")

        except KeyError:
            bot.send_message(call.message.chat.id, "Сперва необходимо проверить корзину.")
        except IntegrityError:
            bot.send_message(call.message.chat.id, "Этот заказ уже оформлен.")
