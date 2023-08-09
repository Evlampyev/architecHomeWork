from HomeWorks.Task_6.data.iBookRepository import IBookRepository
from HomeWorks.Task_6.domain.book import Book


class InMemoryBookStore(IBookRepository):

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def book_in_books(self, new_book):
        books = self.get_all_books()
        if new_book in books:
            return True
        else:
            return False

    def remove_book(self, del_book):
        if self.book_in_books(del_book):
            self.books.remove(del_book)

    def get_all_books(self) -> list:
        return self.books

    def __len__(self):
        return len(self.books)

    def get_book_by_id(self, id):
        books = self.get_all_books()
        for book in books:
            if book.id == id:
                result = book
        if result is not None:
            return result
        else:
            print("Такого id не обнаружено")
