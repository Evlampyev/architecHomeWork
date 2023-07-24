# Фасад — структурный паттерн проектирования, позволяющий дать интерфейс
# более высокого уровня к сложной системе.
# В отличие от адаптера, используется новый интерфейс.
# Большой минус в том, что в данной концепции, фасад может стать
# godlike, связанным со всей системой.
# Иногда фасад превращают в синглтон, т.к. обычно нужен всего 1 фасад.


# Класс для выполнения задачи A
class TaskA:
    def execute(self):
        print("Выполнение задачи A")


# Класс для выполнения задачи B
class TaskB:
    def execute(self):
        print("Выполнение задачи B")


# Класс для выполнения задачи C
class TaskC:
    def execute(self):
        print("Выполнение задачи C")


# Фасад
class Facade:
    def __init__(self):
        self.task_a = TaskA()
        self.task_b = TaskB()
        self.task_c = TaskC()

    def do_all_tasks(self):
        self.task_a.execute()
        self.task_b.execute()
        self.task_c.execute()


if __name__ == "__main__":
    facade = Facade()
    facade.do_all_tasks()
