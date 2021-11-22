import sys
from pathlib import Path
import os
import unittest
import test_types

project_name = Path(os.path.abspath(__file__)).parent.parent.parent.name
cwd = Path.cwd()
parts = cwd.parts
basefolder_index = parts.index(project_name)
basepath = Path(*parts[:basefolder_index + 1])
sys.path.append(str(basepath))
from ttools.skyprotests.tests import SkyproTestCase  # noqa: E402

def summer_returns_int(*args):
    return 0

def summer_returns_str(*args):
    return "qwe"

def divider_returns_int(a , b):
    return 0

def divider_returns_str(*args):
    return "qwe"


class DecorTestCase(SkyproTestCase):
    def setUp(self):
        self.testfunc_sum = test_types.test_summer
        self.testfunc_devider = test_types.test_divider
    
    # def test_sum_selfcheck(self):
    #     test_types.divider = summer_returns_int
    #     with self.assertRaises(AssertionError,
    #         msg="%@Проверяют ли Ваше тесты что функция summer возвращает тип Int когда следует"):
    #         self.testfunc_sum()

    # def test_one_selfcheck(self):
    #     test_types.divider = zero_divider
    #     with self.assertRaises(AssertionError,
    #         msg="%@Проверьте что Ваш тест проверяет второе условие задания"):
    #         self.testfunc_big_number()

    # def test_many_selfcheck(self):
    #     test_simple.divider = error_check_divider
    #     with self.assertRaises(AssertionError,
    #         msg="%@Проверьте что Ваш тест проверяет второе условие задания"):
    #         self.testfunc_one_arg()


if __name__ == "__main__":
    unittest.main()