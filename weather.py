import requests
import argparse

def draw_header():
    print("''''''       '' ''''")
    print("''''            ''''")
    print("'''  ''    ''")
    print("'''   '' ''")
    print("'''     ''")
    print("")
    print("''''''''''''''''''''''''''''''''''''''''''")
    print("'''      WEATHER APP BY        '''")
    print("''''''''''''''''''''''''''''''''''''''''''")
    print("")

def get_weather_icon(description):
    description = description.lower()
    if "clear" in description:
        return "☀️"
    elif "cloud" in description:
        return "☁️"
    elif "rain" in description:
        return "🌧️"
    elif "snow" in description:
        return "❄️"
    elif "storm" in description or "thunder" in description:
        return "⛈️"
    elif "mist" in description or "fog" in description:
        return "🌫️"
    else:
        return "🌈"

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    print("''''''''''''''''''''''''''''''''''''''''''")
    if response.status_code == 200:
        weather_desc = data['weather'][0]['description']
        icon = get_weather_icon(weather_desc)

        print(f"'''  City       : {city_name.capitalize():<20}     '''")
        print(f"'''  Temp       : {data['main']['temp']}°C{' ' * (22 - len(str(data['main']['temp'])))}'''")
        print(f"'''  Condition  : {weather_desc.title():<20} {icon}  '''")
        print(f"'''  Humidity   : {data['main']['humidity']}%{' ' * (22 - len(str(data['main']['humidity'])))}'''")
        print(f"'''  Wind Speed : {data['wind']['speed']} m/s{' ' * (18 - len(str(data['wind']['speed'])))}'''")
    else:
        print(f"'''  Error: {data.get('message', 'Failed to get data'): <33}'''")
    print("''''''''''''''''''''''''''''''''''''''''''")

# Replace this with your actual API key
API_KEY = "ce171131c4091bf7d88c3309169cc094"

# Parse command-line arguments
parser = argparse.ArgumentParser(description="ASCII Weather App - Zeeshan")
parser.add_argument("--city", help="Enter your city name", required=True)
args = parser.parse_args()

# Run the app
draw_header()
get_weather(args.city, API_KEY)
