import requests

API_KEY = 'abd4899fcccc951f8b4b5c5da07e025a'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather(city):
    params = {
        "q": city,
        "appid":API_KEY,
        "units":"metric"
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def parse_weather(data):
    city = data['name']
    temperature = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    return{
        "city": city,
        "temperature": temperature,
        "description": description,
        "humidity": humidity,
        "wind_speed": wind_speed
    }

# Example
city = 'Medellin'
weather_data = fetch_weather(city)
if weather_data:
    parse_weather(weather_data)