import unittest
from unittest.mock import Mock
from unittest.mock import patch
from task_2_card import PaymentForm
from task_3_weather import WeatherReporter
from task_4_hotel import BookingService

# Создайте объект класса `PaymentForm`, передайте ему мок-объект в качестве аргумента.
# 6. Вызовите метод `pay()` и убедитесь, что мок-объект вызывает метод `charge()`
class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.payment_form = PaymentForm(Mock())

    def test_pay_calls_charge(self):
        self.payment_form.pay(54.9)
        self.payment_form.credit_card.charge.assert_called_once()


class TestWeather(unittest.TestCase):
    def setUp(self) -> None:
        with patch('task_3_weather.WeatherService') as mock_service:
            self.weather_report = WeatherReporter(mock_service)

    def test_weather(self):
        self.weather_report.generate_report()
        self.weather_report.weather_service.get_current_temperature.assert_called()

class TestHotel(unittest.TestCase):

    @patch('task_4_hotel.HotelService')
    def test_booking(self, mock_booking):
        self.booking_service = BookingService(mock_booking)
        room_id = 8
        self.booking_service.book_room(room_id)
        self.booking_service.hotel_service.is_room_available.assert_called_once_with(room_id)

if __name__ == '__main__':
    unittest.main()