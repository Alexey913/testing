# Проект Vehicle. Написать следующие тесты с использованием JUnit5:
#  - Проверить, что экземпляр объекта Car также является экземпляром транспортного средства (используя # оператор instanceof).
#  - Проверить, что объект Car создается с 4-мя колесами.
#  - Проверить, что объект Motorcycle создается с 2-мя колесами.
#  - Проверить, что объект Car развивает скорость 60 в режиме тестового вождения (используя метод testDrive()).
#  - Проверить, что объект Motorcycle развивает скорость 75 в режиме тестового вождения (используя метод testDrive()).
#  - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта)
# машина останавливается (speed = 0).
#  - Проверить, что в режиме парковки (сначала testDrive, потом park, т.е. эмуляция движения транспорта)
# мотоцикл останавливается (speed = 0).

from vehicle import Vehicle
from car import Car
from motorcycle import Motorcycle
import unittest

class TestCar(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car('Hyundai', 'Sorais', 2010)
    
# - проверка того, что экземпляр объекта Car также является экземпляром транспортного средства; (instanceof)
    def test_type_car(self):
        self.assertIsInstance(self.car, Car, 'Тип автомобиля не соответсвует Car')
        self.assertIsInstance(self.car, Vehicle, 'Тип автомобиля не соответсвует Vehicle')

# - проверка того, объект Car создается с 4-мя колесами
    def test_num_wheels_car(self):
        self.assertEqual(self.car.num_wheels, 4, "Количество колес не равно 4")

# - проверка того, объект Car развивает скорость 60 в режиме тестового вождения (testDrive())
    def test_test_drive_car(self):
        self.car.test_drive()
        self.assertEqual(self.car.speed, 60, "Скорость автомсобиля не равна 60")

# - проверить, что в режиме парковки (сначала testDrive, потом park, т.е эмуляция движения транспорта) машина останавливается (speed = 0)
    def test_park_car(self):
        self.car.test_drive()
        self.car.park()
        self.assertEqual(self.car.speed, 0, "Скорость автомобиля не равна 0")


class TestMotorcycle(unittest.TestCase):

    def setUp(self) -> None:
        self.motorcycle = Motorcycle('Suzuki', 'gsx', 2014)
    
# - проверка того, что экземпляр объекта Motorcycle также является экземпляром транспортного средства; (instanceof)
    def test_type_moto(self):
        self.assertIsInstance(self.motorcycle, Motorcycle, 'Тип мотоцикла не соответсвует Motorcycle')
        self.assertIsInstance(self.motorcycle, Vehicle, 'Тип мотоцикла не соответсвует Vehicle')

# - проверка того, объект Motorcycle создается с 2-мя колесами
    def test_num_wheels_moto(self):
        self.assertEqual(self.motorcycle.num_wheels, 2, "Количество колес не равно 2")

# - проверка того, объект Motorcycle развивает скорость 75 в режиме тестового вождения (testDrive())
    def test_test_drive_moto(self):
        self.motorcycle.test_drive()
        self.assertEqual(self.motorcycle.speed, 75, "Скорость мотоцикла не равна 75")

# - проверить, что в режиме парковки (сначала testDrive, потом park  т.е эмуляция движения транспорта) мотоцикл останавливается (speed = 0)
    def test_park_moto(self):
        self.motorcycle.test_drive()
        self.motorcycle.park()
        self.assertEqual(self.motorcycle.speed, 0, "Скорость мотоцикла не равна 0")


if __name__ == "__main__":
    unittest.main()