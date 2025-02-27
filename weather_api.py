import requests


def get_weather(lat=50.4501, lon=30.5234):  # Координати Києва
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    response = requests.get(url)
    data = response.json()
    return data["current_weather"]["temperature"], data["current_weather"]["weathercode"]


temperature, weather_code = get_weather()
print(f"Температура: {temperature}°C, Код погоди: {weather_code}")
