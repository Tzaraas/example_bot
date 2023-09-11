from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import front_lv_1
from loader import bot


@bot.callback_query_handler(func=lambda call: True, state=Level.lv_2)
def query_lv_2(call: CallbackQuery):
    match call.data:
# -----------------------------------------------------------------------------------------
        case "back_l1_k1":
            front_lv_1.kb_1(call)
        case "back_l1_k2":
            front_lv_1.kb_2(call)
        case "back_l1_k3":
            front_lv_1.kb_2(call)
# -----------------------------------------------------------------------------------------
        case _:
            bot.send_message(call.message.chat.id, f"Вызов функции {call.data}")