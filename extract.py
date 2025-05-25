import requests
import logging

logging.basicConfig(level=logging.INFO)

def extract_weather_data(city="Cairo"):
    url = f"http://api.weatherapi.com/v1/current.json?key=da97b518669e4ee4ae5113321252505&q={city}"
    response = requests.get(url)
    response.raise_for_status()  # Raises error if not 200
    logging.info("✅ Weather data extracted.")
    return response.json()
