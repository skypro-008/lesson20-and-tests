from unittest.mock import MagicMock
import requests

class AdressGetter:
    def get_cities(city):
        response = requests.get(f'https://give_me_adress.com?search={city}')
        return response.data


adressgetter = AdressGetter()

adressgetter.get_cities = MagicMock(return_value=['Cамара, Краснодар, Нинжекамск'])
breakpoint()
pass