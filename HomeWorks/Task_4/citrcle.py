from math import pi
from shape import Shape
from correctinut import CorrectInput


class Circle(Shape):
    """Круг \n
    :param радиус"""
    __radius: float

    def __init__(self):
        self.__radius = self.getParametres()

    def __str__(self):
        return f'Круг, r={self.__radius}'

    def getParametres(self):
        result = False
        while not result:
            radius = int(input('Введите радиус круга: '))
            result = CorrectInput(radius).allFigureParametresInputCorrect()
            if not result:
                print("Не корректный ввод, значения должны быть больше 0")
        return radius
    def getArea(self) -> float:
        """Площадь круга"""
        return pi * self.__radius ** 2

    def getPerimeter(self) -> float:
        """Длина окружности"""
        return 2 * pi * self.__radius

    @staticmethod
    def nameClass():
        return 'Круг'
