# Мы хотим улучшить функциональность нашего интернет-магазина.
# Ваша задача - добавить два новых метода в класс Shop:
# Метод sortProductsByprice, который сортирует список продуктов по стоимости.
# Метод getMostExpensiveProduct(), который возвращает самый дорогой продукт.

# Напишите тесты, чтобы проверить, что магазин хранит верный список продуктов
# (правильное количество продуктов, верное содержимое корзины).
# Напишите тесты для проверки корректности работы метода getMostExpensiveProduct.
# Напишите тесты для проверки корректности работы метода sortProductsByPrice
# (проверьте правильность сортировки).
# Используйте класс Product для создания
# экземпляров продуктов и класс Shop для написания методов сортировки и тестов.


class Product():

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
    
    def __eq__(self, other) -> bool: #равно ==
        if self.price == other.price:
            return True
        return False
    
    def __ne__(self, other) -> bool: #не равно !=
        if self.price != other.price:
            return True
        return False

    def __gt__(self, other) -> bool: # больше, >
        if self.price > other.price:
            return True
        return False

    def __ge__(self, other) -> bool: # не больше, меньше или равно, <=
        if self.price <= other.price:
            return True
        return False
    
    def __lt__(self, other) -> bool: # меньше, <
        if self.price < other.price:
            return True
        return False
    
    def __le__(self, other) -> bool: # не меньше, больше или равно, >=
        if self.price >= other.price:
            return True
        return False
    
    def __str__(self):
        return f'{self.name} - {self.price}'


class Shop():

    def __init__(self, list_product) -> None:
        self.list_product = list_product

    def add(self, product: Product) -> None:
        self.list_product.append(product)
    
    def sort_product_by_price(self):
        self.list_product.sort()

        
    def get_most_expencive_product(self):
        return max(self.list_product)
    
    def __str__(self):
        return "\n".join(f"=={prod}==" for prod in self.list_product)


if __name__ == "__main__":
    product_1 = Product('Chocolate', 100)
    product_2 = Product('Milk', 70)
    products = []
    shop = Shop(products)
    print(product_2)
    print(shop)