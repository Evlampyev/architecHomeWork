# Представление
class TaskView:
    def display_task(self, tasks):
        print('Список задач: ')
        for task in tasks:
            print(f"- {task}")
