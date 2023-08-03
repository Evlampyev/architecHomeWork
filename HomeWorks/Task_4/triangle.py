from math import sqrt
from shape import Shape
from correctinut import CorrectInput


class Triangle(Shape):
    """Треугольник \n
    :param три стороны"""
    __side1: float
    __side2: float
    __side3: float

    def __init__(self):
        sides = self.getParametres()
        self.__side1 = sides[0]
        self.__side2 = sides[1]
        self.__side3 = sides[2]

    def __str__(self):
        return f"Треугольник, a={self.__side1}, b={self.__side2}, c={self.__side3}"

    def getParametres(self):
        result = False
        sides = []
        while not result:
            sides.append(int(input('Сторона a треугольника: ')))
            sides.append(int(input('Сторона b треугольника: ')))
            sides.append(int(input('Сторона c треугольника: ')))
            result = CorrectInput(*sides).allFigureParametresInputCorrect()
            if not result:
                print("Не корректный ввод, значения должны быть больше 0")
                sides = []
            trianglResult = CorrectInput(*sides).triangleParametresInputCorrect()
            if not trianglResult:
                print("Не корректный ввод. Треугольника с такими сторонами не существует")
                sides = []
                result = False
        return sides

    def getArea(self) -> float:
        s = (self.__side1 + self.__side2 + self.__side3) / 2
        return sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))

    def getPerimeter(self) -> float:
        return self.__side1 + self.__side2 + self.__side3

    @staticmethod
    def nameClass():
        return 'Треугольник'
