"""
Обработчик команды /help.
Показывает список всех доступных команд.
"""


def register_help_handler(bot):
    """Регистрирует обработчик команды /help."""
    
    @bot.message_handler(commands=['help'])
    def help_command(message):
        """Отправляет пользователю список всех команд с описанием."""
        help_text = (
            "Доступные команды:\n\n"
            "/start - Приветствие\n"
            "/help - Показать это сообщение\n"
            "/time - Текущее время\n"
            "/date - Сегодняшняя дата\n"
            "/random - Случайное число от 1 до 100\n"
            "/weather <город> - Погода в указанном городе\n\n"
            "Пример: /weather Москва"
        )
        bot.send_message(message.chat.id, help_text)