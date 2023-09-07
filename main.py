from loader import bot
from telebot.custom_filters import StateFilter

from utils import set_bot_commands
from database import db_conf
import handlers


if __name__ == "__main__":
    db_conf.create_models()
    bot.add_custom_filter(StateFilter(bot))
    set_bot_commands.set_default_commands(bot)
    bot.polling()
