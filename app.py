import json
import requests
import datetime

def get_helsinki_weather():
    api_url = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=60.192059&lon=24.945831'
    # send user info to the api to get access to the data
    headers = {
        'User-Agent': 'weather-report-app github.com/weather-report-app'
    }
    response = requests.get(api_url, headers=headers)
    
    if response.status_code == 200:
        weather_data = response.json()
        # pretty the JSON response
        print(json.dumps(weather_data, indent=4))
    else:
        print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
        
def get_dates():
    today = datetime.date.today()
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    day_after_tomorrow = datetime.date.today() + datetime.timedelta(days=2)
    
    days = [str(today), str(tomorrow), str(day_after_tomorrow)]
    return days
    
if __name__ == "__main__":
    get_helsinki_weather()
    print(get_dates())