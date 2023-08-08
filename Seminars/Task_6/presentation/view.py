"""Запуск приложения и
управление товараи в интернет магазинке"""
from Seminars.Task_6.data.fileProductRepository import FileProductRepository
from Seminars.Task_6.data.inMemoryProductRepository import InMemoryProductRepository
from Seminars.Task_6.domain.product import Product


def view(product_repository):
    product1 = Product(1, "Смартфон", 499)
    product2 = Product(2, "Ноутбук", 899)
    product_repository.add_product(product1)
    product_repository.add_product(product2)

    ## Получаем и выводим список всех товаров
    products = product_repository.get_all_products()
    for product in products:
        print(f"Товар: {product.name}. Цена: {product.price} руб.")