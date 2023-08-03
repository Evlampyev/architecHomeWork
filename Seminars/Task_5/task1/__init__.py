from user import User, UserDao

# Бизнес логика

user_dao = UserDao()

user1 = User(1, "Alice")
user2 = User(2, "Bob")

user_dao.append(user1)
user_dao.append(user2)

print("-- Все пользователи: --")
for user in user_dao.get_all_users():
    print(user.name)
print("-- Только пользователь с id=1 --")
print(user_dao.get_user(1).name)

print("-- Изменили имя пользователя с id=1 --")
user_dao.update_user(User(1, "Alicia"))
print(user_dao.get_user(1).name)

print("-- Удалили пользователя user1 --")
user_dao.delete_user(user1)
for user in user_dao.get_all_users():
    print(user.name)
