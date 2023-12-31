class Student:
    def __init__(self, id, name, course):
        self.__id = id
        self.__name = name
        self.__course = course

    # Геттеры и сеттеры
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_course(self):
        return self.__course


class StudentDao:
    def __init__(self):
        self.students = []

    def get_all_students(self):
        return self.students.copy()

    def get_student(self, id):
        for student in self.students:
            if student.get_id() == id:
                return student
        return None

    def insert_student(self, student):
        self.students.append(student)

    def update_student(self, student):
        existing_student = self.get_student(student.get_id())
        if existing_student:
            index = self.students.index(existing_student)
            self.students[index] = student

    def delete_student(self, student):
        self.students = [s for s in self.students if s.get_id() != student.get_id()]
