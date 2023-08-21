class Book:

    def __init__(self, title, author, year, pages, borrow=False):
        """Новая книга в библиотеке \n
        :param title, author, year, pages"""
        self.id = 0
        self.title = title
        self.author = author
        self.publish_year = year
        self.pages = pages
        self.borrow = borrow  # книга читают (True - на руках, False - в библиотеке)

    def __str__(self):
        return (f"Id={self.id}, Title: {self.title}, "
                f"Author: {self.author}, borrowed={self.borrow}")

    def dump(self):
        return {"BooksList": {'id': self.id,
                              'title': self.title,
                              'author': self.author,
                              'borrowed': self.borrow}}
