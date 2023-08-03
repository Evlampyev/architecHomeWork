from student import Student, StudentDao

student_dao = StudentDao()
student1 = Student(1, "Alice", "Computer Science")
student2 = Student(2, "Bob", "Physics")

student_dao.insert_student(student1)
student_dao.insert_student(student2)

for student in student_dao.get_all_students():
    print(student.get_name())

print(student_dao.get_student(1).get_name())

student_dao.update_student(Student(1, "Alicia", "Computer Science"))
print(student_dao.get_student(1).get_name())

student_dao.delete_student(student1)
for student in student_dao.get_all_students():
    print(student.get_name())
