from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.aux_func import aux_func
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith('l1_'), state=Level.lv_1)
def query_lv_1(call: CallbackQuery):
    match call.data:
# ------------------------------------------------------------ Базовая информация о стране
        case "l1_k1_b1":  # Пример работы API
            bot.set_state(call.from_user.id, Level.listen_country)
            bot.send_message(call.message.chat.id, "Введите название страны:")
            bot.register_next_step_handler(call.message, aux_func.enter_country)
        case "l1_k1_b2":  # Замечания о работе c API
            front_lv_2.kb_1(call)
        case "l1_k1_b3":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# ------------------------------------------------------------------------ Погода за окном
        case "l1_k2_b1":  # Пример работы API
            bot.set_state(call.from_user.id, Level.listen_city)
            bot.send_message(call.message.chat.id, "Введите название населенного пункта:")
            bot.register_next_step_handler(call.message, aux_func.enter_city)
        case "l1_k2_b2":  # Замечания о работе c API
            front_lv_2.kb_2(call)
        case "l1_k2_b3":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# ---------------------------------------------------------------- Полноценный web магазин
        case "l1_k3_b1":  # Пример работы API
            front_lv_2.kb_3(call)
        case "l1_k3_b2":  # Замечания о работе c API
            front_lv_2.kb_4(call)
        case "l1_k3_b3":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# ------------------------------------------------------------------------------------ back
        case "l1_back_main":  # В главное меню
            front_lv_0.kb_base(call)
        case _:
            bot.send_message(call.message.chat.id, "Этого тут быть не должно.")
