class BookCase:

    def __init__(self):
        self.books = []
        self.book_ids = set()

    def __add__(self, other):
        id = 1
        while id in self.book_ids:
            id += 1
        other.id = id
        self.book_ids.add(id)
        self.books.append(other)

    def __len__(self):
        return len(self.books)

    def get_books(self):
        return self.books

    def __str__(self):
        result = ""
        for book in self.books:
            result += book.__str__() + '\n'
        return result

    def __delitem__(self, key):
        for book in self.books:
            if book.id == key:
                delit_book = book
                break
        self.book_ids.remove(delit_book.id)
        self.books.remove(delit_book)
