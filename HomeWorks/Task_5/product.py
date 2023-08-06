class Product:
    """Продукт"""
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_product_id(self):
        """Получить номер продукта"""
        return self.product_id

    def get_name(self):
        """Получить название продукта"""
        return self.name

    def get_price(self):
        """Получить цену продукта"""
        return self.price
