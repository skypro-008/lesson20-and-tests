import requests
import os
from unittest.mock import MagicMock
import requests
import pytest

# Класс, подлежащий тестированию
class AdressGetter:
    def get_cities(city):
        response = requests.get(f'https://give_me_adress.com?search={city}')
        return response.data
    
    # Необходимо протестировать этот метод
    def show_offices(self):
        cities = self.get_cities()
        cities = ", ".join(cities)
        return f"Расположение офисов: {cities}."
    
    # Необходимо протестировать этот метод
    def show_warehouses(self):
        cities = self.get_cities()
        cities = ", ".join(cities)
        return f"Расположение cкладов: {cities}."
    
    # Необходимо протестировать этот метод
    def show_markets(self):
        cities = self.get_cities()
        cities = ", ".join(cities)
        return f"Расположение магазинов: {cities}."

@pytest.fixture
def adressgetter():
	adressgetter = AdressGetter()
	adressgetter.get_cities = MagicMock(return_value=["Санкт-Петербург", "Самара", "Краснодар"])
	return adressgetter

def test_show_offices(adressgetter: AdressGetter):
    expected_string = "Расположение офисов: Санкт-Петербург, Самара, Краснодар."
    assert adressgetter.show_offices() == expected_string

def test_show_warehouses(adressgetter: AdressGetter):
    expected_string = "Расположение cкладов: Санкт-Петербург, Самара, Краснодар."
    assert adressgetter.show_warehouses() == expected_string

def test_show_markets(adressgetter: AdressGetter):
    expected_string = "Расположение магазинов: Санкт-Петербург, Самара, Краснодар."
    assert adressgetter.show_markets() == expected_string

if __name__=="__main__":
    os.system("pytest test_mock_fixture")
