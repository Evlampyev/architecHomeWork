from shape import Shape
from correctinut import CorrectInput


class Rectangle(Shape):
    """Прямоугольник \n
    :param ширина и длина"""
    __length: float
    __width: float

    def __init__(self):
        length, width = self.getParametres()
        self.__length = length
        self.__width = width

    def __str__(self):
        return f"Прямоугольник, длина={self.__length}, ширина={self.__width}"

    def getParametres(self):
        result = False
        while not result:
            len = int(input("Длина прямоугольника: "))
            wid = int(input("Ширина прямоугольника: "))
            result = CorrectInput(len, wid).allFigureParametresInputCorrect()
            if not result:
                print("Не корректный ввод, значения должны быть больше 0")
        return len, wid

    def getArea(self) -> float:
        return self.__length * self.__width

    def getPerimeter(self) -> float:
        return 2 * (self.__length + self.__width)

    @staticmethod
    def nameClass():
        return 'Прямоугольник'
