from telebot.types import Message, CallbackQuery

from utils.api import weather_api, country_api
from states.base_states import Level
from keyboards.inline import menu_lv_0, menu_lv_1, menu_lv_2
from loader import bot


@bot.callback_query_handler(func=lambda call: True, state=Level.lv_1)
def base_query(call: CallbackQuery):
    match call.data:
# -------------------------------------------------------------------------------------kb_1
        case "b1":  # Пример работы API
            bot.set_state(call.from_user.id, Level.listen_country)
            bot.send_message(call.message.chat.id, "Введите название страны:")
            bot.register_next_step_handler(call.message, enter_country)
        case "b2":  # Замечания о работе c API
            menu_lv_2.kb_2(call)
        case "b3":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# -------------------------------------------------------------------------------------kb_2
        case "b4":  # Пример работы API
            bot.set_state(call.from_user.id, Level.listen_city)
            bot.send_message(call.message.chat.id, "Введите название населенного пункта:")
            bot.register_next_step_handler(call.message, enter_city)
        case "b5":  # Замечания о работе c API
            menu_lv_2.kb_5(call)
        case "b6":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# -------------------------------------------------------------------------------------kb_3
        case "b7":  # Пример работы API
            pass
        case "b8":  # Замечания о работе c API
            menu_lv_2.kb_8(call)
        case "b9":  # Статистика использования API
            bot.send_message(call.message.chat.id, "В разработке.")
# -------------------------------------------------------------------------------------back
        case "back":
            menu_lv_0.kb_base(call)


def enter_city(message: Message):
    coord = weather_api.weather_api_request('search', message.text)
    if coord:
        answer = weather_api.weather_api_request('get', coord)
        bot.reply_to(message, answer)
    else:
        bot.send_message(message.chat.id, "Такой город не найден.")
    menu_lv_1.kb_2(message)


def enter_country(message: Message):
    answer = country_api.country_api_request(message.text)
    if answer:
        bot.reply_to(message, answer)
    else:
        bot.send_message(message.chat.id, "Такая страна не найдена.")
    menu_lv_1.kb_1(message)
