from book import Book
from books_view_model import BooksViewModel

books = [Book("Властелин колец"), Book("1984"), Book("Убить пересмешника")]

view_model = BooksViewModel(books)
view_model.get_displayable_books()

while (data := input("Введите номер книги, "
                     "чтобы отметить её как прочитанную, или exit - для выхода ")) != 'exit':

    try:
        book_id = int(data) - 1
        view_model.mark_book_as_read(book_id)
    except Exception:
        print("Не верный ввод")
    finally:
        view_model.get_displayable_books()
