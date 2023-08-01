# Класс, представляющий калькулятор

class Addition():
    """Сложение"""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Сложение \n
        :param (a, b) \n
        :return a + b"""
        return a + b


class Subtraction:
    """Вычитание"""

    @staticmethod
    def substraction(a, b):
        return a - b


class Multiplication:
    """Умножение"""

    @staticmethod
    def multiplication(a, b):
        return a * b


class Division:
    """Деление"""

    @staticmethod
    def divide(a, b):
        if b == 0:
            ZeroDivisionError("Division by zero is not allowed.")
        else:
            return a / b


class Calculator:
    adder: Addition()
    subtractor: Subtraction()
    multiplier: Multiplication()
    divider: Division()

    def __init__(self, a, b, oper):
        self.adder = Addition()
        self.subtractor = Subtraction()
        self.multiplier = Multiplication()
        self.divider = Division()
        self.a = a
        self.b = b
        match oper:
            case '+':
                self.result = self.add()
            case '-':
                self.result = self.substract()
            case '*':
                self.result = self.multiply()
            case '/':
                self.result = self.divide()

    def add(self):
        return self.adder.add(self.a, self.b)

    def substract(self):
        return self.subtractor.substraction(self.a, self.b)

    def multiply(self):
        return self.multiplier.multiplication(self.a, self.b)

    def divide(self):
        return self.divider.divide(self.a, self.b)
