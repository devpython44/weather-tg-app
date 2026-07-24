"""
Модуль инициализации и запуска Telegram-бота.
Регистрирует все обработчики команд.
"""

import telebot
from src.config import BOT_TOKEN, validate_config
from src.handlers.start import register_start_handler
from src.handlers.help import register_help_handler
from src.handlers.time_date import register_time_date_handlers
from src.handlers.random_number import register_random_handler  # ИСПРАВЛЕНО
from src.handlers.weather import register_weather_handler


def create_bot():
    """
    Создаёт и настраивает экземпляр бота.
    Возвращает объект бота.
    """
    # Проверяем конфигурацию перед запуском
    validate_config()
    
    # Создаём бота
    bot = telebot.TeleBot(BOT_TOKEN)
    
    # Регистрируем все обработчики команд
    register_start_handler(bot)
    register_help_handler(bot)
    register_time_date_handlers(bot)
    register_random_handler(bot)
    register_weather_handler(bot)
    
    return bot


def start_bot():
    """
    Запускает бота в режиме бесконечного опроса.
    """
    bot = create_bot()
    print("Бот успешно запущен и готов к работе!")
    print("Доступные команды: /start, /help, /time, /date, /random, /weather <город>")
    bot.infinity_polling()