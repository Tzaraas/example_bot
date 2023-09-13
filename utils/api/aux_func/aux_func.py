from telebot.types import Message, CallbackQuery

from utils.api import weather_api, country_api
from database.models import Cities, Countries
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from loader import bot


def enter_city(message: Message):
    coord = weather_api.weather_api_request('search', message.text)
    if coord:
        answer = weather_api.weather_api_request('get', coord)
        bot.reply_to(message, answer)

        if Cities.get_or_none(Cities.city_name == message.text.title()):
            city = Cities.update(city_count = Cities.city_count + 1).where(Cities.city_name == message.text.title())
            city.execute()
        else:
            Cities.create(city_user_id=message.from_user.id,
                        city_name=message.text.title(),
                        city_count = 1)   
    else:
        bot.send_message(message.chat.id, "Такой город не найден.")
    front_lv_1.kb_2(message)


def enter_country(message: Message):
    answer = country_api.country_api_request(message.text)
    if answer:
        bot.reply_to(message, answer)

        if Countries.get_or_none(Countries.country_name == message.text.title()):
            country = Countries.update(country_count = Countries.country_count + 1).where(Countries.country_name == message.text.title())
            country.execute()
        else:
            Countries.create(country_user_id=message.from_user.id,
                        country_name=message.text.title(),
                        country_count = 1)
    else:
        bot.send_message(message.chat.id, "Такая страна не найдена.")
    front_lv_1.kb_1(message)