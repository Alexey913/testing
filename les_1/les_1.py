from math import sqrt
from datetime import datetime

# Задачи 1-2


def square_root(num: float) -> float:
    # ручное тестирование в функции
    # assert isinstance(num, int | float), "Необходимо ввести число"
    # assert num > 0, "Число не должно быть отрицательным"
    return sqrt(num)


def test_square_root_positive() -> float:
    assert square_root(25) == 5, "Тест с положительными числами провален"


def test_square_root_zero():
    assert square_root(0) == 0, "Тест с нулевым значением провален"


def test_square_root_negative():
    try:
        square_root(-10)
    except ValueError:
        print('Тест на отрицательнре значение завершен')

# Задача 4


def happy_NY():
    current_date = datetime.now()
    new_year_day = datetime(year=2024, month=1, day=1,
                            hour=0, minute=0, microsecond=0)
    assert current_date >= new_year_day, '2024 год еще не наступил'


if __name__ == '__main__':
    # print(square_root(10))
    # print(square_root(2.5))
    test_square_root_positive()
    test_square_root_zero()
    test_square_root_negative()
    happy_NY()
