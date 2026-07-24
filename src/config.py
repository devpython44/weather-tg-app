"""
Модуль конфигурации.
Загружает переменные окружения из .env файла.
"""

import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Токены и настройки
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
DEFAULT_CITY = os.getenv("DEFAULT_CITY", "Moscow")

def validate_config():
    """Проверяет наличие обязательных переменных окружения."""
    if not BOT_TOKEN:
        raise ValueError(
            "BOT_TOKEN не найден! "
            "Создайте файл .env на основе .env.example и укажите токен бота."
        )
    if not WEATHER_API_KEY:
        print("WEATHER_API_KEY не задан. Команда /weather будет использовать имитацию данных.")