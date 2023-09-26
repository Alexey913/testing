# Напишите функцию для поиска среднего значения в списке чисел
# и соответствующие юниттесты с использованием фреймворка pytest.

# Модифицируйте функцию find_average так, чтобы она вызывала исключение TypeError,
# если ей передается не список.
# Напишите тест, который проверяет вызов этого исключения

import pytest

def find_average(numbers: list[float|int]) -> float:
    if type(numbers) != list:
        raise TypeError('Неверный формат входных данных')
    if len(numbers) == 0:
        return 0.0
    return sum(numbers) / len(numbers)

def test_find_average():
    lst = [1, 2, 3, 4, 5]
    assert find_average(lst) == 3

def test_find_average_empty_list():
    assert find_average([]) == 0

def test_find_average_one_element():
    assert find_average([2]) == 2

def test_find_average_error():
    with pytest.raises(TypeError):
        assert find_average(2)

if __name__ == "__main__":
    pytest.main(['-v'])
