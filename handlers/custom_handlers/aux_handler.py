from telebot.types import Message, CallbackQuery

from states.base_states import Level
from utils.api import weather_api, country_api
from database.models import Cities, Countries
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.loader import bot


@bot.message_handler(state=Level.listen_country)
def enter_country(message: Message):
    ''' Отвечает за логику работы API с информацией о странах '''

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
        front_lv_1.kb_1(message)
    else:
        bot.send_message(message.chat.id, "Такая страна не найдена.")


@bot.message_handler(state=Level.listen_city)
def enter_city(message: Message):
    ''' Отвечает за логику работы API погоды '''

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
        front_lv_1.kb_2(message)
    else:
        bot.send_message(message.chat.id, "Такой город не найден.")
