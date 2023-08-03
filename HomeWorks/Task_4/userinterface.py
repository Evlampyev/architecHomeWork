from citrcle import Circle
from triangle import Triangle
from rectangle import Rectangle


class UserInterFace:
    def __init__(self):
        print('Начнём')
        print("1. Круг")
        print("2. Прямоугольник")
        print("3. Треугольник")
        print("0. Выход")
        while (number := input('Ваш выбор: ')) != 0:
            match number:
                case '1':
                    figure = Circle()
                case '2':
                    figure = Rectangle()
                case '3':
                    figure = Triangle()
                case '0':
                    exit()
            print(f" -- {figure} -- \nПлощадь фигуры: {figure.getArea():5.3f}")
            print(f"Периметр фигуры: {figure.getPerimeter():5.3f}")
