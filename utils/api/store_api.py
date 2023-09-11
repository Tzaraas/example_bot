import requests
import json

from config_data.config import API_STORE_KEY, API_STORE_BASE_URL


def store_api_request(method, mode, query):

    suffix = 'geo/1.0/direct'
    url = f'{API_STORE_BASE_URL}{suffix}'
    params = {'q': query, 
                'limit': 1, 
                'appid': API_STORE_KEY, 
                'lang': 'ru'}

    response = requests.request(method, url, params)

    if response.status_code == 200:
        raw_data = json.loads(response.text)
        data = raw_data
        return data
    else:
        return None