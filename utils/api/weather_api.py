import requests
import json

from config_data.config import API_WEATHER_KEY, API_WEATHER_BASE_URL


def weather_api_request(mode, query):
    match mode:
        case 'search':
            suffix = 'geo/1.0/direct'
            url = f'{API_WEATHER_BASE_URL}{suffix}'
            params = {'q': query, 
                      'limit': 1, 
                      'appid': API_WEATHER_KEY, 
                      'lang': 'ru'}
        case 'get':
            suffix = 'data/2.5/weather'
            url = f'{API_WEATHER_BASE_URL}{suffix}'
            params = {'lat': query[0], 
                      'lon': query[1], 
                      'appid': API_WEATHER_KEY,
                      'units': 'metric',
                      'lang': 'ru'}

    response = requests.get(url, params)

    if response.status_code == 200:
        raw_data = json.loads(response.text)
        match mode:
            case 'search':
                try:
                    data = (raw_data[0]['lat'], 
                            raw_data[0]['lon'])
                except IndexError:
                    return None
                
            case 'get':
                tem_b = raw_data['main']['temp']
                tem_f = raw_data['main']['feels_like']
                wea = raw_data['weather'][0]['description']
                wind = raw_data['wind']['speed']
                atm = raw_data['main']['pressure']

                data = f"Температура воздуха {tem_b:.0f} градусов (ощущается как {tem_f:.0f}). "\
                       f"{wea.capitalize()}. Скорость ветра - {int(wind):.0f} м/с. "\
                       f"Атмосферное давление - {atm * 0.75:.0f} мм.рт.ст"
        return data
    else:
        return None
