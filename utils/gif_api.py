import requests
import json

from config_data.config import API_GIF_KEY, API_BASE_URL


def api_request(mode, query, offset):
    params_search = {'api_key': API_GIF_KEY, 'q': query, 'limit': '1', 'offset': offset, 'rating': 'r', 'lang': 'ru', 'bundle': 'messaging_non_clips'}
    params_random = {'api_key': API_GIF_KEY, 'tag': query, 'rating': 'r'}
    url = f'{API_BASE_URL}{mode}'

    response = requests.get(url, params_search if mode == 'search' else params_random)

    if response.status_code == 200:
        raw_data = json.loads(response.text)
        try:
            gif_url = raw_data['data'][0]['images']['original']['url']
        except (IndexError, KeyError):
            try:
                gif_url = raw_data['data']['images']['original']['url']
            except TypeError:
                return None
        return gif_url
    else:
        return None
