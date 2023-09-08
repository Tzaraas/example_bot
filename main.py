from telebot.custom_filters import StateFilter

import handlers
from loader import bot
from database import db_conf
from utils import set_bot_commands


if __name__ == "__main__":
    db_conf.create_models()
    bot.add_custom_filter(StateFilter(bot))
    set_bot_commands.set_default_commands(bot)
    bot.polling()
