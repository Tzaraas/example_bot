from telebot.types import Message, CallbackQuery

from states.base_states import Level
from keyboards.inline import menu_lv_1
from loader import bot


@bot.callback_query_handler(func=lambda call: True, state=Level.lv_0)
def base_query(call: CallbackQuery):
    match call.data:
# -----------------------------------------------------------------------------------------
        case "b1":
            menu_lv_1.kb_1(call)
        case "b2":
            menu_lv_1.kb_2(call)
        case "b3":
            menu_lv_1.kb_3(call)
# -----------------------------------------------------------------------------------------
        case "exit":
            bot.stop_bot()
            bot.delete_state(call.from_user.id)
            bot.send_message(call.message.chat.id, "До новых встреч!")
