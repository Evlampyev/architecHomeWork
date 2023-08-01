# Класс для геометрических фигур

from math import pi, sqrt


class Shape:
    """Общие поля и методы для всех геометрических фигур"""

    def getArea(self) -> float:
        """Вычесление площади фигуры \n
        :return float"""
        pass

    def getPerimeter(self) -> float:
        """Вычисление периметра фигуры \n
        :return float"""
        pass


# Класс для круга
class Circle(Shape):
    """Круг \n
    :param радиус"""
    __radius: float

    def __init__(self, radius: float):
        self.__radius = radius

    def getArea(self) -> float:
        return pi * self.__radius ** 2

    def getPerimeter(self) -> float:
        return 2 * pi * self.__radius

    def __str__(self):
        return f'Круг, r={self.__radius}'


# Класс для прямоугольника

class Rectangle(Shape):
    """Прямоугольник \n
    :param ширина и длина"""
    __length: float
    __width: float

    def __init__(self, width: float, length: float):
        self.__width = width
        self.__length = length

    def getArea(self) -> float:
        return self.__length * self.__width

    def getPerimeter(self) -> float:
        return 2 * (self.__length + self.__width)

    def __str__(self):
        return f"Прямоугольник, длина={self.__length}, ширина={self.__width}"


# Класс для треугольника
class Triangle(Shape):
    """Треугольник \n
    :param три стороны"""
    __side1: float
    __side2: float
    __side3: float

    def __init__(self, side1: float, side2: float, side3: float):
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def getArea(self) -> float:
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def getPerimeter(self) -> float:
        return self.__side1 + self.__side2 + self.__side3

    def __str__(self):
        return f"Треугольник, a={self.__side1}, b={self.__side2}, c={self.__side3}"
