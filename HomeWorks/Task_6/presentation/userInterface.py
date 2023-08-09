from abc import ABC
class UserInterface(ABC):
    def iremove_book(self):
        """Пользовательский интерфейс для получения id книги для удаления"""
        pass
    def iadd_book(self):
        """Пользовательский интерфейс для добавления новой книги"""
        pass
    def iprint_all_books(self):
        """Пользовательский интерфейс для вывода списка всех книг"""
        pass
