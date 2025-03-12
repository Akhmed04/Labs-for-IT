class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        return self._name

    @property
    def autor(self) -> str:
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Подкласс БумажнаяКнига. Родительский класс Книга """
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        return self._pages

    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [Name: {self.name!r}, Autor: {self.autor!r}, Pages: {self.pages}]"


class AudioBook(Book):
    """Подкласс АудиоКнига. Родительский класс Книга """
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        return self._duration

    def __repr__(self):
        return f"{self.__class__.__name__} [Name: {self.name!r}, Autor: {self.autor!r}, Pages: {self.duration}]"