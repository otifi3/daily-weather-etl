from transform import transform_weather_data

def test_transform_sample():
    sample_input = {
        "location": {"name": "Cairo", "country": "Egypt"},
        "current": {
            "temp_c": 32.5,
            "humidity": 25,
            "wind_kph": 12,
            "condition": {"text": "Sunny"}
        }
    }
    df = transform_weather_data(sample_input)
    assert not df.empty
    assert "temperature_c" in df.columns
    print("✅ Transformation test passed")
