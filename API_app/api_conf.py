import requests

from config_data.config import API_BASE_URL, API_DICT_KEY


def api_request(endpoint: str, params={}) -> requests.Response:
    params['key'] = API_DICT_KEY
    return requests.get(f'{API_BASE_URL}/{endpoint}', params=params)


def get_langs():
    response = api_request('getLangs');
    return response.json()


def lookup(lang: str, text: str, ui: str = 'ru'):
    response = api_request('lookup', params={
        'lang': lang,
        'text': text,
        'ui': ui
    })

    return response.json().get('def', {})


class LookupResult():
    def __init__(self, dictionary) -> None:
        if isinstance(dictionary, list):
            self.object = dictionary[0].get("text")
            if isinstance(dictionary[0].get("tr"), list):
                self.translate = [dct["text"] for dct in dictionary[0].get("tr")]
    
    def __str__(self) -> str:
        return f'{self.object} -> {self.translate}.'