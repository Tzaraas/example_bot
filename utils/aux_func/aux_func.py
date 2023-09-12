from telebot.types import Message, CallbackQuery

from utils.api import weather_api, country_api
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from loader import bot


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