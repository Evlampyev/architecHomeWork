import operator
from abc import ABC


class Sorting(ABC):
    """Интерфейс методов сортировки списка книг"""

    def by_author(books: list) -> list:
        """Сортировка по автору книги по алфавиту"""
        for i in range(len(books) - 1):
            for j in range(i + 1, len(books)):
                if books[i].get_author() > books[j].get_author():
                    books[i], books[j] = books[j], books[i]
        return books

    def by_author_reverse(books: list) -> list:
        """Сортировка по автору по убыванию"""
        pass

    def by_price(books: list) -> list:
        """Сортировка по цене по возрастанию"""
        return sorted(books, key=operator.attrgetter('price'))

    def by_price_reverse(books: list) -> list:
        """Сортировка по цене по убыванию"""
        return sorted(books, key=operator.attrgetter('price'), reverse=True)
