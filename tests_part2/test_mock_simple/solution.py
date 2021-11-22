import requests
import os
import requests
from unittest.mock import MagicMock

class AdressGetter:
    def get_cities(city):
        response = requests.get(f'https://give_me_adress.com?search={city}')
        return response.data
    
    def show_cities(self):           # Необходимо протестировать этот метод
        cities = self.get_cities()   # Здесь происходить вызов стороннего сервиса
        cities = ", ".join(cities)
        return f"Расположение офисов: {cities}."


def test_show_cities():
    adressgetter = AdressGetter()
    adressgetter.get_cities = MagicMock(return_value=["Санкт-Петербург", "Самара", "Краснодар"])
    expected_string = "Расположение офисов: Санкт-Петербург, Самара, Краснодар."
    assert adressgetter.show_cities() == expected_string

if __name__=="__main__":
    os.system("pytest")