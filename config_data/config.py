import os
from dotenv import load_dotenv, find_dotenv


# Окружение
# ====================================================
if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()
    print('Загрузка прошла успешно')
# ====================================================


# Токен бота
# ====================================================
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    exit("BOT_TOKEN отсутствует в переменных окружения")
# ====================================================


# Базы данных
# ====================================================
if os.path.exists(r"database\database_dynamic.db"):
    DB_DYNAMIC_PATH = r"database\database_dynamic.db"
else:
    with open(r"database\database_dynamic.db", 'w') as db:
        DB_DYNAMIC_PATH = r"database\database_dynamic.db"

DB_STATIC_PATH = r"database\database_static.db"
# ====================================================


# Команды по умолчанию
# ====================================================
DEFAULT_COMMANDS = (
    ("start", "Начало"),
    ("help", "Справка"),
    ("empty", "Почистить кэш")
)
# ====================================================


# gif api
# ====================================================
API_GIF_KEY = os.getenv("API_GIF_KEY")
if API_GIF_KEY is None:
    exit("API_GIF_KEY отсутствует в переменных окружения")

API_BASE_URL = "https://api.giphy.com/v1/gifs/"
# ====================================================