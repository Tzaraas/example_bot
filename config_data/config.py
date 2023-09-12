import os
from dotenv import load_dotenv, find_dotenv


# ================== Окружение =======================
if not find_dotenv():
    exit("Переменные окружения не загружены т.к отсутствует файл .env")
else:
    load_dotenv()
# ====================================================


# ================== Токен бота ======================
BOT_TOKEN = os.getenv("BOT_TOKEN")
if BOT_TOKEN is None:
    exit("BOT_TOKEN отсутствует в переменных окружения")
# ====================================================


# ================= Базы данных ======================
if os.path.exists(r"database\database.db"):
    DB_PATH = r"database\database.db"
else:
    with open(r"database\database.db", 'w') as db:
        DB_PATH = r"database\database.db"
# ====================================================


# ============= Команды по умолчанию =================
DEFAULT_COMMANDS = (
    ("start", "Начало"),
    ("help", "Справка")
)
# ====================================================


# ====================== API =========================

# ---------------------- GIF -------------------------
API_GIF_KEY = os.getenv("API_GIF_KEY")
if API_GIF_KEY is None:
    exit("API_GIF_KEY отсутствует в переменных окружения")

API_GIF_BASE_URL = "https://api.giphy.com/v1/gifs/"
# ----------------------------------------------------

# -------------------- COUNTRY -----------------------
API_COUNTRY_BASE_URL = "https://restcountries.com/v3.1/translation/"
# ----------------------------------------------------

# -------------------- WEATHER -----------------------
API_WEATHER_KEY = os.getenv("API_WEATHER_KEY")
if API_WEATHER_KEY is None:
    exit("API_WEATHER_KEY отсутствует в переменных окружения")

API_WEATHER_BASE_URL = "https://api.openweathermap.org/"
# ----------------------------------------------------

# --------------------- STORE ------------------------
API_STORE_KEY = os.getenv("API_STORE_KEY")
if API_STORE_KEY is None:
    exit("API_STORE_KEY отсутствует в переменных окружения")

API_STORE_BASE_URL = "https://my-store2.p.rapidapi.com/"
API_STORE_HOST = "my-store2.p.rapidapi.com"
# ----------------------------------------------------
# ====================================================