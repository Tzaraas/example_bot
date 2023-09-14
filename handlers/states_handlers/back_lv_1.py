from telebot.types import Message, CallbackQuery

from states.base_states import Level
from database.models import Cities, Countries
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from database.models import Orders, Products
from utils.loader import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith('l1_'))
def query_lv_1(call: CallbackQuery):
    ''' Отвечает за отлов callback-ов на уровне 1 '''

    match call.data:
# ------------------------------------------------------------- Базовая информация о стране
        case "l1_k1_b1":                                                    # Запустить API
            bot.set_state(call.from_user.id, Level.listen_country)
            bot.send_message(call.message.chat.id, "Введите название страны:")
        case "l1_k1_b2":                                         # Замечания о работе c API
            front_lv_2.kb_1(call)
        case "l1_k1_b3":                             # DataBase: Часто запрашиваемые страны
            countries = Countries.select().order_by(Countries.country_count.desc()).limit(5)
            if countries:
                for country in countries:
                    bot.send_message(call.message.chat.id, country)
            else:
                bot.send_message(call.message.chat.id, "Список пока пуст.")
# ------------------------------------------------------------------------- Погода за окном
        case "l1_k2_b1":                                                    # Запустить API
            bot.set_state(call.from_user.id, Level.listen_city)
            bot.send_message(call.message.chat.id, "Введите название населенного пункта:")
        case "l1_k2_b2":                                         # Замечания о работе c API
            front_lv_2.kb_2(call)
        case "l1_k2_b3":                             # DataBase: Часто запрашиваемые города
            cities = Cities.select().order_by(Cities.city_count.desc()).limit(5)
            if cities:
                for city in cities:
                    bot.send_message(call.message.chat.id, city)
            else:
                bot.send_message(call.message.chat.id, "Список пока пуст.")
# ----------------------------------------------------------------- Полноценный web магазин
        case "l1_k3_b1":                                                    # Запустить API
            front_lv_2.kb_3(call)
        case "l1_k3_b2":                                         # Замечания о работе c API
            front_lv_2.kb_4(call)
        case "l1_k3_b3":                                    # DataBase: последние 5 заказов
            orders = Orders.select().where(Orders.order_user_id == call.from_user.id).limit(5)
            if orders:
                for order in orders:
                    bot.send_message(call.message.chat.id, 
                                     f'Заказ номер {order.order_local} от {order.order_date}: '\
                                     f'сумма - {order.order_total}, получатель - {order.order_customer}.')
                    products = Products.select().where(Products.product_order == order.order_local)
                    for product in products:
                        bot.send_message(call.message.chat.id, 
                                     f'{product.product_name}. Стоимость {product.product_price}.')
            else:
                bot.send_message(call.message.chat.id, "Список пока пуст.")
# ------------------------------------------------------------------------------------ back
        case "l1_back_main":                                               # В главное меню
            front_lv_0.kb_base(call)
        case _:
            bot.send_message(call.message.chat.id, "Этого тут быть не должно.")
