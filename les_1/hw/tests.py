from calculatror import Calculator
from shop import Shop, Product

## Тестирование задания 1
print('Тестирование задания 1\n')
# Деление на 0
assert Calculator.division(10, 2) == 5, 'Ожидается 5'

# Подсчет суммы с учетом скидки
assert Calculator.calculate_discount(100, 5) == 95, 'Ожидается 95'

# Неверный формат ввода при подсчете скидки
try:
    Calculator.calculate_discount('number', 'number')
except ArithmeticError:
    print('Получено исключение при неверном формате ввода')
print('Тестирование задания 1 завершено без ошибок\n')



## Тестирование задания 2
print('Тестирование задания 2\n')
product_1 = Product('Chocolate', 100)
product_2 = Product('Milk', 70)
product_3 = Product('Cookies', 140)
product_4 = Product('Souce', 75)

products = []

shop = Shop(products)

shop.add(product_1)
shop.add(product_2)
shop.add(product_3)
shop.add(product_4)

assert product_1 > product_2
assert shop.get_most_expencive_product() == product_3
shop.sort_product_by_price()
assert shop == [product_2, product_4, product_1, product_3]
print('Тестирование задания 2 завершено без ошибок')