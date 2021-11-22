import sys
from pathlib import Path
import os
import unittest

from requests.models import HTTPError
import test_mock
import requests

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402

class AdressGetter:
    def get_cities(city):
        response = requests.get(f'https://give_me_adress.com?search={city}')
        return response.data
    
    def show_cities(self):           # Необходимо протестировать этот метод
        cities = self.get_cities()   # Здесь происходить вызов стороннего сервиса
        cities = ", ".join(cities)
        return f"Расположение офисов: {cities}."


class RightAdressGetter(AdressGetter):
    def get_cities(self):           # Необходимо протестировать этот метод
        return ["Санкт-Петербург", "Самара", "Краснодар"]   # Здесь происходить вызов стороннего сервиса

class DecorTestCase(SkyproTestCase):
    def setUp(self):
        self.testfunc_sum = test_mock.test_show_cities
    
    def test_fail_selfcheck(self):
        try:
            self.testfunc_sum()
        except Exception:
            raise self.fail("%@Ваш тест вызвает ошибку. Сделали ли вы в своём тесте мок метода get_cities")


if __name__ == "__main__":
    unittest.main()