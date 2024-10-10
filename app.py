import json
import requests

def get_helsinki_weather():
    api_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.192059&lon=24.945831'
    headers = {
        'User-Agent': 'weather-report-app github.com/weather-report-app'  # Custom user-agent header with contact info
    }
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        weather_data = response.json()  # Parse the response as JSON
        print(json.dumps(weather_data, indent=4))  # Pretty-print the JSON response
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")

if __name__ == "__main__":
    get_helsinki_weather()