# Создайте два класса: Person и Bank. Класс Person должен иметь метод transfer_money,
# который позволяет перевести деньги в Bank.
# Класс Bank должен иметь метод receive_money.
# Напишите тесты, проверяющие корректность взаимодействия этих классов.
import pytest


class Person:
    def __init__(self, balance: int) -> None:
        self.balance = balance

    def add_money(self, money: int) -> None:
        self.balance += money

    def transfer_money(self, money: int) -> int:
        if self.balance > money:
            self.balance -= money
            return money
        else:
            raise ValueError('Недостаточно средств')


class Bank:
    def __init__(self, sum_money: int, list_of_persons: list) -> None:
        self.sum_money = sum_money
        self.list_of_person = list_of_persons

    def recieve_money(self, money: int, person: Person) -> None:
        if person in self.list_of_person:
            self.sum_money += person.transfer_money(money)
        else:
            raise ValueError('Пользователя не существует')


@pytest.fixture
def setup():
    person_1 = Person(100)
    person_2 = Person(200)
    bank = Bank(1000, [person_1])
    return person_1, person_2, bank


def test_transfer_money(setup):
    person_1, person_2, bank = setup
    # тест 1
    # assert person_1.balance == 100
    
    # тест 2
    # bank.recieve_money(50, person_1)
    # assert bank.sum_money == 1050 and person_1.balance == 50
    
    # тест 3
    # with pytest.raises(ValueError):
    #     assert person_1.transfer_money(200)

    # тест 4
    with pytest.raises(ValueError):
        assert bank.recieve_money(100, person_1)

    # еще по хорошему добавить условие перевода отрицательной суммы

if __name__ == "__main__":
    pytest.main(['-v'])
