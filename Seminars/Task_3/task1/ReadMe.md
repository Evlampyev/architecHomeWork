Принцип единственной ответственности

__Исходные данные__

    class Book:
        def __init__(self, title, author):
            self.title = title
            self.author = author
    
        # Геттеры
        def get_title(self):
            return self.title
    
        def get_author(self):
            return self.author
    
        def save(self):
            print(f"Сохранение информации о книге '{self.title}' в базе данных.")
    
        def print_book(self):
            print(f"Печать книги '{self.title}' автора '{self.author}'.")
    
    
    if __name__ == "__main__":
        book = Book("Властелин Колец", "Толкин")
        book.save()
        book.print_book()