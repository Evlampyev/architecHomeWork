# Класс "UserInterface"
from calculator import Calculator


class UserInterface:


    def start(self):
        num1 = self.getUserInput("Enter the first number: ")
        num2 = self.getUserInput("Enter the second number: ")
        operator = self.getOperator()
        result = self.performOperation(num1, num2, operator)
        self.displayResult(result)

    @staticmethod
    def getUserInput(message: str):
        return float(input(message))
        # Здесь можно реализовать логику для получения
        # числового ввода от пользователя

    def getOperator(self):
        return (input('operator = '))
        # Здесь можно реализовать логику для
        # получения оператора от пользователя

    def performOperation(self, num1: float, num2: float, operator):
        _calc = Calculator(num1, num2, operator)
        return _calc.result

        # Здесь вызываются методы калькулятора
        # для выполнения операций

    def displayResult(self, result: float):
        print(f'Result = {result}')
        # Здесь можно реализовать логику для отображения
        # результата пользователю
