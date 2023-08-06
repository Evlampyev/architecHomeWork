class Customer:
    """Покупатель"""
    def __init__(self, customer_id, name):
        self.customer_id = customer_id
        self.name = name
        self.orders = []

    def get_customer(self):
        """Получить id покупателя"""
        return self.customer_id

    def get_name(self):
        "Получить имя покупателя"
        return self.name

    def get_orders(self):
        """Получить список заказов покупателя"""
        return self.orders

    def add_order(self, order):
        """Добавить новый заказ"""
        self.orders.append(order)
