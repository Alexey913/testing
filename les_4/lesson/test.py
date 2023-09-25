import unittest
from unittest.mock import Mock
from unittest.mock import patch
from task_2_card import PaymentForm
from task_3_weather import WeatherReporter
from task_4_hotel import BookingService
from task_5_message import NotificationService
from task_6_db import DataProcessor
from task_7_http import WebService

# Создайте объект класса `PaymentForm`, передайте ему мок-объект в качестве аргумента.
# Вызовите метод `pay()` и убедитесь, что мок-объект вызывает метод `charge()`


class TestCard(unittest.TestCase):
    def setUp(self) -> None:
        self.payment_form = PaymentForm(Mock())

    def test_pay_calls_charge(self):
        self.payment_form.pay(54.9)
        self.payment_form.credit_card.charge.assert_called_once()

# Вам нужно протестировать другой класс, WeatherReporter, который использует WeatherService.
# Создайте мок-объект для WeatherService с использованием Mockito.


class TestWeather(unittest.TestCase):
    def setUp(self) -> None:
        with patch('task_3_weather.WeatherService') as mock_service:
            self.weather_report = WeatherReporter(mock_service)

    def test_weather(self):
        self.weather_report.generate_report()
        self.weather_report.weather_service.get_current_temperature.assert_called()

# Вам необходимо проверить правильность работы класса BookingService, который
# использует HotelService для бронирования номера, если он доступен.


class TestHotel(unittest.TestCase):
    @patch('task_4_hotel.HotelService')
    def test_booking(self, mock_booking):
        self.booking_service = BookingService(mock_booking)
        room_id = 8
        self.booking_service.book_room(room_id)
        self.booking_service.hotel_service.is_room_available.assert_called_once_with(
            room_id)

# Вам необходимо проверить правильность работы класса NotificationService,
# который использует MessageService для отправки уведомлений.


class TestMessage(unittest.TestCase):
    @patch('task_5_message.MessageService')
    def test_sending(self, mock_sending):
        self.notification_service = NotificationService(mock_sending)
        self.notification_service.sending()
        self.notification_service.message_service.send_message.assert_called_once()

# Вам необходимо проверить правильность работы класса DataProcessor,
# который использует Database для выполнения запроса и обработки результатов.


class TestDb(unittest.TestCase):
    def setUp(self) -> None:
        self.data_processor = DataProcessor(Mock())

    def testdata_base_query(self):
        self.data_processor.data_base_query('FROM table SELECT *')
        self.data_processor.db.query.assert_called_once_with(
            'FROM table SELECT *')

# Вам необходимо проверить правильность работы класса WebService,
# который использует HttpClient для получения данных с веб-сайта.

class TestHttp(unittest.TestCase):
    @patch('task_7_http.HttpClient')
    def test_get_request(self, mock_http_client):
        self.web_service = WebService(mock_http_client)
        url = 'https://www.ya.ru'
        self.web_service.get_request(url)
        self.web_service.http_client.get.assert_called_once_with(url)
        
if __name__ == '__main__':
    unittest.main()
