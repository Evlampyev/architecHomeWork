from task_model import TaskModel
from task_presenter import TaskPresenter
from consol_task_view import ConsolTaskView

model = TaskModel()
view = ConsolTaskView()
presenter = TaskPresenter(model, view)


presenter.on_add_task_button_clicked()
presenter.on_add_task_button_clicked()
