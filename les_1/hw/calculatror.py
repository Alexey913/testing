# В классе Calculator создайте метод calculateDiscount,
# который принимает сумму покупки и процент скидки
# и возвращает сумму с учетом скидки.
# Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
# Если метод calculateDiscount получает недопустимые аргументы,
# он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения.

class Calculator():

    def __new__(cls):
        instance = super().__new__(cls)
        return instance

    def addition(num_1: float, num_2: float) -> float:
        return num_1 + num_2

    def difference(num_1: float, num_2: float) -> float:
        return num_1 - num_2

    def multiplicate(num_1: float, num_2: float) -> float:
        return num_1 * num_2

    def division(num_1: float, num_2: float) -> float:
        if num_2 == 0:
            raise ArithmeticError('На 0 делить нельзя')
        return num_1 / num_2

    def calculate_discount(sum_of_buy: float | int, percent_discount: float | int) -> float:
        if not isinstance(sum_of_buy, int | float) or not isinstance(percent_discount, int | float):
            raise ArithmeticError('Неверный формат ввода')
        return sum_of_buy - sum_of_buy * percent_discount / 100


if __name__ == "__main__":
    result = Calculator.addition(5, 2)
    print(result)
    buy_sum = Calculator.calculate_discount(888, 15)
    print(buy_sum)
