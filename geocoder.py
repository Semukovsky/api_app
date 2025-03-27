import requests

API_KEY = "a38cc5bc-54e0-44a2-bba9-568082c91a2e"


def geocode(address):
    # Собираем запрос для геокодера.
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": API_KEY,
        "geocode": address,
        "format": "json",
    }

    response = requests.get(geocoder_request, params=geocoder_params)

    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()
    else:
        raise RuntimeError(
            f"""Ошибка выполнения запроса:
            {geocoder_request}
            Http статус: {response.status_code} ({response.reason})""")

    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"] if features else None


midle = (44.534370, 48.757662)


# Получаем координаты объекта по его адресу.
def get_coordinates(address):
    toponym = geocode(address)
    if not toponym:
        return None, None

    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    return float(toponym_longitude), float(toponym_lattitude)


# Находим ближайшие к заданной точке объекты заданного типа.
def get_nearest_object(point, kind):
    ll = "{0},{1}".format(point[0], point[1])
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        "apikey": API_KEY,
        "geocode": ll,
        "format": "json"}
    if kind:
        geocoder_params['kind'] = kind
    response = requests.get(geocoder_request, params=geocoder_params)
    if not response:
        raise RuntimeError(
            f"""Ошибка выполнения запроса:
            {geocoder_request}
            Http статус: {response.status_code,} ({response.reason})""")

    json_response = response.json()

    features = json_response["response"]["GeoObjectCollection"]["featureMember"]
    return features[0]["GeoObject"]["name"] if features else None


def get_address(address):
    toponym = geocode(address)
    return toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']


def get_index(address):
    toponym = geocode(address)
    try:
        area = toponym['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']
        return area['Locality']['Thoroughfare']['Premise']['PostalCode']['PostalCodeNumber']
    except Exception as e:
        return None


def reversed_geocode(coords):
    try:
        geocode_request = "http://geocode-maps.yandex.ru/1.x/"
        params = {
            'apikey': API_KEY,
            'format': 'json',
            'geocode': ','.join(map(str, coords))
        }
        response = requests.get(geocode_request, params=params)
        toponym = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
        address = toponym['metaDataProperty']['GeocoderMetaData']['Address']['formatted']
        return address
    except Exception as e:
        return None
