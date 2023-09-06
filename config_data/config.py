import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv('.venv'):
    exit("Переменные окружения не загружены т.к отсутствует файл .venv")
else:
    load_dotenv(r'config_data/.venv')
    print('Загрузка прошла успешно')

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    exit("BOT_TOKEN отсутствует в переменных окружения")

API_DICT_KEY = os.getenv("API_DICT_KEY")
if API_DICT_KEY is None:
    exit("API_DICT_KEY отсутствует в переменных окружения")

DB_PATH = r"database\database.db"

DATE_FORMAT = "%d.%m.%Y"

DEFAULT_COMMANDS = (
    ("start", "Начало"),
    ("newtask", "Создать задачу"),
    ("tasks", "Последние 10 задач"),
    ("today", "Задачи на сегодня")
)