class Book:

    def __init__(self, title: str, author: str, year_publication: int, genre: str) -> None:
        self._title = title
        self._author = author
        self._year_publication = year_publication
        self._genre = genre

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year_publication(self):
        return self._year_publication

    @property
    def genre(self):
        return self._genre
