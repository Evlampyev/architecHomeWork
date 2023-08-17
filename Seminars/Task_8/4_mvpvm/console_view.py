from task_view import TaskView
from task_view_model import TaskViewModel


class ConsoleView(TaskView):

    def show_task(self, task_view_models):
        for i in range(len(task_view_models)):
            res = TaskViewModel(task_view_models[i])
            print(f"{i+1}. {res.get_display_name()} ")
