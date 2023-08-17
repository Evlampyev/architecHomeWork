# view
from abc import ABC, abstractmethod


class TaskView(ABC):

    @abstractmethod
    def show_task(self, task_view_model):
        """Вывод ...
        :param нечто"""
        pass
