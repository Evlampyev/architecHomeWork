# Посетитель (Visitor)
# Поведенческий паттерн проектирования, который описывает операцию,
# выполняемую с каждым объектом из некоторой структуры.
# Паттерн посетитель позволяет определить новую операцию,
# не изменяя классы этих объектов.
# Посетитель — это Команда

class FruitVisitor():
    """Посетитель"""

    def draw(self, fruit):
        methods = {  # methods - это словарь, где тип фрукта - ключ, а self.... - значение
            Apple: self.draw_apple,
            Pear: self.draw_pear,
        }
        draw = methods.get(type(fruit), self.draw_unknown)  # метод get - вызывает значение по ключю, ключ указывается
                                                            # типом (классом), для неизвестных ключей вызывается draw_unknown
        draw(fruit)

    def draw_apple(self, fruit):
        print('Яблоко')

    def draw_pear(self, fruit):
        print('Груша')

    def draw_unknown(self, fruit):
        print('Фрукт')


class Fruit(object):
    """Фрукты"""

    def draw(self, visitor):
        visitor.draw(self)


class Apple(Fruit):
    """Яблоко"""
    pass


class Pear(Fruit):
    """Груша"""
    pass


class Banana(Fruit):
    """Банан"""
    pass


if __name__ == '__main__':
    visitor = FruitVisitor()

    apple = Apple()
    apple.draw(visitor)
    # Яблоко

    pear = Pear()
    pear.draw(visitor)
    # Груша

    banana = Banana()
    banana.draw(visitor)
    # Фрукт
