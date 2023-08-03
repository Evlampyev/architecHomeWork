#  Интерфейс определяет операции, которые должен
#  поддерживать DAO.
from abc import ABC, abstractmethod


class UserDAO(ABC):
    @abstractmethod
    def getAllUsers(self) -> list:
        pass

    @abstractmethod
    def getUser(self, id):
        pass

    @abstractmethod
    def updateUser(self, user):
        pass

    @abstractmethod
    def deleteUser(self, user):
        pass


# Класс User представляет объект данных пользователя.
class User:
    __id: int
    __name: str

    def __init__(self, id, name):
        self.__name = name
        self.__id = id


#     // добавьте больше полей по мере необходимости
#
#     // методы getters and setters здесь


# // Имплементация
# UserDAO для работы с базой данных SQL.


class UserDAOImpl(UserDAO):
    def __init__(self, dbConnection):
        self.dbConnection = dbConnection

    def getAllUsers(self):
        pass
        # // Используйте dbConnection для получения пользователей из базы данных
        # // и верните их как список объектов User.

    def getUser(self):
        pass
        # // Используйте dbConnection для получения пользователя с заданным id из базы данных
        # // и верните его как объект User.

    def updateUser(self):
        pass

    # // Используйте dbConnection и данные объекта user для обновления пользователя
    # // в базе данных.

    def deleteUser(self):
        pass
# // Используйте dbConnection и данные объекта user для удаления пользователя
# // из базы данных.
