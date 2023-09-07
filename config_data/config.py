import os
from dotenv import load_dotenv, find_dotenv


if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()
    print('Загрузка прошла успешно')

BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    exit("BOT_TOKEN отсутствует в переменных окружения")

API_GIF_KEY = os.getenv("API_GIF_KEY")
if API_GIF_KEY is None:
    exit("API_GIF_KEY отсутствует в переменных окружения")

if os.path.exists(r"database\database.db"):
    DB_PATH = r"database\database.db"
else:
    with open(r"database\database.db", 'w') as db:
        DB_PATH = r"database\database.db"

DEFAULT_COMMANDS = (
    ("start", "Начало"),
    ("help", "Справка")
)

DEFAULT_LANG = "ru"

API_BASE_URL = "https://api.giphy.com/v1/gifs/"