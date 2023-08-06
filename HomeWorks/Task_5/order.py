class Order:
    """Заказ"""
    def __init__(self, order_id):
        self.order_id = order_id
        self.products = []

    def get_products(self):
        """Получить список продуктов в заказе"""
        return self.products

    def add_product(self, product):
        """Добавить продукт в заказ"""
        self.products.append(product)

    def get_order_id(self):
        """Получить номер заказа"""
        return self.order_id