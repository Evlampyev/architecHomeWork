from Seminars.Task_6.data.fileProductRepository import FileProductRepository
from Seminars.Task_6.data.inMemoryProductRepository import InMemoryProductRepository
from Seminars.Task_6.presentation.view import view

data = int(input("1 - В памяти список; 2 - в файле данные: ..."))
if data == 1:
    product_repository = InMemoryProductRepository()
else:
    file_path = 'products.dat'
    product_repository = FileProductRepository(file_path)

view(product_repository)
