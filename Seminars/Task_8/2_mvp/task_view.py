# представление (абстрактный интерфейс)
from abc import ABC, abstractmethod


class iTaskView(ABC):

    @abstractmethod
    def display_task(self, tasks):
        """Вывод на экран всех задач \n
        :param tasks"""
        pass

    @abstractmethod
    def get_user_input(self):
        """Добавление новой задачи"""
        pass
