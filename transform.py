import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def transform_weather_data(raw_data):
    df = pd.DataFrame([{
        "city": raw_data["location"]["name"],
        "country": raw_data["location"]["country"],
        "temperature_c": raw_data["current"]["temp_c"],
        "humidity": raw_data["current"]["humidity"],
        "wind_kph": raw_data["current"]["wind_kph"],
        "condition": raw_data["current"]["condition"]["text"]
    }])
    logging.info("✅ Weather data transformed.")
    return df
