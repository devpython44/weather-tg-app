"""
Главный файл запуска Telegram-бота "Помощник".
Точка входа в приложение.
"""

from src.bot import start_bot


if __name__ == "__main__":
    print("Запуск бота...")
    start_bot()