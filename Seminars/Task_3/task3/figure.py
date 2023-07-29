from abc import ABC, abstractmethod


class Figure(ABC):

    @abstractmethod  #Метод который можно переопределять
    def get_area(self):
        raise NotImplementedError()  # Обязательный к наследованию и переопределению метод

