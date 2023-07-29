from abc import ABC, abstractmethod


class IGreet(ABC):
    def __init__(self, type):
        self.type = type

    @abstractmethod
    def greet(self):
        raise NotImplementedError()  # Обязательный к наследованию класс, указывающий,
        # что будет выведена эта ошибка если нет наследования
