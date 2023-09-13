from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.api import aux_store
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith('l2_'), state=Level.lv_2)
def query_lv_2(call: CallbackQuery):
    match call.data:
# -------------------------------------------------- Замечания о работе c restcountries.com
        case "l2_k1_b1":                                                        # Нет ключа
            pass
        case "l2_k1_b2":                                                  # Мало переменных
            pass
        case "l2_k1_b3":                                                 # Настройка вывода
            pass
# ------------------------------------------------- Замечания о работе c openweathermap.org
        case "l2_k2_b1":                                                   # Разные запросы
            pass
        case "l2_k2_b2":                                                 # Адаптация данных
            pass
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
            pass
        case "l2_k4_b2":                                           # Описание кода на сайте
            pass
        case "l2_k4_b3":                                                         # GetOrder
            pass
        case "l2_k4_b4":                                             # Хранение результатов
            pass
# ------------------------------------------------------------------------------------ back
        case "l2_back_l1_k1":                        # В меню "Базовая информация о стране"
            front_lv_1.kb_1(call)
        case "l2_back_l1_k2":                                    # В меню "Погода за окном"
            front_lv_1.kb_2(call)
        case "l2_back_l1_k3":                            # В меню "Полноценный web магазин"
            front_lv_1.kb_3(call)
        case _:
            bot.send_message(call.message.chat.id, "Этого тут быть не должно.")