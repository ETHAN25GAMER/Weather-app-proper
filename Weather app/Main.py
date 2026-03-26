import requests
from datetime import datetime

def get_weather(city: str):
    url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1'
    response = requests.get(url).json()  # ✅ added .json()

    if not response.get('results'):      # ✅ use response not data
        print('Put a real city name!')
        return
    
    result = response["results"][0]      # ✅ use response not data
    lat = result["latitude"]
    lon = result["longitude"]
    name = result["name"]
    country = result["country"]

    weather_url = (f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current=temperature_2m,weathercode,windspeed_10m"
        f"&daily=temperature_2m_max,temperature_2m_min"
        f"&forecast_days=3&timezone=auto")
    
    weather = requests.get(weather_url).json()  # ✅ added .json()
    current = weather['current']                # ✅ use weather not response
    daily = weather['daily']

    print(f'Weather in {name}, {country}')      # ✅ added spaces
    print(f'Current temp: {current["temperature_2m"]} Degree Celsius')  # ✅ fixed quotes
    print(f'Wind Speed: {current["windspeed_10m"]} km/h')               # ✅ fixed quotes

    if current['temperature_2m'] > 25:          # ✅ added current[...]
        print('Its hot asf out here')
    else:                                        # ✅ fixed elseif → else, added colon
        print('Thas calm shi')

    print(f'\n3-Day Forecast:')
    for i in range(3):
        date = daily["time"][i]
        hi = daily["temperature_2m_max"][i]
        lo = daily["temperature_2m_min"][i]
        print(f'  {date}  High: {hi}°C  Low: {lo}°C')

    print()

def main():
    print('Welcome to this weather shit')
    print('Type a city name to get the zaa temp or "quit" to go bye bye')
    while True:
        city = input('Enter city:').strip()
        if city.lower() == 'quit':
            print("Goodbye! 👋")
            break
        if city:
            get_weather(city)

if __name__ == "__main__":
    main()