from telebot.types import Message, CallbackQuery

from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from utils.loader import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith('l0_'))
def query_lv_0(call: CallbackQuery):
    ''' Отвечает за отлов callback-ов на уровне 0 '''
    
    match call.data:
# -----------------------------------------------------------------------------------------
        case "l0_kb_b1":                   # Простой пример - информация о выбранной стране
            front_lv_1.kb_1(call)
        case "l0_kb_b2":                      # Стандартный уровень - запрос текущей погоды
            front_lv_1.kb_2(call)
        case "l0_kb_b3":                                    # Полноценный API - web магазин
            front_lv_1.kb_3(call)
# -----------------------------------------------------------------------------------------
        case _:
            bot.send_message(call.message.chat.id, "Этого тут быть не должно.")
