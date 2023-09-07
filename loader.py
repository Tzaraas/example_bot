from telebot import TeleBot
from telebot.storage import StateMemoryStorage

from config_data import config


my_states_storage = StateMemoryStorage()
bot = TeleBot(token=config.BOT_TOKEN, state_storage=my_states_storage)
