# метод evenOddNumber, который проверяет, является ли переданное число четным или нечетным

def even_odd_number(number: int | float) -> bool:
    return True if number % 2 == 0 else False

# метод numberInInterval, который проверяет, попадает ли переданное число в интервал (25;100)

def number_in_interval(number: int | float) -> bool:
    return True if 25 < number < 100 else False