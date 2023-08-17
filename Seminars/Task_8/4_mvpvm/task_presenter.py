from task import Task


class TaskPresenter:

    def __init__(self, view):
        self.view = view
        self.tasks = []
        self.tasks.append(Task("Помыть посуду"))
        self.tasks.append(Task("Постирать бельё"))

    def display_task(self):
        task_view_models = self.tasks
        self.view.show_task(task_view_models)

    def complete_task(self, index):
        self.tasks[index].compete()


