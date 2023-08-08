class Product:
    """Создает новый экземпляра класса Product
    @param id идентификатор товара
    @parameter name название товара
    @param price цена товара"""

    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

# Геттеры и сеттеры

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def set_id(self, id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price
