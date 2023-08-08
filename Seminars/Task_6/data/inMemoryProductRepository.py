from Seminars.Task_6.data.productRepository import ProductRepository


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        self.products = []

    def get_all_products(self):
        return self.products

    def get_product_by_id(self):
        return self.products.get(id)

    def add_product(self, product):
        self.products.append(product)
