import requests
import json

from config_data.config import API_GIF_KEY, API_GIF_BASE_URL


def gif_api_request(mode, query, offset):
    url = f'{API_GIF_BASE_URL}{mode}'
    querystring = {'api_key': API_GIF_KEY, 
              'q': query, 
              'limit': '1', 
              'offset': offset, 
              'rating': 'r', 
              'lang': 'ru', 
              'bundle': 'messaging_non_clips'}

    response = requests.get(url, querystring)

    if response.status_code == 200:
        raw_data = json.loads(response.text)
        try:
            gif_url = raw_data['data'][0]['images']['original']['url']
            return gif_url
        except (IndexError, KeyError):
            return None
    else:
        return None
