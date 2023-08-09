from HomeWorks.Task_6.data.iBookSorting import Sorting
from HomeWorks.Task_6.domain.book import Book


class Views:
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
        # self.print_all_books(book_store)

        # удаляем третью и снова выводим
        # book_store.remove_book(book3)
        # self.print_all_books(book_store)
        print("---- \n"
              "1 - добавить книгу в БД, \n"
              "2 - удалить книгу из БД \n"
              "3 - вывести список всех книг в БД \n"
              "4 - выход \n")
        act = input("Что делаем? ")
        while act != '4':
            match act:
                case '1':
                    self.iadd_book()
                case '2':
                    self.iremove_book()
                case '3':
                    self.iprint_all_books()
                case _:
                    print("Неверный ввод")
            act = input("Что делаем? ")

    def iremove_book(self):
        self.iprint_all_books()
        remove_id = int(input('Введите id книги, которую хотите удалить'))
        book = self.book_store.get_book_by_id(remove_id)
        self.book_store.remove_book(book)
        print(f"Книга с id = {remove_id} удалена")


    def iadd_book(self):
        print('---Добавление книги---')
        id = int(input('Введите id книги: '))
        title = input("Введите название книги: ")
        author = input("Введите автора: ")
        price = float(input("Цена книги: "))
        book = Book(id, title, author, price)
        self.book_store.add_book(book)

    def iprint_all_books(self):
        all_books = self.choose_sorting(self.book_store.get_all_books())
        print("------------------------- \n     Список всех книг:")
        for book in all_books:
            print(book)
        print(f'В базе {len(self.book_store)} книг(и)')

    @staticmethod
    def choose_sorting(all_books):
        sort = int(input("--Сортировать:--\n"
                         "1 - не сортировать, \n"
                         "2 - по алфавиту, \n"
                         "3 - сортировать по цене по возрастанию: \n"
                         "4 - сортировать по цене убыванию: \n... "))
        if sort == 2:
            all_books = Sorting.by_author(all_books)
        elif sort == 3:
            all_books = Sorting.by_price(all_books)
        elif sort == 4:
            all_books = Sorting.by_price_reverse(all_books)
        return all_books
