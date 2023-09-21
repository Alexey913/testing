from abc import ABC, abstractmethod

from book_query import BookQuery


class BookRepository(ABC):

    @abstractmethod
    def get_info(self, book_query: BookQuery):
        ...
