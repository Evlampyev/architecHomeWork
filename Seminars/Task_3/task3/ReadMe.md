## Принцип Барбары Лиски
## Поведение наследников не должно нарушать поведения родителей

__Исходные данные__

class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_area(self):
        return self.width * self.height


class Square(Rectangle):
    def set_width(self, width):
        super().set_width(width)
        super().set_height(width)

    def set_height(self, height):
        super().set_width(height)
        super().set_height(height)


if __name__ == "__main__":
    rect = Square()
    rect.set_width(5)
    rect.set_height(10)
    print(rect.get_area())  # выводит 50
_____________________