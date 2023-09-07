from telebot.types import Message

from states.my_states import Status
from loader import bot


@bot.message_handler(state=Status.main, content_types=['text'])
def main_status(message: Message):
    match message.text:
        case "Поднять себе настроение":
            pass

        case "Заняться делом":
            pass

        case _:
            bot.send_message(message.chat.id, "Это что-то на китайском?")



    
