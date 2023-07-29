from abc import ABC, abstractmethod


class IHumanWorker(ABC):

    @abstractmethod
    def eat(self):
        raise NotImplementedError()  # Обязательный к наследованию и переопределению метод

    @abstractmethod
    def work(self):
        raise NotImplementedError()  # Обязательный к наследованию и переопределению метод


class IRobotWorker(ABC):

    @abstractmethod
    def work(self):
        raise NotImplementedError()  # Обязательный к наследованию и переопределению метод
