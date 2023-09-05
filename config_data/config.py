import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv('.venv'):
    exit("Переменные окружения не загружены т.к отсутствует файл .venv")
else:
    load_dotenv('config_data\.venv')
    print('Загрузка прошла успешно')

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_DICT_KEY = os.getenv("API_DICT_KEY")
