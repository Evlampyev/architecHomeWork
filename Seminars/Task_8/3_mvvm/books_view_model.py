class BooksViewModel:
    def __init__(self, books):
        self.books = books

    def get_displayable_books(self):
        for i in range(len(self.books)):
            print(f"{i + 1}. {self.books[i]}")

    def mark_book_as_read(self, index):
        self.books[index].mark_as_read()
