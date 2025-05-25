import requests

def test_api_response():
    url = "http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=Cairo"
    response = requests.get(url)
    assert response.status_code == 200
    print("✅ API test passed")
