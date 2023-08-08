from Seminars.Task_6.data.productRepository import ProductRepository
from Seminars.Task_6.domain.product import Product


class FileProductRepository(ProductRepository):
    """Класс предоставляет реализацию интерфейса productRepository,
    использую файл для хранения данных"""

    def __init__(self, file_path):
        """Создает новый экземпляр класса
        :param file_path имя файла"""
        self.file_path = file_path

    def get_all_products(self):
        products = []
        try:
            with open(self.file_path, 'r') as f:
                for line in f:
                    lin = line.split()
                    product = Product(lin[0], lin[1], lin[2])
                    products.append(product)
        except IOError:
            print("Такого файла не существует")
        return products

    def add_product(self, product):
        try:
            with open(self.file_path, 'r') as old_f:
                old_data = old_f.read()
        except IOError:

            old_data = ""
        try:
            with open(self.file_path, 'w') as new_f:
                line = str(product.id) + " " + str(product.name) \
                       + " " + str(product.price) + "\n"
                new_f.write(old_data + line)
        except IOError:
            print("Ошибка с записью в файл")

    def get_product_by_id(self, id):
        products = self.get_all_products()
        for product in products:
            if product.id == id:
                return product
        return None
