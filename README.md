# 🤖 Telegram-бот "Помощник"

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-blue)](https://t.me/your_bot_username)

Простой и функциональный Telegram-бот с полезными командами: время, дата, случайные числа и прогноз погоды.

---

## 📋 Функционал

| Команда | Описание | Пример ответа |
|---------|----------|---------------|
| `/start` | Приветствие | `👋 Привет! Я бот-помощник...` |
| `/help` | Список команд | `📚 Доступные команды...` |
| `/time` | Текущее время | `🕒 Сейчас 14:35` |
| `/date` | Сегодняшняя дата | `📅 Сегодня 24.07.2026` |
| `/random` | Случайное число | `🎲 Выпало число: 57` |
| `/weather Москва` | Погода в городе | `🌍 Москва, RU 🌡 +25°C 💨 3 м/с` |

---

## 🚀 Быстрый старт

### Предварительные требования

- **Python 3.8** или выше
- **pip** (менеджер пакетов Python)
- **Токен Telegram бота** (получить у [@BotFather](https://t.me/BotFather))
- **API ключ OpenWeatherMap** (опционально, для реальной погоды)

### Установка

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/your-username/telegram-helper-bot.git
cd telegram-helper-bot

# 2. Создайте виртуальное окружение
python -m venv venv

# 3. Активируйте виртуальное окружение
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate

# 4. Установите зависимости
pip install -r requirements.txt