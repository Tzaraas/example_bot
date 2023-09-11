from telebot.types import Message, CallbackQuery

from utils.api import weather_api, country_api
from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from loader import bot


@bot.callback_query_handler(func=lambda call: True, state=Level.lv_1)
def query_lv_1(call: CallbackQuery):
    match call.data:
# -------------------------------------------------------------------------------------kb_1
        case "l1_k1_b1":  # Пример работы API
            bot.set_state(call.from_user.id, Level.listen_country)
            bot.send_message(call.message.chat.id, "Введите название страны:")
            bot.register_next_step_handler(call.message, enter_country)
        case "l1_k1_b2":  # Замечания о работе c API
            front_lv_2.kb_1(call)
        case "l1_k1_b3":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# -------------------------------------------------------------------------------------kb_2
        case "l1_k2_b1":  # Пример работы API
            bot.set_state(call.from_user.id, Level.listen_city)
            bot.send_message(call.message.chat.id, "Введите название населенного пункта:")
            bot.register_next_step_handler(call.message, enter_city)
        case "l1_k2_b2":  # Замечания о работе c API
            front_lv_2.kb_2(call)
        case "l1_k2_b3":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# -------------------------------------------------------------------------------------kb_3
        case "l1_k3_b1":  # Пример работы API
            pass
        case "l1_k3_b2":  # Замечания о работе c API
            front_lv_2.kb_3(call)
        case "l1_k3_b3":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# -------------------------------------------------------------------------------------back
        case "back_main":
            front_lv_0.kb_base(call)


def enter_city(message: Message):
    coord = weather_api.weather_api_request('search', message.text)
    if coord:
        answer = weather_api.weather_api_request('get', coord)
        bot.reply_to(message, answer)
    else:
        bot.send_message(message.chat.id, "Такой город не найден.")
    front_lv_1.kb_2(message)


def enter_country(message: Message):
    answer = country_api.country_api_request(message.text)
    if answer:
        bot.reply_to(message, answer)
    else:
        bot.send_message(message.chat.id, "Такая страна не найдена.")
    front_lv_1.kb_1(message)
