# Задание
# У вас есть класс BookService, который использует интерфейс BookRepository для получения информации о книгах из базы данных.
# Ваша задача написать unit-тесты для BookService, используя Mockito для создания мок-объекта BookRepository.

import unittest
from unittest.mock import Mock
from unittest.mock import patch

from book_service import BookService


class TestBookService(unittest.TestCase):
    def setUp(self) -> None:
        self.book_service = BookService(Mock())

    def test_book_query(self):
        sql = 'title'
        self.book_service.get_info(sql)
        self.book_service.book_query.get_book.assert_called_once_with(sql)


class TestBookServicePatch(unittest.TestCase):
    @patch('book_service.BookService')
    def test_book_query(self, mock_book_service):
        self.book_service = BookService(mock_book_service)
        self.book_service.get_info('title')
        self.book_service.book_query.get_book.assert_called_once()


if __name__ == '__main__':
    unittest.main()
