def recommend_outfit(temperature, weather_description):
    if temperature < 0:
        return "Рекомендується теплий одяг: пальто, шапка, шарф, рукавички."
    elif 0 <= temperature < 10:
        return "Рекомендується одягати куртку, светр та закрите взуття."
    elif 10 <= temperature < 20:
        return "Рекомендується легка куртка або светр."
    else:
        return "Рекомендується легкий одяг: футболка, шорти."
