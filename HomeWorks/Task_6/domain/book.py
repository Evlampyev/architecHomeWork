class Book:
    """Класс, представляющий книгу"""

    def __init__(self, id, title, author, price, ):
        self.id = id
        self.title = title
        self.author = author
        self.price = price

    def get_id(self):
        """получение id  книги
        :return id"""
        return self.id

    def get_title(self):
        """Получение названия книги
        :return title название"""
        return self.title

    def __eq__(self, other):
        return self.author == other.author \
            and self.title == other.title

    def get_author(self):
        """Получение автора книги
        :return author автор"""
        return self.author

    def get_price(self):
        """Получение стоимости книги
        :return price стоимость"""
        return self.price

    def __str__(self):
        return f"Id = {self.id}, Книга: {self.get_title()}, " \
               f"Автор: {self.get_author()}, Цена: $ {self.get_price()}"

    def set_price(self, price):
        """Установка стоимости книги \n
        :param price стоимость"""
        self.price = price

    def __lt__(self, other):
        """Метод для сравнения двух книг, \n
        сортируются по цене"""
        return self.price < other.price
