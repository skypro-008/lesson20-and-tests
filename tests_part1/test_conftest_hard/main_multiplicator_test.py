# фаил c тестами № 2
# Основной текст задания находится в файле main_summer_test.py
#
from functools import reduce

# Исходная функция:
def multiplicator(*args):
    return reduce(lambda x, y: x*y, args)


# TODO здесь необходимо сделать рефакторинг
incoming_list = [1, "2", 10, "20", 1, 5, 3 ,8]


def test_multiplicator(list_creator):
    # TODO напишите тест здесь
    pass