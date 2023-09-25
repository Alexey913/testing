from book_repository import BookRepository
from book import Book
from book_query import BookQuery


class BookService(BookRepository):

    def __init__(self, book_query: BookQuery) -> None:
        self._book_query = book_query

    @property
    def book_query(self):
        return self._book_query

    def get_info(self, sql: str) -> str:
        book = self._book_query.get_book(sql)
        return f'{book.title}\n\
                 {book.author}\n\
                 {book.genre}\n\
                 {book.year_publication}'
