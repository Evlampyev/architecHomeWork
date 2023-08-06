# паттерн Domain Model (Модель предметной области)

from customer import Customer
from order import Order
from product import Product

customer = Customer(1, "Петров А.В.")
prod1 = Product(1, 'Мобила', 15000)
prod2 = Product(2, 'Точила', 30000)

order = Order(1)
order.add_product(prod1)
order.add_product(prod2)

customer.add_order(order)

order2 = Order(2)
order2.add_product(prod2)
customer.add_order(order2)

print("Клиент:" + customer.get_name())
print('Заказы:')
for customer_order in customer.get_orders():
    print("Заказ №" + str(customer_order.get_order_id()))
    print("  Товары: ")
    for product in customer_order.get_products():
        print("    - " + str(product.get_name()) + " (" + str(product.get_price()) + " руб.)")
    print()
