"""
Обработчики команд /time и /date.
Показывают текущее время и дату.
"""

from datetime import datetime


def register_time_date_handlers(bot):
    """Регистрирует обработчики команд /time и /date."""
    
    @bot.message_handler(commands=['time'])
    def time_command(message):
        """Отправляет текущее время в формате ЧЧ:ММ."""
        current_time = datetime.now().strftime("%H:%M")
        bot.send_message(message.chat.id, f"Сейчас {current_time}")
    
    @bot.message_handler(commands=['date'])
    def date_command(message):
        """Отправляет сегодняшнюю дату в формате ДД.ММ.ГГГГ."""
        current_date = datetime.now().strftime("%d.%m.%Y")
        bot.send_message(message.chat.id, f"Сегодня {current_date}")