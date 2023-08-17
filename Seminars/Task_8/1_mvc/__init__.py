from task_controller import TaskController
from task_view import TaskView
from task_model import TaskModel

model = TaskModel()
view = TaskView()
conroller = TaskController(model, view)

conroller.add_task("Подготовить презентацию")
conroller.add_task("Закончить проект")
conroller.add_task("Сделать покупки")

# Результат:
# Список задач:
# - Подготовить презентацию
# - Закончить проект
# - Сделать покупки
