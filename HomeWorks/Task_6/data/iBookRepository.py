from abc import ABC, abstractmethod


class IBookRepository(ABC):
    """Абстрактный интерфейс для работы с БД"""

    @abstractmethod
    def add_book(self, book):
        """Добавление новой книги в БД
        :param book книга"""
        pass

    @abstractmethod
    def remove_book(self, book):
        """Удаление книги из БД
        :param book книга"""
        pass

    @abstractmethod
    def get_all_books(self):
        """Получение списка всех книг
        :return список книг"""
        pass

    @abstractmethod
    def book_in_books(self, book):
        """Проверяет наличии книги в БД
        :return boolean"""
        pass

    @abstractmethod
    def __len__(self):
        """Определяет количество книг в БД /n
        :return int"""
        pass
    def get_book_by_id(self):
        """Возвращает книгу по id"""
        pass