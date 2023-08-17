class TaskViewModel:

    def __init__(self, task):
        compl = 'complete' if task.is_completed() else ""
        self.display_name = f"{task.get_name()}  {compl}"

    def get_display_name(self):
        return self.display_name
