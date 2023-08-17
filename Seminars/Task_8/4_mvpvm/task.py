
# Model
class Task:

    def __init__(self, name):
        self.name = name
        self.completed = False

    def is_completed(self):
        return self.completed

    def compete(self):
        self.completed = True

    def get_name(self):
        return self.name

