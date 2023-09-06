import json

from API_app import api_conf
from database.db_conf import set_script, get_script
from .states import States


available_langs = api_conf.get_langs()

def initialization_dictionary_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data in ["set_lang", "lookup"])
    def callback_api(call):
        match call.data:
            case "set_lang":
                set_lang_command(call)
            case "lookup":
                lookup_command(call)


    def set_lang_command(call):
        user_id = call.from_user.id
        lang_list = ', '.join(available_langs)
        bot.send_message(user_id, f'Выберите один из представленных направлений перевода:\n\n{lang_list}')
        bot.set_state(user_id, States.lang)


    @bot.message_handler(state=States.lang)
    def set_lang(message):
        chosen_lang = message.text
        if chosen_lang not in available_langs:
            bot.send_message(message.chat.id, 'Такого направления перевода нет. Попробуйте еще раз')
            return

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            data['lang'] = message.text
            set_script(message.from_user.id, data['lang'])
            bot.send_message(message.chat.id, f'Выбрано направление {data["lang"]}.\nДля активации поиска используйте кнопки внизу.')

        bot.set_state(message.from_user.id, States.main)


    def lookup_command(call):
        user_id = call.from_user.id
        bot.send_message(user_id, "Введите текст или фразу для поиска.")
        bot.set_state(user_id, States.lookup)


    @bot.message_handler(state=States.lookup)
    def lookup(message):
        if message.text in ["Планировщик задач", "Перевод текста"]:
            bot.send_message(message.chat.id, "Возвращаемся в главное меню... Готово.")
            bot.set_state(message.from_user.id, States.main)
            return

        with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
            result = api_conf.lookup(text=message.text, lang=data.get('lang', get_script(message.from_user.id)))
            
            try:
                answer = api_conf.LookupResult(result)
                bot.send_message(message.chat.id, answer)
                bot.send_message(message.chat.id, "Используйте кнопки для выбора дальнейших действий.")
                bot.set_state(message.from_user.id, States.main)

            except IndexError:
                bot.send_message(message.chat.id, "Слово не распознано.\nВведите текст или фразу для поиска.")
