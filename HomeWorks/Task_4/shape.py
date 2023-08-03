# Класс для геометрических фигур

from abc import ABC, abstractmethod


class Shape(ABC):
    """Общие поля и методы для всех геометрических фигур"""

    def getParametres(self):
        """Получение параметров фигуры из терминала"""
        pass
    def __str__(self):
        """Вывод на экран названия и параметров фигуры """
        pass

    @staticmethod
    def nameClass():
        pass
