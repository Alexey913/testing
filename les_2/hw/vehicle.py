from abc import ABC, abstractmethod

class Vehicle(ABC):
    _company: str
    _model: str
    _year_release: int
    _num_wheels: int
    _speed: int

    @abstractmethod
    def test_drive(self):
        ...

    @abstractmethod
    def park(self):
        ...
