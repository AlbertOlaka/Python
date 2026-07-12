def city_country(city_name, country):
    """Return a city name and it's country
    Args:
        city_name (str): the cities name.
        city_country (str): thry city country.
    Returns:
        str: return a string formatted like "Santiago, Chile"
    """
    formatted_city = f"{city_name}, {country}"
    return formatted_city.title()

city = city_country('santiago', 'chile')
print(city)

city = city_country('porto', 'portugal')
print(city)

city = city_country('nairobi', 'kenya')
print(city)