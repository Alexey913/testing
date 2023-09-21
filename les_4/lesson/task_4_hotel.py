# Вам необходимо написать тест с использованием моков для сервиса бронирования отелей.
# Условие: У вас есть класс HotelService с методом public boolean isRoomAvailable(int roomId), 
# который обычно проверяет, доступен ли номер в отеле. 
# Вам необходимо проверить правильность работы класса BookingService, который 
# использует HotelService для бронирования номера, если он доступен.

from random import choice

class HotelService:
    def is_room_available(self, room_id: int) -> bool:
        if room_id:
            return choice([True, False])

class BookingService:
    def __init__(self, hotel_service: HotelService) -> None:
        self._hotel_service = hotel_service

    @property
    def hotel_service(self):
        return self._hotel_service
    
    def book_room(self, room_id: int) -> str:
        if self._hotel_service.is_room_available(room_id):
            return 'Номер свободен'
        return 'Номер занят'