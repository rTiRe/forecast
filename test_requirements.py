"""Test on local weather host."""

from os import environ
import json
import pytest
import requests
from dotenv import load_dotenv

TEST_COORDINATES = (
    (55.0, 55.0),
)
load_dotenv()
YANDEX_URL = 'https://api.weather.yandex.ru/v2/informers/?lat={1}&lon={2}'
LOCAL_URL = 'http://127.0.0.1:8000/'
OK = 200
KEY = environ.get('YANDEX_KEY')
headers = {'x-Yandex-API-Key': KEY}


def check_weather(coordinates: tuple[float]) -> bool:
    yandex_response = requests.get(YANDEX_URL.format(*coordinates), headers=headers, timeout=5)
    local_response = requests.get(LOCAL_URL.format(*coordinates), timeout=5)
    if yandex_response == OK and local_response == OK:
        yandex_weather = json.loads(yandex_response.content)
        local_weather = json.loads(local_response.content)
        if local_weather == yandex_weather['forecast']['parts'][0]:
            return True


@pytest.mark.parametrize('coordinates', TEST_COORDINATES)
def test_weather(coordinates: tuple):
    assert check_weather(coordinates)
