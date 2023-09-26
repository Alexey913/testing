# Напишите функцию multiply(a, b), которая возвращает произведение a и b.
# Затем напишите параметризованный тест, который проверяет эту функцию
# на нескольких наборах данных.
import pytest

def multiply(a: int, b: int) -> int:
    return a * b

@pytest.mark.parametrize('a, b, result', [
                                          (2, 3, 6),
                                          (1, 1, 1),
                                          (0, 2, 0),
                                          (-1, 2, -2),
                                          (-4, -4, 16)
                                          ])
def test_multiply(a, b, result):
    assert multiply(a, b) == result

if __name__ == "__main__":
    pytest.main(['-v'])