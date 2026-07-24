"""
Обработчик команды /start.
Отправляет приветственное сообщение.
"""


def register_start_handler(bot):
    """Регистрирует обработчик команды /start."""
    
    @bot.message_handler(commands=['start'])
    def start_command(message):
        """Приветствует пользователя и предлагает посмотреть список команд."""
        welcome_text = (
            "Привет! Я бот-помощник. "
            "Напиши /help чтобы увидеть список команд."
        )
        bot.send_message(message.chat.id, welcome_text)