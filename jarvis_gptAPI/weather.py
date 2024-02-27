# api from www.weatherapi.com :  68c3bfbcc0c5462caaa165341242702
# url = http://api.weatherapi.com/v1/current.json?key=68c3bfbcc0c5462caaa165341242702&q=darbhanga

import requests
from config import weatherAPI_key

def get_weather_report(location):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": weatherAPI_key,
        "q": location
    }

    weather_report = {}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if "error" in data:
            print(f"Error: {data['error']['message']}")
        else:
            weather_report['Temprature'] = current_condition['temp_c']
            weather_report['Condition'] = current_condition['condition']['text']
            weather_report['Wind Speed'] = current_condition['wind_kph']
            weather_report['Pressure'] = current_condition['pressure_mb']

            # print(weather_report)
            return weather_report

    except requests.RequestException as e:
        print(f"Request failed: {e}")

