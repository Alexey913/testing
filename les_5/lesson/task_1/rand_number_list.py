# Создайте два модуля. Первый модуль генерирует список случайных чисел.
# Второй модуль находит максимальное число в этом списке. 
# Вам нужно сначала написать юнит-тесты для каждого модуля,
# затем написать интеграционный тест, который проверяет,
# что оба модуля работают вместе правильно

from random import randint

def rand_number_list(quantity_elem: int):
    return [randint(-quantity_elem, quantity_elem) for _ in range(quantity_elem)]