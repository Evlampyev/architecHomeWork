import sys

from HomeWorks.Task_6.domain.book import Book
from HomeWorks.Task_6.presentation.iValidate import IValidate
from HomeWorks.Task_6.presentation.sortingService import SortingService
from HomeWorks.Task_6.presentation.userInterface import UserInterface


class Views(UserInterface):
    def __init__(self, book_store):
        self.book_store = book_store
        # Добавляем книги в магазин
        book1 = Book(1, "Clean Code", "Robert C. Martin", 34.99)
        book2 = Book(2, "Effective Java", "Joshua Bloch", 29.99)
        book3 = Book(3, "Изучаем Python", "Марк Лутц", 21.98)
        book4 = Book(4, "Снежная королева", "Ганс Х. Андерсон", 34.00)

        self.book_store.add_book(book1)
        book_store.add_book(book2)
        book_store.add_book(book3)
        book_store.add_book(book4)

        # Получаем список всех книг
        # self.iprint_all_books()

        # удаляем третью и снова выводим
        print('Я удалил книгу с id=3')
        book_store.remove_book(book3)
        # self.iprint_all_books()
        print("---- \n"
              "1 - добавить книгу в БД, \n"
              "2 - удалить книгу из БД \n"
              "3 - вывести список всех книг в БД \n"
              "4 - выход \n")
        act = input("Что делаем? ")
        while True:
            match act:
                case '1':
                    self.iadd_book()
                case '2':
                    self.iremove_book()
                case '3':
                    self.iprint_all_books()
                case '4':
                    sys.exit()
                case _:
                    print("Неверный ввод")
            act = input("Что делаем? ")

    def iremove_book(self):

        self.iprint_all_books()
        remove_id = int(input('Введите id книги, которую хотите удалить: '))
        book = self.book_store.get_book_by_id(remove_id)
        if book == None:
            print("Такого id не обнаружено")
        else:
            self.book_store.remove_book(book)
            print(f"Книга с id = {remove_id} удалена")

    def iadd_book(self):
        """Пользовательский интерфейс для добавления новой книги"""
        print('---Добавление книги---')
        while True:
            id = int(input('Введите id книги: '))
            if IValidate.id_valid(self.book_store.get_book_by_id(id)):
                break
            else:
                print("Такой id уже есть в БД")

        title = input("Введите название книги: ")
        while True:
            author = input("Введите автора: ")
            if IValidate.author_valid(author):
                break
            else:
                print("Должно быть два-три слова с заглавной буквы")

        price = float(input("Цена книги: "))
        book = Book(id, title, author, price)
        self.book_store.add_book(book)

    def iprint_all_books(self):
        """Пользовательский интерфейс для вывода списка всех книг"""
        all_books = SortingService.coose_sorting(self.book_store.get_all_books())
        print("------------------------- \n     Список всех книг:")
        for book in all_books:
            print(book)
        print(f'В базе {len(self.book_store)} книг(и)')
