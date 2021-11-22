# В этом задании Вам предстоит сделать мок метода класса.
# Представим простой сценарий:
# У нас имеется класс AdressGetter один из методов которого,
# использует услуги платных сервисов с целью получения 
# списка предлагаемых адресов (в данном случае для упрощения - городов).
# К примеру, при запросе на сторонний сервис данная функция возвращает список вида:
# ["Санкт-Петербург", "Самара", "Краснодар"].
# Каждый раз обращаться к платным сервисам для 
# тестирования было бы мягко говоря не экономично.
#
# Вместе с тем, данным методом пользуется другой метод show_cities.
# Который, преобразовывет полученный список этот в строку вида:
# Расположение офисов: Санкт-Петербург, Самара, Краснодар.
# Попробуйте мокнуть метод get_adress класса AdressGetter, так чтобы
# show_cities работал корректно и получал необходимые ему данные.
# Для этого следуйте следующим шагам
#
# 1. В теле тестовой функции test_show_cities:
#    - Создайте экземпляр класса AdressGetter     
#    - Cделайте мок метода get_cities класса AdressGetter
#    - вызовите метод show_cities и проверьте ожидаемый результат
#
import requests
import os
from unittest.mock import MagicMock
import requests

# Класс, подлежащий тестированию
class AdressGetter:
    def get_cities(city):
        response = requests.get(f'https://give_me_adress.com?search={city}')
        return response.data
    
    # Необходимо протестировать этот метод
    def show_cities(self):
        cities = self.get_cities()
        cities = ", ".join(cities)
        return f"Расположение офисов: {cities}."


def test_show_cities():
    adressgetter = AdressGetter()
    adressgetter.get_cities = MagicMock(return_value=["Санкт-Петербург", "Самара", "Краснодар"])
    expected_string = "Расположение офисов: Санкт-Петербург, Самара, Краснодар."
    assert adressgetter.show_cities() == expected_string

if __name__=="__main__":
    os.system("pytest")
