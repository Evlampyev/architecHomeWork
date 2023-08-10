from abc import ABC, abstractmethod


class UserInterface(ABC):
    @abstractmethod
    def iremove_book(self):
        """Пользовательский интерфейс для получения id книги для удаления"""
        pass

    @abstractmethod
    def iadd_book(self):
        """Пользовательский интерфейс для добавления новой книги"""
        pass

    @abstractmethod
    def iprint_all_books(self):
        """Пользовательский интерфейс для вывода списка всех книг"""
        pass
