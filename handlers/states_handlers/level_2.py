from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import menu_lv_1
from loader import bot


@bot.callback_query_handler(func=lambda call: True, state=Level.lv_2)
def base_query(call: CallbackQuery):
    match call.data:
# -----------------------------------------------------------------------------------------
        case "back_1":
            menu_lv_1.kb_1(call)
        case "back_2":
            menu_lv_1.kb_2(call)
        case "back_3":
            menu_lv_1.kb_2(call)
# -----------------------------------------------------------------------------------------
        case _:
            bot.send_message(call.message.chat.id, f"Вызов функции {call.data}")