# Вам нужно написать тест с использованием моков для сервиса отправки сообщений.
# Условие: У вас есть класс MessageService с методом
# public void sendMessage(String message, String recipient),
# который отправляет сообщение получателю.
# Вам необходимо проверить правильность работы класса NotificationService,
# который использует MessageService для отправки уведомлений.

class MessageService:
    def __init__(self, message: str, recipient: str) -> None:
        self._message = message
        self._recipient = recipient

    def send_message(self):
        ...
    
    @property
    def message(self):
        return self._message

    @property
    def recipient(self):
        return self._recipient
    
class NotificationService:
    def __init__(self, message_service: MessageService) -> None:
        self._message_service = message_service

    @property
    def message_service(self):
        return self._message_service
    
    def sending(self) -> None:
        self._message_service.send_message()
