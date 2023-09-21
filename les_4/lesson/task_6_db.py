# Вам требуется протестировать класс, который обрабатывает
# запросы к базе данных.
# Условие: У вас есть класс Database с методом
# public List<String> query(String sql),
# который выполняет SQLзапрос и возвращает результат.
# Вам необходимо проверить правильность работы класса
# DataProcessor, который использует Database для
# выполнения запроса и обработки результатов.

class DataBase:
    def query(self, sql: str) -> list[str]:
        ...
        return ['Результат', 'запроса']

class DataProcessor:
    def __init__(self, db: DataBase) -> None:
        self._db = db

    @property
    def db(self):
        return self._db

    def data_base_query(self, sql: str):
        self._db.query(sql)
        return "Операция выполнена успешно"
