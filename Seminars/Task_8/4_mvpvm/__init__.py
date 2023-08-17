from console_view import ConsoleView
from task_presenter import TaskPresenter

view = ConsoleView()
presenter = TaskPresenter(view)

presenter.display_task()

while (task_id := input("Введите номер задачи, "
                        "чтобы отметить её как завершенную: ")) != 'exit':
    try:
        task_id = int(task_id) - 1
        presenter.complete_task(task_id)
    except Exception:
        print('Не верный ввод')
    finally:
        presenter.display_task()
