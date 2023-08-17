class Book:
    def __init__(self, title):
        self.title = title
        self.isRead = False

    def mark_as_read(self):
        self.isRead = True

    def isRead(self):
        return self.isRead

    def __str__(self):
        read = "прочитана" if self.isRead else "непрочитана"
        return f"{self.title} - {read}"
