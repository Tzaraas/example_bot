from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data import config


levels_storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=levels_storage)
