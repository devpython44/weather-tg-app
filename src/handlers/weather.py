"""
Обработчик команды /weather.
Получает реальную погоду через OpenWeatherMap API.
Если API ключ не задан, использует демо-режим с имитацией данных.
"""

import requests
from src.config import WEATHER_API_KEY


def register_weather_handler(bot):
    """Регистрирует обработчик команды /weather."""
    
    @bot.message_handler(commands=['weather'])
    def weather_command(message):
        """
        Обрабатывает команду /weather.
        Извлекает название города и получает погоду.
        """
        # Извлекаем название города из сообщения
        parts = message.text.split(maxsplit=1)
        
        # Проверяем, указан ли город
        if len(parts) < 2:
            bot.send_message(
                message.chat.id,
                "Пожалуйста, укажите город.\n"
                "Пример: /weather Киев"
            )
            return
        
        city = parts[1].strip()
        
        # Отправляем индикатор набора текста, пока получаем данные
        bot.send_chat_action(message.chat.id, 'typing')
        
        # Получаем данные о погоде
        weather_text = get_weather(city)
        bot.send_message(message.chat.id, weather_text)


def get_weather(city):
    """
    Получает данные о погоде для указанного города.
    
    Если задан WEATHER_API_KEY, использует реальное API OpenWeatherMap.
    Иначе работает в демо-режиме с имитацией данных.
    """
    if WEATHER_API_KEY:
        return get_real_weather(city)
    else:
        return get_demo_weather(city)


def get_real_weather(city):
    """
    Получает реальные данные о погоде через OpenWeatherMap API.
    
    API: https://openweathermap.org/current
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": WEATHER_API_KEY,
        "units": "metric",  # Температура в градусах Цельсия
        "lang": "ru"        # Описание на русском языке
    }
    
    try:
        response = requests.get(base_url, params=params, timeout=10)
        data = response.json()
        
        if response.status_code == 200:
            city_name = data["name"]
            country = data.get("sys", {}).get("country", "")
            temp = round(data["main"]["temp"])
            feels_like = round(data["main"]["feels_like"])
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            description = data["weather"][0]["description"].capitalize()
            
            weather_text = (
                f"{city_name}, {country}\n"
                f"{description}\n"
                f"Температура: {temp}°C (ощущается как {feels_like}°C)\n"
                f"Влажность: {humidity}%\n"
                f"Ветер: {wind_speed} м/с"
            )
            return weather_text
            
        elif response.status_code == 404:
            return f"Город «{city}» не найден. Проверьте название."
        elif response.status_code == 401:
            return "Ошибка авторизации API. Проверьте WEATHER_API_KEY."
        else:
            return f"Ошибка получения погоды. Код: {response.status_code}"
            
    except requests.exceptions.Timeout:
        return "Превышено время ожидания ответа от сервера погоды."
    except requests.exceptions.ConnectionError:
        return "Ошибка подключения к серверу погоды. Проверьте интернет."
    except Exception as e:
        return f"Неизвестная ошибка: {str(e)}"


def get_demo_weather(city):
    """
    Демо-режим: имитирует данные о погоде для тестирования.
    Используется, когда не задан WEATHER_API_KEY.
    """
    import random
    
    temp = random.randint(15, 35)
    wind = random.randint(1, 10)
    humidity = random.randint(30, 90)
    
    weather_text = (
        f"{city} (демо-режим)\n"
        f"Температура: +{temp}°C\n"
        f"Влажность: {humidity}%\n"
        f"Ветер: {wind} м/с\n\n"
        "Добавьте WEATHER_API_KEY в .env для реальных данных."
    )
    return weather_text