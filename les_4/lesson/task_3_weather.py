# Предположим, у вас есть класс WeatherService, который имеет метод getCurrentTemperature(), 
# обращающийся к внешнему API для получения информации о текущей температуре. 
# Вам нужно протестировать другой класс, WeatherReporter, который использует WeatherService. 
# Создайте мок-объект для WeatherService с использованием Mockito.

from random import randint


class WeatherService:
    def get_current_temperature(self) -> int:
        return randint(-40, 40)
    
class WeatherReporter:
    def __init__(self, weather_service: WeatherService) -> None:
        self._weather_service = weather_service

    @property
    def weather_service(self):
        return self._weather_service
    
    def generate_report(self):
        return self._weather_service.get_current_temperature()
