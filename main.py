from telebot.custom_filters import StateFilter

import handlers
from database import models
from utils import set_bot_commands
from utils.loader import bot


if __name__ == "__main__":
    models.create_models()
    bot.add_custom_filter(StateFilter(bot))
    set_bot_commands.set_default_commands(bot)
    print('Загрузка прошла успешно.')
    bot.infinity_polling()
