"""
Обработчик команды /random.
Генерирует случайное число от 1 до 100.
"""

import random


def register_random_handler(bot):
    """Регистрирует обработчик команды /random."""
    
    @bot.message_handler(commands=['random'])
    def random_command(message):
        """Генерирует и отправляет случайное число от 1 до 100."""
        number = random.randint(1, 100)
        bot.send_message(message.chat.id, f"Выпало число: {number}")