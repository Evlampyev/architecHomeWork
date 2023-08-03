# TableGetAwey
from student import Student, StudentTableGateway

gateway = StudentTableGateway()

alice = Student(1, "Alice", "Computer Science")
bob = Student(2, "Bob", "Physics")

gateway.insert(alice)
gateway.insert(bob)

for student in gateway.find_all():
    print(student.name)

alice_updated = Student(1, "Alicia", "Computer Science")
gateway.update(alice_updated)

print(gateway.find(1).name)

gateway.delete(1)

for student in gateway.find_all():
    print(student.name)
