from telebot import TeleBot, StateMemoryStorage
from telebot.custom_filters import StateFilter
from telebot.types import BotCommand

from database.db_conf import create_models
from .main_handlers import initialization_main_handlers
from .dictionary_handlers import initialization_dictionary_handlers
from .task_handlers import initialization_task_handlers
from config_data.config import BOT_TOKEN, DEFAULT_COMMANDS


state_storage = StateMemoryStorage()
bot = TeleBot(BOT_TOKEN, state_storage=state_storage)

initialization_main_handlers(bot)
initialization_dictionary_handlers(bot)
initialization_task_handlers(bot)

create_models()

bot.add_custom_filter(StateFilter(bot))
bot.set_my_commands([BotCommand(*cmd) for cmd in DEFAULT_COMMANDS])
