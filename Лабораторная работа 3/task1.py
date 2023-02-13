class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name  # инициализируем защищенный атрибут
        self._author = author  # инициализируем защищенный атрибут

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author


book = Book("Букварь", "")  # внутри класса обращаемся к защищенному атрибуту
print(book.name)  # вызов getter свойства

book = Book("", "Пушкин")
print(book.author)


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц в книге."""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количество страниц в книге."""
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


book = PaperBook("", "", 500)
print(book.pages)  # вызываем как атрибут, но срабатывает метод
book.pages = 700  # присваиваем значение атрибуту, но срабатывает метод
print(book.pages)


# def __repr__(self) -> str:
# return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.pages!r})'

class AudioBook(Book):

    def __init__(self, name: str, author: str, duration: int):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self) -> float:
        """Возвращает число продолжительности в книге."""
        return self._duration

    @duration.setter
    def duration(self, new_duration: float) -> None:
        """Устанавливает число продолжительности в книге."""
        if not isinstance(new_duration, int):
            raise TypeError("Число минут должно быть типа float")
        if new_duration <= 0:
            raise ValueError("Число минут должно быть положительным числом")
        self._duration = new_duration


book = AudioBook("", "", 1200)
print(book.duration)  # вызываем как атрибут, но срабатывает метод
book.duration = 1000  # присваиваем значение атрибуту, но срабатывает метод
print(book.duration)

# def __repr__(self) -> str:
# return f'{self.__class__.__name__}({self.name!r}, {self.author!r}, {self.duration!r})'
