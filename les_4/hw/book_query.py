from book import Book


class BookQuery:
    def get_book(self, sql: str) -> Book:
        # Имитация логики получения экземпляра книги
        book = Book(title=sql,
                    author=sql,
                    year_publication=2020,
                    genre=sql)
        return book
