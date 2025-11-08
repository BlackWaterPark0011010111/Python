import json
import datetime
from weather_data import weather_json

#десериализация JSON
try:
    weather_data = json.loads(weather_json)
except json.JSONDecodeError:
    print("Ошибка при загрузке JSON")
    exit()

#извлекаем нужные данные
lon = weather_data["coord"]["lon"]
lat = weather_data["coord"]["lat"]
weather_description = weather_data["weather"][0]["description"]
temperature_kelvin = weather_data["main"]["temp"]
wind_speed = weather_data["wind"]["speed"]
sunrise_timestamp = weather_data["sys"]["sunrise"]
sunset_timestamp = weather_data["sys"]["sunset"]

#температура в цельсии
temperature_celsius = round(temperature_kelvin - 273.15, 2)

#переводим время UNIX в читаемый формат
sunrise_time = datetime.datetime.fromtimestamp(sunrise_timestamp).strftime("%I:%M %p")
sunset_time = datetime.datetime.fromtimestamp(sunset_timestamp).strftime("%I:%M %p")

#рассчитать продолжительность светового дня
daylight_duration = sunset_timestamp - sunrise_timestamp
hours = daylight_duration // 3600
minutes = (daylight_duration % 3600) // 60

# cоздаём новый словарь
processed_data = {
    "Location": f"{lon}°E, {lat}°N",
    "Weather Description": weather_description.capitalize(),
    "Current Temperature": f"{temperature_celsius}°C",
    "Wind Speed": f"{wind_speed} m/s",
    "Sunrise": sunrise_time,
    "Sunset": sunset_time,
    "Duration of Daylight": f"{hours} hours {minutes} minutes"
}

#cериализуем обратно в JSON и сохраняем в файл
try:
    with open("src/processed_weather_data.json", "w") as file:
        json.dump(processed_data, file, indent=4)
except IOError:
    print("Ошибка при записи в файл")
    exit()

# 8. Выводим обработанную информацию в консоль
print("\nProcessed Weather Data:")
for key, value in processed_data.items():
    print(f"{key}: {value}")
