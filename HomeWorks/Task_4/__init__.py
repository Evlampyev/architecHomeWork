# Главный класс приложения
# Пример использования конкретных классов геометрических фигур

from shape import Circle, Rectangle, Triangle, Shape

circle = Circle(5.0)
print(f" -- {circle} -- \nПлощадь окру: {circle.getArea():5.3f}")
print(f"Периметр круга: {circle.getPerimeter():5.3f}")

rectangle = Rectangle(4.0, 6.0)
print(f" -- {rectangle} --\nПлощадь прямоугольника: {rectangle.getArea():5.3f}")
print(f"Периметр прямоугольника: {rectangle.getPerimeter():5.3f}")

triangle = Triangle(3.0, 4.0, 5.0)
print(f" -- {triangle} -- \nПлощадь треугольника: {triangle.getArea():5.3f}")
print(f"Периметр треугольника: {triangle.getPerimeter():5.3f}")
