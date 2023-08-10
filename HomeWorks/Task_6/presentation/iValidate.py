from abc import ABC


class IValidate(ABC):
    """Интерфейс для проверки введенных данных на валидность"""

    def author_valid(author: str) -> bool:
        """Проверка автора на 2-3 слова все с большой буквы \n
        :param author автор \n
        :return bool"""
        if author.istitle():
            return True
        else:
            return False

    def id_valid(data) -> bool:
        """Проверка id на отсутствие в БД
        :param data наличин книги с таким id
        :return bool"""
        if data is None:
            return True
        else:
            return False
