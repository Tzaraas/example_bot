import requests
import json

from config_data.config import API_COUNTRY_BASE_URL


def country_api_request(query):
    url = f'{API_COUNTRY_BASE_URL}{query}'
    params = {'fields': 'name,subregion,capital,currencies'}

    response = requests.get(url, params)

    if response.status_code == 200:
        raw_data = json.loads(response.text)

        name = raw_data[0]['name']['common']
        for val in raw_data[0]['name']['nativeName'].values():
              local_name = val["common"]
        region = raw_data[0]['subregion']
        capital = raw_data[0]['capital'][0]
        for val in raw_data[0]['currencies'].values():
            cur_name = val['name']
            cur_sym = val['symbol']

        data = f"{name} (местное название {local_name}), страна в регионе {region}. "\
                f"Столица - {capital}. Валюта - {cur_name} [{cur_sym}]."

        return data
    else:
        return None