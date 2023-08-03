class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class UserDao:
    # Интерфейс для работы с данными,
    # в данном случае он хранится в списке
    # при изменении способа хранения измениться
    # только этот интерфейс

    def __init__(self):
        self.users = []

    def get_all_users(self):
        return self.users.copy()

    def append(self, user):
        self.users.append(user)

    def get_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def update_user(self, user):
        for index, existing_user in enumerate(self.users):
            if existing_user.id == user.id:
                self.users[index] = user

    def delete_user(self, user):
        self.users = [existing_user for existing_user in self.users \
                      if existing_user.id != user.id]
