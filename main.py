from telebot.custom_filters import StateFilter
import os

import handlers
from loader import bot
from database import models
from utils import set_bot_commands
from config_data.config import DB_STATIC_PATH


if __name__ == "__main__":
    models.create_models()
    if not os.path.exists(DB_STATIC_PATH):
        with open(DB_STATIC_PATH, 'w') as db:
            models.filling_static_db()
    bot.add_custom_filter(StateFilter(bot))
    set_bot_commands.set_default_commands(bot)
    bot.infinity_polling()
