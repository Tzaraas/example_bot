from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_0, front_lv_1, front_lv_2
from loader import bot


@bot.callback_query_handler(func=lambda call: call.data.startswith('l0_'), state=Level.lv_0)
def query_lv_0(call: CallbackQuery):
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
