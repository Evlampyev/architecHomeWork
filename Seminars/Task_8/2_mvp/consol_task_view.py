# вывод в консоль (Реализация представления)
from task_view import iTaskView


class ConsolTaskView(iTaskView):

    def display_task(self, tasks):
        print("Список задач: ")
        for task in tasks:
            print(f"- {task}")

    def get_user_input(self):
        return input("Введите новую задачу: ")
