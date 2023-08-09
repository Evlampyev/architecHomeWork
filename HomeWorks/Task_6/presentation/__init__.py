from HomeWorks.Task_6.data.inMemoryBookStore import InMemoryBookStore
from HomeWorks.Task_6.domain.book import Book


def print_all_books(book_all):
    print("---------- \n     Список всех книг:")
    all_books = book_all.get_all_books()
    for book in all_books:
        print(book)
    print(f'В базе {len(book_all)} книг(и)')


book_store = InMemoryBookStore()
# Добавляем книги в магазин
book1 = Book(1, "Clean Code", "Robert C. Martin", 34.99)
book2 = Book(2, "Effective Java", "Joshua Bloch", 29.99)
book3 = Book(3, "Изучаем Python", "Марк Лутц", 21.98)

book_store.add_book(book1)
book_store.add_book(book2)
book_store.add_book(book3)

# Получаем список всех книг
print_all_books(book_store)

# удаляем третью и снова выводим
book_store.remove_book(book3)
print_all_books(book_store)
