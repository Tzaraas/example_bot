from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils import aux_text, out_kb
from utils.api import aux_store
from utils.loader import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith('l2_'), state=Level.lv_2)
def query_lv_2(call: CallbackQuery):
    ''' Отвечает за отлов callback-ов на уровне 2 '''
    
    match call.data:
# -------------------------------------------------- Замечания о работе c restcountries.com
        case "l2_k1_b1":                                                        # Нет ключа
            bot.send_photo(call.message.chat.id, open('utils\img\img1.jpg', 'rb'))
            bot.send_message(call.message.chat.id, aux_text.l2_k1_b1)
            out_kb.spoon(call)
            front_lv_2.kb_1(call.message)
        case "l2_k1_b2":                                                  # Мало переменных
            bot.send_photo(call.message.chat.id, open('utils\img\img2.jpg', 'rb'))
            bot.send_message(call.message.chat.id, aux_text.l2_k1_b2)
            out_kb.spoon(call)
            front_lv_2.kb_1(call.message)
        case "l2_k1_b3":                                                 # Настройка вывода
            bot.send_message(call.message.chat.id, aux_text.l2_k1_b3_1)
            bot.send_photo(call.message.chat.id, open('utils\img\img3.jpg', 'rb'))
            bot.send_message(call.message.chat.id, aux_text.l2_k1_b3_2)
            out_kb.spoon(call)
            front_lv_2.kb_1(call.message)
# ------------------------------------------------- Замечания о работе c openweathermap.org
        case "l2_k2_b1":                                                   # Разные запросы
            bot.send_photo(call.message.chat.id, open('utils\img\img4.jpg', 'rb'))
            bot.send_message(call.message.chat.id, aux_text.l2_k2_b1)
            out_kb.spoon(call)
            front_lv_2.kb_2(call.message)
        case "l2_k2_b2":                                                 # Адаптация данных
            bot.send_photo(call.message.chat.id, open('utils\img\img5.jpg', 'rb'))
            bot.send_message(call.message.chat.id, aux_text.l2_k2_b2)
            out_kb.spoon(call)
            front_lv_2.kb_2(call.message)
# --------------------------------------------------------------------------------- Магазин
        case "l2_k3_b1":                                                 # Создание позиции
            aux_store.CreateProduct.step1(call)
        case "l2_k3_b2":                                                 # Удаление позиции
            aux_store.DeleteProduct.step1(call)
        case "l2_k3_b3":                                                   # Cписок товаров
            aux_store.GetProductsInCategory.step1(call)
        case "l2_k3_b4":                                                    # Выбрать товар
            aux_store.GetProduct.step1(call)
        case "l2_k3_b5":                                                    # Создать заказ
            aux_store.CreateOrder.step1(call)
        case "l2_k3_b6":                                                # Проверить корзину
            aux_store.GetOrder.step1(call)
        case "l2_k3_b7":                                                 # Добавить в заказ
            aux_store.AddToOrder.step1(call)
        case "l2_k3_b8":                                                # Удалить из заказа
            aux_store.DeleteFromOrder.step1(call)
        case "l2_k3_b9":                                                   # Оформить заказ
            aux_store.MakeAnOrder.CompleteOrder(call)
# ------------------------------------------------------ Замечания о работе c web магазином
        case "l2_k4_b1":                                         # Несколько типов запросов
            bot.send_photo(call.message.chat.id, open('utils\img\img6-1.jpg', 'rb'))
            bot.send_message(call.message.chat.id, aux_text.l2_k4_b1)
            bot.send_photo(call.message.chat.id, open('utils\img\img6-2.jpg', 'rb'))
            out_kb.spoon(call)
            front_lv_2.kb_4(call.message)
        case "l2_k4_b2":                                           # Описание кода на сайте
            bot.send_message(call.message.chat.id, aux_text.l2_k4_b2)
            bot.send_photo(call.message.chat.id, open('utils\img\img7.jpg', 'rb'))
            out_kb.spoon(call)
            front_lv_2.kb_4(call.message)
        case "l2_k4_b3":                                                         # GetOrder
            bot.send_message(call.message.chat.id, aux_text.l2_k4_b3_1)
            bot.send_photo(call.message.chat.id, open('utils\img\img8.jpg', 'rb'))
            bot.send_message(call.message.chat.id, aux_text.l2_k4_b3_2)
            out_kb.spoon(call)
            front_lv_2.kb_4(call.message)
        case "l2_k4_b4":                                             # Хранение результатов
            bot.send_message(call.message.chat.id, aux_text.l2_k4_b4)
            bot.send_photo(call.message.chat.id, open('utils\img\img9.jpg', 'rb'))
            bot.send_photo(call.message.chat.id, open('utils\img\img10.jpg', 'rb'))
            out_kb.spoon(call)
            front_lv_2.kb_4(call.message)
# ------------------------------------------------------------------------------------ back
        case "l2_back_l1_k1":                        # В меню "Базовая информация о стране"
            front_lv_1.kb_1(call)
        case "l2_back_l1_k2":                                    # В меню "Погода за окном"
            front_lv_1.kb_2(call)
        case "l2_back_l1_k3":                            # В меню "Полноценный web магазин"
            front_lv_1.kb_3(call)
        case _:
            bot.send_message(call.message.chat.id, "Этого тут быть не должно.")