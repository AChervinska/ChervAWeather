import tkinter as tk
# Імпортуємо функцію get_weather з файлу weather_api.py
from weather_api import get_weather
# Імпортуємо функцію recommend_outfit з файлу recommendation.py
from recommendation import recommend_outfit


def get_weather_description(weather_code):
    # Створюємо функцію для перетворення коду погоди на опис
    weather_descriptions = {
        0: "Ясне небо",
        1: "Майже ясне небо",
        2: "Невеликий дощ",
        3: "Сильний дощ",
        45: "Туман",
        # Додайте інші коди за потреби
    }
    return weather_descriptions.get(weather_code, "Невідоме погодне явище")


def show_recommendation():
    temperature, weather_code = get_weather()  # Отримуємо температуру і код погоди
    weather_description = get_weather_description(
        weather_code)  # Перетворюємо код погоди на опис
    # Викликаємо функцію з recommendation.py
    recommendation = recommend_outfit(temperature, weather_description)
    result_label.config(text=f"Температура: {temperature}°C\n"
                             f"Погода: {weather_description}\n\n"
                             f"Рекомендація: {recommendation}")


# Створення вікна
root = tk.Tk()
root.title("Рекомендація одягу за погодою")

# Додавання кнопки та мітки
get_recommendation_button = tk.Button(
    root, text="Отримати рекомендацію", command=show_recommendation)
get_recommendation_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Запуск GUI
root.mainloop()
