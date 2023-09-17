from vehicle import Vehicle

class Car(Vehicle):

    def __init__(self, company: str, model: str, year_release: int) -> None:
        self._company = company
        self._model = model
        self._year_release = year_release
        self._num_wheels = 4
        self._speed = 0

    def test_drive(self):
        self._speed = 60

    def park(self):
        self._speed = 0

    @property
    def company(self):
        return self._company
    
    @property
    def model(self):
        return self._model

    @property
    def year_relesse(self):
        return self._year_release

    @property
    def num_wheels(self):
        return self._num_wheels
    
    @property
    def speed(self):
        return self._speed
    
    def __str__(self) -> str:
        return f'Автомобиль {self.company} {self.model}'

if __name__ == "__main__":
    a = Car('Hyundai', 'Sorais', 2010)
    print(a)
    print(a.num_wheels)