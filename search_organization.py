import requests


API_KEY = '6fa239ed-b75f-492c-b144-1eeedfa573f7'


def search_by_coords(coords, address):
    right_coords = ','.join(map(str, coords))
    search_request = 'https://search-maps.yandex.ru/v1/'
    params = {
        'apikey': API_KEY,
        'text': address,
        'll': right_coords,
        "lang": "ru_RU",
        'rspn': 1,
        'spn': '0.01,0.01',
        'type': 'biz'
    }
    try:
        response = requests.get(search_request, params=params)
        toponym = response.json()["features"][0]
        return toponym
    except Exception as e:
        return None