# Используя библиотеку Mockito, напишите модульные тесты для проверки функциональности формы
# оплаты на сайте. Вместо реальной кредитной карты используйте мок-объект.
# 1. Создайте класс `CreditCard` с методами `getCardNumber()`, `getCardHolder()`,
# `getExpiryDate()`, `getCvv()`, `charge(double amount)`.
# 2. Создайте класс `PaymentForm` с методом `pay(double amount)`.
# 3. В тестовом классе, создайте мок-объект для класса `CreditCard`.
# 4. Определите поведение мок-объекта с помощью метода `when()`.
# 5. Создайте объект класса `PaymentForm`, передайте ему мок-объект в качестве аргумента.
# 6. Вызовите метод `pay()` и убедитесь, что мок-объект вызывает метод `charge()`

class CreditCard():

    def __init__(self, card_number: str, card_holder: str, expiry_date: str, cvc: int) -> None:
        self._card_number = card_number
        self._card_holder = card_holder
        self._expiry_date = expiry_date
        self._cvc = cvc

    @property
    def card_number(self):
        return self._card_number
    
    @property
    def card_holder(self):
        return self._card_holder
    
    @property
    def expiry_date(self):
        return self._expiry_date
    
    @property
    def cvc(self):
        return self._cvc
    
    def charge(self, amount: float):
        return f'Оплата картой {self._card_number} на сумму {amount}'

class PaymentForm():
    def __init__(self, card: CreditCard) -> None:
        self._card = card

    @property
    def credit_card(self):
        return self._card
    
    def pay(self, amount: float) -> None:
        self._card.charge(amount)