import pytest
from average import Average
from comparsion_average import ComparisonAverage

# Юнит-тесты для определения работы каждого класса (модуля) поотдельности

# Юнит-тесты для класса Average - тестируем функцию поиска среднего значения
# для граничных условий - список из целых чисел, не список, пустой список,
# список из 1 элемента


def test_average():
    lst = [1, 2, 3, 4, 5]
    assert Average(lst).avg() == 3


def test_average_not_list():
    with pytest.raises(TypeError):
        assert Average(2)


def test_average_empty_list():
    assert Average([]).avg() == 0


def test_average_one_element():
    assert Average([2]).avg() == 2

# Юнит-тесты для класса ComparsionAverage - тестируем взаимодействие классов,
# создаем три списка и тестируем три случая
# При этом тестируется полный функционал программы


@pytest.fixture
def setup():
    lst_1 = [1, 2, 3]
    lst_2 = [2, 4, 8, 10]
    lst_3 = [2, 6, 12, 3, 7]
    return lst_1, lst_2, lst_3


def test_comparsion_first_greater_second(setup):
    lst_2, lst_1, _ = setup
    comp = ComparisonAverage(lst_1, lst_2)
    assert comp.result() == 'Первый список имеет большее среднее значение'


def test_comparsion_first_less_second(setup):
    lst_1, lst_2, _ = setup
    comp = ComparisonAverage(lst_1, lst_2)
    assert comp.result() == 'Второй список имеет большее среднее значение'


def test_comparsion_first_equals_second(setup):
    _, lst_1, lst_2 = setup
    comp = ComparisonAverage(lst_1, lst_2)
    assert comp.result() == 'Средние значения равны'


if __name__ == "__main__":
    pytest.main(['-v'])
