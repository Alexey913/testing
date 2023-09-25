# Вам нужно написать тест с использованием моков для класса,
# который выполняет HTTP-запросы.
# Условие: У вас есть класс HttpClient с методом
# public String get(String url), который выполняет
# HTTP-запрос и возвращает результат.
# Вам необходимо проверить правильность работы класса WebService,
# который использует HttpClient для получения данных с веб-сайта.

class HttpClient:
    def get(url: str) -> str:
        ...
        return 'Результат запроса'
    
class WebService:
    def __init__(self, http_client: HttpClient) -> None:
        self._http_client = http_client
    
    @property
    def http_client(self):
        return self._http_client
    
    def get_request(self, url: str):
        self._http_client.get(url)
        
